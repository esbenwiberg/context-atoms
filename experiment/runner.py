"""Stage 3 — ablation runner.

For each (task, arm, sample): fresh worktree at the PR's base SHA, bring in the
PR's test files (the red oracle), spawn a headless `claude` agent on the issue
text, then run the oracle. Two arms:
  atoms : --append-system-prompt with anchor-matched atoms (anchors hidden)
  none  : no injection
Telemetry per run: pass/fail, tool-call count, file-reveal calls in first 5,
tokens, cost, duration. Appends one JSON line per run to results.jsonl.

Run (smoke):  python -m experiment.runner --tasks 9 61 --samples 1 --max-turns 30
Run (full) :  python -m experiment.runner --samples 3
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from atoms.inject import render  # noqa: E402
from atoms.schema import load_atoms  # noqa: E402
from atoms.select import select  # noqa: E402
from experiment import profiles  # noqa: E402
from experiment.harness import (  # noqa: E402
    add_worktree, checkout_paths_from, prepare_worktree, run_pytest,
)

PROMPT = """\
You are fixing an issue in this repository. The repository already contains \
failing tests that encode the exact behavior required. Your job: make those \
tests pass by editing the SOURCE code under `src/` only.

Rules:
- Do NOT edit, delete, or weaken any test file. Changing tests is cheating.
- Edit only source code to satisfy the existing tests.
- You may run the failing tests at any time with EXACTLY this command:
    {test_cmd}

=== ISSUE ===
{issue}
"""

AGENT_TOOLS = ["Read", "Edit", "Write", "Grep", "Glob", "Bash"]


def parse_stream(stdout: str) -> dict:
    """Extract telemetry from a stream-json transcript."""
    tool_calls: list[str] = []
    result: dict = {}
    for line in stdout.splitlines():
        line = line.strip()
        if not line or line[0] != "{":
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = ev.get("type")
        if t == "assistant":
            for block in (ev.get("message", {}) or {}).get("content", []) or []:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    tool_calls.append(block.get("name", "?"))
        elif t == "result":
            result = ev
    usage = result.get("usage", {}) or {}
    file_reveal = {"Read", "Grep", "Glob"}
    first5 = tool_calls[:5]
    return {
        "n_tool_calls": len(tool_calls),
        "tool_sequence": tool_calls[:40],
        "files_opened_first5": sum(1 for n in first5 if n in file_reveal),
        "input_tokens": usage.get("input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
        "cache_read": usage.get("cache_read_input_tokens", 0),
        "cost_usd": float(result.get("total_cost_usd") or 0.0),
        "num_turns": result.get("num_turns", 0),
        "agent_duration_ms": result.get("duration_ms", 0),
        "is_error": bool(result.get("is_error")),
        "result_subtype": result.get("subtype", ""),
    }


def build_issue_text(task: dict) -> str:
    title = task.get("title", "").strip()
    body = task.get("body", "").strip()
    return f"{title}\n\n{body}".strip()


def atom_block(atoms, task: dict) -> str:
    envelope = task["src_files"] + task["test_files"]
    matched = select(atoms, envelope)
    return render(matched, show_anchors=False), matched


def run_one(task: dict, arm: str, sample: int, atoms, prof,
            model: str, max_turns: int, timeout: int) -> dict:
    base = task["base_sha"]
    test_files = task["test_files"]
    venv_python = prof.venv_python
    test_cmd = (f"PYTHONPATH={prof.pythonpath_subdir} {venv_python} -m pytest "
                + " ".join(test_files) + " -q -p no:cacheprovider")
    issue = build_issue_text(task)
    prompt = PROMPT.format(test_cmd=test_cmd, issue=issue)

    rec: dict = {"pr": task["pr"], "stratum": task["stratum"], "arm": arm,
                 "sample": sample, "model": model}

    wt = add_worktree(prof.repo, base, label=f"run-{task['pr']}-{arm}-{sample}")
    try:
        prepare_worktree(wt, prof.prepare_files)
        checkout_paths_from(wt, task["merge_sha"], test_files)

        args = [
            "claude", "-p",
            "--model", model,
            "--max-turns", str(max_turns),
            "--output-format", "stream-json",
            "--verbose",
            "--add-dir", str(wt.path),
            "--allowedTools", *AGENT_TOOLS,
            "--permission-mode", "acceptEdits",
        ]
        block = ""
        n_atoms = 0
        if arm == "atoms":
            block, matched = atom_block(atoms, task)
            n_atoms = len(matched)
            if block:
                args += ["--append-system-prompt", block]
        rec["n_atoms_injected"] = n_atoms

        t0 = time.time()
        try:
            proc = subprocess.run(args + [prompt], cwd=str(wt.path),
                                  capture_output=True, text=True, timeout=timeout)
            stdout = proc.stdout
            rec["wall_s"] = round(time.time() - t0, 1)
            rec["agent_rc"] = proc.returncode
            if proc.returncode != 0 and not stdout.strip():
                rec["agent_stderr"] = proc.stderr[-400:]
        except subprocess.TimeoutExpired:
            rec["wall_s"] = round(time.time() - t0, 1)
            rec["agent_rc"] = -9
            rec["timeout"] = True
            stdout = ""

        rec.update(parse_stream(stdout))

        # Oracle: did the agent make the red tests green?
        res = run_pytest(wt, venv_python, test_files, timeout=240,
                         pythonpath=prof.pythonpath(wt.path))
        rec["passed"] = res.passed
        rec["test_rc"] = res.returncode
        rec["n_passed"] = res.n_passed
        rec["n_failed"] = res.n_failed
        rec["n_error"] = res.n_error
    finally:
        wt.remove()
    return rec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default="pr-guardian", help="repo profile (see profiles.py)")
    ap.add_argument("--tasks-dir", type=Path, default=Path("experiment/tasks"))
    ap.add_argument("--atoms-dir", type=Path, default=Path("experiment/atoms"))
    ap.add_argument("--out", type=Path, default=Path("experiment/results.jsonl"))
    ap.add_argument("--tasks", nargs="*", type=int, help="PR numbers (default: all)")
    ap.add_argument("--arms", nargs="*", default=["atoms", "none"])
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--max-turns", type=int, default=40)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args(argv)

    prof = profiles.get(args.profile)
    atoms = load_atoms(args.atoms_dir.resolve())

    task_files = sorted(args.tasks_dir.glob("task-*.json"))
    tasks = [json.loads(p.read_text()) for p in task_files]
    if args.tasks:
        want = set(args.tasks)
        tasks = [t for t in tasks if t["pr"] in want]
    if not tasks:
        print("no tasks selected", file=sys.stderr)
        return 1

    plan = [(t, arm, s) for t in tasks for arm in args.arms for s in range(args.samples)]
    print(f"{len(plan)} runs: {len(tasks)} tasks x {len(args.arms)} arms x "
          f"{args.samples} samples | model={args.model} atoms={len(atoms)}",
          file=sys.stderr)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    total_cost = 0.0
    with args.out.open("a") as fh:
        for i, (task, arm, sample) in enumerate(plan, 1):
            rec = run_one(task, arm, sample, atoms, prof,
                          args.model, args.max_turns, args.timeout)
            total_cost += rec.get("cost_usd", 0.0)
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            print(f"[{i}/{len(plan)}] PR#{rec['pr']} {arm} s{sample}: "
                  f"pass={rec['passed']} tools={rec.get('n_tool_calls')} "
                  f"first5_reveal={rec.get('files_opened_first5')} "
                  f"atoms={rec.get('n_atoms_injected','-')} "
                  f"${rec.get('cost_usd',0):.3f} ({rec.get('wall_s')}s) "
                  f"cum=${total_cost:.2f}", file=sys.stderr)

    print(f"\nDONE {len(plan)} runs, cost ${total_cost:.2f} -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

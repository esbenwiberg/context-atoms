"""Stage 2 — mine red->green benchmark tasks from merged PRs.

A valid task: a merged PR small enough to be one focused change, that touches at
least one test file and one source file, where checking out the PR's *base*
commit + bringing in only the PR's test files leaves those tests RED. The agent's
job (Stage 3) is to make them green from the issue text alone.

Run: python -m experiment.mine --repo ~/repos/pr-guardian --out experiment/tasks \
        --want-simple 5 --want-medium 7 --want-novel 3
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from experiment import profiles  # noqa: E402
from experiment.harness import (  # noqa: E402
    add_worktree, checkout_paths_from, git, prepare_worktree, run_tests,
)

DEFAULT_MAX_LOC = 150


def gh_json(repo: Path, *args: str):
    r = subprocess.run(["gh", *args], cwd=str(repo), capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {r.stderr.strip()}")
    return json.loads(r.stdout)


def list_merged_prs(repo: Path, limit: int):
    return gh_json(repo, "pr", "list", "--state", "merged", "--limit", str(limit),
                   "--json", "number,title,body,additions,deletions,mergeCommit,files")


def stratum(n_src_files: int, loc: int, novel: bool) -> str:
    if novel:
        return "novel"
    if n_src_files <= 1 and loc <= 70:
        return "simple"
    return "medium"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", required=True, help="repo profile (see profiles.py)")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--pr-limit", type=int, default=200)
    ap.add_argument("--max-loc", type=int, default=DEFAULT_MAX_LOC)
    ap.add_argument("--want-simple", type=int, default=5)
    ap.add_argument("--want-medium", type=int, default=7)
    ap.add_argument("--want-novel", type=int, default=3)
    args = ap.parse_args(argv)

    prof = profiles.get(args.profile)
    repo = prof.repo.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    want = {"simple": args.want_simple, "medium": args.want_medium, "novel": args.want_novel}
    have = {"simple": 0, "medium": 0, "novel": 0}

    prs = list_merged_prs(repo, args.pr_limit)
    print(f"scanning {len(prs)} merged PRs (targets {want})", file=sys.stderr)
    tasks = []

    for pr in prs:
        if sum(have.values()) >= sum(want.values()):
            break
        num = pr["number"]
        loc = (pr.get("additions") or 0) + (pr.get("deletions") or 0)
        if loc == 0 or loc > args.max_loc:
            continue
        files = [f["path"] for f in (pr.get("files") or [])]
        test_files = [f for f in files if prof.is_test(f)]
        src_files = [f for f in files if prof.is_src(f)]
        if not test_files or not src_files:
            continue
        merge_sha = (pr.get("mergeCommit") or {}).get("oid")
        if not merge_sha:
            continue
        try:
            base_sha = git(repo, "rev-parse", f"{merge_sha}^").strip()
        except RuntimeError:
            continue

        novel = len(src_files) >= 4 or any("/__init__" in f for f in src_files)
        strat = stratum(len(src_files), loc, novel)
        if have[strat] >= want[strat]:
            continue  # stratum full; keep scanning for others

        # Verify RED: base + PR's test files only -> tests should NOT all pass.
        wt = add_worktree(repo, base_sha, label=f"mine-{num}")
        try:
            prepare_worktree(wt, prof.prepare_files, prof.prepare_symlinks)
            checkout_paths_from(wt, merge_sha, test_files)
            res = run_tests(wt, prof, test_files, timeout=240)
        finally:
            wt.remove()

        if res.passed:
            print(f"  PR#{num} [{strat}] SKIP: tests already green at base "
                  f"(not a red->green task)", file=sys.stderr)
            continue
        if res.returncode == -9:
            print(f"  PR#{num} SKIP: pytest timeout", file=sys.stderr)
            continue

        # Verify GREEN at merge: the PR's full change must actually make the test
        # pass in isolation. Filters bogus reds (missing fixtures, flaky) so every
        # mined task is provably solvable.
        wt2 = add_worktree(repo, merge_sha, label=f"mine-{num}-green")
        try:
            prepare_worktree(wt2, prof.prepare_files, prof.prepare_symlinks)
            green = run_tests(wt2, prof, test_files, timeout=240)
        finally:
            wt2.remove()
        if not green.passed:
            print(f"  PR#{num} [{strat}] SKIP: not green at merge "
                  f"(rc={green.returncode}) -> unsolvable in isolation", file=sys.stderr)
            continue

        task = {
            "pr": num,
            "title": pr["title"],
            "body": (pr.get("body") or "")[:1500],
            "stratum": strat,
            "base_sha": base_sha,
            "merge_sha": merge_sha,
            "test_files": test_files,
            "src_files": src_files,
            "loc": loc,
            "red_check": {"returncode": res.returncode, "n_failed": res.n_failed,
                          "n_error": res.n_error, "n_passed": res.n_passed},
        }
        (out / f"task-{num:04d}-{strat}.json").write_text(json.dumps(task, indent=2))
        tasks.append(task)
        have[strat] += 1
        print(f"  PR#{num} [{strat}] OK red (failed={res.n_failed} err={res.n_error}) "
              f"loc={loc} :: {pr['title'][:60]}", file=sys.stderr)

    (out / "index.json").write_text(json.dumps(
        {"have": have, "want": want, "tasks": [t["pr"] for t in tasks]}, indent=2))
    print(f"\nMINED {sum(have.values())} tasks {have}", file=sys.stderr)
    if sum(have.values()) < 10:
        print("*** STAGE-2 WARNING: <10 tasks; widen pr-limit or loosen filters ***",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

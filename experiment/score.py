"""Stage 4 — aggregate runs against the pre-registered kill criteria.

Reads results.jsonl, computes the four metrics from experiment/plan.md and emits
a green/yellow/red table + verdict. Pure function over the data; no model calls.

Run: python -m experiment.score --in experiment/results.jsonl
"""
from __future__ import annotations

import argparse
import json
import statistics as stats
from collections import defaultdict
from pathlib import Path


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else 0.0


def band(value, green, yellow, higher_is_better):
    """Return GREEN/YELLOW/RED given thresholds. green/yellow are the cut points."""
    if higher_is_better:
        if value >= green:
            return "GREEN"
        if value >= yellow:
            return "YELLOW"
        return "RED"
    else:
        if value <= green:
            return "GREEN"
        if value <= yellow:
            return "YELLOW"
        return "RED"


def load(path: Path):
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def by_arm(rows, key, arm):
    return [r.get(key) for r in rows if r["arm"] == arm]


def rate(rows, arm):
    rs = [1 if r.get("passed") else 0 for r in rows if r["arm"] == arm]
    return (sum(rs) / len(rs)) if rs else 0.0, len(rs)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", type=Path, default=Path("experiment/results.jsonl"))
    ap.add_argument("--md", type=Path, default=None, help="optional markdown report path")
    args = ap.parse_args(argv)
    rows = load(args.inp)
    if not rows:
        print("no rows")
        return 1

    arms = sorted({r["arm"] for r in rows})
    lines = []
    def out(s=""):
        lines.append(s)
        print(s)

    out(f"# Ablation results  ({len(rows)} runs)\n")

    # --- success rates ---
    r_atoms, n_a = rate(rows, "atoms")
    r_none, n_n = rate(rows, "none")
    succ_delta_pp = (r_atoms - r_none) * 100
    out("## Success")
    out(f"- atoms : {r_atoms:.1%}  (n={n_a})")
    out(f"- none  : {r_none:.1%}  (n={n_n})")
    out(f"- delta : {succ_delta_pp:+.1f} pp")

    # per-stratum
    out("\n### Per stratum (pass rate atoms / none)")
    strata = defaultdict(lambda: {"atoms": [], "none": []})
    for r in rows:
        strata[r["stratum"]][r["arm"]].append(1 if r.get("passed") else 0)
    for s in ("simple", "medium", "novel"):
        a, n = strata[s]["atoms"], strata[s]["none"]
        ra = mean(a) if a else float("nan")
        rn = mean(n) if n else float("nan")
        out(f"- {s:<7}: {ra:.0%}/{rn:.0%}  (n={len(a)}/{len(n)})")
    simple_a = strata["simple"]["atoms"]
    simple_n = strata["simple"]["none"]
    simple_delta_pp = ((mean(simple_a) - mean(simple_n)) * 100) if simple_a and simple_n else 0.0

    # --- exploration ---
    expl_a = mean(by_arm(rows, "files_opened_first5", "atoms"))
    expl_n = mean(by_arm(rows, "files_opened_first5", "none"))
    expl_ratio = (expl_a / expl_n) if expl_n else float("nan")
    tools_a = mean(by_arm(rows, "n_tool_calls", "atoms"))
    tools_n = mean(by_arm(rows, "n_tool_calls", "none"))
    out("\n## Exploration")
    out(f"- file-reveal calls in first 5: atoms {expl_a:.2f} / none {expl_n:.2f}  "
        f"-> ratio {expl_ratio:.2f}")
    out(f"- total tool calls: atoms {tools_a:.1f} / none {tools_n:.1f}")

    # --- cost / tokens ---
    in_a = mean(by_arm(rows, "input_tokens", "atoms"))
    in_n = mean(by_arm(rows, "input_tokens", "none"))
    cost_a = mean(by_arm(rows, "cost_usd", "atoms"))
    cost_n = mean(by_arm(rows, "cost_usd", "none"))
    tok_overhead = ((in_a / in_n) - 1) * 100 if in_n else float("nan")
    cost_overhead = ((cost_a / cost_n) - 1) * 100 if cost_n else float("nan")
    out("\n## Cost")
    out(f"- $ per run: atoms ${cost_a:.3f} / none ${cost_n:.3f}  -> {cost_overhead:+.1f}%")
    out(f"  (cost is the honest overhead measure; usage.input_tokens excludes cached "
        f"prompt so it is NOT used for the verdict)")
    n_inj = mean(by_arm(rows, "n_atoms_injected", "atoms"))
    out(f"- mean atoms injected (atoms arm): {n_inj:.1f}")

    # --- ceiling/floor guard: success is only informative if arms can differ ---
    ceiling = min(r_atoms, r_none) >= 0.95
    floor = max(r_atoms, r_none) <= 0.05

    # --- verdict table ---
    out("\n## Kill criteria (pre-registered)")
    v_succ = band(succ_delta_pp, 3, 0, higher_is_better=True)
    if ceiling or floor:
        v_succ = "UNINFORMATIVE"
    v_expl = band(expl_ratio, 1.3, 1.5, higher_is_better=False)
    v_simple = band(simple_delta_pp, 0, -2, higher_is_better=True)
    if ceiling or floor:
        v_simple = "UNINFORMATIVE"
    v_cost = band(cost_overhead, 15, 25, higher_is_better=False)
    out(f"| Metric | Value | Verdict |")
    out(f"|---|---|---|")
    out(f"| Success delta | {succ_delta_pp:+.1f} pp | {v_succ} |")
    out(f"| Exploration ratio | {expl_ratio:.2f} | {v_expl} |")
    out(f"| Simple-task delta | {simple_delta_pp:+.1f} pp (n={len(simple_a)}) | {v_simple} |")
    out(f"| Cost overhead | {cost_overhead:+.1f}% | {v_cost} |")

    out("\n## Verdict")
    if ceiling:
        out(f"**SUCCESS METRIC CEILINGED ({r_atoms:.0%}/{r_none:.0%}).** Every task was "
            f"solved by both arms, so the pre-registered PRIMARY metric (success delta) "
            f"cannot discriminate. The bet is NEITHER proven NOR refuted by success.")
        out("")
        if abs(expl_ratio - 1.0) < 0.1:
            out("The behavioural metric the bet hinged on — file-reveal calls in the first "
                f"5 tool calls — is FLAT (ratio {expl_ratio:.2f}). Anchor-matched injection "
                "did not measurably reduce early exploration on this benchmark.")
            out("")
            out("=> DO NOT build the mechanism on this evidence. The benchmark lacks "
                "discriminating power (tasks too easy / budget too generous). Re-run with "
                "harder discrimination (lower turn budget, harder tasks, or weaker model) "
                "BEFORE any green light. Total-tool-calls did drop "
                f"({tools_a:.1f} vs {tools_n:.1f}) — a weak secondary signal worth chasing "
                "in the re-run, not acting on now.")
        else:
            out(f"Exploration ratio {expl_ratio:.2f} is the only live signal; treat as "
                "indicative and re-run with a discriminating benchmark.")
    elif all(v == "GREEN" for v in (v_succ, v_expl, v_simple, v_cost)):
        decision = "ALL GREEN -> build the selector, CLI, MCP."
        out(decision)
    elif any(v == "RED" for v in (v_succ, v_expl, v_simple, v_cost)):
        out("RED present -> STOP. Do not polish. Diagnose or abandon.")
    else:
        out("MIXED -> narrow scope (e.g. inject only on the class that helped).")

    if args.md:
        args.md.write_text("\n".join(lines) + "\n")
        print(f"\n(report written to {args.md})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

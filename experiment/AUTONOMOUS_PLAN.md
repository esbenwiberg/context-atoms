# Autonomous execution plan (Esben away, 2026-05-29)

Standing authorization from Esben: execute the sequence below **without waiting
for approval**, gating each step on the previous one's results. Track cumulative
spend; report at each gate. This file is the source of truth if context is lost.

## The cell we're filling

| | easy tasks | hard tasks |
|---|---|---|
| complex app | pr-guardian → ceiling (dead) | **TARGET (steps 2,3)** |
| library | — | sqlglot (step 1 / B) |

The bet helps most in *complex app + hard tasks* (agent must explore). That cell
has no clean evidence yet. Steps 2 and 3 attack it.

## Sequence + gates

### Step 1 — finish B (sqlglot / sonnet, 96 runs) → score
- Score `experiment/sqlglot/results.jsonl` → `experiment/sqlglot/RESULTS.md`.
- B is the *library+hard* cell. It informs interpretation but does NOT gate step 2
  (different cell). Run step 2 regardless of B's verdict.

### Step 2 — harder pr-guardian (complex app + hard tasks)
- Re-mine pr-guardian for HARD, cross-subsystem tasks: `--max-loc 400`, prefer PRs
  touching multiple subsystems/files (the big ones excluded in the first mine).
  Output: `experiment/pg-hard/tasks`. Reuse existing atoms `experiment/atoms`.
- Run ablation (sonnet, samples 2-3) → `experiment/pg-hard/results.jsonl` → score.
- **GATE → step 3:**
  - Step 2 is **INFORMATIVE** if pass rate ∈ [15%, 90%] for at least one arm
    (i.e. not a 100/100 ceiling, not a 0/0 floor) AND a non-degenerate delta read.
    → We have a complex-app answer. Report it. Step 3 becomes CONFIRMATORY:
    attempt it, but it is lower priority.
  - Step 2 is **UNINFORMATIVE** (ceiling ≥90% both arms, or floor ≤10% both, like
    the first pr-guardian run) → step 3 is REQUIRED for a genuinely complex +
    discriminating test.

### Step 3 — autopod (node-ts, pnpm monorepo) — conditional / confirmatory
- Decision-006 confound (author's trained eye, doc-rich): tolerable as a 4th data
  point read against sqlglot; note it loudly in results.
- **De-risk FIRST** (like vitest/pytest were): prove a single autopod test runs in
  an isolated worktree (pnpm store + per-package vitest via turbo). If isolation
  cannot be made reliable, **STOP and report** — do not burn hours/spend on a
  broken harness.
- If de-risked: add `autopod` profile (package-aware src/test paths, per-package
  node_modules), extract (48 ADRs), mine (green-at-merge), smoke (gate full run on
  the smoke discriminating: not 0/0, not 100/100), then full run → score.

## Stop conditions (do NOT plow past these)
- A harness that can't produce reliable green/red (e.g. autopod isolation broken).
- Any step erroring on >25% of runs (infra problem, not signal) → diagnose first.
- Cumulative spend report at each gate; these run on Claude auth (plan usage).

## Spend so far (approx, Claude-auth usage)
- pr-guardian sonnet+haiku: ~$24 | sqlglot extract+mine: ~$2 | B (running): ~$60 est
- pr-guardian/sqlglot atoms + PS extract: ~$6

## What's NOT being done
- portfolio-simulation / luumi as benchmarks: too few minable tasks (3 / thin).
  node-ts support is built + proven (vitest isolation works); PS parked.
- A public TS library: redundant with sqlglot (same library+hard cell).

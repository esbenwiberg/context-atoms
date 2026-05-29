# Experiment harness — two-week ablation, executed

This is the running implementation of `docs/design/experiment/plan.md`. It tests
the single bet: **does anchor-matched atom injection change agent behaviour vs no
injection** — operationalised as success ↑, exploration ↓, cost ~flat.

Everything runs on the local `claude` CLI in headless mode (`-p`), so it rides
your existing Claude auth instead of a metered API key. No `ANTHROPIC_API_KEY`.

## Pilot repo

`~/repos/pr-guardian` (category B — Esben's own project; decision 006 prefers a
colleague's repo, this is "acceptable"). **Confounds to keep in mind when reading
results:** pr-guardian is doc-rich AND an autopod consumer — the same two things
decision 006 avoided by ruling out autopod. A green result therefore needs the
"is this just tuned to your idioms?" asterisk. The clean confirmation is a later
run on a colleague's non-autopod repo.

## Pipeline

```
extract.py   docs        -> 83 atoms        (Stage 1)   `claude -p` per source
mine.py      merged PRs   -> 8 red->green    (Stage 2)   gh + git worktree + pytest
runner.py    tasks        -> results.jsonl   (Stage 3)   `claude -p` agent x2 arms x3
score.py     results.jsonl-> verdict table   (Stage 4)   pure function
```

Reproduce:

```bash
python -m experiment.extract --repo ~/repos/pr-guardian --out experiment/atoms
python -m experiment.mine    --repo ~/repos/pr-guardian --out experiment/tasks \
       --max-loc 250 --want-simple 8 --want-medium 8 --want-novel 4
python -m experiment.runner  --samples 3 --max-turns 40
python -m experiment.score   --in experiment/results.jsonl --md experiment/RESULTS.md
```

## What a "task" is

A merged PR small enough to be one focused change, touching ≥1 test and ≥1 source
file, where: checkout the PR's **base** commit, bring in **only** the PR's test
files, and those tests are **RED**. The agent's job (from the issue text alone) is
to make them green by editing source. Validity = the red state is a real assertion
failure, verified per task at mine time.

Isolation: every checkout is a `git worktree` under `/tmp/ca-bench`, so the pilot
repo's real working tree is never touched. Tests run with `PYTHONPATH=<worktree>/src`
so the checked-out source wins over any editable install in the shared venv.

## Methodology decisions (extending the design's open questions)

These are choices the plan left open or that the implementation forced. They are
recorded here because they materially shape how results should be read.

1. **Oracle envelope (upper-bound test).** At task start there is no diff, so the
   selector has nothing to anchor against. We feed `select()` the PR's *actual*
   changed files as the envelope. This is the optimistic case: atoms are perfectly
   scoped. If perfectly-scoped atoms don't help, nothing will (clean kill). If they
   do, the *next* question — can a real selector derive the envelope — becomes worth
   answering. Results are an **upper bound**, not a production estimate.

2. **Anchors hidden in the injected block.** Atoms are *selected* by anchor∩files,
   but the injected text omits the anchor file paths (`render(show_anchors=False)`).
   Otherwise arm A would get a free "edit these files" location hint, confounding
   "intent helps" with "file pointer helps". We isolate the intent/constraint effect.

3. **Flat injection, no relevance cap.** Faithful to the plan ("anchor-match → system
   prompt, no selector"). Consequence: multi-file tasks pull many atoms (up to ~34 of
   83). Those tasks approximate *flat always-on* injection and will inflate the token
   metric. Reported per-task, not hidden.

4. **Path-only anchors** (open-question 2). No tree-sitter at v0.

5. **Model = sonnet, max-turns = 40.** A behaviour experiment wants a consistent,
   capable agent. Note the **ceiling risk**: at a generous budget sonnet may solve
   easy tasks regardless of arm, flattening success-delta. When that happens the
   signal lives in exploration-ratio and token-overhead, and success is reported as
   "ceiling" rather than gamed by tuning the turn cap.

## Known limitations of this pilot

- **N is small.** pr-guardian has ~64 merged PRs; only 8 yield clean red→green
  small tasks. Final batch = 8 tasks × 2 arms × 3 samples = 48 runs (design wanted
  ~90). Adequate for a go/no-go, thin for stratum-level claims.
- **Simple stratum is n=1.** The "simple-task delta ≥ 0" criterion (atoms must not
  *hurt* easy work) is underpowered here. Treat that cell as indicative only.
- **Single pilot, author-owned, doc-rich, autopod-consumer.** See confounds above.

## Files

- `claude_cli.py` — headless `claude` wrappers (text transform + stream parse helpers)
- `harness.py` — git worktree + isolated pytest plumbing
- `extract.py` / `mine.py` / `runner.py` / `score.py` — the four stages
- `atoms/` — extracted atoms (the Stage-1 output, committed as evidence)
- `tasks/` — mined task specs (the Stage-2 output)
- `results.jsonl` — one JSON line per run (the Stage-3 output)
- `RESULTS.md` — the scored verdict (the Stage-4 output)

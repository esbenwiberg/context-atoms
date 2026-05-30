# context-atoms

> ## ⚰️ Dead on arrival
>
> **The central bet does not hold. We tested it before building the mechanism, and it failed.**
>
> Anchor-matched atom injection produced **+0.0pp success delta** across **250 ablation
> runs** (4 repos, 2 languages, 2 models) — including on the *one* benchmark with real
> headroom (sqlglot, 69% pass). It never reduced exploration (ratio 0.95–1.15) and added
> 0–15% cost. Even with the test rigged in its favour (perfectly-scoped *oracle* atoms),
> nothing moved.
>
> Independently corroborated: ETH Zürich's [AGENTS.md study](https://arxiv.org/abs/2602.11988)
> finds **LLM-generated / auto-extracted context is neutral-to-negative** (−0.5/−2% success,
> +20% cost) on real codebases. The only thing with positive evidence is **human-authored**
> context (~4%) — which is *not* what this design auto-extracts.
>
> **Verdict: do not build the selector / graph / distill / MCP.** Full autopsy →
> [`experiment/FINDINGS.md`](experiment/FINDINGS.md). The harness lives on; the mechanism doesn't.

Tool-neutral, repo-local context-persistence for AI coding agents. Small,
anchored, kind-typed markdown atoms instead of heavy always-on spec files.

This repo held **the design** and **an experiment that tested its central bet
before any production tooling was built**. The experiment came back negative (above).
It is not — and per the evidence, should not become — a shipping tool.

## The bet

> Selective, anchor-scoped injection of atoms changes agent behaviour vs flat /
> no injection — success up, exploration down, cost ~flat.

Unproven by design. `experiment/` exists to measure it on a real repo before we
build the selector, link graph, MCP, or any of the mechanism.

## Layout

```
docs/design/        the architecture as it stands (read README.md there first)
docs/premortem/     the failure-mode analysis that shaped the decisions
atoms/              v0 CLI: atom schema, shape lint, flat anchor-match select, inject
tests/              unit tests for the pure-function core
experiment/         the executed ablation (extract -> mine -> run -> score)
```

## The CLI (v0 — measurement substrate only)

```bash
pip install -e .
atoms --atoms-dir docs/context init
atoms --atoms-dir docs/context new rationale why-we-chose-x
atoms --atoms-dir docs/context --anchor-root . lint
atoms --atoms-dir docs/context --anchor-root . select --diff HEAD
atoms --atoms-dir docs/context --anchor-root . inject --diff HEAD
```

Deliberately small. It implements only what the experiment needs (format, lint,
flat anchor-match, prompt injection). It does **not** implement the selector graph
walk, kind ordering, relevance scoring, distill, or MCP — those are the mechanism,
and the mechanism is not built until the bet is proven. See
`docs/design/experiment/plan.md` → "What this experiment does NOT build".

## The experiment

Runs entirely on the local `claude` CLI (headless) — no API key. See
`experiment/README.md` for methodology, the pilot repo + its confounds, and how to
reproduce. The scored verdict lands in `experiment/RESULTS.md`.

## Status

Design: stable after a multi-session exploration (2026-05-28).

Experiment: **complete — the bet is NOT supported.** 250 ablation runs across 4
repos (pr-guardian, sqlglot, portfolio-simulation, autopod), 2 languages, 2 models.
Anchor-matched atom injection showed +0.0pp success delta everywhere (including the
one benchmark that genuinely discriminates), never reduced exploration, and added
cost. **Do not build the mechanism.** Full write-up: `experiment/FINDINGS.md`.

The harness (pytest + vitest, single-package & monorepo) is reusable to re-test if
one variable changes (weaker model, larger codebase, human-curated atoms). Open
questions resolved: 1 (pilot → pr-guardian), 5 (name → `context-atoms`).

# context-atoms

Tool-neutral, repo-local context-persistence for AI coding agents. Small,
anchored, kind-typed markdown atoms instead of heavy always-on spec files.

This repo holds **the design** and **a running experiment that tests its central
bet before any production tooling is built**. It is not (yet) a shipping tool.

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
Experiment: harness built and executed against `pr-guardian`. Open question 1
(pilot repo) resolved → pr-guardian; open question 5 (repo name) resolved → this
repo, `context-atoms`.

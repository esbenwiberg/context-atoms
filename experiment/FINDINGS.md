# Findings — does anchor-matched atom injection change agent behaviour?

**Verdict: NO, on the evidence gathered. Do not build the mechanism.**

250 ablation runs across 4 repos, 2 languages, 2 models. The single bet —
*selective, anchor-scoped injection of atoms produces fundamentally different
agent behaviour than no injection* (success ↑, exploration ↓, cost ~flat) — is
**not supported**. Per the design's own pre-registered rule ("any red → stop, do
not polish"), this is a STOP.

## The data

| Pilot | lang / kind | runs | discriminates? | success Δ (atoms−none) | exploration ratio | cost Δ |
|---|---|---|---|---|---|---|
| pr-guardian easy (sonnet) | py / app | 48 | no — 100/100 ceiling | +0.0 pp | 0.99 | −1% |
| pr-guardian (haiku) | py / app | 48 | no — 100/100 ceiling | +0.0 pp | 0.95 | +2% |
| pr-guardian hard (sonnet) | py / app | 40 | no — 100/100 ceiling | +0.0 pp | 1.09 | −7% |
| **sqlglot (sonnet)** | py / library | 96 | **YES — 69% pass** | **+0.0 pp** | **1.01** | **+9%** |
| autopod-daemon (sonnet) | ts / app (monorepo) | 18 | no — 100/100 ceiling | +0.0 pp | 1.08 | +15% |

## What the numbers say

1. **Success delta is +0.0 pp everywhere** — including the one benchmark that
   genuinely discriminates (sqlglot, 69% pass, real headroom both ways). Where
   atoms *could* have moved success, they did not, identically per stratum.
2. **Exploration never decreased.** The ratio sits at 0.95–1.15 — at or slightly
   *above* 1.0. The bet predicted a *decrease*. This is the cleanest refutation of
   the core mechanism: anchor-matched injection did not make the agent explore
   less; if anything marginally more (it sometimes goes to check the injected
   context).
3. **Cost is flat-to-+15%**, scaling with how many atoms match. Injection is a
   net tax with no measured benefit.

## Why this is a strong (not weak) result

- **It's not just a ceiling artifact.** sqlglot discriminates (69%) and still shows
  exactly zero effect. pr-guardian ceilings are uninformative on success, but the
  exploration + cost signals there agree with sqlglot.
- **The test was rigged in the bet's favour (oracle envelope).** The atoms arm was
  given *perfectly scoped* atoms — selected by the PR's actual changed files, which
  no real selector could know in advance. Even with this best case, no effect. A
  real selector could only do worse.

## Honest limits — what could still change the verdict

The bet is unsupported *as operationalised and within the range tested*. Specific
untested regimes that could revive it:

- **Weaker/smaller models.** sonnet & haiku are capable enough to ceiling on most
  app tasks — they often don't need the context. A smaller local model might.
- **Much larger / unfamiliar codebases.** The bet's premise (agent is "lost" and
  must explore) barely triggered: even autopod's daemon tasks were solved in 5–12
  tool calls. Genuinely sprawling/unfamiliar code might show an effect.
- **Human-curated atoms (pre-work capture, decision 005).** We tested *doc-import*
  atoms only. Higher-signal, intent-bearing atoms might differ.
- **File-pointer injection.** We hid anchors to isolate the *intent* effect. Showing
  "the relevant files are X" might help — but via a different mechanism than the bet.

## Methodology finding (reusable)

**Red→green-from-a-title fits libraries, not apps.** sqlglot yielded 24 isolatable
tasks trivially; every *app* repo did not — pr-guardian *ceilings* (frontier models
ace its tasks at any size), and portfolio-simulation / autopod-daemon yield only ~3
cleanly-isolatable single-package tasks because real app changes are cross-cutting.
This is *also* why the bet's home turf (complex apps) is hard to test this way, and
is the biggest caveat on the verdict.

## Recommendation

- **Do not build** the selector graph walk, kind ordering, relevance scoring,
  distill, or MCP. The foundation is unproven and the one clean test says null.
- If revisiting, change one variable from "honest limits" above and re-run — the
  harness now supports pytest + vitest, single-package and monorepo, two models, in
  ~an afternoon per pilot.
- The atom *format* + *lint* + *flat select* (the `atoms/` CLI) are cheap, correct,
  and harmless to keep as a writing aid; they are not the mechanism.

## Provenance
Autonomous run 2026-05-29/30, per `AUTONOMOUS_PLAN.md`. Raw per-run data in each
`experiment/*/results.jsonl`; per-pilot scores in `experiment/*/RESULTS.md`.
Total cost ≈ $85 (Claude-auth/plan usage; no metered API key).

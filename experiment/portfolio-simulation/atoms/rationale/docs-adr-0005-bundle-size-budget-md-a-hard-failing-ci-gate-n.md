---
kind: rationale
claim: A hard-failing CI gate (not a soft warning) was chosen for bundle-size enforcement
  because soft warnings get ignored and bundle drift accumulates one small PR at a
  time in a way that code review reliably misses.
anchors:
- tools/check-bundle-size.mjs
- .github/workflows/build-and-smoke.yml
tags:
- bundle-size
- ci-gate
- rationale
- drift
source: doc-import:docs/adr/0005-bundle-size-budget.md
status: active
---
A hard-failing CI gate (not a soft warning) was chosen for bundle-size enforcement because soft warnings get ignored and bundle drift accumulates one small PR at a time in a way that code review reliably misses.

Alternatives explicitly rejected: (1) no budget — relies on reviewers who don't run the build locally to measure; (2) soft warning only — warnings become noise and engineers stop acting on them; (3) per-route/chunk budgets — inapplicable because the app ships a single inlined HTML with no routes or chunks. The current hybrid (hard cap + 2 MB soft warning) was adopted in the 2026-05-24 revision to reduce false-positive failures on legitimate feature growth while preserving the forcing function for real bloat.

---
kind: constraint
claim: Demand-distribution primitives (`distributeSpan`, `carveSpanHole`) are proven
  via unit tests against analytic identities rather than captured fixtures because
  POC divergence is authorised for that surface (per ADR-0011); the parity-coverage
  gate filename contract still applies.
anchors:
- src/math/distributeSpan.ts
- tests/parity/distributeSpan.spec.ts
- tools/check-parity-coverage.mjs
tags:
- testing
- math
- demand
- parity
- adr
- exception
source: doc-import:docs/adr/0004-parity-test-workflow.md
status: active
---
Demand-distribution primitives (`distributeSpan`, `carveSpanHole`) are proven via unit tests against analytic identities rather than captured fixtures because POC divergence is authorised for that surface, as decided in ADR-0011 (2026-05-28).

This supersedes the captured-fixture requirement from ADR-0004 for these specific modules only. The parity-coverage gate (`tools/check-parity-coverage.mjs`) still enforces the filename contract — a `tests/parity/distributeSpan.spec.ts` must exist — but its content uses analytic identity checks rather than replaying POC-captured (input, output) pairs.

Orchestrator parity (`runScheduleSuggestions`) remains fully in force under ADR-0004 with captured fixtures.

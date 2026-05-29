---
kind: rationale
claim: distributeSpan.ts parity spec asserts analytic identities rather than replaying
  captured POC fixtures because the POC contains the same bug the new code fixes,
  making POC-captured fixtures the wrong oracle.
anchors:
- src/math/distributeSpan.ts
- tests/parity/distributeSpan.spec.ts
- tests/fixtures/distributeSpan
tags:
- parity
- testing
- demand-distribution
- adr-0011
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#relationship-to-adr-0004
status: active
---
distributeSpan.ts parity spec asserts analytic identities rather than replaying captured POC fixtures because the POC contains the same bug the new code fixes. Capturing from the POC would lock in the wrong answer; capturing from the new code would be tautological. The identities used are: Σ across covering periods equals span.hours; split-then-sum equals unsplit; weekend-only spans distribute to zero. This is an authorised divergence from ADR-0004's captured-fixture workflow, scoped only to the demand-distribution primitives added by ADR-0011. The orchestrator surface (runScheduleSuggestions and composing modules) continues to use captured fixtures as the empirical oracle per ADR-0004.

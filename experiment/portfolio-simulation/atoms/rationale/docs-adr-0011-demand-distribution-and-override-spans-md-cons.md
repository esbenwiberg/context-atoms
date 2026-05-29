---
kind: rationale
claim: distributeSpan and carveSpanHole are proven by analytic-identity unit tests
  rather than captured POC-parity fixtures, as an explicit carve-out from ADR-0004.
anchors:
- src/math/distributeSpan.ts
- tests/parity/distributeSpan.spec.ts
- tests/fixtures/distributeSpan
tags:
- testing
- parity
- demand-math
- adr-0004
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#consequences
status: active
---
distributeSpan and carveSpanHole are proven by analytic-identity unit tests rather than captured POC-parity fixtures, as an explicit carve-out from ADR-0004. The historical POC's computeRoleDemandForPeriod + curve weighting was the oracle that prior parity fixtures captured, but the new distribution math intentionally diverges from the POC because the POC behaviour was the source of the Q→M→edit-Feb→Q→M bug. Since the POC is no longer a valid oracle for this surface, analytic identities (sum-to-original, split-then-sum, edge cases) replace captured fixtures for these primitives. The runScheduleSuggestions parity workflow is retained and its fixtures were recaptured against the new math.

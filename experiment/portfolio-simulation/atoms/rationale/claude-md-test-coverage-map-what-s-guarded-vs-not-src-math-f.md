---
kind: rationale
claim: src/math/* functions are validated via parity fixtures in tests/fixtures/poc-parity/
  rather than ad-hoc unit tests, to assert behavioral equivalence with the original
  PoC implementation.
anchors:
- src/math/
- tests/parity/
- tests/fixtures/poc-parity/
tags:
- testing
- math
- parity
- poc
source: doc-import:CLAUDE.md#test-coverage-map-what-s-guarded-vs-not
status: active
---
src/math/* functions are validated via parity fixtures in tests/fixtures/poc-parity/ rather than ad-hoc unit tests, to assert behavioral equivalence with the original PoC implementation. Each JSON fixture captures an input/output pair recorded from the PoC; the parity specs in tests/parity/*.spec.ts replay every fixture and fail if the TypeScript implementation diverges. This approach means a refactor that accidentally changes numeric output will fail even if the new code looks correct in isolation. Performance is additionally guarded by tests/bench/math.bench.ts. Do not replace fixture-driven parity specs with hand-written unit tests — the fixture set IS the behavioral contract.

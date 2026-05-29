---
kind: constraint
claim: "tools/check-parity-coverage.mjs still enforces the src/math/<name>.ts \u2192\
  \ tests/parity/<name>.spec.ts filename contract even though ADR-0011 relaxes the\
  \ required spec content for distributeSpan."
anchors:
- tools/check-parity-coverage.mjs
- src/math/distributeSpan.ts
- tests/parity/distributeSpan.spec.ts
tags:
- parity
- coverage-gate
- ci
- adr-0011
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#relationship-to-adr-0004
status: active
---
tools/check-parity-coverage.mjs still enforces the src/math/<name>.ts → tests/parity/<name>.spec.ts filename contract even though ADR-0011 relaxes the required spec content for distributeSpan. ADR-0011 does not relax the gate, only the content of the spec for that one file. Any new math module added under src/math/ must still have a corresponding parity spec file or the coverage check will fail.

---
kind: constraint
claim: Every module under src/math/ must have a corresponding parity spec in tests/parity/;
  the check-parity-coverage.mjs gate enforces this in CI.
anchors:
- src/math/
- tests/parity/
- tools/check-parity-coverage.mjs
tags:
- testing
- math
- parity
- ci
source: doc-import:docs/adr/README.md
status: active
---
Every module under src/math/ must have a corresponding parity spec in tests/parity/; the check-parity-coverage.mjs gate enforces this in CI. Math modules are the core IP of the application; their behaviour is locked via captured JSON fixtures under tests/fixtures/poc-parity/. Adding a new math module without a matching parity spec will fail the parity-coverage gate.

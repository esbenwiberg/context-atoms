---
kind: constraint
claim: Every src/math/<name>.ts file must have a corresponding tests/parity/<name>.spec.ts;
  missing coverage is a CI gate failure.
anchors:
- src/math
- tests/parity
- tools/check-parity-coverage.mjs
tags:
- parity-coverage
- testing
- ci-gate
source: doc-import:CLAUDE.md#self-validation-is-non-negotiable
status: active
---
Every src/math/<name>.ts file must have a corresponding tests/parity/<name>.spec.ts; missing coverage is a CI gate failure. The check is enforced by tools/check-parity-coverage.mjs via npm run check:parity-coverage. If a math module legitimately has no captured fixture, add it to the ALLOWLIST in that tool with a one-line reason — do not relax the rule to make the build green.

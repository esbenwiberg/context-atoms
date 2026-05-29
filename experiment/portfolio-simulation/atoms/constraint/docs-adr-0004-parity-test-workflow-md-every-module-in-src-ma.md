---
kind: constraint
claim: Every module in `src/math/` must have a matching parity spec under `tests/parity/`
  driven by captured fixtures in `tests/fixtures/`; `tools/check-parity-coverage.mjs`
  fails the build if any math module lacks one.
anchors:
- src/math
- tests/parity
- tests/fixtures
- tools/check-parity-coverage.mjs
tags:
- testing
- math
- parity
- build-gate
- constraint
source: doc-import:docs/adr/0004-parity-test-workflow.md
status: active
---
Every module in `src/math/` must have a matching parity spec under `tests/parity/` driven by captured fixtures in `tests/fixtures/`; `tools/check-parity-coverage.mjs` fails the build if any math module lacks one.

The gate runs as part of `npm run verify` (`npm run check:parity-coverage`). When a math module lands without a parity spec, the gate fails closed — there is no shortcut.

An allow-list exists for type-only or pure-helper modules that have no fixture counterpart (their behavior is exercised indirectly through consumer parity specs). The allow-list must be used sparingly, with a one-line reason per entry.

If behavior is intentionally changed, the parity fixtures must be recaptured and the reason documented. Silent divergence is a parity bug, not a feature.

---
kind: constraint
claim: '`src/math/**` must be pure TypeScript with no imports from React, ReactDOM,
  Zustand, DOM APIs, `parent.Xrm`, or any adapter/platform/state/view folder.'
anchors:
- src/math/**
- .dependency-cruiser.cjs
tags:
- math-purity
- constraint
- dependency-cruiser
source: doc-import:docs/adr/0002-ports-and-adapters-with-math-purity.md
status: active
---
`src/math/**` must be pure TypeScript with no imports from React, ReactDOM, Zustand, DOM APIs, `parent.Xrm`, or any adapter/platform/state/view folder.

Enforced by `.dependency-cruiser.cjs` rule `math-stays-pure` — fails the build if any `src/math/**` module imports from the forbidden namespaces. This ensures math modules are unit-testable as pure functions (required by the parity test suite in `tests/parity/`) and reusable outside xPM.

---
kind: constraint
claim: All code under src/math/ must be pure TypeScript with no React, Xrm, DOM, or
  side-effect imports.
anchors:
- src/math/
tags:
- math
- purity
- no-react
- no-dom
source: doc-import:CLAUDE.md#conventions
status: active
---
All code under src/math/ must be pure TypeScript with no React, Xrm, DOM, or side-effect imports. Parity tests in tests/parity/ validate math functions against captured fixtures in tests/fixtures/. Violating this boundary makes the math layer untestable in isolation and breaks the parity test contract.

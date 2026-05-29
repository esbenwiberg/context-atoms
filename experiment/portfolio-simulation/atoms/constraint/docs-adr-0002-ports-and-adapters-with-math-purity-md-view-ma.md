---
kind: constraint
claim: "View, math, state, and entry code may only import `src/adapters/types.ts`\
  \ and the `src/adapters/index.ts` barrel \u2014 direct imports from `src/adapters/fixture/**`\
  \ or `src/adapters/xrm/**` are forbidden."
anchors:
- src/adapters/index.ts
- src/adapters/types.ts
- src/adapters/fixture/index.ts
- src/adapters/xrm/index.ts
- .dependency-cruiser.cjs
tags:
- ports-and-adapters
- constraint
- dependency-cruiser
- adapter-isolation
source: doc-import:docs/adr/0002-ports-and-adapters-with-math-purity.md
status: active
---
View, math, state, and entry code may only import `src/adapters/types.ts` and the `src/adapters/index.ts` barrel — direct imports from `src/adapters/fixture/**` or `src/adapters/xrm/**` are forbidden.

Enforced by `.dependency-cruiser.cjs` rule `ports-adapters-impl-leak`. This preserves the fixture-only dev story (swap adapters without touching view or math) and keeps Dataverse wiring mechanically scoped to `src/adapters/xrm/**`. Consequence: when the contract needs a new field (e.g. on `Initiative`), the change must touch `src/adapters/types.ts` first, then both adapter implementations, then consumers.

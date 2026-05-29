---
kind: rationale
claim: Zustand was chosen as the sole state container over Redux Toolkit (too heavy,
  ~13 kB vs ~1 kB) and React Context + reducers (re-render granularity breaks down
  beyond ~3 slices).
anchors:
- src/state/store.ts
tags:
- state-management
- bundle-size
- zustand
source: doc-import:docs/adr/0003-in-memory-zustand-no-browser-persistence.md
status: active
---
Zustand was chosen as the sole state container over Redux Toolkit (too heavy, ~13 kB vs ~1 kB) and React Context + reducers (re-render granularity breaks down beyond ~3 slices).

Redux Toolkit was rejected for bundle size and ceremony — the state shape (~10 slices) doesn't justify the devtools/middleware ecosystem, and the project has a strict bundle budget (ADR-0005). React Context was rejected because splitting contexts for performance is exactly what Zustand already provides with less code; aggressive memoization would be required otherwise.

One store at src/state/store.ts; slices composed inline. zustand is the only state-management runtime dependency in package.json.

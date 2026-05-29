---
kind: constraint
claim: localStorage must never be used as a source of truth; all runtime state lives
  in-memory in the Zustand store at src/state/store.ts.
anchors:
- src/state/store.ts
tags:
- state
- storage
- zustand
source: doc-import:ARCHITECTURE.md
status: active
---
localStorage must never be used as a source of truth; all runtime state lives in-memory in the Zustand store at src/state/store.ts. The store is organised in slices (bootstrap, ranking, filters, constraint, etc.) with no prop-drilling beyond one level. Persisting state across sessions is handled exclusively by the scenario serialisation layer (src/scenarios/), not by browser storage.

---
kind: rationale
claim: dateOverrides is keyed by Initiative.id (not row index, not a scenario-composite)
  because Initiative.id is the only stable key that survives sort changes and adapter
  re-fetches.
anchors:
- src/state/store.ts
- src/adapters/types.ts
- src/math/getEffectiveDates.ts
tags:
- dateOverrides
- keying
- store
source: doc-import:docs/adr/0007-date-overrides-keying.md
status: active
---
dateOverrides is keyed by Initiative.id (not row index, not a scenario-composite) because Initiative.id is the only stable key that survives sort changes and adapter re-fetches.

Rejected alternatives:
- Row index in sortedRows: sort order can change, causing the override to silently target a different initiative.
- `Initiative.id + scenarioId` composite: scenarios persistence has not landed; every read site would need to guess the current scenario. When scenarios land, the Map gets scoped to the active scenario in the store, but the key shape stays plain `string`.
- `Record<string, DateOverride>`: Map gives O(1) .has/.delete/.get without prototype-pollution risk and stable insertion-order iteration; Record requires Object.keys enumeration plus numeric-string-key guards.

The store slice type is `Map<string, DateOverride>` where DateOverride is the type exported from src/math/getEffectiveDates.ts (the single source of truth for the shape).

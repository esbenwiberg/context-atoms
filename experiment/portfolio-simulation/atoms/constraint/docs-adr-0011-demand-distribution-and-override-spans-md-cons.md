---
kind: constraint
claim: Demand overrides must compose per-date so that a broad quarterly edit and a
  finer monthly correction can coexist without either silently clobbering the other.
anchors:
- src/state/demandOverrideSpan.ts
- src/math/distributeSpan.ts
tags:
- overrides
- composition
- demand
- granularity
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#consequences
status: active
---
Demand overrides must compose per-date so that a broad quarterly edit and a finer monthly correction can coexist without either silently clobbering the other. The old model resolved overrides by exact key match, meaning a Q-level edit and an M-level edit to the same period could not coexist — one would silently win. The new model stores spans and resolves conflicts per calendar date, so analysts can layer a coarse Q override with a precise M correction and both take effect in their respective date ranges.

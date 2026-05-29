---
kind: rationale
claim: dateOverrides stores Date objects (not ISO strings) to avoid a serialize/parse
  round-trip on every render and to match the shape getEffectiveDates.ts already expects.
anchors:
- src/math/getEffectiveDates.ts
- src/math/dateIso.ts
- src/state/store.ts
tags:
- dateOverrides
- date-format
- performance
source: doc-import:docs/adr/0007-date-overrides-keying.md
status: active
---
dateOverrides stores Date objects (not ISO strings) to avoid a serialize/parse round-trip on every render and to match the shape getEffectiveDates.ts already expects.

Dates must be local-time Date instances constructed via parseIsoDate or new Date(y, m, d) per the src/math/dateIso.ts convention — never `new Date(isoString)` with a Z-suffix (which would be UTC).

Rejected alternative — ISO strings: would add a parse on every render of every consuming component (timeline bars, heatmap, ranking date cells). The parse cost is small but non-zero, and there is no upside because the single-page bundle never persists.

Consequence: when Dataverse-backed scenarios land, the write path will need an explicit `Array.from(map.entries())` step to serialize, since JSON.stringify on a Map yields `{}`.

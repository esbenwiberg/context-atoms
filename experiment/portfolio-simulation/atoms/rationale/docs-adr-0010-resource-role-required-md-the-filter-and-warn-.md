---
kind: rationale
claim: The filter-and-warn approach for roleless resources was rejected because it
  silently dropped ~45% of demand hours by routing orphan-targeted demand to bucket
  keys that no role row walked.
anchors:
- src/heatmap/useHeatmapData.ts
- tools/dv-propose-targets.mjs
tags:
- heatmap
- orphan-resources
- data-loss
- filter-rejected
source: doc-import:docs/adr/0010-resource-role-required.md
status: active
---
The filter-and-warn approach for roleless resources was rejected because it silently dropped ~45% of demand hours by routing orphan-targeted demand to bucket keys that no role row walked. A cross-tab of the dev tenant showed 33 proposes targeting orphan resources = 17,620 hours vs 51 proposes targeting role-assigned resources = 21,375 hours. The re-keying code (bucketKeyByResourceId.get(resId) ?? resId) routed orphan demand to a key no bucket walked, making the heatmap look nearly empty. A dismissible warning label does not fix invisible data. The chosen alternative — a synthesised Unassigned bucket — keeps demand visible and makes the data-quality gap self-evident as a permanent row.

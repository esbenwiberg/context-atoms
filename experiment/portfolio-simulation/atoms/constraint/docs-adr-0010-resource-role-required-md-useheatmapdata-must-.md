---
kind: constraint
claim: '`useHeatmapData` must receive the translated Unassigned bucket label via an
  `unassignedRoleLabel` parameter rather than calling `t()` internally, to preserve
  the math/IP boundary.'
anchors:
- src/heatmap/useHeatmapData.ts
- src/heatmap/HeatmapPanel.tsx
- src/i18n/en.ts
tags:
- i18n
- math-ip-boundary
- hook-api
- unassigned-bucket
source: doc-import:docs/adr/0010-resource-role-required.md
status: active
---
`useHeatmapData` must receive the translated Unassigned bucket label via an `unassignedRoleLabel` parameter rather than calling `t()` internally, to preserve the math/IP boundary. The hook lives in the math layer and must remain free of i18n concerns. The caller (HeatmapPanel or equivalent UI layer) passes the i18n-resolved string in. This pattern matches the broader architectural rule that pure math/data hooks do not import from src/i18n.

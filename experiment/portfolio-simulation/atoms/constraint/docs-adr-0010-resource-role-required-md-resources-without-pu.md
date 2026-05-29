---
kind: constraint
claim: "Resources without `pum_role` must be keyed to the sentinel `UNASSIGNED_ROLE_KEY`\
  \ and aggregated into a single synthesised bucket \u2014 never filtered out and\
  \ never split into per-resource rows."
anchors:
- src/heatmap/useHeatmapData.ts
- src/adapters/xrm/mappers.ts
- tests/heatmap/useHeatmapData.spec.tsx
tags:
- heatmap
- orphan-resources
- unassigned-bucket
- UNASSIGNED_ROLE_KEY
source: doc-import:docs/adr/0010-resource-role-required.md
status: active
---
Resources without `pum_role` must be keyed to the sentinel `UNASSIGNED_ROLE_KEY` and aggregated into a single synthesised bucket — never filtered out and never split into per-resource rows. Filtering drops load-bearing demand hours (see rejected alternative). Per-orphan rows recreate the named-resource heatmap that role grouping exists to avoid. The single bucket sums capacity from every orphan member and accepts any demand whose propose targets an orphan resource. The row label ('Unassigned (no role)') is the data-quality signal — no separate dismissible warning. The bucket disappears automatically once all resources have a role assigned, requiring no cleanup state across reloads. `Resource.roleId` remains optional in the type system.

---
kind: constraint
claim: 'Override overlap is resolved per calendar date, not per span: buildContributions
  folds override layers in createdAt order so that two overlapping overrides share
  intent along the specific days each owns.'
anchors:
- src/heatmap/buildContributions.ts
- src/math/distributeSpan.ts
tags:
- overrides
- carving
- conflict-resolution
- latest-wins
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#decision
status: active
---
Override overlap is resolved per calendar date, not per span: buildContributions folds override layers in createdAt order so that two overlapping overrides share intent along the specific days each owns. The algorithm: materialise a propose-side base span per (resource, initiative) pair, sort the pair's overrides by (createdAt asc, arrayIdx asc), then fold each layer in order — carve its [start, end) hole out of every lower-layer piece via carveSpanHole, then append the override sliver on top. Each surviving sliver is distributed via distributeSpan and summed into per-period output. carveSpanHole omits zero-weekday pieces (never emits hours: 0 sub-spans).

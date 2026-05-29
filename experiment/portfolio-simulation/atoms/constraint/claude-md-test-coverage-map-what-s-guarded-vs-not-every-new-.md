---
kind: constraint
claim: Every new UI surface must ship with a matching component test; extending the
  three known untested surfaces is mandatory gap-closure.
anchors:
- src/app/App.tsx
- src/ranking/renderGroupedBody.tsx
- src/ranking/RankingTable.tsx
- tests/ranking/
- tests/heatmap/
- tests/timeline/
- tests/app/
tags:
- testing
- ui
- coverage-policy
source: doc-import:CLAUDE.md#test-coverage-map-what-s-guarded-vs-not
status: active
---
Every new UI surface must ship with a matching component test; extending the three known untested surfaces is mandatory gap-closure. The three documented gaps are: (1) App.tsx split-resize handle — pointer and keyboard interactions are not exercised; (2) portfolio grouping render shape — groupByPortfolio is unit-tested on data but the rendered group rows have no component test; (3) ConstraintBanner — capacity vs columnCap modes and over-cap recolor have no component test (the math inputs are tested separately). When any of these surfaces is modified, adding the missing test is the expected outcome.

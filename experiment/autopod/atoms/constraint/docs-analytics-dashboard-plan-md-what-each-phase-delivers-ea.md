---
kind: constraint
claim: "Each analytics dashboard phase must ship a complete vertical slice: migration\
  \ (if any), then daemon endpoint, then Swift API client, then middle-pane card,\
  \ then right-pane drill-in \u2014 in that order, with no partial deliveries."
anchors:
- packages/daemon/src/db/migrations
- packages/daemon/src/api/routes
tags:
- analytics
- delivery
- vertical-slice
- phase-structure
source: doc-import:docs/analytics-dashboard-plan.md#what-each-phase-delivers
status: active
---
Each analytics dashboard phase must ship a complete vertical slice: migration (if any), then daemon endpoint, then Swift API client, then middle-pane card, then right-pane drill-in — in that order, with no partial deliveries. This means no phase is done until all five layers exist and are wired together. When adding a new analytics phase, the daemon migration and route must land before any UI work begins, and the drill-in view must be included in the same phase as the summary card — splitting card and drill-in across phases is not permitted.

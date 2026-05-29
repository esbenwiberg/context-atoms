---
kind: constraint
claim: "The throughput analytics endpoint (GET /pods/analytics/throughput) must return\
  \ both hour-of-day \xD7 day-of-week bucketed counts and time-in-status percentiles\
  \ in a single response, not split across calls."
anchors:
- packages/daemon/src/api/routes/pods.ts
- packages/daemon/src/pods/throughput-aggregator.ts
tags:
- analytics
- api
- throughput
- heatmap
source: doc-import:docs/analytics-dashboard-plan.md#phase-5-throughput-heatmap-escalations
status: active
---
The throughput analytics endpoint (GET /pods/analytics/throughput) must return both hour-of-day × day-of-week bucketed counts and time-in-status percentiles in a single response, not split across calls. The endpoint accepts from= and to= query params. A companion endpoint GET /pods/analytics/escalations handles escalation aggregates separately. Keeping heatmap data and percentiles co-located avoids a second round-trip when the right-pane drill-down opens.

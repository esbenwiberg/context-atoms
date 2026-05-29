---
kind: constraint
claim: The cost analytics endpoint (`GET /pods/analytics/cost`) must aggregate and
  parse `phase_token_usage` JSON server-side, not push raw JSON to the client.
anchors:
- packages/daemon/src/api/routes/pods.ts
- packages/daemon/src/pods/pod-repository.ts
tags:
- analytics
- cost
- endpoint
- aggregation
source: doc-import:docs/analytics-dashboard-plan.md#phase-1-cost-drill-in
status: active
---
The cost analytics endpoint (`GET /pods/analytics/cost`) must aggregate and parse `phase_token_usage` JSON server-side, not push raw JSON to the client. The plan specifies the endpoint signature as `GET /pods/analytics/cost?from=&to=&groupBy=phase|profile|model` and states it 'aggregates over pods table; parses phase_token_usage JSON server-side'. Pushing raw blobs to the client would expose unstable internal JSON shape and force clients to re-implement aggregation logic. Open risk: the JSON shape of `phase_token_usage` keys must be confirmed stable across all phase transitions before grouping is shipped.

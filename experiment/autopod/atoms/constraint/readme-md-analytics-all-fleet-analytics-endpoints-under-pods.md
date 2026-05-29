---
kind: constraint
claim: All fleet analytics endpoints under /pods/analytics/* accept a ?days=N query
  parameter with a default of 30 and a hard maximum of 365.
anchors:
- packages/daemon/src/api/routes/pods.ts
- packages/daemon/src/pods/cost-aggregation.ts
- packages/daemon/src/pods/reliability-aggregator.ts
- packages/daemon/src/pods/throughput-aggregator.ts
- packages/daemon/src/pods/safety-aggregator.ts
- packages/daemon/src/pods/quality-score.ts
- packages/daemon/src/pods/escalations-aggregator.ts
- packages/daemon/src/pods/models-aggregator.ts
tags:
- analytics
- api
- query-params
- bounds
source: doc-import:README.md#analytics
status: active
---
All fleet analytics endpoints under /pods/analytics/* accept a ?days=N query parameter with a default of 30 and a hard maximum of 365. Any new analytics route or aggregator added to this path must honour the same default and cap — callers (including the macOS Analytics tab) depend on consistent behaviour across all endpoints. Inputs outside [1, 365] must be rejected or clamped; never silently accept unbounded ranges.

---
kind: constraint
claim: 'All analytics queries must filter to a terminal cohort: non-workspace pods
  with final status (complete, killed, failed) that completed within the query window.'
anchors:
- packages/daemon/src/pods/throughput-aggregator.ts
- packages/daemon/src/pods/reliability-aggregator.ts
- packages/daemon/src/pods/cost-aggregation.ts
- packages/daemon/src/pods/safety-aggregator.ts
- packages/daemon/src/pods/models-aggregator.ts
- packages/daemon/src/pods/escalations-aggregator.ts
- packages/daemon/src/api/routes/pods.ts
tags:
- analytics
- cohort
- filtering
source: doc-import:ARCHITECTURE.md#analytics
status: active
---
All analytics queries must filter to a terminal cohort: non-workspace pods with final status (complete, killed, failed) that completed within the query window.

Workspace pods and in-progress pods must be excluded from every aggregator. Including them would skew metrics: workspace pods have different lifecycles and incomplete pods have no settled cost, rework count, or validation outcome to measure against.

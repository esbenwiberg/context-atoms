---
kind: constraint
claim: "Every analytics aggregation must filter pods to isWorkspace=false AND status\
  \ IN ('complete','killed','failed','rejected') AND completedAt within the trailing\
  \ window \u2014 widening this filter requires superseding purpose.md non-goals."
anchors:
- packages/daemon/src/pods/throughput-aggregator.ts
- packages/daemon/src/pods/reliability-aggregator.ts
- packages/daemon/src/pods/models-aggregator.ts
- packages/daemon/src/pods/quality-score-repository.ts
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- analytics
- pod-filter
- aggregation
source: doc-import:docs/analytics-dashboard-plan.md#established-conventions-locked-by-phase-0-phase-1
status: active
---
Every analytics aggregation must filter pods to isWorkspace=false AND status IN ('complete','killed','failed','rejected') AND completedAt within the trailing window — widening this filter requires superseding purpose.md non-goals.

This three-part predicate was locked in Phase 1 as the canonical pod population for all analytics. Workspace pods and in-flight/pending pods are explicitly excluded. The trailing window uses SQLite's `datetime('now', '-' || @days || ' days')` (precedent: quality-score-repository.ts:167), defaults to 30 days, and is parameterised via `?days=N` (≥ 1) on every endpoint.

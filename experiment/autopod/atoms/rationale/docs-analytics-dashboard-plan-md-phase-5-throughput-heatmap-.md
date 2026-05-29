---
kind: rationale
claim: "Escalation pattern clustering uses na\xEFve frequency-counted strings rather\
  \ than ML or semantic clustering, intentionally deferred as a simplicity choice\
  \ for the initial implementation."
anchors:
- packages/daemon/src/pods/escalation-repository.ts
- packages/daemon/src/pods/escalations-aggregator.ts
tags:
- escalations
- analytics
- clustering
source: doc-import:docs/analytics-dashboard-plan.md#phase-5-throughput-heatmap-escalations
status: active
---
Escalation pattern clustering uses naïve frequency-counted strings rather than ML or semantic clustering, intentionally deferred as a simplicity choice for the initial implementation. The plan explicitly states 'start naïve, just frequency-counted strings' for top blocking patterns derived from report_blocker payloads. Upgrading to semantic clustering is a future concern and should not be pulled into the Phase 5 scope.

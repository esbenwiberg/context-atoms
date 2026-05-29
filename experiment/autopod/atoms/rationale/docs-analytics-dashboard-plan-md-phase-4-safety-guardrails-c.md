---
kind: rationale
claim: Container log retention was explicitly excluded from the safety analytics phase
  because security proof lies in the absence of cross-boundary events, not log contents;
  the existing history-workspace flow handles forensic drill-downs.
anchors:
- packages/daemon/src/history/history-exporter.ts
tags:
- container-logs
- security
- deferred
source: doc-import:docs/analytics-dashboard-plan.md#phase-4-safety-guardrails
status: active
---
Container log retention was explicitly excluded from the safety analytics phase because security proof lies in the absence of cross-boundary events, not log contents; the existing history-workspace flow handles forensic drill-downs. Retaining raw container logs is a storage trap. When someone needs to investigate a specific pod, direct them to history-workspace rather than adding a log-retention pipeline.

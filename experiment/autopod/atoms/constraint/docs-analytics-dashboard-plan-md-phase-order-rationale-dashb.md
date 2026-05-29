---
kind: constraint
claim: "Dashboard phases 4\u20136 cannot be parallelised because each has a hard prerequisite\
  \ from an earlier phase: Safety needs a new DB table and writer-side change, Throughput\
  \ reuses phase 1's time-bucketing, and Models requires all per-model data plumbing\
  \ established by prior phases."
anchors:
- packages/daemon/src/pods/safety-aggregator.ts
- packages/daemon/src/pods/throughput-aggregator.ts
- packages/daemon/src/pods/models-aggregator.ts
tags:
- analytics
- dashboard
- phase-order
- dependencies
source: doc-import:docs/analytics-dashboard-plan.md#phase-order-rationale
status: active
---
Dashboard phases 4–6 cannot be parallelised because each has a hard prerequisite from an earlier phase: Safety needs a new DB table and writer-side change, Throughput reuses phase 1's time-bucketing, and Models requires all per-model data plumbing established by prior phases. Phases 1–3 are independent after the Phase 0 shell ships and could be parallelised, but 4–6 form a strict sequential chain.

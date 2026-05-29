---
kind: rationale
claim: Cost was chosen as the first feature phase because the data already exists
  and it validates the drill-in UI pattern end-to-end before later phases depend on
  it.
anchors:
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- analytics
- dashboard
- phase-order
- cost
source: doc-import:docs/analytics-dashboard-plan.md#phase-order-rationale
status: active
---
Cost was chosen as the first feature phase because the data already exists and it validates the drill-in UI pattern end-to-end before later phases depend on it. This maximises early operator value at minimum risk: no new writer-side changes are needed, and the drill-in pattern it proves becomes the template that Quality, Safety, Throughput, and Models phases all reuse.

---
kind: rationale
claim: The Models phase was placed last because it is the most ambitious (includes
  a simulator) and depends on per-model data plumbing that only exists after all earlier
  phases ship.
anchors:
- packages/daemon/src/pods/models-aggregator.ts
tags:
- analytics
- dashboard
- phase-order
- models
- simulator
source: doc-import:docs/analytics-dashboard-plan.md#phase-order-rationale
status: active
---
The Models phase was placed last because it is the most ambitious (includes a simulator) and depends on per-model data plumbing that only exists after all earlier phases ship. Doing it last means the simulator can be built on a fully-populated per-model data layer rather than having to stub or backfill it mid-stream.

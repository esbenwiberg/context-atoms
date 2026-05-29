---
kind: rationale
claim: The POST /pods/analytics/simulate endpoint is intentionally deferred because
  the what-if redirect math can run client-side against the per-model aggregates already
  returned by GET /pods/analytics/models.
anchors:
- packages/daemon/src/api/routes/pods.ts
tags:
- analytics
- simulate
- endpoint
- deferred
source: doc-import:docs/analytics-dashboard-plan.md#phase-6-models-leaderboard-what-if
status: active
---
The POST /pods/analytics/simulate endpoint is intentionally deferred because the what-if redirect math can run client-side against the per-model aggregates already returned by GET /pods/analytics/models. The design doc explicitly calls out 'Could also be done client-side; defer the call.' This means the daemon only needs one new read endpoint for Phase 6; the simulate endpoint should only be added if client-side math proves insufficient (e.g., the payload is too large, or server-side caching of simulation results becomes necessary). Avoid adding the POST endpoint speculatively.

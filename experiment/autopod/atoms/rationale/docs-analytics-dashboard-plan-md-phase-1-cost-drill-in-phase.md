---
kind: rationale
claim: "Phase-grain cost analytics are built on top of the `phase_token_usage` JSON\
  \ column in `pods`, which is already populated by migration 089 \u2014 no new instrumentation\
  \ is required."
anchors:
- packages/daemon/src/db/migrations/089_pod_phase_token_usage.sql
- packages/daemon/src/api/routes/pods.ts
tags:
- analytics
- cost
- phase_token_usage
- migration
source: doc-import:docs/analytics-dashboard-plan.md#phase-1-cost-drill-in
status: active
---
Phase-grain cost analytics are built on top of the `phase_token_usage` JSON column in `pods`, which is already populated by migration 089 — no new instrumentation is required. The plan explicitly calls out that `pods.phase_token_usage` is 'already populated by migration 089_pod_phase_token_usage.sql', making server-side aggregation over existing rows viable from day one. The chosen approach of parsing JSON server-side (rather than streaming raw blobs to the client) was selected to keep per-phase stacked-bar data aggregatable at the daemon boundary.

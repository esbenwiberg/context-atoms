---
kind: constraint
claim: 'The validation-failure breakdown must decompose by exactly these stage keys
  sourced from the `validations.result` JSON column: build, health, smoke, lint, sast,
  facts, taskReview.'
anchors:
- packages/daemon/src/pods/validation-repository.ts
- packages/daemon/src/db/migrations/011_acceptance_criteria.sql
- packages/daemon/src/db/migrations/
tags:
- analytics
- validation
- failure-stages
- schema
source: doc-import:docs/analytics-dashboard-plan.md#phase-2-lifecycle-funnel-reliability
status: active
---
The validation-failure breakdown must decompose by exactly these stage keys sourced from the `validations.result` JSON column: build, health, smoke, lint, sast, facts, taskReview. Any new endpoint aggregating validation failures must use these keys verbatim as the column identifiers — both for the per-stage failure-rate endpoint (`GET /pods/analytics/validation-failures`) and for the per-profile failure heatmap (profile rows × these stage cols). Adding or renaming a stage requires a coordinated migration of the stored JSON structure and a UI schema change.

---
kind: rationale
claim: Pre-Phase-1 pods that lack `phase_token_usage` rows are reconstructed at aggregation
  time as a single synthetic `agent_legacy` entry rather than backfilled into the
  database, because the phase taxonomy is forward-only (ADR-016).
anchors:
- packages/daemon/src/db/migrations/089_pod_phase_token_usage.sql
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- token-usage
- analytics
- ADR-016
- migration
source: doc-import:docs/analytics-dashboard-plan.md#established-conventions-locked-by-phase-0-phase-1
status: active
---
Pre-Phase-1 pods that lack `phase_token_usage` rows are reconstructed at aggregation time as a single synthetic `agent_legacy` entry rather than backfilled into the database, because the phase taxonomy is forward-only (ADR-016).

Decision recorded as ADR-016 during Phase 1. The `phase_token_usage` table carries phases: `agent_initial`, `agent_rework_<N>`, `review`, `plan_eval`. Any pod created before this schema existed has no rows; aggregators must synthesise an `agent_legacy` bucket from total token counts rather than reading per-phase rows. No backfill migration will be written — the forward-only constraint avoids reprocessing historical pod data.

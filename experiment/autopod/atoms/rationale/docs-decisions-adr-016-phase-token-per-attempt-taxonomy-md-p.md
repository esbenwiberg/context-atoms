---
kind: rationale
claim: Per-attempt phase token taxonomy was chosen over per-rework-reason (requires
  storing why each rework started) and coarse 3-bucket (reduces to existing opaque
  totals) because it exposes where rework cycles consume budget using an attempt counter
  that already exists.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/cost-aggregation.ts
- packages/daemon/src/db/migrations/089_pod_phase_token_usage.sql
tags:
- token-usage
- cost
- analytics
- phase-tokens
source: doc-import:docs/decisions/ADR-016-phase-token-per-attempt-taxonomy.md
status: active
---
Per-attempt phase token taxonomy was chosen over per-rework-reason (requires storing why each rework started) and coarse 3-bucket (reduces to existing opaque totals) because it exposes where rework cycles consume budget using an attempt counter that already exists.

Three taxonomies were evaluated:
- per-rework-reason: more diagnostic but requires pod-manager to remember the rework trigger for each iteration — added state to the validation loop.
- coarse 3-bucket: collapsed to what already existed (agent total + review + plan_eval) — no new signal.
- per-attempt: sweet spot — `agent_initial` for attempt 0, `agent_rework_<N>` for N ≥ 1; writer hooks into the existing `complete`-event handler at pod-manager.ts:4306-4321 which already has an attempt counter; no runtime stream parser changes needed.

No DB migration was required because `phase_token_usage` (migration 089) is already `TEXT NULL` JSON — new keys are additive at the application layer.

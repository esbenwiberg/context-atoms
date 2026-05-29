---
kind: constraint
claim: "Pods that completed before per-attempt instrumentation shipped must be represented\
  \ by a synthetic `agent_legacy` bucket computed as `pod.inputTokens \u2212 sum(known\
  \ phase buckets)` so historical cost totals still reconcile."
anchors:
- packages/daemon/src/pods/cost-aggregation.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- token-usage
- cost
- backward-compatibility
- analytics
source: doc-import:docs/decisions/ADR-016-phase-token-per-attempt-taxonomy.md
status: active
---
Pods that completed before per-attempt instrumentation shipped must be represented by a synthetic `agent_legacy` bucket computed as `pod.inputTokens − sum(known phase buckets)` so historical cost totals still reconcile.

Data is forward-only — no backfill of pre-instrumentation pods. Old rows have `null` or only the `review`/`plan_eval` shape. The cost aggregation layer must:
1. Sum all present `agent_initial` + `agent_rework_*` + `review` + `plan_eval` tokens.
2. Subtract from the pod-level `inputTokens`/`outputTokens` totals.
3. Expose the remainder as `agent_legacy` in the per-phase breakdown.

Missing keys must be treated as `{ inputTokens: 0, outputTokens: 0 }` — never as an error.

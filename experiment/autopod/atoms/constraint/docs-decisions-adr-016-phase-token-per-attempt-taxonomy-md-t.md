---
kind: constraint
claim: The four `phaseTokenUsage` bucket families (`agent_initial`, `agent_rework_<N>`,
  `review`, `plan_eval`) are a committed contract; any code reading `phase_token_usage`
  must tolerate an open-ended set of `agent_rework_*` keys, and adding a new family
  requires a follow-up ADR.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- token-usage
- contract
- phase-tokens
- schema
source: doc-import:docs/decisions/ADR-016-phase-token-per-attempt-taxonomy.md
status: active
---
The four `phaseTokenUsage` bucket families (`agent_initial`, `agent_rework_<N>`, `review`, `plan_eval`) are a committed contract; any code reading `phase_token_usage` must tolerate an open-ended set of `agent_rework_*` keys, and adding a new family requires a follow-up ADR.

Specific invariants:
- `agent_rework_<N>` keys are unbounded — a pod that reworks 50 times produces 50 keys. Readers must not enumerate or hard-code a max N.
- The `PhaseTokenUsage` type annotation must document the open-ended `agent_rework_${number}` pattern explicitly.
- UI rendering must collapse high-N reworks (e.g. '+ N more reworks') rather than rendering each as a stack segment.
- `review` and `plan_eval` keys continue to be written by their existing paths — no change to those writers.

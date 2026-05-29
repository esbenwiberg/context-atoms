---
kind: constraint
claim: The `computeCost` helper from `@autopod/shared/pricing` is the single computation
  site for token-derived cost; both the parser write path and the `effectiveCostUsd`
  read path must call this same helper so that their results are identical by construction
  and cannot drift.
anchors:
- packages/daemon/src/runtimes/codex-stream-parser.ts
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- cost
- invariant
- pricing
- adr-026
source: doc-import:docs/decisions/ADR-026-parser-side-cost-for-non-claude-runtimes.md
status: active
---
The `computeCost` helper from `@autopod/shared/pricing` is the single computation site for token-derived cost. Two code paths now produce a cost figure for non-Claude runtimes: the parser at write time (emitting on `AgentCompleteEvent.costUsd`) and `effectiveCostUsd(pod)` at read time (fallback when `pod.costUsd == 0`). Drift between them is prevented by construction because both call the same `computeCost(model, inputTokens, outputTokens)` function — there are no separate per-path price tables or env-var overrides. The pricing JSON in `@autopod/shared` remains the single source of truth and is updated manually (ADR-015 stance unchanged). Once `pod.costUsd` is written by the parser it becomes sticky (same as Claude today); the retroactive-repricing property of read-time aggregation is partially lost, and this is accepted as a known trade-off mirroring Claude's existing behavior.

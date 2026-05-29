---
kind: constraint
claim: Cost aggregation must prefer pod.costUsd when it is positive (Claude native
  cost from the stream) and fall back to computing cost from token counts via the
  pricing catalog for runtimes that emit no native cost (Codex, Copilot).
anchors:
- packages/daemon/src/pods/cost-aggregation.ts
- packages/daemon/src/runtimes/claude-stream-parser.ts
tags:
- cost
- pricing
- runtime
source: doc-import:docs/decisions/ADR-015-model-pricing-bundled-json.md
status: active
---
Cost aggregation must prefer pod.costUsd when it is positive (Claude native cost from the stream) and fall back to computing cost from token counts via the pricing catalog for runtimes that emit no native cost (Codex, Copilot). The canonical expression is: effectiveCost = pod.costUsd > 0 ? pod.costUsd : computeCost(pod.model, inputTokens, outputTokens). Claude populates costUsd from the runtime stream's total_cost_usd field (claude-stream-parser.ts:180); Codex emits only total_token_usage with no dollar figure; Copilot is similar. Violating this pattern either double-counts Claude costs or reports $0 for non-Claude pods.

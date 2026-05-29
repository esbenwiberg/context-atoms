---
kind: constraint
claim: Historical `pods.model` rows must never be rewritten; all analytics coalescing
  of old short alias values must happen on the read side via `MODEL_CANONICAL` to
  avoid changing what was actually stored.
anchors:
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- analytics
- historical-data
- pods
source: doc-import:docs/decisions/ADR-028-canonical-model-id-input-policy.md
status: active
---
Historical `pods.model` rows must never be rewritten. The decision explicitly rejects a full `pods.model` migration because it would hide what was actually stored and risk changing historical analytics semantics. Read-side coalescing from ADR-022 (`MODEL_CANONICAL` mapping) is the designated boundary for analytics. `MODEL_CANONICAL.opus` therefore remains mapped to `claude-opus-4-7` permanently so old pod rows continue to describe what actually ran, even though new profile writes map `opus` forward to 4.8. Only profile rows (not pod rows) are migrated forward by migration 110.

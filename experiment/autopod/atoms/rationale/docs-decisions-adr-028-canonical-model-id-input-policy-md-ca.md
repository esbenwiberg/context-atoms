---
kind: rationale
claim: 'Canonical provider model IDs (e.g. `claude-opus-4-8`) are required for all
  new profile and pod writes because accepting short aliases like `opus` after Opus
  4.8 would make the same string mean two different things: the new 4.8 for new writes
  and 4.7 for historical pod analytics, breaking cost, quality, and UI reasoning.'
anchors:
- packages/daemon/src/profiles/profile-validator.ts
- packages/daemon/src/db/migrations/110_canonicalize_profile_model_aliases.sql
tags:
- model-aliases
- canonical-ids
- analytics
source: doc-import:docs/decisions/ADR-028-canonical-model-id-input-policy.md
status: active
---
Canonical provider model IDs are required for all new profile and pod writes because short aliases would become ambiguous after Opus 4.8. Prior to this policy, Autopod accepted `opus`, `sonnet`, and `haiku` as input. ADR-022 added `MODEL_CANONICAL` to coalesce historical `pods.model` rows on the read side, mapping `opus` → `claude-opus-4-7`. But if new writes also accept `opus`, the same string would simultaneously mean `claude-opus-4-8` (new profile intent) and `claude-opus-4-7` (historical pod analytics), making cost, quality, and UI display ambiguous. Alternative rejected: keeping `opus` as accepted public input was rejected precisely because of this dual meaning after 4.8 landed. `MODEL_CANONICAL.opus` is intentionally frozen at 4.7 as a historical read-side shim, not a forward-mapping contract.

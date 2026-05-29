---
kind: rationale
claim: A hand-maintained `MODEL_CANONICAL` alias map (Option A) was chosen over deduplicating
  `model-pricing.json` or persisting a `canonical_model` DB column because it fixes
  analytics bisection at read time with zero schema cost and leaves the pricing lookup
  paths untouched.
anchors:
- packages/daemon/src/db/migrations/110_canonicalize_profile_model_aliases.sql
- packages/daemon/src/pods/pod-repository.ts
tags:
- analytics
- model-aliases
- pricing
- adr-022
source: doc-import:docs/decisions/ADR-022-model-canonical-alias-map.md
status: active
---
A hand-maintained `MODEL_CANONICAL` alias map (Option A) was chosen over deduplicating `model-pricing.json` or persisting a `canonical_model` DB column because it fixes analytics bisection at read time with zero schema cost and leaves the pricing lookup paths untouched. `pods.model` is a free-form string that can hold either canonical IDs (`claude-opus-4-7`) or short aliases (`opus`), causing analytics rollups keyed on that column to split the same underlying model into two rows. Option B (deduplicate pricing JSON, use only aliases as keys) was rejected because canonical IDs are what appears in CLI output and API headers — forcing alias keys everywhere is regressive. Option C (persist `canonical_model` on `pods`) was rejected because it requires a migration, a JS-map-dependent backfill, and rewriting historical rows when new aliases are added; coalescing at read time over a trailing window is microseconds at realistic fleet sizes. `MODEL_CANONICAL` and `canonicalModelKey()` live in `packages/shared/src/pricing/index.ts` because the pricing module is the canonical home for all model-identity concerns.

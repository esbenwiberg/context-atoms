---
kind: constraint
claim: Every analytics rollup that groups by model must pass raw `pods.model` through
  `canonicalModelKey()` before keying aggregates; grouping directly on the raw column
  is forbidden, and unknown models must bucket under the literal string `<unknown>`
  with null (not zero) pricing fields.
anchors:
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/db/migrations/110_canonicalize_profile_model_aliases.sql
tags:
- analytics
- model-aliases
- adr-022
- constraint
source: doc-import:docs/decisions/ADR-022-model-canonical-alias-map.md
status: active
---
Every analytics rollup that groups by model must pass raw `pods.model` through `canonicalModelKey()` before keying aggregates; grouping directly on the raw column is forbidden, and unknown models must bucket under the literal string `<unknown>` with null (not zero) pricing fields. `pods.model` holds whatever free-form string was written at pod creation — canonical IDs and short aliases both appear. Grouping without coalescing bisects cohorts for the same underlying model. The `<unknown>` bucket key uses angle brackets to mirror the phase-5b `<small profiles>` synthetic-row convention; its `totalCostUsd` and `dollarPerPr` are null rather than zero so the `<unknown>` row cannot silently win the cheapest-$/PR headline. The raw unrecognised strings are surfaced in an `unknownModels[]` list (capped at 10) so operators know which model strings need adding to the pricing catalog. Adding a new short alias requires updating both `model-pricing.json` AND `MODEL_CANONICAL` — omitting either silently re-introduces bisection.

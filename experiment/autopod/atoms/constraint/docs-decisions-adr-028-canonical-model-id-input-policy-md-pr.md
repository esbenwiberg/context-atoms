---
kind: constraint
claim: Profile writes must reject exact short Claude aliases (`opus`, `sonnet`, `haiku`)
  in `defaultModel`, `reviewerModel`, and `escalation.askAi.model`; pod creation must
  reject them in `model` overrides.
anchors:
- packages/daemon/src/profiles/profile-validator.ts
- packages/daemon/src/profiles/profile-store.ts
- packages/daemon/src/api/routes/pods.ts
tags:
- model-aliases
- validation
- profile
- pod
source: doc-import:docs/decisions/ADR-028-canonical-model-id-input-policy.md
status: active
---
Profile writes must reject exact short Claude aliases (`opus`, `sonnet`, `haiku`) in `defaultModel`, `reviewerModel`, and `escalation.askAi.model`; pod creation must likewise reject them in `model` overrides. Runtime/provider helper alias expansion (defensive read compatibility) may remain internally but is explicitly not a public input contract. Public docs, CLI templates, and Desktop curated pickers must show canonical IDs such as `claude-opus-4-8`. Short alias price rows may remain as a legacy-internal cost shim until cost lookup paths are canonicalized (tracked separately in issue #139).

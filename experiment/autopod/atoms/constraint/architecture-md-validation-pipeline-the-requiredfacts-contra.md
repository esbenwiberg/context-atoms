---
kind: constraint
claim: The `requiredFacts` (contract proof) phase must never be exposed as a skippable
  phase via the `skipValidationPhases` profile setting because it is the durable proof
  layer.
anchors:
- packages/daemon/src/db/migrations/086_profile_skip_validation_phases.sql
- packages/daemon/src/db/migrations/101_pod_contract.sql
- packages/daemon/src/api/schemas.ts
tags:
- validation
- contract
- skip
- constraint
- proof
source: doc-import:ARCHITECTURE.md#validation-pipeline
status: active
---
The `requiredFacts` (contract proof) phase must never be exposed as a skippable phase via the `skipValidationPhases` profile setting because it is the durable proof layer. `skipValidationPhases` accepts `lint`, `sast`, `build`, `test`, `health`, `pages`, `ac`, and `review` — the required-facts phase is deliberately absent from this list. Contract facts serve as tamper-evident proof-of-work that survives across rework cycles; allowing it to be skipped at the profile level would undermine the audit chain. Rejected alternative: adding `facts` as a skip option was intentionally not added to the public schema.

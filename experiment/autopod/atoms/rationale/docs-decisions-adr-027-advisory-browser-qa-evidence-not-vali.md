---
kind: rationale
claim: Advisory browser QA was made evidence-only (not a validation phase) because
  model-driven browser judgment is not durable enough to serve as a merge gate, even
  when deterministic required-fact checks pass.
anchors:
- packages/daemon/src/db/migrations/105_advisory_browser_qa_enabled.sql
- packages/daemon/src/db/migrations/106_profile_advisory_browser_qa_enabled.sql
- packages/daemon/src/interfaces/validation-engine.ts
tags:
- browser-qa
- validation
- advisory
- adr-027
source: doc-import:docs/decisions/ADR-027-advisory-browser-qa-evidence-not-validation.md
status: active
---
Advisory browser QA was made evidence-only (not a validation phase) because model-driven browser judgment is not durable enough to serve as a merge gate, even when deterministic required-fact checks pass. A guided browser pass can capture useful screenshots and observations, but the model's visual judgment can be wrong or inconsistent — making it unsuitable as a blocking proof layer. The rejected alternative was treating browser QA results as a first-class ValidationPhase that could change ValidationResult.overall. Required facts remain the only blocking proof layer; if an advisory concern should block future merges, it must be promoted to a required fact or a narrow human_review item via a contract update.

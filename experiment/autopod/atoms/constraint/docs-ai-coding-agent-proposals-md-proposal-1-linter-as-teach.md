---
kind: constraint
claim: Validation phase results must carry a `remediation` field alongside `stdout`/`stderr`,
  and AI review prompts must explicitly request concrete fix suggestions, not just
  problem descriptions.
anchors:
- packages/daemon/src/interfaces/validation-engine.ts
- packages/daemon/src/pods/validation-repository.ts
tags:
- validation
- schema
- ai-review
- correction-message
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-1-linter-as-teacher-pattern
status: active
---
Validation phase results must carry a `remediation` field alongside `stdout`/`stderr`, and AI review prompts must explicitly request concrete fix suggestions, not just problem descriptions. For build failures, the remediation field is populated by pattern-matching common error types (TypeScript, ESLint, Jest). For test failures, it contains structured data: test name, failing assertion, expected vs actual values. For AI task review failures, the reviewer prompt must be worded to produce actionable suggestions — a description of the problem alone does not satisfy this invariant. All remediation context flows into the correction message sent back to the agent via `buildCorrectionMessage()`.

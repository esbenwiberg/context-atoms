---
kind: rationale
claim: Validation correction messages must embed remediation hints alongside failure
  descriptions because agents currently only learn *what* failed, causing wasted tokens
  and repeated fix attempts.
anchors:
- packages/daemon/src/interfaces/validation-engine.ts
tags:
- validation
- correction-message
- agent-feedback
- linter-as-teacher
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-1-linter-as-teacher-pattern
status: active
---
Validation correction messages must embed remediation hints alongside failure descriptions because agents currently only learn *what* failed, causing wasted tokens and repeated fix attempts. The linter-as-teacher pattern (used by OpenAI custom linters and Stripe) injects explicit fix guidance directly into the error text so the agent reads the failure and knows exactly what to do. Rejected alternative: forwarding raw compiler/test output and letting the agent infer remediation on its own — this burns context and produces inconsistent recovery. The change enriches existing messages without architectural changes: build failures get pattern-matched hints (missing imports, type errors), test failures get structured assertion context (test name, expected vs actual), and AI review phases must ask for concrete fix suggestions rather than problem descriptions.

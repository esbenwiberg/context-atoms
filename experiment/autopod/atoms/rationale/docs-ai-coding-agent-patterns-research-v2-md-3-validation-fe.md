---
kind: rationale
claim: Correction messages on validation failure are intended to teach remediation
  steps, not merely report failure details, so the agent receives actionable fix instructions
  rather than just an error dump.
anchors:
- packages/daemon/src/pods/correction-context.ts
tags:
- validation
- correction
- feedback
- agent-instructions
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#3-validation-feedback-loops
status: active
---
Correction messages on validation failure are intended to teach remediation steps, not merely report failure details, so the agent receives actionable fix instructions rather than just an error dump. This mirrors OpenAI's pattern of injecting remediation instructions directly into agent context when custom linters fail. The buildCorrectionMessage() function is the primary surface for this — it should answer 'how to fix' not just 'what broke'. Rejected alternative: raw stderr/stdout passthrough — agents treat opaque error output as noise and retry identically.

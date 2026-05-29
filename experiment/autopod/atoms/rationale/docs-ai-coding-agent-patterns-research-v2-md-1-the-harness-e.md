---
kind: rationale
claim: "Quality tracking, CLAUDE.md generation guidance, and architectural feedback\
  \ features were prioritised as Autopod improvements because user-facing harness\
  \ quality \u2014 not just orchestration \u2014 was identified as the primary gap."
anchors:
- packages/daemon/src/pods/quality-score.ts
- packages/daemon/src/pods/quality-score-recorder.ts
- packages/daemon/src/pods/quality-signals.ts
- packages/daemon/src/pods/system-instructions-generator.ts
tags:
- quality
- harness-gap
- product-direction
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#1-the-harness-engineering-paradigm
status: active
---
Quality tracking, CLAUDE.md generation guidance, and architectural feedback features were prioritised as Autopod improvements because user-facing harness quality — not just orchestration — was identified as the primary gap. The research concluded Autopod handles the orchestration layer well but leaves users without tooling to build better harnesses inside their own projects (richer CLAUDE.md, architectural guidance, quality signals). This is the explicit rationale behind investment in quality-score, quality-signals, and system-instructions-generator enhancements.

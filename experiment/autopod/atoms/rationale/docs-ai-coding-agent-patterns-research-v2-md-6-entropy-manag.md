---
kind: rationale
claim: The global/profile-scoped memory system is designed to encode 'golden principles'
  injected into every session's system instructions, functioning as automated standards
  enforcement rather than just contextual recall.
anchors:
- packages/daemon/src/pods/memory-selector.ts
- packages/daemon/src/pods/system-instructions-generator.ts
- packages/daemon/src/pods/memory-repository.ts
- packages/daemon/src/pods/memory-extraction.ts
- packages/daemon/src/pods/memory-candidate-recorder.ts
tags:
- memory
- golden-principles
- session-instructions
- profile-scope
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#6-entropy-management-quality-tracking
status: active
---
The global/profile-scoped memory system is designed to encode 'golden principles' injected into every session's system instructions, functioning as automated standards enforcement rather than just contextual recall. The hierarchy (global > profile > pod) reflects the intent that global memory holds repo-wide invariants, profile memory holds team/project standards, and pod memory holds ephemeral task context. When sessions fail, lessons are auto-extracted into profile memory (memory-extraction, memory-candidate-recorder) to close the feedback loop — mirroring the pattern where PR review outcomes feed back into future agent behaviour. Memory selected for injection (memory-selector) must therefore distinguish between recall-only entries and injected-principles entries.

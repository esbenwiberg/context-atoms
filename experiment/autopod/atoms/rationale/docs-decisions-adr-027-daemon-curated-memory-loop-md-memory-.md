---
kind: rationale
claim: Memory curation is daemon-owned (not agent-driven) because agent self-suggestion
  produced a noisy approval queue, while tightening that bar caused useful memories
  to stop appearing entirely.
anchors:
- packages/daemon/src/pods/memory-candidate-recorder.ts
- packages/daemon/src/pods/memory-selector.ts
- packages/daemon/src/pods/system-instructions-generator.ts
- packages/daemon/src/pods/memory-repository.ts
tags:
- memory
- architecture
- reviewer-model
source: doc-import:docs/decisions/ADR-027-daemon-curated-memory-loop.md
status: active
---
Memory curation is daemon-owned (not agent-driven) because agent self-suggestion produced a noisy approval queue, while tightening that bar caused useful memories to stop appearing entirely. The daemon background recorder listens to outcome events, computes lesson potential, and invokes the reviewer model only when evidence crosses a threshold — recording at most one durable profile candidate per pod outcome. Agents may still create pod-scoped ephemeral notes and manually suggest durable memories, but durable learning cannot depend on agents self-filtering perfectly. Rejected alternative: agent-only `memory_suggest` was the original noisy path.

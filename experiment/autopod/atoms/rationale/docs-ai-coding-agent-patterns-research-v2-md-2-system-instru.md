---
kind: rationale
claim: Memory extraction from completed pod sessions is intended to auto-improve agent
  instructions over time, modeled on the pattern of extracting lessons from human
  reviewer feedback into persistent memory entries.
anchors:
- packages/daemon/src/pods/memory-extraction.ts
- packages/daemon/src/pods/memory-candidate-recorder.ts
tags:
- memory
- auto-learning
- sessions
- feedback
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#2-system-instructions-context-engineering
status: active
---
Memory extraction from completed pod sessions is intended to auto-improve agent instructions over time, modeled on the pattern of extracting lessons from human reviewer feedback into persistent memory entries.

Industry basis (Logic Inc pattern): when a PR is merged, a prompt analyzes human reviewer comments and extracts lessons into CLAUDE.md — agent instructions improve automatically from human review feedback without manual edits.

For Autopod: when sessions succeed or fail, lessons are extracted and stored as profile-level or global memory entries. This is why memory extraction runs as part of the pod lifecycle rather than as a one-off administrative task — it is the mechanism for continuous instruction improvement driven by session outcomes.

---
kind: constraint
claim: Human approval for durable memories is mandatory and daemon-auto-generated
  durable candidates are profile-scoped only in v1; the daemon never auto-generates
  global-scoped memories.
anchors:
- packages/daemon/src/pods/memory-candidate-recorder.ts
- packages/daemon/src/pods/memory-candidate-repository.ts
- packages/daemon/src/pods/memory-repository.ts
tags:
- memory
- approval
- scope
- safety
source: doc-import:docs/decisions/ADR-027-daemon-curated-memory-loop.md
status: active
---
Human approval for durable memories is mandatory and daemon-auto-generated durable candidates are profile-scoped only in v1; the daemon never auto-generates global-scoped memories. Durable candidates remain pending until human approval; approval of an overlapping candidate increments the existing memory version rather than creating a duplicate. Global scope is reserved for manual/rare creation because it has the highest blast radius. Auto-disabling stale memories is also deferred to a future version — v1 surfaces staleness evidence for human review only.

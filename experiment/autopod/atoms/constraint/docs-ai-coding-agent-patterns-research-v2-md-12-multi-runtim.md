---
kind: constraint
claim: All model-specific behavior must be encapsulated within a concrete runtime
  implementation; the rest of the daemon must remain model-agnostic and program only
  against the Runtime interface.
anchors:
- packages/daemon/src/interfaces/runtime-registry.ts
- packages/daemon/src/runtimes/
tags:
- constraint
- interface
- model-agnostic
- encapsulation
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#12-multi-runtime-model-agnostic-architecture
status: active
---
All model-specific behavior must be encapsulated within a concrete runtime implementation; the rest of the daemon must remain model-agnostic and program only against the Runtime interface. Leaking provider-specific logic (Claude tool-call formats, Codex event shapes, Copilot auth flows) outside the runtimes/ layer breaks the abstraction and makes model swaps require cross-cutting changes. Stream parsers, state stores, and CLI runners are all scoped per-runtime for the same reason.

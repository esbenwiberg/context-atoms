---
kind: rationale
claim: The event bus uses an edge-triggered (incremental event) model, and a level-triggered
  (full-state snapshot per update) alternative has been identified as preferable for
  reducing client-side reconstruction complexity.
anchors:
- packages/daemon/src/pods/event-bus.ts
tags:
- event-bus
- state-management
- level-triggered
- client-rendering
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#10-agent-reliability-tool-design-ona-todo
status: active
---
The event bus uses an edge-triggered (incremental event) model, and a level-triggered (full-state snapshot per update) alternative has been identified as preferable for reducing client-side reconstruction complexity. Edge-triggered: the client stitches state from discrete events (item added, item completed) — complex, brittle, bug-prone. Level-triggered: every update delivers complete state; the client just renders what it receives, no reconstruction needed. This pattern change was validated by Ona, and the recommendation is to evaluate applying it to session state updates sent to the CLI/desktop.

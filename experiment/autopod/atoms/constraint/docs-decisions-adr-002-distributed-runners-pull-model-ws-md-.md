---
kind: constraint
claim: "The runner\u2013daemon WebSocket protocol uses JSON text frames (with a correlation\
  \ `id`) for control messages and binary frames for workspace tar payloads, where\
  \ binary frames are scoped to the most recent `workspace_*_start` message id."
anchors:
- packages/daemon/src/api/websocket.ts
tags:
- websocket
- protocol
- framing
- correlation-id
- workspace
source: doc-import:docs/decisions/ADR-002-distributed-runners-pull-model-ws.md
status: active
---
The runner–daemon WebSocket protocol uses JSON text frames (with a correlation `id`) for control messages and binary frames for workspace tar payloads, where binary frames are scoped to the most recent `workspace_*_start` message id. Heartbeats fire at an interval specified in the daemon's `welcome` message (default 10 s). The runner reconnects with exponential backoff capped at 30 s on WS close. Streaming exec calls (`execStreaming`) require multi-message chunk/end semantics rather than a single request/response pair, which requires careful protocol handling on both sides.

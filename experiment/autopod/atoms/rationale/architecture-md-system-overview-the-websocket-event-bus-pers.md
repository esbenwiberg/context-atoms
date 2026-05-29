---
kind: rationale
claim: The WebSocket event bus persists events to the database and supports replay
  so late-joining or reconnecting clients receive missed events without re-running
  the pod.
anchors:
- packages/daemon/src/pods/event-bus.ts
- packages/daemon/src/pods/event-repository.ts
tags:
- websocket
- events
- replay
- persistence
source: doc-import:ARCHITECTURE.md#system-overview
status: active
---
The WebSocket event bus persists events to the database and supports replay so late-joining or reconnecting clients receive missed events without re-running the pod. This design was chosen over a pure in-memory pub/sub because operator interfaces (macOS app, CLI, Teams) can disconnect mid-run and need a consistent view of pod history on reconnect. The consequence is that every event emitted during a pod's lifetime must be durable and ordered; ephemeral/fire-and-forget event emission breaks the replay contract.

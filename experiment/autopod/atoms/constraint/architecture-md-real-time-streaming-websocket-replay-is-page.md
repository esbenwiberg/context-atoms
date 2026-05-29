---
kind: constraint
claim: WebSocket replay is paged and hard-capped at 10,000 events; clients that have
  fallen further behind must resync via the REST API rather than through replay.
anchors:
- packages/daemon/src/api/websocket.ts
- packages/daemon/src/pods/event-repository.ts
tags:
- websocket
- replay
- events
- pagination
source: doc-import:ARCHITECTURE.md#real-time-streaming
status: active
---
WebSocket replay is paged and hard-capped at 10,000 events; clients that have fallen further behind must resync via the REST API rather than through replay. The replay mechanism uses monotonic _eventId values on wire events to let clients request events since a given lastEventId. Any code that extends replay must respect the 10,000-event ceiling and must not attempt to serve arbitrarily large catch-ups inline — REST remains the authoritative fallback path for stale clients.

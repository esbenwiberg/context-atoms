---
kind: constraint
claim: All event-bus content must be sanitized via processContentDeep() before being
  broadcast over the WebSocket endpoint to prevent PII leakage.
anchors:
- packages/daemon/src/api/websocket.ts
- packages/daemon/src/pods/event-bus.ts
tags:
- websocket
- pii
- security
- events
source: doc-import:ARCHITECTURE.md#real-time-streaming
status: active
---
All event-bus content must be sanitized via processContentDeep() before being broadcast over the WebSocket endpoint to prevent PII leakage. This applies to every event emitted on the wire regardless of event type or source namespace. Skipping sanitization before broadcast is not acceptable even for system/lifecycle events that appear to contain no user content, because nested fields may carry agent output.

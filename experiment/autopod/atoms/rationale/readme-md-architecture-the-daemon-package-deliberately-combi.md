---
kind: rationale
claim: The daemon package deliberately combines the Fastify HTTP API and the pod orchestration
  loop in a single process rather than splitting them into separate services.
anchors:
- packages/daemon/src/api/server.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- architecture
- daemon
- fastify
- orchestration
source: doc-import:README.md#architecture
status: active
---
The daemon package deliberately combines the Fastify HTTP API and the pod orchestration loop in a single process rather than splitting them into separate services. This means the daemon is simultaneously the REST/WebSocket server consumed by the CLI and web UI, and the process driving pod state machines, container lifecycle, and validation cycles. Any contributor touching API routes or orchestration logic must account for this shared ownership — there is no separate orchestration service to deploy independently.

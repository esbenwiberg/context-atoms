---
kind: rationale
claim: The runner dials out to the daemon over WebSocket (never the reverse) so that
  runners behind NAT or home networks require no inbound firewall holes.
anchors:
- packages/daemon/src/api/websocket.ts
tags:
- networking
- websocket
- nat
- runner
- topology
source: doc-import:docs/decisions/ADR-002-distributed-runners-pull-model-ws.md
status: active
---
The runner dials out to the daemon over WebSocket (never the reverse) so that runners behind NAT or home networks require no inbound firewall holes. Rejected alternatives: (1) daemon pushes over HTTPS REST to the runner — requires inbound reachability on the runner, which breaks NAT/home-network scenarios; (2) gRPC bidi stream — solves the same problem but adds a dependency where WebSocket is already present in the codebase; revisit only if strict typing/codegen is needed. (3) SSE from daemon + HTTPS POSTs from runner — splits the logical stream across two transports, complicates ordering. The outbound-dial pattern matches how GitHub Actions, Buildkite, and Depot runners work.

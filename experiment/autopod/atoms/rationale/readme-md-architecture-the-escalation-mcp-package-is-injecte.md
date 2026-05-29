---
kind: rationale
claim: The escalation-mcp package is injected into agent containers at runtime to
  give agents in-container access to escalation and self-validation tooling, rather
  than routing those calls back through the daemon API.
anchors:
- packages/daemon/src/pods/injection-merger.ts
- packages/daemon/src/api/mcp-handler.ts
- packages/daemon/src/containers/sidecar-manager.ts
tags:
- escalation
- mcp
- container
- agent
- injection
source: doc-import:README.md#architecture
status: active
---
The escalation-mcp package is injected into agent containers at runtime to give agents in-container access to escalation and self-validation tooling, rather than routing those calls back through the daemon API. It is a package that travels with the agent rather than a host-side service, keeping escalation and self-validation latency low and avoiding a round-trip through the daemon for every agent tool call. The daemon's injection-merger and sidecar-manager are the host-side components responsible for wiring this package into new containers.

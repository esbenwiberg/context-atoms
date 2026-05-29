---
kind: rationale
claim: "`@autopod/daemon` is the system's single source of truth \u2014 all state,\
  \ orchestration, and container management is centralized there rather than distributed\
  \ across packages."
anchors:
- packages/daemon/src/
tags:
- daemon
- architecture
- state
- orchestration
source: doc-import:ARCHITECTURE.md#packages
status: active
---
`@autopod/daemon` is the system's single source of truth — all state, orchestration, and container management is centralized there rather than distributed across packages.

This design avoids the split-brain and consistency problems that arise when multiple processes own overlapping state. The CLI, desktop app, and MCP server are all pure clients: they observe daemon state via REST/WebSocket but never mutate it locally. Any new feature that persists data or drives containers must be implemented server-side in the daemon, not in a client package.

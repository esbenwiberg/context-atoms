---
kind: constraint
claim: "`@autopod/cli` must remain a stateless thin client \u2014 it may only call\
  \ the daemon REST API and stream WebSocket events, and must hold no local state\
  \ of its own."
anchors:
- packages/cli/src/index.ts
- packages/cli/src/commands
tags:
- cli
- stateless
- architecture
source: doc-import:ARCHITECTURE.md#packages
status: active
---
`@autopod/cli` must remain a stateless thin client — it may only call the daemon REST API and stream WebSocket events, and must hold no local state of its own.

Any feature that requires persisting state, orchestrating containers, or managing sessions belongs in `@autopod/daemon`, not in the CLI. Adding config caching, local queues, or business logic to the CLI violates this invariant and creates split-brain scenarios where the CLI's view diverges from the daemon's authoritative state.

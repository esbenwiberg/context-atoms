---
kind: constraint
claim: "The monorepo dependency graph must flow strictly: shared \u2190 daemon, cli,\
  \ validator, escalation-mcp; and daemon \u2190 validator, escalation-mcp \u2014\
  \ no reverse or cross-cutting dependencies allowed."
anchors:
- package.json
- packages/cli/package.json
- packages/daemon/package.json
tags:
- monorepo
- dependency-graph
- architecture
source: doc-import:CLAUDE.md#architecture
status: active
---
The monorepo dependency graph must flow strictly: shared ← daemon, cli, validator, escalation-mcp; and daemon ← validator, escalation-mcp — no reverse or cross-cutting dependencies allowed. Adding a dependency from `shared` to `daemon` or `cli`, or from `cli` to `daemon`, would violate this invariant and create circular or unexpected coupling across the workspace packages.

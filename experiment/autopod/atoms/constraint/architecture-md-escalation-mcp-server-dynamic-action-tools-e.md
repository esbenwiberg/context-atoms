---
kind: constraint
claim: Dynamic action tools exposed to agents are generated one-per-ActionDefinition
  from the pod's resolved action policy, making the MCP tool surface profile-scoped
  and not static.
anchors:
- packages/daemon/src/actions/action-engine.ts
- packages/daemon/src/actions/policy-resolver.ts
- packages/daemon/src/actions/action-registry.ts
tags:
- mcp
- actions
- policy
- dynamic-tools
source: doc-import:ARCHITECTURE.md#escalation-mcp-server
status: active
---
Dynamic action tools exposed to agents are generated one-per-ActionDefinition from the pod's resolved action policy, making the MCP tool surface profile-scoped and not static. An agent only sees the tools permitted by its profile's action policy; adding or removing an ActionDefinition in the profile directly changes the available MCP tools at runtime. All invocations are gated, audited, and PII-sanitized before reaching GitHub, ADO, Azure, or configured HTTP endpoints.

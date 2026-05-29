---
kind: rationale
claim: The MCP bridge (mcp-handler / mcp-proxy) exists to give pods native connectivity
  to internal services and databases, because agent output quality is directly bounded
  by what the agent can reach at runtime.
anchors:
- packages/daemon/src/api/mcp-handler.ts
- packages/daemon/src/api/mcp-proxy-handler.ts
- packages/daemon/src/api/mcp-proxy-route.test.ts
tags:
- mcp
- connectivity
- context
- network
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#9-background-agent-infrastructure-patterns-ona-ramp
status: active
---
The MCP bridge (mcp-handler / mcp-proxy) exists to give pods native connectivity to internal services and databases, because agent output quality is directly bounded by what the agent can reach at runtime. Industry research (Stripe's remote devboxes with native monorepo and DB replica access) established the 'Connectivity and context' layer as essential: 'Agent output quality depends on what the agent can reach.' The MCP proxy is the mechanism that bridges the container network boundary to the daemon, enabling pods to call internal APIs and services without relaxing container-level network isolation.

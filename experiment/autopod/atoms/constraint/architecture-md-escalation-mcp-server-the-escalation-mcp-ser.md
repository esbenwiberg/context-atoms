---
kind: constraint
claim: The escalation MCP server authenticates every HTTP call back to the daemon
  using a pod-scoped HMAC token, not a shared secret.
anchors:
- packages/daemon/src/api/mcp-handler.ts
- packages/daemon/src/api/mcp-proxy-handler.ts
tags:
- security
- mcp
- auth
- hmac
source: doc-import:ARCHITECTURE.md#escalation-mcp-server
status: active
---
The escalation MCP server authenticates every HTTP call back to the daemon using a pod-scoped HMAC token, not a shared secret. Each pod receives its own token so that a compromised container cannot impersonate another pod. Any code that validates inbound escalation-MCP requests must verify the HMAC against the pod-specific secret, not a global credential.

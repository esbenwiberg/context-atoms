---
kind: constraint
claim: Blocking MCP tools (ask_human, report_blocker, validate_in_browser) must suspend
  agent execution through a PendingRequests Promise-map and only resume when the daemon
  resolves them via API callback.
anchors:
- packages/daemon/src/pods/pod-bridge-impl.ts
- packages/daemon/src/api/mcp-handler.ts
tags:
- mcp
- blocking
- pending-requests
- escalation
source: doc-import:ARCHITECTURE.md#escalation-mcp-server
status: active
---
Blocking MCP tools (ask_human, report_blocker, validate_in_browser) must suspend agent execution through a PendingRequests Promise-map and only resume when the daemon resolves them via API callback. The agent container awaits the Promise; resolution happens externally when a human responds or a browser check completes. Non-blocking tools (report_plan, report_progress, report_task_summary, check_messages) must NOT use this mechanism — they fire-and-forget or return immediately. Mixing these patterns will either block the agent indefinitely or drop human-in-the-loop responses.

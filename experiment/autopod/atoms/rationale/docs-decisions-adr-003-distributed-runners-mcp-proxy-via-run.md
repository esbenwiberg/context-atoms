---
kind: rationale
claim: Container MCP calls proxy through the runner's loopback (via persistent WebSocket)
  rather than dialing the daemon directly, to avoid coupling container network policy
  to daemon location.
anchors:
- packages/daemon/src/api/mcp-proxy-handler.ts
- packages/daemon/src/api/mcp-proxy-route.test.ts
- packages/daemon/src/api/mcp-handler.ts
tags:
- mcp
- networking
- runner
- proxy
- architecture
source: doc-import:docs/decisions/ADR-003-distributed-runners-mcp-proxy-via-runner.md
status: active
---
Container MCP calls proxy through the runner's loopback (via persistent WebSocket) rather than dialing the daemon directly, to avoid coupling container network policy to daemon location. When a container runs on a remote runner's Docker network, AUTOPOD_CONTAINER_HOST is set to host.docker.internal:<runner-mcp-port> instead of the daemon's public URL. The runner then forwards each HTTP MCP request over its persistent WS connection to the daemon. Rejected alternative: having the container dial the daemon directly via Tailscale/public URL. This was rejected because it requires the daemon's address to be in the container's egress allowlist, and breaks cleanly whenever the daemon moves (e.g., Pi → Azure VM). The proxy approach means container firewall rules never need to know where the daemon lives.

---
kind: constraint
claim: The daemon HTTP server must bind only to loopback (127.0.0.1); mobile/phone
  access must be routed through `tailscale serve`, never by widening HOST to 0.0.0.0.
anchors:
- packages/daemon/src/api/server.ts
- packages/daemon/src/index.ts
tags:
- networking
- security
- mobile
source: doc-import:CLAUDE.md#environment-variables
status: active
---
The daemon HTTP server must bind only to loopback (127.0.0.1); mobile/phone access must be routed through `tailscale serve`, never by widening HOST to 0.0.0.0. Binding to 0.0.0.0 would expose the unauthenticated dev endpoint on all interfaces. The supported pattern for mobile access is documented in docs/mobile.md and uses Tailscale's reverse-proxy instead.

---
kind: constraint
claim: 'The runner must be auth-transparent: it forwards session-scoped Bearer tokens
  to the daemon without intercepting or validating them, so the daemon retains sole
  authority over token verification and runners cannot impersonate sessions.'
anchors:
- packages/daemon/src/api/mcp-proxy-handler.ts
- packages/daemon/src/api/plugins/auth.ts
tags:
- auth
- security
- mcp
- runner
- bearer-token
source: doc-import:docs/decisions/ADR-003-distributed-runners-mcp-proxy-via-runner.md
status: active
---
The runner must be auth-transparent: it forwards session-scoped Bearer tokens to the daemon without intercepting or validating them, so the daemon retains sole authority over token verification and runners cannot impersonate sessions. The existing session-scoped Bearer token auth flow is unchanged by the proxy hop — the runner passes tokens through verbatim. A runner that validates or strips tokens would break this invariant and could create an impersonation vector. This was an explicit design goal stated in ADR-003: 'Runner can't impersonate a session — the Bearer token is validated by the daemon.'

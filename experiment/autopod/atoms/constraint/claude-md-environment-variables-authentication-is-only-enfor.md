---
kind: constraint
claim: Authentication is only enforced when NODE_ENV=production; dev instances run
  without auth by default.
anchors:
- packages/daemon/src/api/plugins/auth.ts
- packages/daemon/src/api/server.ts
tags:
- auth
- security
- dev
source: doc-import:CLAUDE.md#environment-variables
status: active
---
Authentication is only enforced when NODE_ENV=production; dev instances run without auth by default. Any change that gates new functionality on auth checks must still work correctly in both modes — adding a hard auth requirement without a NODE_ENV guard will break local dev. Conversely, never skip the production auth path on the assumption that the daemon won't be publicly reachable.

---
kind: constraint
claim: When NODE_ENV is not 'production', the daemon stubs authentication to accept
  all tokens, bypassing real Entra validation.
anchors:
- packages/daemon/src/index.ts
- packages/daemon/src/api/plugins/auth.ts
tags:
- daemon
- auth
- dev-mode
- security
source: doc-import:CLAUDE.md#daemon-startup-requirements
status: active
---
When NODE_ENV is not 'production', the daemon stubs authentication to accept all tokens, bypassing real Entra validation. This is intentional for local development convenience but means any request is authorised in non-production environments. Code that branches on auth state must never assume the stub is absent in test environments.

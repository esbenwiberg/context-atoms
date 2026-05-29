---
kind: constraint
claim: Fastify HTTP endpoint integration tests must use `app.inject()` rather than
  binding a real port and issuing actual HTTP requests.
anchors:
- packages/daemon/src/integration.test.ts
- packages/daemon/src/api/server.ts
tags:
- testing
- integration
- fastify
- http
source: doc-import:CLAUDE.md#testing-patterns
status: active
---
Fastify HTTP endpoint integration tests must use `app.inject()` rather than binding a real port and issuing actual HTTP requests. This is the pattern established in `packages/daemon/src/integration.test.ts`. Using `app.inject()` keeps tests port-free, avoids OS-level socket conflicts in CI, and exercises the full Fastify plugin/middleware stack (auth, CORS, rate-limit, etc.) without a live server. Tests that spin up a real listener and use `fetch`/`axios` are out of pattern for this codebase.

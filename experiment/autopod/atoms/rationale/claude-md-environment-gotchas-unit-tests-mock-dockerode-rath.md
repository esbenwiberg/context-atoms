---
kind: rationale
claim: Unit tests mock Dockerode rather than calling Docker directly because the CI/dev
  sandbox may not have Docker available at all.
anchors:
- packages/daemon/src/containers/mock-container-manager.ts
- packages/daemon/src/containers/docker-container-manager.test.ts
tags:
- docker
- testing
- mocking
- sandbox
source: doc-import:CLAUDE.md#environment-gotchas
status: active
---
Unit tests mock Dockerode rather than calling Docker directly because the CI/dev sandbox may not have Docker available at all. The daemon requires Docker at runtime, but unit-test suites are deliberately written against the mock-container-manager so they pass in sandboxes without a Docker daemon. Do not add real Docker calls to unit tests; use the mock instead. Integration or e2e tests that genuinely need Docker must be gated on Docker availability.

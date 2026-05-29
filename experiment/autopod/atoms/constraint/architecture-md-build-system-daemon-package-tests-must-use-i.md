---
kind: constraint
claim: Daemon package tests must use in-memory SQLite via `createTestDb()` and must
  never require Docker.
anchors:
- packages/daemon/src
tags:
- testing
- sqlite
- daemon
- no-docker
source: doc-import:ARCHITECTURE.md#build-system
status: active
---
Daemon package tests must use in-memory SQLite via `createTestDb()` and must never require Docker. All test files under packages/daemon/src that exercise database logic must obtain a database handle through `createTestDb()` rather than spinning up an external database or container. This keeps the test suite runnable without any container runtime and is the established pattern across the entire daemon package.

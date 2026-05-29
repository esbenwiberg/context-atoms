---
kind: constraint
claim: All daemon package tests must run against in-memory SQLite; no external database
  process is required or allowed.
anchors:
- packages/daemon/src/**/*.test.ts
tags:
- testing
- sqlite
- daemon
source: doc-import:CLAUDE.md#build-system
status: active
---
All daemon package tests must run against in-memory SQLite; no external database process is required or allowed. This means test fixtures set up and tear down the full schema in-process via the migrate helper, and tests that add new DB state must account for schema migrations being applied fresh each run. Tests must not assume a persistent or shared DB state across test files.

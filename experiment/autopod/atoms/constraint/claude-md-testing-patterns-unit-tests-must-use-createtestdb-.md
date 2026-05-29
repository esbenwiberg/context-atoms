---
kind: constraint
claim: Unit tests must use `createTestDb()` from `packages/daemon/src/test-utils/mock-helpers.ts`
  to set up a real SQLite database with all migrations applied, not an in-memory mock
  or bare schema.
anchors:
- packages/daemon/src/test-utils/mock-helpers.ts
- packages/daemon/src/db/migrations
tags:
- testing
- database
- sqlite
- migrations
source: doc-import:CLAUDE.md#testing-patterns
status: active
---
Unit tests must use `createTestDb()` from `packages/daemon/src/test-utils/mock-helpers.ts` to set up a real SQLite database with all migrations applied, not an in-memory mock or bare schema. The helper also wires in mocked container, runtime, and network infrastructure, so tests get a realistic database layer without requiring Docker or external services. Skipping `createTestDb()` in favor of hand-rolled schemas risks missing schema changes introduced by new migrations and causes divergence between test and production data models.

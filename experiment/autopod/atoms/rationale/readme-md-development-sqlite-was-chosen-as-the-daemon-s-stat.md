---
kind: rationale
claim: SQLite was chosen as the daemon's state store because it requires zero external
  infrastructure while still providing ACID transactions.
anchors:
- packages/daemon/src/db/connection.ts
- packages/daemon/src/db/migrate.ts
- packages/daemon/src/db/backup.ts
tags:
- sqlite
- database
- state
- daemon
source: doc-import:README.md#development
status: active
---
SQLite was chosen as the daemon's state store because it requires zero external infrastructure while still providing ACID transactions. This keeps the daemon self-contained — no separate database process to provision, configure, or connect to — while still guaranteeing consistent pod orchestration state. The tradeoff (no horizontal scale-out) is acceptable because the daemon runs as a single local/per-tenant process.

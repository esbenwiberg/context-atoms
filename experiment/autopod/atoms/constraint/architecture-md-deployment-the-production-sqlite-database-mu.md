---
kind: constraint
claim: The production SQLite database must be persisted by mounting a volume at /data
  and setting DB_PATH=/data/autopod.db.
anchors:
- Dockerfile
- packages/daemon/src/db/connection.ts
tags:
- deployment
- sqlite
- volume
- configuration
source: doc-import:ARCHITECTURE.md#deployment
status: active
---
The production SQLite database must be persisted by mounting a volume at /data and setting DB_PATH=/data/autopod.db. Without this mount, the database lives inside the container layer and is lost on every restart. The environment variable DB_PATH is the single source of truth for the database file location used by the daemon's connection layer.

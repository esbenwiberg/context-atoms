---
kind: constraint
claim: 'The SQLite database must be stored at the path supplied by `DB_PATH`, which
  must resolve inside the `/data` volume mount (default: `/data/autopod.db`).'
anchors:
- Dockerfile
- packages/daemon/src/db/connection.ts
tags:
- sqlite
- persistence
- volume
source: doc-import:CLAUDE.md#docker-production
status: active
---
The SQLite database must be stored at the path supplied by `DB_PATH`, which must resolve inside the `/data` volume mount (default: `/data/autopod.db`). `/data` is the sole declared Docker volume for the production image; placing the database anywhere else risks data loss on container restart because the rest of the filesystem is ephemeral. Deployment configs and compose files must mount a durable volume at `/data` and set `DB_PATH` accordingly.

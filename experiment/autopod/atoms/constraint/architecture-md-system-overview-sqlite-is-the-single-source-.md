---
kind: constraint
claim: "SQLite is the single source of truth for all daemon state \u2014 no secondary\
  \ database is used."
anchors:
- packages/daemon/src/db/
tags:
- database
- sqlite
- state
source: doc-import:ARCHITECTURE.md#system-overview
status: active
---
SQLite is the single source of truth for all daemon state — no secondary database is used. Every persistent entity (pods, profiles, actions, events, security scans, scheduled jobs, memory, etc.) lives in the same SQLite file managed under packages/daemon/src/db/. Adding a new state store outside this boundary violates the architectural invariant and will break the backup/migration pipeline.

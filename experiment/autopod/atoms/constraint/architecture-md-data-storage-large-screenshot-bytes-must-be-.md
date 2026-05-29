---
kind: constraint
claim: Large screenshot bytes must be stored on disk, not in the SQLite database.
anchors:
- packages/daemon/src/pods/screenshot-store.ts
- packages/daemon/src/api/routes/screenshots.ts
- packages/daemon/src/db/migrations/091_drop_screenshot_blobs.sql
tags:
- screenshots
- sqlite
- storage
- blob
source: doc-import:ARCHITECTURE.md#data-storage
status: active
---
Large screenshot bytes must be stored on disk, not in the SQLite database. Storing binary blobs in SQLite inflates the DB file and degrades write/read performance under concurrent pod activity. Migration 091_drop_screenshot_blobs.sql records the deliberate removal of any prior blob column, so any future code that attempts to persist screenshot data back into the DB is a regression against this architectural decision.

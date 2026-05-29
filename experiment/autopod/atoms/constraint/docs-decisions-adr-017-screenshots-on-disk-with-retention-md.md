---
kind: constraint
claim: "Migration 091 uses drop-on-cutover semantics with no backfill \u2014 pre-cutover\
  \ pod screenshots are permanently lost from the UI, and a mandatory DB snapshot\
  \ to `backups/<timestamp>-pre-screenshot-cutover.db` must succeed before the migration\
  \ runs or the migration must not proceed."
anchors:
- packages/daemon/src/db/migrations/091_drop_screenshot_blobs.sql
- packages/daemon/src/db/backup.ts
- packages/daemon/src/db/migrate.ts
tags:
- migration
- screenshots
- data-loss
- rollback
source: doc-import:docs/decisions/ADR-017-screenshots-on-disk-with-retention.md
status: active
---
Migration 091 uses drop-on-cutover semantics with no backfill — pre-cutover pod screenshots are permanently lost from the UI, and a mandatory DB snapshot to `backups/<timestamp>-pre-screenshot-cutover.db` must succeed before the migration runs or the migration must not proceed. The migration drops the `validations.screenshots` column and strips embedded `screenshotBase64` / `screenshot` / `screenshots[]` fields from `validations.result` JSON. There is no plan to ever backfill pre-cutover screenshots. The only rollback path is: stop daemon → restore the pre-migration snapshot → revert daemon/desktop code to a pre-cutover commit → restart. This decision was made intentionally to keep the migration simple; the cost is that support/debugging on pre-cutover pods cannot reach screenshots via the UI.

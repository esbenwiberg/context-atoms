---
kind: constraint
claim: Every migration file under packages/daemon/src/db/migrations/ must have a unique
  numeric prefix; two files sharing a prefix causes the second to be silently skipped
  forever.
anchors:
- packages/daemon/src/db/migrations/
- packages/daemon/src/db/migrate.ts
- .claude/hooks/migration-prefix-check.sh
- .githooks/pre-commit
tags:
- migrations
- sqlite
- schema-version
- data-integrity
source: doc-import:ARCHITECTURE.md#data-storage
status: active
---
Every migration file under packages/daemon/src/db/migrations/ must have a unique numeric prefix; two files sharing a prefix causes the second to be silently skipped forever. The migration runner uses the NNN_ numeric prefix as the schema version key, so a collision does not error — it silently drops the second file on every startup. A pre-commit hook (migration-prefix-check.sh) enforces uniqueness locally, but collisions can still reach the repo if the hook is bypassed or a migration is added outside the normal commit flow.

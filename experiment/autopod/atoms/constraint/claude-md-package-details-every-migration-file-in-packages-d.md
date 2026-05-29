---
kind: constraint
claim: Every migration file in packages/daemon/src/db/migrations/ must have a unique
  numeric prefix; sharing a prefix causes the second file to be silently skipped forever.
anchors:
- packages/daemon/src/db/migrations/
- packages/daemon/src/db/migrate.ts
- .claude/hooks/migration-prefix-check.sh
tags:
- database
- migrations
- schema-versioning
source: doc-import:CLAUDE.md#package-details
status: active
---
Every migration file in packages/daemon/src/db/migrations/ must have a unique numeric prefix; sharing a prefix causes the second file to be silently skipped forever. The migration runner uses the numeric prefix as the schema version identifier. When two files share the same prefix, the runner applies the first one alphabetically and marks that version as done, permanently skipping the second. A local PreToolUse hook (.claude/hooks/migration-prefix-check.sh) blocks Write/Edit on colliding prefixes at commit time, but the cross-branch collision case still requires manual rebase resolution. Always verify the highest existing prefix with `ls packages/daemon/src/db/migrations/ | tail -5` before creating a new migration. Never reuse a number.

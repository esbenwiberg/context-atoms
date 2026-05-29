---
kind: constraint
claim: The scheduled-job DB model tracks catch-up state with a single `catchup_pending
  BOOLEAN`, not a missed-run counter, because only one catch-up run per job is ever
  created.
anchors:
- packages/daemon/src/db/migrations/042_scheduled_jobs.sql
- packages/daemon/src/scheduled-jobs/scheduled-job-repository.ts
tags:
- scheduled-jobs
- db-schema
- catch-up
source: doc-import:docs/decisions/ADR-013-scheduled-pods-one-catchup-prompt-per-job.md
status: active
---
The scheduled-job DB model tracks catch-up state with a single `catchup_pending BOOLEAN`, not a missed-run counter, because only one catch-up run per job is ever created.

The design explicitly rejects storing a count of missed fires. Code that processes catch-up state must not introduce a counter column or attempt to queue multiple sessions for a single job's backlog. The boolean is sufficient: set it when a fire is missed, clear it when the catch-up session is created or declined.

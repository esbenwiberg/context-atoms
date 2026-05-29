---
kind: rationale
claim: The scheduled-jobs system uses a DB-driven 60-second polling loop instead of
  an in-process cron library because node-cron has no persistence and silently misses
  jobs when the daemon restarts.
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-manager.ts
- packages/daemon/src/db/migrations/042_scheduled_jobs.sql
tags:
- scheduler
- persistence
- cron
- restarts
source: doc-import:docs/decisions/ADR-012-scheduled-pods-db-driven-scheduler.md
status: active
---
The scheduled-jobs system uses a DB-driven 60-second polling loop instead of an in-process cron library because node-cron has no persistence and silently misses jobs when the daemon restarts. `next_run_at` is stored in the `scheduled_jobs` table; each poll executes `SELECT * FROM scheduled_jobs WHERE enabled = 1 AND catchup_pending = 0 AND next_run_at <= datetime('now')`. On daemon restart the reconciler detects rows where `next_run_at < now()` and marks them `catchup_pending`, enabling recovery. An external scheduler (cron, GitHub Actions, Lambda) was also rejected because it requires infrastructure the user does not have — the daemon is designed to run locally on a developer laptop. The accepted trade-off is ±60s jitter on fire time, which is acceptable because sub-minute scheduling is not a requirement.

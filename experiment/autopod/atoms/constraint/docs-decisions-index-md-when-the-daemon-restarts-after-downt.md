---
kind: constraint
claim: When the daemon restarts after downtime, a scheduled job receives at most one
  catch-up prompt regardless of how many cron fires were missed during the outage.
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-manager.ts
tags:
- scheduler
- catch-up
- idempotency
source: doc-import:docs/decisions/index.md
status: active
---
When the daemon restarts after downtime, a scheduled job receives at most one catch-up prompt regardless of how many cron fires were missed during the outage. Firing once per missed interval would flood the system with redundant sessions; a single catch-up is enough to re-synchronize state. The scheduler must not iterate over every missed fire window — it must collapse them into a single deferred trigger.

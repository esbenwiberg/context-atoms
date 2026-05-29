---
kind: rationale
claim: Scheduled jobs that miss fires while the daemon is down show exactly one catch-up
  prompt per job, not one per missed fire, to avoid notification floods on restart.
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-manager.ts
tags:
- scheduled-jobs
- catch-up
- ux
source: doc-import:docs/decisions/ADR-013-scheduled-pods-one-catchup-prompt-per-job.md
status: active
---
Scheduled jobs that miss fires while the daemon is down show exactly one catch-up prompt per job, not one per missed fire, to avoid notification floods on restart.

When a daemon restarts after extended downtime, each job with missed fires presents a single prompt: "this job was last run X days ago — run now?" If accepted, one session is created and `next_run_at` advances from `now()` using the cron expression. No replay of missed runs is attempted.

**Rejected alternatives:**
- One prompt per missed fire: correct in theory but unusable — 14 days down = 14 notifications that users dismiss, making the feature feel broken.
- Auto-fire all missed runs on startup: dangerous — could spawn dozens of sessions unexpectedly, hit concurrency limits, consume token budget, and open many PRs without explicit user consent.

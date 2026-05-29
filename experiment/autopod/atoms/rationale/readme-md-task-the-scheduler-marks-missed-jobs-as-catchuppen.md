---
kind: rationale
claim: The scheduler marks missed jobs as catchupPending on daemon restart and requires
  explicit ap schedule catchup review rather than auto-replaying them, to avoid silently
  triggering potentially destructive work without human decision.
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-manager.ts
tags:
- scheduled-jobs
- catchup
- safety
- daemon-restart
source: doc-import:README.md#task
status: active
---
The scheduler marks missed jobs as catchupPending on daemon restart and requires explicit ap schedule catchup review rather than auto-replaying them, to avoid silently triggering potentially destructive work without human decision.

When the daemon restarts mid-window, any cron job whose fire time was missed gets a catchupPending flag set instead of being automatically retried. The operator must run `ap schedule catchup` to interactively review each missed run and decide run or skip. This design trades convenience for safety: scheduled jobs like security audits or dependency upgrades can have side effects (PRs opened, packages updated, alerts sent), and silent auto-replay on restart could cause duplicates or unexpected mutations.

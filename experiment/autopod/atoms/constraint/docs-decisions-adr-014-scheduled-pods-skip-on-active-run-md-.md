---
kind: constraint
claim: A scheduled job must not fire if any non-terminal pod tied to that job already
  exists; the job's next_run_at must still advance normally so the schedule stays
  on track.
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/api/routes/scheduled-jobs.ts
tags:
- scheduled-jobs
- concurrency
- skip-policy
source: doc-import:docs/decisions/ADR-014-scheduled-pods-skip-on-active-run.md
status: active
---
A scheduled job must not fire if any non-terminal pod tied to that job already exists; the job's next_run_at must still advance normally so the schedule stays on track.

Check before each fire:
  SELECT COUNT(*) FROM pods
  WHERE scheduled_job_id = ? AND status NOT IN ('complete', 'failed', 'killed')
If count > 0: skip the fire but still update next_run_at.

For manual catch-up fires (user clicking Run in a desktop notification while the previous run is still active), return HTTP 400 with:
  { error: "Previous run still active — wait for it to complete before catching up." }

This prevents two pods from the same job competing to push the same branch in PR-mode. A very long-running pod may cause many skipped fires; this is observable via GET /scheduled-jobs (lastRunAt goes stale) and is accepted as a known trade-off.

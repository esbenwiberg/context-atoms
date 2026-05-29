---
kind: rationale
claim: Parallel scheduled-job runs were rejected because whether a job is safe to
  parallelize depends on its profile's output mode (PR-mode vs read-only), and that
  distinction is not available at fire time on the job itself.
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-manager.ts
tags:
- scheduled-jobs
- pr-mode
- concurrency
- design-decision
source: doc-import:docs/decisions/ADR-014-scheduled-pods-skip-on-active-run.md
status: active
---
Parallel scheduled-job runs were rejected because whether a job is safe to parallelize depends on its profile's output mode (PR-mode vs read-only), and that distinction is not available at fire time on the job itself.

Read-only jobs (e.g., vuln scans) could safely run in parallel. PR-mode jobs cannot — two pods competing to push the same branch would corrupt history or produce conflicting PRs. Because the output mode lives in the profile (not the scheduled job record), there is no cheap way to gate parallelism per-job without resolving the full profile at fire time.

Killing the previous run and firing a new one was also rejected: users may be actively watching the running pod, and silent unexpected kills are confusing.

The chosen invariant (skip-on-active) is the simplest rule that is safe for all job types without needing to inspect profile state.

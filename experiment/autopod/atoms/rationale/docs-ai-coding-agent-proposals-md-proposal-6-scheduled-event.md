---
kind: rationale
claim: The hardcoded CI-failure fix-session spawning in the merge-polling loop is
  intentionally meant to be collapsed into the generic scheduled-jobs trigger system
  rather than remain a special case.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-manager.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
tags:
- scheduled-jobs
- fix-session
- merge-polling
- refactor
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-6-scheduled-event-triggered-sessions
status: active
---
The hardcoded CI-failure fix-session spawning in the merge-polling loop is intentionally meant to be collapsed into the generic scheduled-jobs trigger system rather than remain a special case. The existing `maybeSpawnFixSession` logic (on check_run.completed with conclusion=failure) was identified as a one-off trigger hardwired into `startMergePolling()`. The design intent is that this becomes an event-trigger consumer — 'on CI failure, spawn fix session' — expressed as configuration rather than code. Keeping it hardcoded would mean every new automated trigger requires a new code path; collapsing it into the trigger system gives the same behaviour without special-casing and validates the trigger abstraction against an already-working flow.

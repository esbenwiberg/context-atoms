---
kind: constraint
claim: When a placement target (e.g. `runner:laptop-ewi`) is offline, sessions must
  queue indefinitely and never be automatically rerouted to a fallback target.
anchors:
- packages/daemon/src/pods/pod-queue.ts
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/pods/runtime-resolver.ts
tags:
- scheduling
- placement
- queuing
- runner
source: doc-import:docs/decisions/ADR-005-distributed-runners-no-auto-spillover.md
status: active
---
When a placement target is offline, sessions must queue indefinitely and never be automatically rerouted to a fallback. The scheduler has no fallback chains, no timeouts, and no priority rules — a session is on the target it was assigned to, full stop. Users can manually retarget a queued session via the session API, but the system itself must not do so automatically. The desktop UI is expected to surface 'target X is offline' so users can act deliberately.

---
kind: rationale
claim: Recovery of orphaned pods re-queues them to `queued` with a `recoveryWorktreePath`
  field rather than introducing a dedicated `resumeSession()` method, to avoid duplicating
  the ~250-line interleaved setup inside `processSession()`.
anchors:
- packages/daemon/src/pods/local-reconciler.ts
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/db/migrations/015_recovery_worktree_path.sql
tags:
- recovery
- restart
- pod-lifecycle
- architecture
source: doc-import:docs/decisions/ADR-007-local-recovery-requeue-not-resume.md
status: active
---
Recovery of orphaned pods re-queues them to `queued` with a `recoveryWorktreePath` field rather than introducing a dedicated `resumeSession()` method, to avoid duplicating the ~250-line interleaved setup inside `processSession()`.

`processSession()` performs worktree creation, network config, skills resolution, CLAUDE.md generation, credentials injection, and registry config before spawning the agent — all of which must also run during recovery (except worktree creation). A `resumeSession()` path would duplicate or re-extract all of this.

Rejected alternative: a separate `resumeSession()` that replays container setup independently.

Trade-off accepted: recovery is not instant (pod waits its turn in the queue), but crash recovery is not latency-sensitive.

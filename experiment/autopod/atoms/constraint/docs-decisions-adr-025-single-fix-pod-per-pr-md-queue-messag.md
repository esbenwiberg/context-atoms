---
kind: constraint
claim: Queue messages in pending_fix_feedback must be deleted from the database only
  after the consuming fix-pod iteration's running transition is committed (delete-after-running
  contract), so that daemon crashes between provisioning and running leave the queue
  intact for free restart recovery.
anchors:
- packages/daemon/src/pods/fix-feedback-repository.ts
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/db/migrations/099_single_fix_pod.sql
tags:
- fix-pod
- queue
- recovery
- sqlite
- invariant
source: doc-import:docs/decisions/ADR-025-single-fix-pod-per-pr.md
status: active
---
Queue messages in pending_fix_feedback must be deleted from the database only after the consuming fix-pod iteration's running transition is committed (delete-after-running contract), so that daemon crashes between provisioning and running leave the queue intact for free restart recovery. FixFeedbackRepository.drain is a single SQLite transaction that runs atomically at the running transition. If the daemon crashes between provisioning and running, the SQLite transaction rolls back and messages remain queued — no dedicated reconciler hook is needed. This aligns with ADR-021 (sleep-recovery via reconcile-on-wake) and ADR-007 (re-queue recovery). Violating this contract (e.g. draining at enqueue time or at provisioning) would silently drop feedback if the daemon restarts mid-iteration.

---
kind: rationale
claim: The single-fix-pod design was chosen over spawning a new child pod per feedback
  round because the legacy spawn model caused PR pile-ups, silent 202 UX failures
  on manual spawn, and ambiguous merge ownership between parent poller and fix pod.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/fix-feedback-repository.ts
- packages/daemon/src/db/migrations/099_single_fix_pod.sql
- packages/daemon/src/db/migrations/077_reuse_fix_pod.sql
tags:
- fix-pod
- merge
- queue
- design
source: doc-import:docs/decisions/ADR-025-single-fix-pod-per-pr.md
status: active
---
The single-fix-pod design was chosen over spawning a new child pod per feedback round because the legacy spawn model caused PR pile-ups, silent 202 UX failures on manual spawn, and ambiguous merge ownership between parent poller and fix pod. Specifically: (1) with reuseFixPod:false (the historical default), N children per PR accumulated on the same branch causing merge conflicts; (2) maybeSpawnFixSession silently no-oped when a fix pod was alive — POST /spawn-fix returned 202 but nothing happened; (3) both the parent's startMergePolling and the fix pod's approveSession called mergePr, making merge ownership unclear. The rejected alternative (deduplicate-at-spawn-layer) would have left the silent-no-op and dual-ownership bugs; live MCP injection was rejected because it breaks the 'task is the contract' model and makes work-product depend on queue timing.

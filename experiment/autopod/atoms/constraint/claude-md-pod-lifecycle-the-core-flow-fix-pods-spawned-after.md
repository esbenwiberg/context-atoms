---
kind: constraint
claim: Fix pods spawned after merge failures or CHANGES_REQUESTED review comments
  are capped at maxPrFixAttempts (default 3) total attempts.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- fix-pod
- retry
- merge
- pr
source: doc-import:CLAUDE.md#pod-lifecycle-the-core-flow
status: active
---
Fix pods spawned after merge failures or CHANGES_REQUESTED review comments are capped at maxPrFixAttempts (default 3) total attempts. The merge_pending state is the branching point: pod-manager.ts:startMergePolling() polls PR status every 60 s and calls maybeSpawnFixPod() when it detects an actionable failure (CI failure or CHANGES_REQUESTED). Each spawned fix pod counts against the cap; once exhausted the pod transitions to failed rather than spawning another fix pod. The cap exists to prevent infinite retry loops on unfixable failures.

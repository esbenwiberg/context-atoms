---
kind: constraint
claim: Fix pods must push to the same branch as the original pod, not a new branch.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- fix-pod
- branch
- pr
source: doc-import:README.md#how-it-works
status: active
---
Fix pods must push to the same branch as the original pod, not a new branch.

When a pod's PR is blocked — by CI failures, failing checks, or CHANGES_REQUESTED review comments — the daemon spawns a fix pod automatically. The fix pod receives the original task brief plus sanitized failure summaries and reviewer notes, and it pushes its corrections to the same branch. This keeps the PR open and the review thread intact rather than opening a parallel PR.

The cycle repeats up to `maxPrFixAttempts` (default: 3). Violating this by targeting a different branch would break the PR-fix loop and orphan reviewer comments.

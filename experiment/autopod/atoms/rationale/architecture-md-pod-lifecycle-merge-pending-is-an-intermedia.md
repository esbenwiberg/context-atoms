---
kind: rationale
claim: '`merge_pending` is an intermediate state introduced specifically to serialize
  the window between PR creation and merge confirmation, preventing race conditions.'
anchors:
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- pod-lifecycle
- merge
- race-condition
source: doc-import:ARCHITECTURE.md#pod-lifecycle
status: active
---
`merge_pending` is an intermediate state introduced specifically to serialize the window between PR creation and merge confirmation, preventing race conditions. Without it, two concurrent processes could both observe a PR as unmerged and attempt to act on it. A fix pod is spawned from `merge_pending` when CI fails or review comments arrive.

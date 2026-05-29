---
kind: constraint
claim: A pod reaching the `validated` state never triggers an automatic merge; an
  explicit `ap approve` command is always required before anything merges.
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/db/migrations/027_merge_pending.sql
tags:
- merge
- approval
- workflow
- safety
source: doc-import:README.md#faq
status: active
---
A pod reaching the `validated` state never triggers an automatic merge; an explicit `ap approve` command is always required before anything merges. `validated` means autopod's own quality checks passed — it is not a merge signal. Any code path that would merge a PR without going through the approve flow (e.g. auto-merging on validation success) violates this invariant. The distinction between `validated` and `merge_pending`/merged states must be preserved in the state machine.

---
kind: constraint
claim: Only one fix pod may exist per PR at any time; it must be recycled across all
  PR-review feedback rounds rather than spawning a fresh fix pod per failure.
anchors:
- packages/daemon/src/db/migrations/099_single_fix_pod.sql
- packages/daemon/src/db/migrations/077_reuse_fix_pod.sql
- packages/daemon/src/pods/pod-manager.ts
tags:
- fix-pod
- pr
- lifecycle
source: doc-import:docs/decisions/index.md
status: active
---
Only one fix pod may exist per PR at any time; it must be recycled across all PR-review feedback rounds rather than spawning a fresh fix pod per failure. Previously a new fix pod was spawned for each actionable PR failure, which caused resource waste and lost context between rounds. The single-fix-pod invariant (migration 099) means pod-manager logic must look up and reuse an existing fix pod for a PR before ever creating a new one, and any path that would spawn a second concurrent fix pod for the same PR is a bug.

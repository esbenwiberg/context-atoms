---
kind: constraint
claim: In `single` PR mode only the leaf (final) pod creates a PR; in `stacked` mode
  each pod gets its own PR and non-root pods must not start until the parent pod's
  PR has merged; in `none` mode pods push branches but never open PRs.
anchors:
- packages/daemon/src/db/migrations/067_pod_pr_mode.sql
- packages/daemon/src/db/migrations/052_pod_wait_for_merge.sql
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/pod-repository.ts
tags:
- series
- pr-mode
- single
- stacked
- none
- merge-gating
source: doc-import:ARCHITECTURE.md#series-workflows
status: active
---
In `single` PR mode only the leaf (final) pod creates a PR; in `stacked` mode each pod gets its own PR and non-root pods must not start until the parent pod's PR has merged; in `none` mode pods push branches but never open PRs. These are the only three valid PR modes — any new pod-spawning logic must branch on exactly these values. The merge-gating invariant for `stacked` is critical: violating it would cause non-root pods to start on a base branch that does not yet contain the parent's changes, producing incorrect diffs and broken dependency chains.

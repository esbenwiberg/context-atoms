---
kind: constraint
claim: After validation completes, the pod's container must be stopped but not removed,
  so an on-demand preview can be launched against the agent's work before approval.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/pods/preview-supervisor.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- container
- preview
- lifecycle
source: doc-import:README.md#how-it-works
status: active
---
After validation completes, the pod's container must be stopped but not removed, so an on-demand preview can be launched against the agent's work before approval.

Once the validation pipeline finishes (pass or fail), the container transitions to stopped state. Removing it at this point would destroy the filesystem snapshot that a preview session depends on. The operator or reviewer can launch an on-demand preview — a live browser session against the container — before running `ap approve`. Only after the pod reaches a terminal state (complete, killed) can the container be safely removed.

This constraint means container cleanup logic must check pod state before tearing down, and must not conflate 'validation done' with 'container no longer needed'.

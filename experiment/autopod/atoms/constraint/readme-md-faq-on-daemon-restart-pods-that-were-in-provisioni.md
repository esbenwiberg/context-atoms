---
kind: constraint
claim: On daemon restart, pods that were in `provisioning` or `running` state at shutdown
  must be re-attached to their existing containers rather than re-created, so in-progress
  agent work is not lost.
anchors:
- packages/daemon/src/pods/local-reconciler.ts
- packages/daemon/src/pods/reconciler.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- recovery
- resilience
- daemon
- pod-lifecycle
source: doc-import:README.md#faq
status: active
---
On daemon restart, pods that were in `provisioning` or `running` state at shutdown must be re-attached to their existing containers rather than re-created, so in-progress agent work is not lost. The reconciler is responsible for scanning persisted pod state on startup and re-establishing container attachment for any pod that did not reach a terminal state. Creating a new container for such pods (instead of reattaching) would silently discard the agent's ongoing work.

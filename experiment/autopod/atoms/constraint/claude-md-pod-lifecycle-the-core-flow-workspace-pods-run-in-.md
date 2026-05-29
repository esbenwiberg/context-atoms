---
kind: constraint
claim: Workspace pods run in interactive mode with no agent and must auto-push their
  branch on exit, bypassing the validating/approved/merging states entirely.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- workspace-pod
- interactive
- lifecycle
- state-machine
source: doc-import:CLAUDE.md#pod-lifecycle-the-core-flow
status: active
---
Workspace pods run in interactive mode with no agent and must auto-push their branch on exit, bypassing the validating/approved/merging states entirely. Their lifecycle is strictly queued → provisioning → running → complete. The 'running' state is interactive (human-driven), so no agent loop executes. On exit, the branch is automatically pushed. Any code path that assumes a pod will pass through validation or merging states must first check whether the pod is a workspace pod.

---
kind: constraint
claim: During pod provisioning the PAT must be stripped from the remote URL before
  the container starts.
anchors:
- packages/daemon/src/pods/pod-manager.ts
tags:
- security
- provisioning
- pat
source: doc-import:ARCHITECTURE.md#orchestration-loop
status: active
---
During pod provisioning the PAT must be stripped from the remote URL before the container starts. The bare repo is cloned with the credential-bearing URL, then the remote is rewritten to a PAT-free form so the running container never holds a live token in its git config. Failing to strip the PAT would expose credentials inside the container's process environment and git history.

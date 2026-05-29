---
kind: rationale
claim: The thin-runner design was chosen to mirror the already-established AciContainerManager
  pattern, which is itself a thin executor that delegates all git and PR logic to
  the daemon.
anchors:
- packages/daemon/src/containers/aci-container-manager.ts
- packages/daemon/src/interfaces/container-manager.ts
tags:
- runner
- aci
- container-manager
- consistency
source: doc-import:docs/decisions/ADR-001-distributed-runners-thin-runner.md
status: active
---
The thin-runner design was chosen to mirror the already-established AciContainerManager pattern, which is itself a thin executor that delegates all git and PR logic to the daemon. The ContainerManager interface is transport-agnostic by design, making the thin-runner mapping straightforward. This consistency means daemon-only deployment changes (Raspberry Pi, Azure VM) do not require corresponding runner changes, and the runner package stays small and easy to install on new hosts.

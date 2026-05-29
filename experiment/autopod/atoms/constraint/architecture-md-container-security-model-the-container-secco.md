---
kind: constraint
claim: The container seccomp profile must block both container-escape syscalls (`unshare`,
  `setns`, `pivot_root`, `mount`) and `AF_ALG` sockets (kernel crypto API).
anchors:
- packages/daemon/src/containers/seccomp-profile.json
- packages/daemon/src/containers/docker-container-manager.ts
tags:
- seccomp
- security
- container
- syscall
source: doc-import:ARCHITECTURE.md#container-security-model
status: active
---
The container seccomp profile must block both container-escape syscalls (`unshare`, `setns`, `pivot_root`, `mount`) and `AF_ALG` sockets (kernel crypto API). The escape syscalls prevent a compromised agent from re-entering the host namespace. `AF_ALG` is blocked because it exposes the kernel's crypto subsystem as a socket interface, which has been a source of kernel exploits and is not needed by agent workloads. Any change to `seccomp-profile.json` that re-enables these must be treated as a security regression.

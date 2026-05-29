---
kind: rationale
claim: Each agent task runs in its own isolated container so that dozens of agents
  can execute concurrently across repos and runtimes without interfering with each
  other or the host environment.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/containers/aci-container-manager.ts
- packages/daemon/src/containers/docker-network-manager.ts
tags:
- architecture
- containers
- isolation
- concurrency
source: doc-import:README.md
status: active
---
Each agent task runs in its own isolated container so that dozens of agents can execute concurrently across repos and runtimes without interfering with each other or the host environment. The dual container-manager implementations (Docker for local, ACI for cloud) both exist to enforce this isolation boundary. Running agents share nothing at the OS layer; isolation is the primary reason containers were chosen over in-process execution or shared VMs. Rejected alternative: a shared execution environment would be simpler but would allow one agent's file-system mutations, environment variables, or installed dependencies to corrupt another agent's run.

---
kind: constraint
claim: The thin-runner workspace-tar transfer design is valid only while repos remain
  under ~500 MB; if any repo grows past 1 GB this architectural decision must be revisited.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/containers/aci-container-manager.ts
tags:
- runner
- performance
- scalability
- workspace
source: doc-import:docs/decisions/ADR-001-distributed-runners-thin-runner.md
status: active
---
The thin-runner workspace-tar transfer design is valid only while repos remain under ~500 MB; if any repo grows past 1 GB this architectural decision must be revisited. The decision memo explicitly notes that typical workspace tar transfers over Tailscale run ~30 seconds for repos in this size range, which was deemed acceptable. The memo flags > 1 GB as the threshold where the transfer cost becomes prohibitive and a thick-runner (or hybrid) approach should replace the current design. Additionally, the daemon must remain reachable throughout upload/download; a network blip during transfer can fail the session.

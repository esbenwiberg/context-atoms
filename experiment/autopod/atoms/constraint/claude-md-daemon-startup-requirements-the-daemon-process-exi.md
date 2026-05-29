---
kind: constraint
claim: The daemon process exits at startup if the Docker socket is unreachable, checked
  via a ping before any other initialisation.
anchors:
- packages/daemon/src/index.ts
tags:
- daemon
- startup
- docker
- fail-fast
source: doc-import:CLAUDE.md#daemon-startup-requirements
status: active
---
The daemon process exits at startup if the Docker socket is unreachable, checked via a ping before any other initialisation. This means the host must have a running Docker daemon and the socket must be accessible to the process (e.g. mounted into a container). There is no graceful degradation — a missing socket is a hard stop.

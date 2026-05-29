---
kind: rationale
claim: tini is used as the container init process in the production image specifically
  to ensure correct signal forwarding and zombie-process reaping inside Docker.
anchors:
- Dockerfile
tags:
- deployment
- docker
- signals
- tini
source: doc-import:ARCHITECTURE.md#deployment
status: active
---
tini is used as the container init process in the production image specifically to ensure correct signal forwarding and zombie-process reaping inside Docker. Node.js running as PID 1 does not handle SIGTERM/SIGINT the same way a real init process does, which can cause unclean shutdowns and orphaned child processes. tini acts as a minimal init that forwards signals to the Node process and reaps zombies, enabling graceful container shutdown.

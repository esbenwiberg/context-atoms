---
kind: constraint
claim: The production container must run as the non-root user `autopod` with UID 1000
  and use tini as PID 1 for correct signal handling.
anchors:
- Dockerfile
tags:
- docker
- security
- signals
source: doc-import:CLAUDE.md#docker-production
status: active
---
The production container must run as the non-root user `autopod` with UID 1000 and use tini as PID 1 for correct signal handling. Running non-root limits blast radius if the container is compromised. Tini is required because Node.js does not reap zombie processes or forward signals correctly when it is PID 1, which causes unclean shutdowns in container orchestrators. Any change to the production stage of the Dockerfile must preserve both the `USER autopod:1000` directive and the tini entrypoint.

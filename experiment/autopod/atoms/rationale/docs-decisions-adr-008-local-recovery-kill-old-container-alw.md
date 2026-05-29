---
kind: rationale
claim: After daemon restart, orphaned Docker containers are always killed and a fresh
  container is spawned rather than reused, because the worktree bind-mount preserves
  all file state and container reuse has an unacceptably large failure surface.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/pods/local-reconciler.ts
- packages/daemon/src/pods/recovery-context.ts
tags:
- recovery
- containers
- docker
- restart
source: doc-import:docs/decisions/ADR-008-local-recovery-kill-old-container-always.md
status: active
---
After daemon restart, orphaned Docker containers are always killed and a fresh container is spawned rather than reused, because the worktree bind-mount preserves all file state and container reuse has an unacceptably large failure surface.

Alternative considered: exec into the still-running container to resume work.

Rejected because: reuse requires checking container health and leaves stale env vars, broken network config, zombie agent processes, and expired credentials in the container environment. The code complexity for safely detecting and handling all those failure modes outweighs the ~2-3s extra startup time.

Fresh spawn benefits: gets the latest image, a clean process tree, and freshly written credentials/CLAUDE.md/skills/registry config — all with no special-case handling.

---
kind: constraint
claim: "Container-only state \u2014 any files or processes living outside the /workspace\
  \ bind-mount \u2014 is ephemeral by design and must never be relied upon to survive\
  \ a pod recovery or daemon restart."
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/pods/recovery-context.ts
- packages/daemon/src/pods/local-reconciler.ts
tags:
- recovery
- containers
- state
- ephemeral
- invariant
source: doc-import:docs/decisions/ADR-008-local-recovery-kill-old-container-always.md
status: active
---
Container-only state — any files or processes living outside the /workspace bind-mount — is ephemeral by design and must never be relied upon to survive a pod recovery or daemon restart.

The ADR-008 decision to always kill and respawn containers is predicated on this invariant: anything worth keeping must be written into the worktree (under /workspace). If any feature stores durable state inside the container but outside /workspace, it will silently vanish on recovery, violating the assumption that recovery is lossless for the working tree.

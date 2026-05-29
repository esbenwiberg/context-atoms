---
kind: constraint
claim: Containers must be designed to be trivially discarded and recreated if they
  enter a bad state, rather than attempting in-place recovery.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/pods/recovery-context.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- containers
- recovery
- disposable
- resilience
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#5-container-isolation-environment-design
status: active
---
Containers must be designed to be trivially discarded and recreated if they enter a bad state, rather than attempting in-place recovery. This is the 'disposable-first' principle derived from Stripe's devbox model, where a bad-state devbox is simply discarded. Recovery logic that tries to repair a compromised or wedged container adds complexity and risk; the right answer is a clean slate. See `pod_worktree_compromised` flag (migration 056) and `recovery-context.ts` — these exist, but the architecture goal is to make discard+recreate so cheap that recovery is rarely needed.

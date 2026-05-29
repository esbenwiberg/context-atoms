---
kind: rationale
claim: Sleep recovery reuses the existing reconcileLocalSessions() path rather than
  forgiving timestamps or introducing a new paused state, because dead LLM TCP sockets
  cannot be healed by bumping watchdog references, and a new sleep-paused state would
  duplicate ADR-006's never-built runner_offline concept for no added user value.
anchors:
- packages/daemon/src/pods/local-reconciler.ts
- packages/daemon/src/pods/sleep-detector.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- sleep-recovery
- reconciler
- adr
source: doc-import:docs/decisions/ADR-021-sleep-recovery-via-reconcile-on-wake.md
status: active
---
Sleep recovery reuses the existing reconcileLocalSessions() path rather than forgiving timestamps or introducing a new paused state, because dead LLM TCP sockets cannot be healed by bumping watchdog references, and a new sleep-paused state would duplicate ADR-006's never-built runner_offline concept for no added user value. Option A (forgive timestamps) leaves the dead Anthropic/OpenAI/Copilot stream in place; existing retry budgets were not designed for multi-hour gaps and pods would limp or hang. Option C (explicit paused state) adds a new state, transitions, and UI handling to model something the reconciler-on-restart pattern already handles correctly. The chosen path (Option B) kills old containers, spawns fresh ones, and bind-mounts the existing worktree so Claude pods can resume via --resume <claude_session_id>; non-Claude runtimes receive a wake-correction postscript pointing at git log / git diff main.

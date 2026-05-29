---
kind: rationale
claim: The `runner_offline` pod state was chosen over fail-fast or SIGSTOP/SIGCONT
  because laptops disconnect predictably (sleep, Wi-Fi, Tailscale) and resuming on
  reconnect avoids aborting work every time the user closes the lid.
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/local-reconciler.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- runner-offline
- state-machine
- reconnect
- laptop
source: doc-import:docs/decisions/ADR-006-distributed-runners-runner-offline-state.md
status: active
---
The `runner_offline` pod state was chosen over fail-fast or SIGSTOP/SIGCONT because laptops disconnect predictably (sleep, Wi-Fi, Tailscale) and resuming on reconnect avoids aborting work every time the user closes the lid.

Rejected alternatives:
- Fail-fast (option 1): simpler, but aborts and requires manual retry on every lid-close — bad UX for the primary laptop workflow.
- SIGSTOP/SIGCONT (option 3): requires detecting *imminent* disconnect, which laptops do not provide; engineering fiction.

The chosen approach keeps the container alive on the runner across brief disconnects, reconciles container liveness on reconnect, and surfaces an explicit 'runner offline — waiting for reconnect' UI state. Sessions stuck offline for an extended period should expose a timestamp so users can kill stale ones.

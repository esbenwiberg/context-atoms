---
kind: constraint
claim: "The pod state machine must enforce exactly four `runner_offline` transitions:\
  \ running\u2192runner_offline on WS drop, runner_offline\u2192running if container\
  \ is still running on reconnect, runner_offline\u2192failed if container is stopped/unknown\
  \ on reconnect, and runner_offline\u2192killing on explicit user kill."
anchors:
- packages/daemon/src/pods/state-machine.ts
tags:
- runner-offline
- state-machine
- transitions
source: doc-import:docs/decisions/ADR-006-distributed-runners-runner-offline-state.md
status: active
---
The pod state machine must enforce exactly four `runner_offline` transitions: running→runner_offline on WS drop, runner_offline→running if container is still running on reconnect, runner_offline→failed if container is stopped/unknown on reconnect, and runner_offline→killing on explicit user kill.

Edge cases that reconciliation logic must handle:
- Container restarted with a different ID between disconnect and reconnect.
- Runner's Docker state drifted from daemon's last known state.
- Container exit events missed during the network partition.

No other transitions into or out of `runner_offline` are valid; adding new ones requires updating state-machine, the valid-transitions constant list, and runtime handling together.

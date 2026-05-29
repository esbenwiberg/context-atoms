---
kind: constraint
claim: Pod status must never be set directly on the pod object; all status transitions
  must go through updateStatus() in pod-repository.ts.
anchors:
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- pods
- state-machine
- status-transitions
source: doc-import:CLAUDE.md#package-details
status: active
---
Pod status must never be set directly on the pod object; all status transitions must go through updateStatus() in pod-repository.ts. The state-machine module (state-machine.ts) exposes validateTransition() and canX() helpers that enforce valid transition paths. Bypassing updateStatus() skips these guards, leaving the pod in an inconsistent state that the rest of the system (event-bus, reconciler, WebSocket layer) will not handle correctly. The valid status transition map is defined in @autopod/shared src/constants.ts as VALID_STATUS_TRANSITIONS.

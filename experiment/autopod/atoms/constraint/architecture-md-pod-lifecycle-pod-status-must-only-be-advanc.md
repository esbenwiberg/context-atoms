---
kind: constraint
claim: "Pod status must only be advanced through `updateStatus()` in pod-repository.ts\
  \ \u2014 no other code path may write pod state."
anchors:
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- pod-lifecycle
- state-machine
- invariant
source: doc-import:ARCHITECTURE.md#pod-lifecycle
status: active
---
Pod status must only be advanced through `updateStatus()` in pod-repository.ts — no other code path may write pod state. All transitions are validated against `VALID_STATUS_TRANSITIONS` before every write, enforcing the finite state machine. Direct status assignment anywhere else in the codebase is forbidden.

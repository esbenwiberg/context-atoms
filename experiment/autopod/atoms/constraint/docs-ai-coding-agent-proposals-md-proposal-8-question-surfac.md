---
kind: constraint
claim: When the question-surfacing heuristic fires, the pod/session state MUST remain
  `running`; the emitted `AGENT_LIKELY_WAITING` event is a pure UX signal and must
  never trigger a state transition.
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/event-bus.ts
tags:
- state-machine
- AGENT_LIKELY_WAITING
- question-detection
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-8-question-surfacing-heuristic
status: active
---
When the question-surfacing heuristic fires, the pod/session state MUST remain `running`; the emitted `AGENT_LIKELY_WAITING` event is a pure UX signal and must never trigger a state transition. The heuristic is explicitly described as a soft-pending hint, not a lifecycle event — the session keeps running, the agent is not blocked, and no `awaiting_input` state is entered. Introducing a state transition here would break the lifecycle contract: the agent may never actually be waiting (false positives are expected) and forcing a pause would stall work unnecessarily.

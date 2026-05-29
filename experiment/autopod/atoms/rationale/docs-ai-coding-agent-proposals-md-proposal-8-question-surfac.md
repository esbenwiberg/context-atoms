---
kind: rationale
claim: "Question-surfacing uses a two-layer defense \u2014 a runtime pattern detector\
  \ plus reinforcement in system instructions \u2014 because agents inevitably drift\
  \ from prompt instructions over long sessions and no system prompt alone can eliminate\
  \ this failure mode."
anchors:
- packages/daemon/src/pods/system-instructions-generator.ts
- packages/daemon/src/pods/event-bus.ts
tags:
- agent-drift
- ask_human
- system-instructions
- defense-in-depth
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-8-question-surfacing-heuristic
status: active
---
Question-surfacing uses a two-layer defense — a runtime pattern detector plus reinforcement in system instructions — because agents inevitably drift from prompt instructions over long sessions and no system prompt alone can eliminate this failure mode. Layer 1: system instructions strongly prefer `ask_human` over inline questions and explicitly warn the agent that inline questions may go unseen (citing the heuristic). Layer 2: the runtime detector catches drift regardless of instruction adherence. The single-layer alternative (prompt-only) was rejected based on operational experience across agent frameworks: prompt rigor reduces but never eliminates inline-question drift over long sessions.

---
kind: constraint
claim: Agent certainty is a three-value enum (detected/suspected/uncertain), not a
  float, and the decision engine rejects any 'detected' claim that lacks supporting
  evidence.
anchors:
- src/pr_guardian/decision/types.py
- src/pr_guardian/decision/validator.py
- src/pr_guardian/decision/engine.py
tags:
- certainty
- validation
- agents
source: doc-import:docs/plan/00-overview.md
status: active
---
Agent certainty is a three-value enum (detected/suspected/uncertain), not a float, and the decision engine rejects any 'detected' claim that lacks supporting evidence.

The enum was chosen over a continuous score to force agents to make a discrete, defensible claim rather than hedging with a probability. The validator enforces that 'detected' verdicts are accompanied by concrete findings/quotes; agents cannot escalate certainty without showing their work. This shapes how agent output structs must be defined and how the validator must check them.

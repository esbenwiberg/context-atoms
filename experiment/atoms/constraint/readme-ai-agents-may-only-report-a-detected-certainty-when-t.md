---
kind: constraint
claim: AI agents may only report a 'detected' certainty when they can cite concrete
  evidence; unsubstantiated claims must be downgraded to 'suspected' or 'uncertain'.
anchors:
- src/pr_guardian/agents/base.py
- src/pr_guardian/decision/validator.py
- src/pr_guardian/models/findings.py
tags:
- agents
- certainty
- verdicts
- evidence
source: doc-import:README.md
status: active
---
Each AI review agent returns a verdict paired with a certainty level: 'detected', 'suspected', or 'uncertain'. Agents are required to show their work — a 'detected' verdict is only valid when the agent supplies traceable evidence (e.g., a file/line reference or quoted snippet). The decision validator enforces this; unsubstantiated 'detected' claims must be treated as invalid and downgraded. This invariant exists to prevent the decision engine from hard-blocking or escalating PRs based on hallucinated findings.

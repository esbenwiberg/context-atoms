---
kind: rationale
claim: The triage engine is deterministic rule-based code (not an AI agent) to avoid
  paying agent invocation costs on low-risk PRs.
anchors:
- src/pr_guardian/triage/classifier.py
tags:
- triage
- cost
- architecture
source: doc-import:docs/plan/03-triage.md
status: active
---
The triage engine is deterministic rule-based code (not an AI agent) to avoid paying agent invocation costs on low-risk PRs. A 1-line typo fix should not trigger 5 agent calls. All AI cost is deferred to the agents that triage selects. The triage layer itself must never call an LLM.

---
kind: constraint
claim: Agent output must never include a risk_score field; numeric scoring is derived
  deterministically by the decision engine from structured findings.
anchors:
- src/pr_guardian/models/output.py
- src/pr_guardian/decision/engine.py
- src/pr_guardian/agents/base.py
tags:
- agent-output
- scoring
- decision-engine
source: doc-import:docs/plan/04-ai-agents.md
status: active
---
Agent output must never include a risk_score field; numeric scoring is derived deterministically by the decision engine from structured findings. Each agent returns verdict, languages_reviewed, findings (with severity/certainty/category/evidence_basis), and cross_language_findings — nothing more. The decision engine owns all numeric aggregation. This prevents LLMs from producing unreliable numeric confidence values while still enabling weighted scoring downstream.

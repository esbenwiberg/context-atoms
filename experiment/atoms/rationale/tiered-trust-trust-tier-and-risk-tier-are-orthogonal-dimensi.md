---
kind: rationale
claim: 'Trust tier and risk tier are orthogonal dimensions: risk tier controls how
  hard the AI looks, while trust tier controls who reviews and what role the AI plays
  (preliminary reviewer vs. review tool).'
anchors:
- src/pr_guardian/triage/trust_classifier.py
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/types.py
tags:
- trust-tier
- risk-tier
- design
- ai-role
source: doc-import:docs/plan/tiered-trust.md
status: active
---
Trust tier and risk tier are orthogonal dimensions: risk tier controls how hard the AI looks, while trust tier controls who reviews and what role the AI plays (preliminary reviewer vs. review tool).

Risk tier (TRIVIAL/LOW/MEDIUM/HIGH) determines pipeline depth — which agents run and how thoroughly.

Trust tier (AI_ONLY/SPOT_CHECK/MANDATORY_HUMAN/HUMAN_PRIMARY) determines the review outcome and AI behaviour:
- AI_ONLY: AI is sole decision-maker, auto-approves if clean.
- SPOT_CHECK: AI auto-approves but requests optional human attention with a short spot-check summary.
- MANDATORY_HUMAN: AI never auto-approves; produces a structured reviewer briefing so the human starts with context.
- HUMAN_PRIMARY: AI never auto-approves; routes to a specific reviewer group (e.g., security-team) with a security-specific checklist briefing.

The distinction matters because a HIGH-risk change can still be AI_ONLY (e.g., a complex but purely internal refactor with no security surface), and a LOW-risk change can be HUMAN_PRIMARY (e.g., a one-line change to a JWT signing key).

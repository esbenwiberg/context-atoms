---
kind: rationale
claim: The decision engine computes risk scores deterministically from structured
  findings rather than asking LLMs to return numeric confidence values.
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/types.py
tags:
- scoring
- deterministic
- llm
- design
source: doc-import:docs/plan/05-decision-engine.md
status: active
---
The decision engine computes risk scores deterministically from structured findings rather than asking LLMs to return numeric confidence values. LLMs produce unreliable confidence numbers, so scoring is kept entirely outside the AI layer. Each finding is scored as SEVERITY_SCORE[severity] × CERTAINTY_WEIGHT[validated_certainty], agent scores are derived from their finding sets (capped at 10), and the combined risk is a weighted average across agents with fixed weights (security_privacy: 3.0, test_quality: 2.5, architecture_intent: 2.0, performance/hotspot: 1.5, code_quality_obs: 1.0). Thresholds: <4.0 auto-approve eligible, >=4.0 human review, >=8.0 hard block.

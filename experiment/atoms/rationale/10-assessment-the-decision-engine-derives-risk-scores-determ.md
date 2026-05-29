---
kind: rationale
claim: The decision engine derives risk scores deterministically from findings rather
  than asking an LLM to generate a score.
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/types.py
tags:
- scoring
- determinism
- llm-boundary
source: doc-import:docs/plan/10-assessment.md
status: active
---
The decision engine derives risk scores deterministically from findings (severity × validated_certainty) rather than asking an LLM to generate a risk_score. This was an explicit design decision: LLM-generated scores were considered and rejected because deterministic derivation is auditable, consistent, and not subject to model variance. Agents produce findings with severity and certainty; the engine owns the numeric aggregation.

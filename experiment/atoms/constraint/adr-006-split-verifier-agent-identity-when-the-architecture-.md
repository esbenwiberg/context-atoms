---
kind: constraint
claim: "When the `architecture` agent skips due to missing ground truth, it must return\
  \ a PASS verdict with explanation text `\"no architecture context found - agent\
  \ skipped\"` \u2014 no new `skipped` verdict enum or DB column may be introduced\
  \ for this case."
anchors:
- src/pr_guardian/decision/types.py
- src/pr_guardian/decision/engine.py
- src/pr_guardian/persistence/models.py
tags:
- agents
- architecture
- skip
- verdict
- schema
source: doc-import:docs/decisions/ADR-006-split-verifier-agent-identity.md
status: active
---
When the `architecture` agent skips due to missing ground truth, it must return a PASS verdict with explanation text `"no architecture context found - agent skipped"` — no new `skipped` verdict enum or DB column may be introduced for this case. The existing `verdict_explanation` field in the persistence model carries the status note, and the review-detail UI renders pass explanations as `Review note`. The exact skip text is a stable UI/test contract. A `skipped` verdict was explicitly rejected because it would require schema and decision-engine changes without adding useful scoring behavior.

---
kind: rationale
claim: "DecisionResult was split into sticky_triggers and finding_reasons (replacing\
  \ the flat override_reasons/trust_tier_reasons arrays) because verification mode\
  \ needs to answer 'are the only remaining human-review reasons finding-derived and\
  \ have those findings been fixed?' \u2014 a question unanswerable from a single\
  \ flat array."
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/types.py
- src/pr_guardian/api/dashboard.py
- specs/verification-mode-and-sticky-triggers/design.md
tags:
- decision-engine
- verification-mode
- escalation-reasons
source: doc-import:docs/decisions/ADR-002-sticky-trigger-split.md
status: active
---
DecisionResult was split into sticky_triggers and finding_reasons (replacing the flat override_reasons/trust_tier_reasons arrays) because verification mode needs to answer 'are the only remaining human-review reasons finding-derived and have those findings been fixed?' — a question unanswerable from a single flat array. Sticky triggers are structural/persistent (new_dep, path_risk, hotspot, trust_tier, repo_risk, high_diff) and survive re-runs until the underlying condition disappears. Finding reasons are transient and clear once findings are addressed. A back-compat union field was explicitly rejected because it would split the source of truth between review_detail.html and the wizard.

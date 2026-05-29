---
kind: constraint
claim: "The sticky_triggers kind set is closed to exactly: new_dep, path_risk, hotspot,\
  \ trust_tier, repo_risk, high_diff \u2014 adding any further kind requires an ADR\
  \ amendment, not a silent enum extension."
anchors:
- src/pr_guardian/decision/types.py
- src/pr_guardian/decision/engine.py
tags:
- sticky-triggers
- closed-enum
- adr
source: doc-import:docs/decisions/ADR-002-sticky-trigger-split.md
status: active
---
The sticky_triggers kind set is closed to exactly: new_dep, path_risk, hotspot, trust_tier, repo_risk, high_diff — adding any further kind requires an ADR amendment, not a silent enum extension. ADR-005 (not yet accepted) proposes adding config_policy and structured StickyTrigger.details; those are not live contract fields until that ADR is accepted and implemented. Any code extending this enum without an accompanying ADR update violates the contract.

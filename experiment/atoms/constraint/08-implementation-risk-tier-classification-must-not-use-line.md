---
kind: constraint
claim: Risk tier classification must not use line counts; tiers must be driven by
  change_profile (semantic type of change) and blast_radius.
anchors:
- src/pr_guardian/triage/classifier.py
- src/pr_guardian/discovery/change_profile.py
- src/pr_guardian/discovery/blast_radius.py
tags:
- triage
- risk-tier
- classification
source: doc-import:docs/plan/08-implementation.md
status: active
---
Risk tier classification must not use line counts; tiers must be driven by change_profile (semantic type of change) and blast_radius. Line-count thresholds that appear in config (e.g. `agent_context_thresholds.compact: 100`) are only context hints that control agent timeout/depth, not tier gates. This invariant is explicitly called out in defaults.yml and is non-obvious because most code-review tools tier by diff size.

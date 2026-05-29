---
kind: constraint
claim: Path risk config (critical_paths / safe_paths) acts as a floor/ceiling applied
  after base tier calculation, not a replacement for the triage algorithm.
anchors:
- src/pr_guardian/triage/path_risk.py
- src/pr_guardian/triage/classifier.py
- src/pr_guardian/config/schema.py
tags:
- triage
- path-risk
- config
source: doc-import:docs/plan/03-triage.md
status: active
---
Path risk config (critical_paths / safe_paths) acts as a floor/ceiling applied after base tier calculation, not a replacement for the triage algorithm. critical_paths.min_tier is applied after the base tier; if base is already higher it stays. safe_paths.max_tier is applied only when its condition is met (e.g. no_production_changes) and can be overridden by amplifiers (repo_risk_class=critical, cross_stack, etc.). This ordering matters: amplifiers must be evaluated before path ceiling is applied so a critical-repo amplifier can still raise a path marked safe.

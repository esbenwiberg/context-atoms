---
kind: constraint
claim: 'A repo''s static risk class (standard/elevated/critical) hard-gates auto-approve:
  elevated repos only auto-approve trivial PRs, and critical repos never auto-approve.'
anchors:
- src/pr_guardian/config/schema.py
- src/pr_guardian/config/defaults.yml
- src/pr_guardian/decision/engine.py
tags:
- risk-class
- auto-approve
- config
source: doc-import:docs/plan/00-overview.md
status: active
---
A repo's static risk class (standard/elevated/critical) hard-gates auto-approve: elevated repos only auto-approve trivial PRs, and critical repos never auto-approve.

The risk class is a per-repo configuration value, not derived dynamically from the PR. It acts as a ceiling on the decision engine: no matter how confident the agents are, the engine must check the repo risk class before emitting an auto-approve decision. Code in the decision engine must consult this value before finalising any approval outcome.

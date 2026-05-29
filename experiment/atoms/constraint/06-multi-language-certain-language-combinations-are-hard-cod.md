---
kind: constraint
claim: 'Certain language combinations are hard-coded risk amplifiers in the decision
  engine: any SQL, Terraform/Bicep, or Dockerfile presence must always trigger the
  security agent; cross-stack PRs (>1 runtime language) must bump risk tier one level;
  and PRs touching >3 languages must be rated HIGH.'
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/types.py
- src/pr_guardian/languages/detector.py
tags:
- risk-scoring
- security
- decision-engine
- multi-language
source: doc-import:docs/plan/06-multi-language.md
status: active
---
Certain language combinations are hard-coded risk amplifiers in the decision engine: any SQL, Terraform/Bicep, or Dockerfile presence must always trigger the security agent; cross-stack PRs (>1 runtime language) must bump risk tier one level; and PRs touching >3 languages must be rated HIGH.

The full rule table:
- `cross_stack = true` (>1 runtime language) → bump risk tier one level
- `sql` present → always trigger security agent (injection risk)
- `terraform` or `bicep` present → always trigger security agent (infra misconfiguration)
- `dockerfile` present → always trigger security agent (container security)
- `language_count > 3` → force risk to HIGH regardless of other signals

These are unconditional overrides, not configurable thresholds. Per-repo config (`review.yml`) can add extra `always_trigger` rules (e.g. `terraform: always_trigger: [security]`) but cannot suppress the hard-coded amplifiers above.

---
kind: constraint
claim: "override_reasons and trust_tier_reasons must not exist on DecisionResult or\
  \ the /api/dashboard/reviews/{id} payload \u2014 they were removed in the same brief\
  \ that introduced sticky_triggers/finding_reasons with no transitional union field."
anchors:
- src/pr_guardian/decision/types.py
- src/pr_guardian/api/dashboard.py
- src/pr_guardian/dashboard/review_detail.html
tags:
- breaking-change
- dashboard-payload
- no-back-compat
source: doc-import:docs/decisions/ADR-002-sticky-trigger-split.md
status: active
---
override_reasons and trust_tier_reasons must not exist on DecisionResult or the /api/dashboard/reviews/{id} payload — they were removed in the same brief that introduced sticky_triggers/finding_reasons with no transitional union field. This was a deliberate clean break: keeping a union field would leave two representations of the same truth and force every future consumer to choose between them. The only existing consumer (review_detail.html) migrated in the same changeset. Storage compatibility for legacy override_reasons rows is handled separately but the live API and model fields are gone.

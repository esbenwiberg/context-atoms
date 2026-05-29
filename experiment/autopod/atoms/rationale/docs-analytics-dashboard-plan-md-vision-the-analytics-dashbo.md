---
kind: rationale
claim: The analytics dashboard surfaces cost, quality, and reliability as primary
  metrics and treats safety as a secondary feature because the intended audience is
  a fleet operator tuning pods, not auditors or managers.
anchors:
- packages/daemon/src/pods/cost-aggregation.ts
- packages/daemon/src/pods/quality-score.ts
- packages/daemon/src/pods/reliability-aggregator.ts
- packages/daemon/src/pods/safety-aggregator.ts
tags:
- analytics
- ux
- prioritization
source: doc-import:docs/analytics-dashboard-plan.md#vision
status: active
---
The analytics dashboard surfaces cost, quality, and reliability as primary metrics and treats safety as a secondary feature because the intended audience is a fleet operator tuning pods, not auditors or managers. The ordering is intentional: cost / quality / reliability lead the card grid; safety is present but not the headline. Rejected framing: a compliance-first view where safety dominates. The audience is a single operator (the person running the daemon), so actionable tuning signals take precedence over audit-trail signals.

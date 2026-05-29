---
kind: constraint
claim: Analytics metric tables must never backfill historical data; new tables capture
  forward only.
anchors:
- packages/daemon/src/db/migrations
tags:
- analytics
- migrations
- database
- metrics
source: doc-import:docs/analytics-dashboard-plan.md#cross-cutting-principles
status: active
---
Analytics metric tables must never backfill historical data; new tables capture forward only. Existing tables already contain sufficient historical data for non-analytics needs. Any new migration that adds analytics-oriented columns or tables must not attempt to populate rows retroactively — forward capture only.

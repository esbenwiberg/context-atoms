---
kind: rationale
claim: Every analytics drill-in view exposes an 'Open as workspace' CTA that reuses
  the existing history-workspace mechanism to launch a forensic pod against the filtered
  set.
anchors:
- packages/daemon/src/api/routes/history.ts
tags:
- analytics
- workspace
- history
- forensics
source: doc-import:docs/analytics-dashboard-plan.md#cross-cutting-principles
status: active
---
Every analytics drill-in view exposes an 'Open as workspace' CTA that reuses the existing history-workspace mechanism to launch a forensic pod against the filtered set. The rationale is to avoid duplicating pod-launch logic by piggy-backing on the already-shipped history-workspace path. Any new analytics drill-in screen must wire its filter context into that existing CTA rather than introducing a parallel launch flow.

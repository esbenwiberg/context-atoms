---
kind: constraint
claim: "All demand and capacity period bucketing must use `workdaysInPeriod` proportions,\
  \ not calendar-day proportions, to avoid 2\u20135% drift between demand and capacity\
  \ math."
anchors:
- src/math/workdaysInPeriod.ts
- src/math/distributeSpan.ts
- src/math/getRoleCapacityForPeriod.ts
tags:
- math
- bucketing
- workdays
- consistency
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#context
status: active
---
All demand and capacity period bucketing must use `workdaysInPeriod` proportions, not calendar-day proportions, to avoid 2–5% drift between demand and capacity math. A prior `committedHoursInPeriod` routine bucketed by calendar-day proportion while the capacity math next to it used weekday-proportional `workdaysInPeriod`, introducing systematic drift. Any new bucketing or distribution logic that touches hours must use the same weekday basis.

---
kind: constraint
claim: 'The quality drill-down view must break down low-quality reasons using exactly
  three signals: low read/edit ratio, edits-without-prior-read count, and user-interrupt
  count.'
anchors:
- packages/daemon/src/pods/quality-signals.ts
- packages/daemon/src/pods/quality-score-repository.ts
- packages/daemon/src/pods/quality-score.ts
tags:
- quality
- signals
- analytics
source: doc-import:docs/analytics-dashboard-plan.md#phase-3-quality-drill-down
status: active
---
The quality drill-down view must break down low-quality reasons using exactly three signals: low read/edit ratio, edits-without-prior-read count, and user-interrupt count.
These three are the designated diagnostic signals for the low-quality reason breakdown section — not a general-purpose signal list.
Any new quality signal added to quality-signals.ts is not automatically surfaced in the drill-down; it must be explicitly included in the breakdown UI.

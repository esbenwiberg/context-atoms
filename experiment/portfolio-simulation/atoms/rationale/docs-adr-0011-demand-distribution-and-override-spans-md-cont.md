---
kind: rationale
claim: 'Three near-identical bucketing routines (`computeRoleDemandForPeriod`, `committedHoursInPeriod`,
  override `Map` + `migrateDemandOverrides`) were consolidated into `distributeSpan`
  because they shared the same root cause: storing bucketed period values instead
  of the continuous spans the data actually has.'
anchors:
- src/math/distributeSpan.ts
- src/state/demandOverrideSpan.ts
- specs/demand-distribution-spans/design.md
tags:
- consolidation
- demand
- bucketing
- deduplication
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#context
status: active
---
Three near-identical bucketing routines were consolidated into `distributeSpan` because they shared the same root cause: storing bucketed period values instead of the continuous spans the data actually has. `computeRoleDemandForPeriod` synthesised from monthly-hours + curve weighting despite Dataverse providing continuous spans; `committedHoursInPeriod` used calendar-day proportion; the override Map used a lossy granularity-keyed scheme. Unifying on a single span-based primitive removes the fan-out and ensures consistent bucketing math across demand, capacity, and override paths.

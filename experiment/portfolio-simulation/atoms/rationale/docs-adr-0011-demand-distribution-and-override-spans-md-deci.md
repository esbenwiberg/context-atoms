---
kind: rationale
claim: "Demand is stored as continuous {start, end, hours} spans rather than pre-bucketed\
  \ period values so that switching granularity (Q\u2194M) never corrupts or loses\
  \ override edits."
anchors:
- src/math/distributeSpan.ts
- src/state/demandOverrideSpan.ts
- src/heatmap/buildContributions.ts
tags:
- demand
- spans
- granularity
- round-trip
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#decision
status: active
---
Demand is stored as continuous {start, end, hours} spans rather than pre-bucketed period values so that switching granularity (Q↔M) never corrupts or loses override edits. The Q→M→edit-Feb→Q→M reproducer was the motivating bug: rebucketing on granularity changes caused round-trip data loss. With spans, the data IS the curve; distributeSpan distributes at render time using weekday-proportional weights (Mon–Fri = 1, Sat/Sun = 0, matching workdaysInPeriod used for capacity). Sum-to-original holds within 1e-6 when the period set fully covers the span. The granularity switch no longer touches the override slice at all.

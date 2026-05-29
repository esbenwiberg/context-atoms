---
kind: rationale
claim: "Captured-fixture parity tests are used as the math contract instead of hand-crafted\
  \ unit tests because hand-written tests encode the developer's reading of the code,\
  \ not the intended behavior \u2014 empirically-tuned math modules have subtly wrong\
  \ intent-reads."
anchors:
- src/math
- tests/parity
- tests/fixtures
tags:
- testing
- math
- parity
- adr
source: doc-import:docs/adr/0004-parity-test-workflow.md
status: active
---
Captured-fixture parity tests are used as the math contract instead of hand-crafted unit tests because hand-written tests encode the developer's reading of the code, not the intended behavior.

The math IP (scoring formulas, must-run semantics, budget-cap roll-up, effective-dates inference, role-demand bucketing) is empirically tuned over years of customer feedback. Tests written from reading the code encode our reading, not the intent. The modules most likely to be misread — `isMustRun`, `getEffectiveDates`, `applyResourceCapacityConstraint`, `runScheduleSuggestions` — are precisely the ones where intent-read diverges in subtle ways.

Property-based tests were rejected as the primary gate because the invariants the math encodes are not yet fully known. Captured fixtures from real inputs are the empirical oracle; property tests can layer on later.

Skipping parity for 'obviously simple' modules was also explicitly rejected — simple-looking modules are precisely where semantics are tuned.

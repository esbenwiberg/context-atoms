---
kind: constraint
claim: "Fixture data must only contain shapes that are faithful subsets of real Dataverse\
  \ pum_* columns \u2014 no ergonomic-but-fake fields."
anchors:
- src/adapters/fixture/data/demo.json
- src/adapters/fixture/index.ts
tags:
- fixture
- dataverse
- parity
- testing
source: doc-import:CLAUDE.md#hard-rules-the-trip-wires
status: active
---
Fixture data must only contain shapes that are faithful subsets of real Dataverse pum_* columns — no ergonomic-but-fake fields. The fixture adapter is used for smoke tests and demo mode; if fixture shapes diverge from the Dataverse schema, tests pass against an impossible world and real-data bugs go undetected. Model new fixture shapes on actual pum_* columns only.

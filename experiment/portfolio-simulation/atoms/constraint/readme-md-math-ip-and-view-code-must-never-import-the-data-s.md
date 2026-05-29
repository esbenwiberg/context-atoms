---
kind: constraint
claim: "Math IP and view code must never import the data source directly \u2014 all\
  \ data dependencies must flow through the types contract in src/adapters/types.ts."
anchors:
- src/adapters/types.ts
- src/math/
- src/adapters/
tags:
- architecture
- ports-and-adapters
- dependency-rule
source: doc-import:README.md
status: active
---
Math IP and view code must never import the data source directly — all data dependencies must flow through the types contract in src/adapters/types.ts. This ports-and-adapters boundary lets the fixture adapter (src/adapters/fixture/) and the XRM production adapter (src/adapters/xrm/) be swapped without touching math or UI code. The .dependency-cruiser.cjs enforces this layer rule in CI; violations fail the precommit and verify pipeline.

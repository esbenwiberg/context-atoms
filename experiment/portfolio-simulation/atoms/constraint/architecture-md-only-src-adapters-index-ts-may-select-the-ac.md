---
kind: constraint
claim: Only src/adapters/index.ts may select the active adapter implementation; all
  other modules must import exclusively from the contract in src/adapters/types.ts.
anchors:
- src/adapters/index.ts
- src/adapters/types.ts
- src/adapters/fixture/index.ts
- src/adapters/xrm/index.ts
tags:
- ports-adapters
- architecture
- dependency
source: doc-import:ARCHITECTURE.md
status: active
---
Only src/adapters/index.ts may select the active adapter implementation; all other modules must import exclusively from the contract in src/adapters/types.ts. The concrete implementations (fixture/ for local dev, xrm/ for production) are invisible to view and math layers. This isolation means swapping Dataverse for a different backend requires changing only the adapter. The rule is enforced by the ports-adapters-impl-leak rule in npm run arch:check (dependency-cruiser).

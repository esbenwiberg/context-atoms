---
kind: constraint
claim: View and math layers must only import adapter types from src/adapters/types.ts
  and must never directly import src/adapters/fixture or src/adapters/xrm.
anchors:
- src/adapters/types.ts
- src/adapters/fixture/index.ts
- src/adapters/xrm/index.ts
tags:
- ports-and-adapters
- dependency
- architecture
source: doc-import:CLAUDE.md#conventions
status: active
---
View and math layers must only import adapter types from src/adapters/types.ts and must never directly import src/adapters/fixture or src/adapters/xrm. This is the ports-and-adapters guarantee: concrete adapter implementations (fixture, xrm) are injected at runtime and must not be coupled into domain or view code.

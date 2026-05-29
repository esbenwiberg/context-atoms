---
kind: constraint
claim: The embedding model is an HTML Web Resource, not a PCF control; switching frameworks
  requires explicit user approval.
anchors:
- index.html
- src/main.tsx
- solution/src/WebResources/pum_portfoliosim_index_html/.gitkeep
tags:
- pcf
- embedding
- dataverse
- architecture
source: doc-import:CLAUDE.md#hard-rules-the-trip-wires
status: active
---
The embedding model is an HTML Web Resource, not a PCF control; switching frameworks requires explicit user approval. Any agent working on embedding, packaging, or host-integration code must surface this constraint before touching framework-level wiring. The PCF path was explicitly rejected — silently switching is a hard stop.

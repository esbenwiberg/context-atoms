---
kind: constraint
claim: The embedding model for this app is an HTML Web Resource; PCF must never be
  introduced.
anchors:
- CLAUDE.md
- solution/src/WebResources/pum_portfoliosim_index_html/.gitkeep
tags:
- architecture
- dataverse
- pcf
- hard-stop
source: doc-import:CONTRIBUTING.md
status: active
---
The embedding model for this app is an HTML Web Resource; PCF must never be introduced. Additional hard stops: do not reintroduce demo mode, do not use localStorage as a source of truth, do not propose Dataverse/pac work without explicit scope, and never relax a banned pattern (eslint/arch/bans) to make a failing build green. CLAUDE.md carries the full list and rationale; CONTRIBUTING.md defers to it on conflicts.

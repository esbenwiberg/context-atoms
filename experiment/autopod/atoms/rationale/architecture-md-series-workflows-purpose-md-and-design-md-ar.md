---
kind: rationale
claim: '`purpose.md` and `design.md` are stored at the top level of the spec folder
  (not inside individual briefs/) so they can be injected into every pod''s CLAUDE.md,
  keeping all pods in a series aligned on the same high-level goal and implementation
  design.'
anchors:
- packages/daemon/src/pods/system-instructions-generator.ts
- packages/daemon/src/db/migrations/069_series_design_and_brief_scope.sql
- packages/daemon/src/pods/section-resolver.ts
tags:
- series
- purpose
- design
- context-injection
- claude-md
source: doc-import:ARCHITECTURE.md#series-workflows
status: active
---
`purpose.md` and `design.md` are stored at the top level of the spec folder (not inside individual briefs/) so they can be injected into every pod's CLAUDE.md, keeping all pods in a series aligned on the same high-level goal and implementation design. The alternative — duplicating or summarising intent in each brief — was rejected because it would drift as briefs are edited. By injecting a single canonical `purpose.md` and `design.md` into each pod's system instructions, all pods share one source of truth for why the series exists and how it should be built, even though each pod has its own narrow brief.

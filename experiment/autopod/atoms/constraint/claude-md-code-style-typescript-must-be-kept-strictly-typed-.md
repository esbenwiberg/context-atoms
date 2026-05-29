---
kind: constraint
claim: 'TypeScript must be kept strictly typed: `any` is banned and unused variables/parameters
  are treated as errors.'
anchors:
- packages/cli/tsconfig.json
- packages/daemon/src/
tags:
- typescript
- strict
- linting
source: doc-import:CLAUDE.md#code-style
status: active
---
TypeScript must be kept strictly typed: `any` is banned and unused variables/parameters are treated as errors. Use unknown + type narrowing instead of any; use explicit parameter types rather than inference where the type would otherwise widen. Biome enforces 2-space indent, 100-char lines, single quotes, trailing commas, and always-semicolons — the biome.json is authoritative for formatting rules.

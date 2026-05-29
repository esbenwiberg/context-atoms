---
kind: rationale
claim: Biome is the sole lint and format tool; ESLint and Prettier are explicitly
  not used.
anchors:
- biome.json
tags:
- tooling
- lint
- format
source: doc-import:CLAUDE.md#build-system
status: active
---
Biome is the sole lint and format tool; ESLint and Prettier are explicitly not used. This means there is no .eslintrc, .prettierrc, or eslint-disable machinery anywhere in the repo. Any lint or format invocation must go through Biome (e.g. `biome check`, `biome format`). Agents adding lint suppressions should use Biome's suppression syntax, not eslint-disable comments.

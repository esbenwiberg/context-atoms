---
kind: rationale
claim: Biome was chosen to replace both ESLint and Prettier, consolidating lint and
  format into a single tool.
anchors:
- biome.json
tags:
- biome
- lint
- format
- tooling
- eslint
- prettier
source: doc-import:README.md#development
status: active
---
Biome was chosen to replace both ESLint and Prettier, consolidating lint and format into a single tool. ESLint and Prettier are the explicit rejected alternatives. Using one tool eliminates config duplication, plugin-version conflicts, and the formatter/linter ordering problem that arises when both run in CI.

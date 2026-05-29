---
kind: rationale
claim: Biome was chosen as the single lint-and-format tool, replacing the separate
  ESLint and Prettier tools that would otherwise be used.
anchors:
- biome.json
tags:
- tooling
- lint
- format
- biome
source: doc-import:ARCHITECTURE.md#build-system
status: active
---
Biome was chosen as the single lint-and-format tool, replacing the separate ESLint and Prettier tools that would otherwise be used. The rejected alternatives are ESLint (lint) and Prettier (format), which are the conventional JS/TS toolchain. Biome combines both responsibilities in one binary with faster execution. Any new lint rules or formatting config changes must go into biome.json; do not introduce ESLint or Prettier config files.

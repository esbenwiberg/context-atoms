---
kind: rationale
claim: The optional C extension is compiled via mypyc from pure Python source rather
  than being a hand-written C extension, so pure Python remains the single source
  of truth.
anchors:
- sqlglotc/
tags:
- performance
- mypyc
- c-extension
source: doc-import:CLAUDE.md#performance-considerations
status: active
---
The optional C extension (sqlglotc/) is compiled via mypyc from pure Python source rather than being a hand-written C extension, so pure Python remains the single source of truth. Installed via `pip install 'sqlglot[c]'`, it compiles core modules (expression_core, tokenizer_core, parser_core, etc.) for a speed boost while keeping the Python implementation authoritative.

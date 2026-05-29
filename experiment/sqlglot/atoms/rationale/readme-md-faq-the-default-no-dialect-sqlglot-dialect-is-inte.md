---
kind: rationale
claim: The default (no-dialect) SQLGlot dialect is intentionally designed as a superset
  of all supported dialects, not as standard ANSI SQL.
anchors:
- sqlglot/dialects/dialect.py
- sqlglot/parser.py
tags:
- dialect
- parsing
- default-behavior
source: doc-import:README.md#faq
status: active
---
The default (no-dialect) SQLGlot dialect is intentionally designed as a superset of all supported dialects, not as standard ANSI SQL. This means omitting a dialect during parsing does not fall back to ANSI SQL — it falls back to a more permissive grammar that tries to accept constructs from all dialects. Consequence: dialect-specific syntax that happens to parse successfully under the superset may produce an incorrect AST. Always pass `dialect=` (or `read=`/`write=`) when the source or target database is known.

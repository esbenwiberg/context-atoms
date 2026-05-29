---
kind: constraint
claim: Both parsing and SQL generation require an explicit dialect argument; omitting
  it on either side silently uses the SQLGlot superset dialect instead of the intended
  database dialect.
anchors:
- sqlglot/__init__.py
- sqlglot/parser.py
- sqlglot/generator.py
tags:
- dialect
- api-contract
- parsing
- generation
source: doc-import:README.md#faq
status: active
---
Both parsing and SQL generation require an explicit dialect argument; omitting it on either side silently uses the SQLGlot superset dialect instead of the intended database dialect. Correct transpilation requires dialect on both ends: `parse_one(sql, dialect='spark').sql(dialect='duckdb')` or equivalently `transpile(sql, read='spark', write='duckdb')`. Leaving either side unspecified is a silent correctness bug, not a parser error — the query may appear to work while producing subtly wrong SQL.

---
kind: rationale
claim: F-strings are never used to build SQL output fragments because they bypass
  quoting, escaping, and dialect-aware identifier handling.
anchors:
- sqlglot/generator.py
- sqlglot/generators
tags:
- sql-generation
- security
- dialects
- f-string
source: doc-import:CLAUDE.md#sqlglot-coding-rules
status: active
---
F-strings are never used to build SQL output fragments because they bypass quoting, escaping, and dialect-aware identifier handling. String interpolation produces SQL that is brittle across dialects (e.g., identifier quoting differs between BigQuery backticks and Postgres double-quotes) and is vulnerable to injection when expression values contain special characters. The approved hierarchy is: `self.func()` for simple function calls → expression builder helpers (`exp.cast`, `exp.column`, operators) → `exp.maybe_parse` + `exp.replace_placeholders` templates for complex structures. Direct `self.sql(some_exp)` is fine for sub-expressions but must be assembled via the AST, not string concatenation.

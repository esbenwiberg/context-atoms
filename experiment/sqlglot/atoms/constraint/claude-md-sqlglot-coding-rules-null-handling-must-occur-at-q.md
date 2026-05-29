---
kind: constraint
claim: NULL handling must occur at query time via IS NULL in generated SQL, not at
  transpile time by inspecting exp.Null() instances in Python.
anchors:
- sqlglot/generator.py
- sqlglot/generators
tags:
- 'null'
- transpile
- sql-generation
- correctness
source: doc-import:CLAUDE.md#sqlglot-coding-rules
status: active
---
NULL handling must occur at query time via IS NULL in generated SQL, not at transpile time by inspecting exp.Null() instances. Compile-time checks like `isinstance(arg, exp.Null)` only catch literal NULL tokens written in the source SQL; they miss NULLs that arrive at runtime from columns, parameters, or sub-expressions. The correct pattern is to emit a CASE WHEN :arg IS NULL THEN NULL ELSE ... END structure using `exp.maybe_parse` templates so the database evaluates nullability at execution time.

---
kind: constraint
claim: Generator methods named `<lowercase_expr_name>_sql` are auto-discovered; TRANSFORMS
  entries must only be used for one-liners, renames, lambdas, or functions with multiple
  entry points.
anchors:
- sqlglot/generator.py
- sqlglot/generators
tags:
- generator
- naming
- transforms
- auto-discovery
source: doc-import:CLAUDE.md#sqlglot-coding-rules
status: active
---
Generator methods named `<lowercase_expr_name>_sql` are auto-discovered — no TRANSFORMS entry is needed. TRANSFORMS should only be used for simple cases: `rename_func("OTHER_NAME")`, lambdas, or when a single generator function handles multiple expression types. Any single-entry-point function that has its own method must live inside the Generator class under the auto-named convention rather than being registered in TRANSFORMS. Violating this causes duplicate dispatch paths and reviewer rejection.

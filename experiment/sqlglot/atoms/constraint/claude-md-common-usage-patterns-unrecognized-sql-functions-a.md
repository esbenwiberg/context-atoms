---
kind: constraint
claim: Unrecognized SQL functions are represented as exp.Anonymous nodes in the AST,
  making 'Anonymous' in repr(tree) the canonical way to detect unknown or unsupported
  function expressions.
anchors:
- sqlglot/expressions/core.py
- sqlglot/expressions/functions.py
- sqlglot/parser.py
tags:
- anonymous
- function
- ast
- validation
- parsing
source: doc-import:CLAUDE.md#common-usage-patterns
status: active
---
Unrecognized SQL functions are represented as exp.Anonymous nodes in the AST, making 'Anonymous' in repr(tree) the canonical way to detect unknown or unsupported function expressions. When the parser encounters a function call that does not map to a known sqlglot expression class, it falls back to exp.Anonymous rather than raising a parse error. This means callers cannot rely on a parse error to detect missing function support — they must inspect the AST for Anonymous nodes. The idiomatic check is: `if "Anonymous" in repr(tree)` after parsing with a specific dialect.

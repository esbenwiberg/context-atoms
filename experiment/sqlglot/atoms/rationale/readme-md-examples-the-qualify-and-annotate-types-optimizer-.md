---
kind: rationale
claim: The `qualify` and `annotate_types` optimizer rules are deliberately excluded
  from the default transpilation pipeline because they add significant overhead and
  complexity, despite being required for accurate type-sensitive transformations.
anchors:
- sqlglot/optimizer/qualify.py
- sqlglot/optimizer/annotate_types.py
- sqlglot/optimizer/optimizer.py
tags:
- optimizer
- transpile
- performance
- defaults
source: doc-import:README.md#examples
status: active
---
The `qualify` and `annotate_types` optimizer rules are deliberately excluded from the default transpilation pipeline because they add significant overhead and complexity, despite being required for accurate type-sensitive transformations. Some dialect translations depend on type inference to understand semantics correctly (e.g., distinguishing overloaded operators by operand type). Callers who need accurate type-sensitive transpilation must opt in by running `qualify` and `annotate_types` explicitly before or during optimization. The default pipeline trades correctness for some edge cases in exchange for lower latency and simpler call semantics.

---
kind: constraint
claim: The optimizer must degrade gracefully and skip interval-expression simplification
  when dateutil is not installed, rather than raising an ImportError.
anchors:
- sqlglot/optimizer/simplify.py
- sqlglot/optimizer/optimizer.py
tags:
- optimizer
- dateutil
- interval
- graceful-degradation
source: doc-import:README.md#optional-dependencies
status: active
---
The optimizer must degrade gracefully and skip interval-expression simplification when dateutil is not installed, rather than raising an ImportError. Concretely, expressions of the form `x + interval '1' month` will be left unsimplified if dateutil is absent. Any code path in the optimizer that calls dateutil must guard the import and treat the missing-module case as a no-op, not an error.

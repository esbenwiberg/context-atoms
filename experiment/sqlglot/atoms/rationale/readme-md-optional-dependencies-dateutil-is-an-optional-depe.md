---
kind: rationale
claim: dateutil is an optional dependency used exclusively to simplify literal timedelta/interval
  expressions in the optimizer.
anchors:
- sqlglot/optimizer/simplify.py
- pyproject.toml
- setup.cfg
tags:
- optimizer
- dateutil
- interval
- optional-dependency
source: doc-import:README.md#optional-dependencies
status: active
---
dateutil is an optional dependency used exclusively to simplify literal timedelta/interval expressions in the optimizer. It was chosen to handle calendar-aware arithmetic (e.g. adding months) that pure Python datetime cannot reliably do. The optimizer detects whether dateutil is importable at runtime; if absent, it skips simplification of those expressions rather than raising an error. No other part of sqlglot requires dateutil.

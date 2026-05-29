---
kind: constraint
claim: SQLGlot must have zero external Python dependencies.
anchors:
- pyproject.toml
- setup.cfg
- setup.py
tags:
- dependencies
- packaging
source: doc-import:README.md
status: active
---
SQLGlot must have zero external Python dependencies. This is a core design invariant — the library is explicitly described as 'no-dependency'. Any new feature, optimization, or dialect addition must be implemented using only the Python standard library. Adding a third-party package would break this guarantee for all downstream users.

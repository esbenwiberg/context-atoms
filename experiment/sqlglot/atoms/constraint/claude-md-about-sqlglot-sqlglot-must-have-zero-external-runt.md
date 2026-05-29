---
kind: constraint
claim: sqlglot must have zero external runtime dependencies.
anchors:
- sqlglot/
- setup.cfg
- pyproject.toml
tags:
- dependencies
- packaging
source: doc-import:CLAUDE.md#about-sqlglot
status: active
---
sqlglot must have zero external runtime dependencies. The library is explicitly described as 'no-dependency', meaning no third-party packages may be added to its runtime requirements. All functionality must be implemented in pure Python using only the standard library.

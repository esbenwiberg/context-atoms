---
kind: constraint
claim: Third-party plugin dialects must register themselves under the `sqlglot.dialects`
  entry-point group so that SQLGlot can discover and load them automatically without
  any changes to the core codebase.
anchors:
- sqlglot/dialects/__init__.py
- sqlglot/dialects/dialect.py
tags:
- dialects
- plugins
- entry-points
- extensibility
source: doc-import:README.md#supported-dialects
status: active
---
Third-party plugin dialects must register themselves under the `sqlglot.dialects` entry-point group so that SQLGlot can discover and load them automatically without any changes to the core codebase. A plugin package declares the mapping `"<name> = <module>:<Class>"` inside the `sqlglot.dialects` entry-point group in its `setup.py` (or `pyproject.toml`). Once installed, the dialect is available by name just like any built-in dialect (e.g. `transpile(..., read="mydb", write="postgres")`). This is the only supported integration path for external dialects; adding a dialect class directly to the `sqlglot/dialects/` directory without going through the entry-point mechanism is not the plugin path.

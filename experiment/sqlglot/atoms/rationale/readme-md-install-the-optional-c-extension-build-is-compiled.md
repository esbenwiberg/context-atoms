---
kind: rationale
claim: The optional C extension build is compiled with mypyc (from type-annotated
  Python) rather than Cython or pybind11.
anchors:
- sqlglotc/pyproject.toml
- sqlglotc/setup.py
- sqlglot/py.typed
tags:
- performance
- mypyc
- c-extensions
- type-annotations
source: doc-import:README.md#install
status: active
---
The optional C extension build is compiled with mypyc (from type-annotated Python) rather than Cython or pybind11. This means the accelerated package (installable via `pip install "sqlglot[c]"`) is generated directly from the typed Python source — no separate C/Cython implementation is maintained. A direct consequence is that the Python source must keep complete, mypyc-compatible type annotations; the `sqlglot/py.typed` marker enforces this contract for consumers. The C extension artifacts are packaged separately under `sqlglotc/` and are only included when the `[c]` extra is requested.

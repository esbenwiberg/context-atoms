---
kind: rationale
claim: Parallel make targets (test/testc, unit/unitc, install-dev/install-devc) exist
  because the mypyc C extension is intentionally optional, treated as a pure performance
  optimisation rather than a required build artifact.
anchors:
- Makefile
- sqlglotc/pyproject.toml
- sqlglotc/setup.py
tags:
- mypyc
- c-extension
- build
- architecture
source: doc-import:CLAUDE.md#development-commands
status: active
---
Parallel make targets (test/testc, unit/unitc, install-dev/install-devc) exist because the mypyc C extension is intentionally optional, treated as a pure performance optimisation rather than a required build artifact. `install-dev` gives a working dev environment with zero native compilation; `install-devc` adds the mypyc-compiled extension on top. The `sqlglotc/` sub-package houses the C extension separately from the main `sqlglot/` package precisely to keep the two modes decoupled. Rejected alternative: shipping only a compiled extension would break environments where mypyc is unavailable and would make the Python source non-authoritative.

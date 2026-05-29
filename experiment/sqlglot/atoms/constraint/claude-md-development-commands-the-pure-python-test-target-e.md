---
kind: constraint
claim: The pure-Python test target explicitly hides compiled `.so` files during execution
  so the Python implementation is validated independently of any C extension.
anchors:
- Makefile
- sqlglot/tokenizer_core.py
tags:
- testing
- c-extension
- mypyc
source: doc-import:CLAUDE.md#development-commands
status: active
---
The pure-Python test target explicitly hides compiled `.so` files during execution so the Python implementation is validated independently of any C extension. `make test` must pass without the mypyc-compiled extension present; `make testc` builds the extension first and then runs the suite against it. This means every code path must remain correct in pure Python — the C extension is a performance layer, not a correctness dependency. Any change that only works when the `.so` is loaded will be caught by the default `make test` run.

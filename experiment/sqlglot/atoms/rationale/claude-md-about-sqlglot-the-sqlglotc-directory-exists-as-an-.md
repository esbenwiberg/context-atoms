---
kind: rationale
claim: The sqlglotc/ directory exists as an optional mypyc-compiled C extension to
  provide performance improvements without breaking the pure-Python guarantee.
anchors:
- sqlglotc/
tags:
- performance
- mypyc
- c-extension
source: doc-import:CLAUDE.md#about-sqlglot
status: active
---
The sqlglotc/ directory exists as an optional mypyc-compiled C extension to provide performance improvements without breaking the pure-Python guarantee. The core sqlglot package remains pure Python and fully functional on its own; sqlglotc is an opt-in accelerator. mypyc was chosen over writing a hand-crafted C extension because it compiles existing typed Python code directly, avoiding a separate C codebase.

---
kind: rationale
claim: The tokenizer is split across two files so that the hot-path core logic in
  `tokenizer_core.py` can be compiled with mypyc when installing the `[c]` extra,
  while `tokens.py` remains a pure-Python fallback.
anchors:
- sqlglot/tokens.py
- sqlglot/tokenizer_core.py
tags:
- tokenizer
- performance
- mypyc
- optional-compilation
source: doc-import:CLAUDE.md#architecture-overview
status: active
---
The tokenizer is split across two files so that the hot-path core logic in `tokenizer_core.py` can be compiled with mypyc when installing the `[c]` extra, while `tokens.py` remains a pure-Python fallback. This means a single logical tokenizer surfaces as two source files for intentional performance reasons, not accidental duplication. Code that touches tokenizer behaviour must be aware that `tokenizer_core.py` is the performance-critical path and that changes there affect the compiled extension.

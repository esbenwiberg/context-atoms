---
kind: rationale
claim: The parser uses recursive descent intentionally; Pratt parsing is explicitly
  rejected as an optimization path.
anchors:
- sqlglot/parser.py
- sqlglot/parsers/base.py
tags:
- parser
- recursive-descent
- pratt
- performance
source: doc-import:CLAUDE.md#performance-considerations
status: active
---
The parser uses recursive descent intentionally; Pratt parsing is explicitly rejected as an optimization path. Despite being a common suggestion for improving parser performance, the project maintainers have deliberately chosen recursive descent and contributors must not propose Pratt parsing as an alternative or optimization.

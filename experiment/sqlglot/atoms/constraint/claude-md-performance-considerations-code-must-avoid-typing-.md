---
kind: constraint
claim: Code must avoid typing.Protocol and use Union types and duck typing instead.
anchors:
- sqlglot/_typing.py
- sqlglot/expressions/core.py
- sqlglot/parser.py
- sqlglot/generator.py
tags:
- typing
- duck-typing
- protocol
source: doc-import:CLAUDE.md#performance-considerations
status: active
---
Code must avoid typing.Protocol and use Union types and duck typing instead. This is a project-wide invariant on how type annotations are written; typing.Protocol is explicitly prohibited in favor of Union Type and duck typing throughout the codebase.

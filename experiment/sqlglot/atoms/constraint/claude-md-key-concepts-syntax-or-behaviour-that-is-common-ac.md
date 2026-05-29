---
kind: constraint
claim: Syntax or behaviour that is common across multiple dialects must be implemented
  in the base 'sqlglot' dialect class, not duplicated across individual dialect subclasses.
anchors:
- sqlglot/dialects/dialect.py
- sqlglot/dialects/
- sqlglot/parsers/base.py
tags:
- dialect
- architecture
- deduplication
source: doc-import:CLAUDE.md#key-concepts
status: active
---
Syntax or behaviour that is common across multiple dialects must be implemented in the base 'sqlglot' dialect class, not duplicated across individual dialect subclasses. The base 'sqlglot' dialect accommodates the common SQL surface shared by all engines; every other dialect extends it and overrides only what diverges. Adding a multi-dialect feature to individual dialect classes instead of the base creates maintenance drift and risks inconsistency across dialects.

---
kind: rationale
claim: SQLGlot uses a three-tier dialect model (Official / Community / Plugin) to
  separate core-team maintenance responsibility from community and third-party ownership
  without excluding those dialects from the ecosystem.
anchors:
- sqlglot/dialects/dialect.py
- sqlglot/dialects/__init__.py
tags:
- dialects
- maintenance
- extensibility
source: doc-import:README.md#supported-dialects
status: active
---
SQLGlot uses a three-tier dialect model (Official / Community / Plugin) to separate core-team maintenance responsibility from community and third-party ownership without excluding those dialects from the ecosystem. Official dialects are maintained by the core team with higher bug-fix priority. Community dialects are fully functional but receive lower issue-resolution priority and depend on contributors. Plugin dialects (introduced in v28.6.0) live in entirely separate packages and are not supported by the SQLGlot team at all. This tiering lets the project grow its dialect coverage broadly while honestly communicating the support contract to users and keeping the core codebase manageable.

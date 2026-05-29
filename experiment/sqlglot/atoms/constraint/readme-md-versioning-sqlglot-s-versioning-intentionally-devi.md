---
kind: constraint
claim: 'SQLGlot''s versioning intentionally deviates from standard semver: PATCH includes
  backwards-compatible feature additions (not just fixes), and MINOR signals backwards-incompatible
  changes.'
anchors:
- CHANGELOG.md
- pyproject.toml
- setup.cfg
tags:
- versioning
- semver
- release-policy
source: doc-import:README.md#versioning
status: active
---
SQLGlot's versioning intentionally deviates from standard semver: PATCH includes backwards-compatible feature additions (not just fixes), and MINOR signals backwards-incompatible changes. Standard semver reserves MINOR for backwards-compatible new features and PATCH strictly for bug fixes; SQLGlot collapses both into PATCH and shifts the incompatibility signal to MINOR. MAJOR is reserved for significant backwards-incompatible changes. Consequence: a PATCH bump may introduce new public API surface, and any MINOR bump must be treated as potentially breaking by consumers. When deciding which version component to bump for a change, use compatibility as the deciding axis, not feature-vs-fix.

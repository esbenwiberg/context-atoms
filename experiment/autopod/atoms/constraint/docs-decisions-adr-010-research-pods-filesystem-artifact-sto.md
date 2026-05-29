---
kind: constraint
claim: "Validation screenshots stay in SQLite (small/embedded) while pod workspace\
  \ artifacts go to the filesystem \u2014 new artifact types must follow this size-based\
  \ split and must not store large blobs in SQLite."
anchors:
- packages/daemon/src/api/routes/screenshots.ts
- packages/daemon/src/api/routes/files.ts
tags:
- artifacts
- screenshots
- sqlite
- storage-split
source: doc-import:docs/decisions/ADR-010-research-pods-filesystem-artifact-storage.md
status: active
---
Validation screenshots stay in SQLite (small/embedded) while pod workspace artifacts go to the filesystem — new artifact types must follow this size-based split and must not store large blobs in SQLite. The ADR explicitly preserves the screenshot storage as-is because they are small and benefit from being embedded. Any new artifact type that is large (binaries, multi-file outputs) must use the filesystem path mechanism (session.artifactsPath) rather than SQLite. Mixing the two backends for the same category would undermine the DB-bloat rationale behind ADR-010.

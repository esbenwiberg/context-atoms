---
kind: rationale
claim: Research pod artifacts are extracted to the host filesystem at <dataDir>/artifacts/<sessionId>/
  rather than stored as SQLite blobs, to avoid DB bloat, handle large binaries naturally,
  and let the existing files-route walk+serve logic work unchanged.
anchors:
- packages/daemon/src/api/routes/files.ts
- packages/daemon/src/api/routes/screenshots.ts
tags:
- artifacts
- storage
- sqlite
- filesystem
- research-pods
source: doc-import:docs/decisions/ADR-010-research-pods-filesystem-artifact-storage.md
status: active
---
Research pod artifacts are extracted to the host filesystem at <dataDir>/artifacts/<sessionId>/ rather than stored as SQLite blobs, to avoid DB bloat, handle large binaries naturally, and let the existing files-route walk+serve logic work unchanged. The rejected alternative was SQLite blob storage (the same approach used for validation screenshots, which are small and embedded). The path is stored in session.artifactsPath so the files.ts route can point at it without modification. Consequence: artifact files must be cleaned up when sessions are deleted (explicitly deferred as acceptable tech debt).

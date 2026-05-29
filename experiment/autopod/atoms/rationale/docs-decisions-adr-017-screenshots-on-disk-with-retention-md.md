---
kind: rationale
claim: Screenshots were moved from SQLite base64 columns to on-disk files because
  the daemon DB was growing monotonically (107 MB+) with no retention, and the desktop
  needed lazy full-resolution fetching that base64-over-API couldn't support.
anchors:
- packages/daemon/src/pods/screenshot-store.ts
- packages/daemon/src/pods/screenshot-retention.ts
- packages/daemon/src/db/migrations/091_drop_screenshot_blobs.sql
tags:
- screenshots
- sqlite
- performance
- desktop-ux
source: doc-import:docs/decisions/ADR-017-screenshots-on-disk-with-retention.md
status: active
---
Screenshots were moved from SQLite base64 columns to on-disk files because the daemon DB was growing monotonically (107 MB+) with no retention, and the desktop needed lazy full-resolution fetching that base64-over-API couldn't support. The old implementation doubly-stored data: `validation-repository.ts` wrote base64 into a dedicated `screenshots` column AND embedded the same bytes inside the `result` JSON column on the same row. The desktop's `ScreenshotThumbnail.swift` clamped thumbnails at 200–300 px with no path to render full resolution on demand. Rejected alternative: keeping the SQLite carve-out from ADR-010 was no longer viable once per-pod screenshot volumes reached tens of MB across rework attempts.

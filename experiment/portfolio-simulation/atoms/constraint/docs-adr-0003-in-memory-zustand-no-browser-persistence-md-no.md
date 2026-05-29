---
kind: constraint
claim: No browser-side storage (localStorage, sessionStorage, IndexedDB) may be used
  anywhere in src/; a refresh must produce a clean slate.
anchors:
- src/state/store.ts
- tools/check-bans.mjs
tags:
- persistence
- state
- security
source: doc-import:docs/adr/0003-in-memory-zustand-no-browser-persistence.md
status: active
---
No browser-side storage (localStorage, sessionStorage, IndexedDB) may be used anywhere in src/; a refresh must produce a clean slate.

Rejected because localStorage has no concept of RBAC, no audit trail, no cross-device sharing, and 'just for now' layers become load-bearing before proper backing is added. The rule is enforced by a build-time ban in tools/check-bans.mjs (pattern: `localStorage.` anywhere in src/, no exclusions).

Any PR that adds persistence to a store slice outside src/scenarios/ is an explicit red flag and should reopen this decision.

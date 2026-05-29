---
kind: constraint
claim: Every action that mutates dateOverrides must return a new Map instance (immutable-style)
  so Zustand detects the change by reference equality.
anchors:
- src/state/store.ts
- tests/state/dateOverrides.spec.ts
tags:
- dateOverrides
- immutability
- zustand
source: doc-import:docs/adr/0007-date-overrides-keying.md
status: active
---
Every action that mutates dateOverrides must return a new Map instance (immutable-style) so Zustand detects the change by reference equality.

In-place `.set()` on the existing Map must not be used; callers must do `new Map(...)` each time. tests/state/dateOverrides.spec.ts asserts that the Map reference changes on every write and that clear semantics are correct.

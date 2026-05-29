---
kind: constraint
claim: 'Profile inheritance is capped at 5 levels and uses different merge strategies
  per field type: child scalars win outright; arrays (skills, MCP servers) merge by
  name with child winning on conflict; smoke pages append.'
anchors:
- packages/daemon/src/profiles/inheritance.ts
- packages/daemon/src/profiles/inheritance.test.ts
tags:
- profiles
- inheritance
- merge-strategy
source: doc-import:ARCHITECTURE.md#profile-system
status: active
---
Profile inheritance is capped at 5 levels and uses different merge strategies per field type: child scalars win outright; arrays (skills, MCP servers) merge by name with child winning on conflict; smoke pages append.

When adding a new array field to the profile schema, you must explicitly implement its merge strategy in `inheritance.ts` — there is no generic fallback. Failing to do so will either silently drop parent values or incorrectly clobber them. The 5-level cap must be enforced at write time to prevent unbounded recursion during resolution.

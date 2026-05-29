---
kind: constraint
claim: '`tools/pack-solution.mjs` must fail the build if the default profile seed
  row is absent, malformed, or not marked as default, to prevent accidental removal
  during solution packaging.'
anchors:
- tools/pack-solution.mjs
- solution/src/Other/Customizations.xml
- solution/src/Other/Solution.xml
tags:
- build
- profiles
- enforcement
- solution
source: doc-import:docs/adr/0008-admin-managed-profiles.md
status: active
---
`tools/pack-solution.mjs` must fail the build if the default profile seed row is absent, malformed, or not marked as default, to prevent accidental removal during solution packaging.

A companion script `tools/check-profile-seed.mjs` validates the seed data, entity schema in `Customizations.xml`, and root components in `Solution.xml`. Both checks run as part of `npm run pack:solution` and can also be invoked standalone. This guarantees that every built solution artifact contains a working default profile.

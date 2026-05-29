---
kind: constraint
claim: '`parent.Xrm` must only be accessed inside `src/adapters/xrm/` or `src/platform/host.ts`;
  any reference outside those paths fails the build.'
anchors:
- src/adapters/xrm/index.ts
- src/platform/host.ts
- tools/check-bans.mjs
tags:
- xrm
- adapter
- ban
- build-enforcement
source: doc-import:docs/adr/0001-html-web-resource-embedding.md
status: active
---
`parent.Xrm` must only be accessed inside `src/adapters/xrm/` or `src/platform/host.ts`; any reference outside those paths fails the build.

`tools/check-bans.mjs` enforces the rule "parent.Xrm outside the xrm adapter" at build time. This keeps view and math code decoupled from the Dataverse platform handle and makes the math layer portable.

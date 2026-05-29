---
kind: constraint
claim: PCF framework markers (`ControlContext`, `IInputs`, `IOutputs`, `pcf-scripts`)
  are banned from `src/` and `package.json` and will fail the build if introduced.
anchors:
- tools/check-bans.mjs
- package.json
- src
tags:
- pcf
- ban
- build-enforcement
source: doc-import:docs/adr/0001-html-web-resource-embedding.md
status: active
---
PCF framework markers (`ControlContext`, `IInputs`, `IOutputs`, `pcf-scripts`) are banned from `src/` and `package.json` and will fail the build if introduced.

`tools/check-bans.mjs` enforces the rule "PCF framework markers". Any future migration to PCF requires explicitly removing this ban along with the `viteSingleFile` config, `check-bundle-size.mjs` budget, and the `parent.Xrm` access ban — all four must come down together with a migration plan.

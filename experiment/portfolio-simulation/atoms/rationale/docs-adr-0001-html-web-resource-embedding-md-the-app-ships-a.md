---
kind: rationale
claim: The app ships as a single-file HTML Web Resource instead of a PCF control because
  PCF couples the codebase to a churn-prone Microsoft API surface, is field/grid-scoped
  (wrong shape for a full-page tool), and would force the math layer into the framework's
  data pipeline.
anchors:
- vite.config.ts
- src/adapters/xrm/index.ts
- src/math
- tools/check-bans.mjs
tags:
- embedding
- pcf
- web-resource
- architecture
source: doc-import:docs/adr/0001-html-web-resource-embedding.md
status: active
---
The app ships as a single-file HTML Web Resource instead of a PCF control because PCF couples the codebase to a churn-prone Microsoft API surface, is field/grid-scoped (wrong shape for a full-page tool), and would force the math layer into the framework's data pipeline.

Alternatives rejected:
- PCF: IInputs/IOutputs/ControlContext versioned by Microsoft; data-set PCF makes math IP impure; PCF is scoped to a single field/grid, not a full-page app.
- Multi-file Web Resource: each asset becomes its own Dataverse record, requiring stable naming; versioning a multi-file bundle across environments is a deployment trap.
- External CDN with thin HTML shim: adds DNS/CSP/networking surface and a second deploy target outside the Dataverse solution package.

The build uses `vite-plugin-singlefile` with `cssCodeSplit: false`, `assetsInlineLimit: 100_000_000`, and `inlineDynamicImports: true` to produce exactly one artifact: `dist/index.html`.

Consequence: no code-splitting or dynamic imports; full bundle cost on every cold load; hard bundle-size cap enforced by `tools/check-bundle-size.mjs`.

---
kind: constraint
claim: The production bundle has a 5 MB hard cap (Dataverse Web Resource upload limit)
  and a 2 MB soft warning, both enforced by tools/check-bundle-size.mjs; raising the
  soft threshold requires a note in that file.
anchors:
- tools/check-bundle-size.mjs
- vite.config.ts
tags:
- bundle
- ci
- dataverse
- build
source: doc-import:docs/adr/README.md
status: active
---
The production bundle has a 5 MB hard cap (Dataverse Web Resource upload limit) and a 2 MB soft warning, both enforced by tools/check-bundle-size.mjs; raising the soft threshold requires a note in that file. The hard cap is not an arbitrary performance target — it is the physical upload limit of the Dataverse Web Resource slot (per ADR 0001). Gzip size is informational only and is not gated.

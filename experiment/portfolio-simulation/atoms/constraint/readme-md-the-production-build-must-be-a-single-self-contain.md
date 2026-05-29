---
kind: constraint
claim: The production build must be a single self-contained HTML file under 5 MB because
  Dataverse Web Resources have a hard 5 MB upload limit.
anchors:
- vite.config.ts
- tools/check-bundle-size.mjs
- tools/pack-solution.mjs
tags:
- build
- dataverse
- bundle-size
source: doc-import:README.md
status: active
---
The production build must be a single self-contained HTML file under 5 MB because Dataverse Web Resources have a hard 5 MB upload limit. vite-plugin-singlefile inlines all assets into dist/index.html to produce this artifact. A 2 MB soft warning sits below the hard cap and is enforced by `npm run check:bundle-size`. Exceeding the limit blocks deployment to xPM entirely — there is no partial-upload fallback.

---
kind: rationale
claim: The app ships as a single self-contained HTML file because the xPM embedding
  model requires an HTML Web Resource; PCF was evaluated and explicitly ruled out.
anchors:
- vite.config.ts
- index.html
tags:
- build
- deployment
- xpm
- pcf
source: doc-import:ARCHITECTURE.md
status: active
---
The app ships as a single self-contained HTML file because the xPM embedding model requires an HTML Web Resource; PCF was evaluated and explicitly ruled out. Vite + vite-plugin-singlefile produce a single dist/index.html with no dynamic chunks. The bundle budget (345 kB raw / 100 kB gzip) is enforced by check:bundle-size. The smoke build bundles the fixture adapter; production strips it via the __INCLUDE_FIXTURE__ flag. Changing to PCF would require a fundamentally different packaging model and is not the target.

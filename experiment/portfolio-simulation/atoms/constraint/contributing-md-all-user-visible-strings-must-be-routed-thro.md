---
kind: constraint
claim: All user-visible strings must be routed through t() from src/i18n and all colors
  must use --xpm-* CSS custom properties defined in src/styles/theme.css; inline hex
  values are banned everywhere else.
anchors:
- src/i18n/index.ts
- src/styles/theme.css
tags:
- i18n
- theming
- ui
- convention
source: doc-import:CONTRIBUTING.md
status: active
---
All user-visible strings must be routed through t() from src/i18n and all colors must use --xpm-* CSS custom properties defined in src/styles/theme.css; inline hex values are banned everywhere else. This applies to every new UI surface. New component tests must be added alongside new components following the existing coverage map in CLAUDE.md.

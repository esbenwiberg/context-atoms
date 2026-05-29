---
kind: rationale
claim: CSS custom properties (`--xpm-*`) were chosen over SCSS variables because only
  CSS custom properties participate in the runtime cascade, allowing the Dataverse/xPM
  host to override theme tokens without shipping new app code.
anchors:
- src/styles/theme.css
tags:
- theming
- css
- dataverse
- cascade
source: doc-import:docs/adr/0006-xpm-css-token-theming.md
status: active
---
CSS custom properties (`--xpm-*`) were chosen over SCSS variables because only CSS custom properties participate in the runtime cascade, allowing the Dataverse/xPM host to override theme tokens without shipping new app code. SCSS variables are compile-time only and cannot be overridden by a host environment at runtime. CSS-in-JS (styled-components, emotion) was also rejected due to runtime cost in a single-bundle artifact and lack of natural cascade exposure. Tailwind was rejected because the ceremony-to-payoff ratio is wrong for ~40 tokens. The 41 `--xpm-*` tokens defined in `src/styles/theme.css` serve as the single source of truth; the xPM host overrides them via the cascade when the app runs embedded.

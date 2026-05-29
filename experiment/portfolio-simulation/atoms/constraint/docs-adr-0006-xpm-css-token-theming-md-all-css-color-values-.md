---
kind: constraint
claim: All CSS color values outside `src/styles/theme.css` must reference `--xpm-*`
  tokens; hardcoded hex/rgb/hsl literals in `src/**/*.{ts,tsx,css}` are banned and
  enforced by `tools/check-bans.mjs` as part of `npm run verify`.
anchors:
- src/styles/theme.css
- tools/check-bans.mjs
tags:
- theming
- css
- enforcement
- ban
source: doc-import:docs/adr/0006-xpm-css-token-theming.md
status: active
---
All CSS color values outside `src/styles/theme.css` must reference `--xpm-*` tokens; hardcoded hex/rgb/hsl literals in `src/**/*.{ts,tsx,css}` are banned and enforced by `tools/check-bans.mjs` as part of `npm run verify`. The ban rule matches `#[0-9a-fA-F]{6}` — line-comment hits are skipped, block-comment and non-color hex strings must live in `theme.css` or be refactored. `src/styles/theme.css` is the only file permitted to contain raw color literals. When a new visual surface needs a color with no existing token, the correct path is: add the token to `theme.css` first, then reference it — never inline the hex value.

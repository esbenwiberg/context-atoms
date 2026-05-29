---
kind: rationale
claim: npm run verify (eleven sequential gates) is the definition of done; passing
  typecheck alone is explicitly insufficient, and UI changes additionally require
  manual visual verification against the running dev server.
anchors:
- package.json
- CLAUDE.md
tags:
- ci
- done-definition
- verify
- process
source: doc-import:CONTRIBUTING.md
status: active
---
npm run verify (eleven sequential gates) is the definition of done; passing typecheck alone is explicitly insufficient, and UI changes additionally require manual visual verification against the running dev server. The eleven gates run in order: lint → format:check → typecheck → test → build → bundle-size → bans → parity-coverage → secrets → unused → arch. This policy exists because typecheck alone does not catch runtime rendering regressions, bundle bloat, secret leaks, or architectural boundary violations.

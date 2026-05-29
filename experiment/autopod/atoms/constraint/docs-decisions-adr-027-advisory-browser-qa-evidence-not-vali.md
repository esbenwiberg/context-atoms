---
kind: constraint
claim: Every API and UI consumer must keep advisory browser QA result display visually
  and semantically separate from validation status to prevent misleading merge-readiness
  signals.
anchors:
- packages/daemon/src/api/routes/pods.ts
- packages/daemon/src/api/schemas.ts
- packages/daemon/src/api/wire-serializers.ts
tags:
- browser-qa
- advisory
- api
- ui
- adr-027
source: doc-import:docs/decisions/ADR-027-advisory-browser-qa-evidence-not-validation.md
status: active
---
Every API and UI consumer must keep advisory browser QA result display visually and semantically separate from validation status to prevent misleading merge-readiness signals. Conflating advisory observations with blocking validation results would undermine the evidence-vs-validation contract. This is a cross-cutting concern affecting any surface that renders or serialises pod results.

---
kind: constraint
claim: A decision earns ADR status only when backed by a check script, dependency-cruiser
  rule, or build-config setting that makes it irreversible without ceremony; uncheckable
  decisions belong in CLAUDE.md instead.
anchors:
- .dependency-cruiser.cjs
- tools/check-bans.mjs
- tools/check-bundle-size.mjs
- CLAUDE.md
tags:
- adr
- governance
- enforcement
source: doc-import:docs/adr/README.md
status: active
---
A decision earns ADR status only when backed by a check script, dependency-cruiser rule, or build-config setting that makes it irreversible without ceremony; uncheckable decisions belong in CLAUDE.md instead. Architectural choices that are real but currently un-enforced — such as telemetry vendor, i18n shim, or test stack — are noted in CLAUDE.md and excluded from the ADR index until enforcement exists. This prevents ADRs from drifting into unverifiable prose.

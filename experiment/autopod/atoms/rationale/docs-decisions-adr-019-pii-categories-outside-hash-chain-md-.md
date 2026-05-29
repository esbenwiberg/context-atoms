---
kind: rationale
claim: PII pattern data is dual-written to both action_audit.pii_categories and safety_events
  rows intentionally, because each serves a distinct purpose.
anchors:
- packages/daemon/src/db/migrations/093_action_audit_pii_categories.sql
- packages/daemon/src/db/migrations/092_safety_events.sql
tags:
- pii
- safety-events
- dual-write
- analytics
source: doc-import:docs/decisions/ADR-019-pii-categories-outside-hash-chain.md
status: active
---
PII pattern data is dual-written to both action_audit.pii_categories and safety_events rows intentionally, because each serves a distinct purpose. safety_events (kind='pii') carries one row per pattern hit across all six active detection sites including the action-engine path — it is the canonical cross-source fleet view. action_audit.pii_categories stores a JSON array of pattern names inline with the action row — it is the per-action-call breakdown and the legacy-bucket disambiguator: rows where pii_detected=1 but pii_categories=NULL are categorized as pattern name 'unknown' in the drill's histogram. Brief 05 treats safety_events as the primary source for forward rows and action_audit.pii_categories as secondary and legacy fallback.

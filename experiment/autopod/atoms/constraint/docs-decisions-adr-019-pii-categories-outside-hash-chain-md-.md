---
kind: constraint
claim: "computeEntryHash's payload definition is locked; any future action_audit column\
  \ that must be tamper-evident requires a superseding ADR and a chain-rehash migration\
  \ plan \u2014 never silently adding to the hash function."
anchors:
- packages/daemon/src/db/migrations/064_audit_chain.sql
- packages/daemon/src/db/migrations/093_action_audit_pii_categories.sql
- packages/daemon/src/db/migrations/095_audit_chain_verifications.sql
tags:
- audit-chain
- hash
- invariant
- governance
source: doc-import:docs/decisions/ADR-019-pii-categories-outside-hash-chain.md
status: active
---
computeEntryHash's payload definition is locked; any future action_audit column that must be tamper-evident requires a superseding ADR and a chain-rehash migration plan — never silently adding to the hash function. The current payload is: SHA-256(prev_hash || pod_id || action_name || params || response_summary || quarantine_score || created_at). Brief 02 must include a hash-stability test proving entry_hash is identical regardless of pii_categories value, specifically to guard against a well-intentioned contributor adding the column to computeEntryHash and silently breaking every existing chain. Analytics/metadata columns that do NOT need attestation follow the sidecar pattern established by pii_categories.

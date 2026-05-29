---
kind: constraint
claim: pii_categories must be stored outside the audit-chain hash payload so that
  privacy metadata can be updated without invalidating the integrity chain.
anchors:
- packages/daemon/src/db/migrations/093_action_audit_pii_categories.sql
- packages/daemon/src/db/migrations/064_audit_chain.sql
- packages/daemon/src/db/migrations/095_audit_chain_verifications.sql
tags:
- audit-chain
- pii
- security
- integrity
source: doc-import:docs/analytics-dashboard-plan.md#status
status: active
---
pii_categories must be stored outside the audit-chain hash payload so that privacy metadata can be updated without invalidating the integrity chain. ADR-019 established this split: fields included in the hash are frozen at write time, but pii_categories (e.g. names, tokens detected in action output) may need retroactive correction or enrichment by privacy pipelines. Any new column added to the audit trail must be explicitly classified as either hash-included (immutable signal) or hash-excluded (mutable metadata); defaulting a new field into the hash body will break chain verification for all rows written after the migration.

---
kind: constraint
claim: The `action_audit.pii_categories` column is stored outside the HMAC hash-chain
  payload so PII categorization can be added or updated retroactively without invalidating
  existing chain verifications.
anchors:
- packages/daemon/src/db/migrations/093_action_audit_pii_categories.sql
- packages/daemon/src/db/migrations/095_audit_chain_verifications.sql
tags:
- audit
- pii
- hash-chain
- integrity
source: doc-import:docs/decisions/index.md
status: active
---
The `action_audit.pii_categories` column is stored outside the HMAC hash-chain payload so PII categorization can be added or updated retroactively without invalidating existing chain verifications. The hash chain covers the core action fields; pii_categories is a mutable annotation appended after the fact. Any code that computes or verifies the audit chain MUST NOT include pii_categories in the hashed payload, and any code that writes pii_categories MUST NOT re-hash or re-sign the chain row.

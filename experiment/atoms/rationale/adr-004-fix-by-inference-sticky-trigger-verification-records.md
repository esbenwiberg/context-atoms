---
kind: rationale
claim: Sticky-trigger verification records are stored in the `finding_dismissals`
  table using a synthesised SHA-256 signature rather than a dedicated table.
anchors:
- src/pr_guardian/persistence/storage.py
- src/pr_guardian/persistence/models.py
- alembic/versions/007_add_finding_dismissals.py
- alembic/versions/018_add_finding_lifecycle.py
- tests/test_finding_lifecycle.py
tags:
- sticky-triggers
- finding-dismissals
- storage
- lifecycle
source: doc-import:docs/decisions/ADR-004-fix-by-inference.md
status: active
---
Sticky-trigger verification records are stored in the `finding_dismissals` table using a synthesised SHA-256 signature rather than a dedicated table. A parallel `sticky_trigger_verifications` table was rejected because it would duplicate the same lifecycle columns (`pr_id`, signature, `verified_by`, `verified_at`). Reusing `finding_dismissals` means `get_finding_states(pr_id)` naturally includes trigger acknowledgements alongside finding lifecycle events, and the wizard's Verification chapter shares the same persistence path as the dismiss flow. The synthesised signature is `sha256(pr_id::trigger_kind::trigger_source)[:16]`.

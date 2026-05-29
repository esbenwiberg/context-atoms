---
kind: constraint
claim: "The signature schemes \u2014 `file::category::agent` for findings and `sha256(pr_id::trigger_kind::trigger_source)[:16]`\
  \ for sticky triggers \u2014 are a breaking-change boundary; altering either invalidates\
  \ all historical lifecycle records."
anchors:
- src/pr_guardian/models/findings.py
- src/pr_guardian/persistence/storage.py
- src/pr_guardian/persistence/models.py
- alembic/versions/018_add_finding_lifecycle.py
tags:
- signatures
- lifecycle
- breaking-change
source: doc-import:docs/decisions/ADR-004-fix-by-inference.md
status: active
---
The signature schemes — `file::category::agent` for findings and `sha256(pr_id::trigger_kind::trigger_source)[:16]` for sticky triggers — are a breaking-change boundary; altering either invalidates all historical lifecycle records. Both signatures are used as the join key in `finding_dismissals` (which stores lifecycle state for both ordinary findings and trigger acknowledgements). Any change to how a signature is computed will silently orphan existing rows — prior `fixed`/`regressed`/`dismissed` states will no longer match re-run findings. Treat any modification to `finding_signature()` or the trigger hash formula as a migration requiring a data backfill.

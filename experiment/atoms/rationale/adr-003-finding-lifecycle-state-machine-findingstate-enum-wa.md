---
kind: rationale
claim: FindingState enum was introduced because a boolean dismissed column cannot
  distinguish 'developer fixed' from 'human dismissed', and two booleans produce undefined
  combined states.
anchors:
- src/pr_guardian/persistence/storage.py
- alembic/versions/018_add_finding_lifecycle.py
- src/pr_guardian/models/findings.py
tags:
- finding-lifecycle
- state-machine
- dismissals
source: doc-import:docs/decisions/ADR-003-finding-lifecycle-state-machine.md
status: active
---
FindingState enum was introduced because a boolean dismissed column cannot distinguish 'developer fixed' from 'human dismissed', and two booleans produce undefined combined states. The wizard needs to audit-differentiate 'dev cleaned it up between runs' (fixed) from 'human said it's fine' (dismissed). A second boolean like fixed_by_inference creates states such as dismissed=True AND fixed=True that have no defined semantics. The enum forces a single authoritative state per (pr_id, signature) row.

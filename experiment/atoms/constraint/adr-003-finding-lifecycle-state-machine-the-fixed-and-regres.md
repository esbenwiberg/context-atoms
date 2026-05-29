---
kind: constraint
claim: The fixed and regressed states are set exclusively by automated signature diffing
  on re-run and must never be set by user action.
anchors:
- src/pr_guardian/persistence/storage.py
- src/pr_guardian/models/findings.py
- tests/test_finding_lifecycle.py
tags:
- finding-lifecycle
- fixed
- regressed
- inference-only
source: doc-import:docs/decisions/ADR-003-finding-lifecycle-state-machine.md
status: active
---
The fixed and regressed states are set exclusively by automated signature diffing on re-run and must never be set by user action. Only dismissed (wizard dismiss button) and verified (wizard Acknowledge & Approve) are user-settable transitions. This separation keeps the audit story clean: fixed/regressed reflect objective code changes between runs, while dismissed/verified reflect human judgement calls.

---
kind: constraint
claim: 'The verified state is terminal: subsequent mark_fixed, mark_regressed, and
  mark_verified calls on an already-verified row must be silent no-ops to preserve
  audit history.'
anchors:
- src/pr_guardian/persistence/storage.py
- tests/test_finding_lifecycle.py
tags:
- finding-lifecycle
- verified
- terminal-state
- audit
source: doc-import:docs/decisions/ADR-003-finding-lifecycle-state-machine.md
status: active
---
The verified state is terminal: subsequent mark_fixed, mark_regressed, and mark_verified calls on an already-verified row must be silent no-ops to preserve audit history. Once a human issues an Acknowledge & Approve action, that record ('alice acknowledged this on 2026-05-18') is permanent and must not be revocable by a later automated inference pass. If the underlying issue reappears on a later run it surfaces either as a new signature or as regressed on the same signature, but the verified row stays verified.

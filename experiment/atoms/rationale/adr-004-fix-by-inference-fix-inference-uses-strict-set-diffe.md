---
kind: rationale
claim: Fix inference uses strict set-difference on `file::category::agent` signatures
  rather than fuzzy or rename-aware matching.
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/models/findings.py
- tests/test_fix_inference.py
tags:
- fix-inference
- signatures
- lifecycle
source: doc-import:docs/decisions/ADR-004-fix-by-inference.md
status: active
---
Fix inference uses strict set-difference on `file::category::agent` signatures rather than fuzzy or rename-aware matching. Fuzzy matching was rejected because it introduces ambiguity ('did this fix auth.py:42 or just move the same bug to auth/jwt.py:38?') and a tuning surface with no clear owner. The diff baseline is the immediately-prior review run for the same `pr_id` (not the original review, which would penalise legitimate intermediate fixes). `fixed = prev_sigs − current_sigs`; `regressed = previously_fixed_sigs ∩ current_sigs` where `previously_fixed_sigs` comes from `get_finding_states(pr_id)` filtered to `FindingState.FIXED`. A side-effect: renaming a file makes the old signature appear 'fixed' and the new signature appear 'new' — accepted as a known trade-off since the audit log still records both events.

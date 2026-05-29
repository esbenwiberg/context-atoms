---
kind: constraint
claim: The root config edit policy blocks auto-approval only when the current diff
  path is exactly `review.yml`; `old_path` rename-away and delete cases are intentionally
  out of scope until a future feature explicitly broadens the policy.
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/types.py
tags:
- config-policy
- auto-approve
- narrow-by-design
- review.yml
source: doc-import:docs/decisions/ADR-005-final-auto-approval-gate.md
status: active
---
The root config edit policy blocks auto-approval only when the current diff path is exactly `review.yml`; `old_path` rename-away and delete cases are intentionally out of scope until a future feature explicitly broadens the policy.

This narrowness is a deliberate v1 scoping choice documented in ADR-005, not an oversight. Any implementation that inspects `old_path` for renames or deletes of `review.yml` is going beyond the contracted scope and should be treated as a scope change requiring its own decision.

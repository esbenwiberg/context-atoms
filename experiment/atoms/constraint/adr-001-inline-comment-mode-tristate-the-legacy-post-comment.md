---
kind: constraint
claim: 'The legacy post_comment: bool field has no compatibility shim; callers passing
  it receive HTTP 422 and must migrate to comment_mode.'
anchors:
- src/pr_guardian/api/review.py
- src/pr_guardian/models/pr.py
tags:
- breaking-change
- api-contract
- comment-mode
source: doc-import:docs/decisions/ADR-001-inline-comment-mode-tristate.md
status: active
---
The legacy post_comment: bool field has no compatibility shim; callers passing it receive HTTP 422 and must migrate to comment_mode.

This was an explicit decision: the API is internal with no known external consumers at the time of the change (2026-05-25), so the breakage was deemed acceptable over the cost of maintaining a shim that silently maps the old field to one of the new modes — which would itself require an arbitrary policy choice about which mode to infer.

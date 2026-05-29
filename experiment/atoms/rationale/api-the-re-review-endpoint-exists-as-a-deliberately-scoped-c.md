---
kind: rationale
claim: The re-review endpoint exists as a deliberately scoped, cheaper alternative
  to a full pipeline re-run when a PR has been updated after an initial review.
anchors:
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/api/review.py
tags:
- re-review
- cost
- design
source: doc-import:docs/api.md
status: active
---
The re-review endpoint exists as a deliberately scoped, cheaper alternative to a full pipeline re-run when a PR has been updated after an initial review. A full review re-runs all agents from scratch and can hallucinate new findings. Re-review skips discovery and mechanical checks entirely, operating only on the delta (last reviewed commit → current HEAD) against the known finding set. The trade-off is intentional: lower cost and no false positives, at the expense of missing genuinely new issues introduced in the update — callers who need full coverage should use `POST /api/review` instead.

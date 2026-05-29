---
kind: constraint
claim: PR Guardian never auto-merges a PR; it only votes approve and posts a summary
  comment, leaving the author to click merge.
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/decision/engine.py
tags:
- auto-approve
- merge
- safety
source: doc-import:docs/plan/00-overview.md
status: active
---
PR Guardian never auto-merges a PR; it only votes approve and posts a summary comment, leaving the author to click merge.

This is a deliberate safety invariant: the pipeline's highest possible outcome is posting an approval vote with a review summary. Auto-merge is explicitly out of scope regardless of how confident the decision engine is. Any code path that interacts with the platform adapter to post outcomes must only call vote/comment APIs, never merge APIs.

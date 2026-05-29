---
kind: constraint
claim: PR Guardian never auto-merges; it only votes approve and posts a summary comment,
  leaving the author to click merge.
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/decision/engine.py
tags:
- auto-approve
- merge
- policy
source: doc-import:README.md
status: active
---
PR Guardian never auto-merges. When the decision engine reaches an auto-approve verdict it casts an approval vote on the platform and posts a summary comment, but the merge action itself must always be performed by the PR author. This is an explicit product invariant — no code path should trigger a platform merge on the author's behalf.

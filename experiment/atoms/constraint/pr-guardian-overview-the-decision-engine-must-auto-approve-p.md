---
kind: constraint
claim: The decision engine must auto-approve PRs but must never auto-merge them; the
  author always performs the merge.
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/decision/engine.py
tags:
- auto-approve
- merge-safety
- decision
source: doc-import:docs/plan/pr-guardian-overview.md
status: active
---
The decision engine must auto-approve PRs but must never auto-merge them; the author always performs the merge. Guardian posts an approval vote and a comment but does not invoke any merge API. This boundary is intentional: Guardian is a safety net, not a gatekeeper. Removing it would make Guardian a hard blocker in the merge path, which violates the design contract and shifts responsibility away from the author.

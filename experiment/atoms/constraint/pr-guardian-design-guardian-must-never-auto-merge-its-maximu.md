---
kind: constraint
claim: Guardian must never auto-merge; its maximum autonomous action is to cast an
  approval vote and post a summary comment, leaving the merge action to the PR author.
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/decision/engine.py
tags:
- auto-approve
- merge
- safety
source: doc-import:docs/plan/pr-guardian-design.md
status: active
---
Guardian must never auto-merge; its maximum autonomous action is to cast an approval vote and post a summary comment, leaving the merge action to the PR author.

The decision output for a passing PR is `{ decision: 'auto_approve', summary, agent_reports }`. The actions layer posts the approval and summary but must not call any merge API. This boundary is intentional: it keeps a human in the loop for the final irreversible action while still removing the review bottleneck for low-risk PRs.

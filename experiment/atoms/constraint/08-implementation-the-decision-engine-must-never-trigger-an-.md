---
kind: constraint
claim: The decision engine must never trigger an auto-merge; the maximum automated
  action is posting a review comment or approving a PR.
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/platform/ado.py
- src/pr_guardian/platform/github.py
tags:
- decision
- safety
- platform
source: doc-import:docs/plan/08-implementation.md
status: active
---
The decision engine must never trigger an auto-merge; the maximum automated action is posting a review comment or approving a PR (+10 ADO vote / GitHub review approval). This is an explicit safety boundary stated in the data flow: 'Platform adapter → PR comment / approve (never auto-merge)'. All merge decisions remain with humans regardless of score.

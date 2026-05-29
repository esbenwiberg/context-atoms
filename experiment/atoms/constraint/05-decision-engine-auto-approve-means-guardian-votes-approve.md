---
kind: constraint
claim: "Auto-approve means Guardian votes approve and posts a summary comment only\
  \ \u2014 Guardian never merges a PR automatically; the author always performs the\
  \ final merge action."
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/decision/engine.py
tags:
- auto-approve
- merge
- safety
- behavior
source: doc-import:docs/plan/05-decision-engine.md
status: active
---
Auto-approve means Guardian votes approve and posts a summary comment only — Guardian never merges a PR automatically; the author always performs the final merge action. When auto-approving, Guardian must: post a PR comment with checks run, agent verdicts, any low-severity findings, risk tier/class/score; cast an approve vote; send a Teams/Slack notification that the PR is ready. The author then decides when to merge. This constraint exists to preserve human intent on every merge even when risk is low.

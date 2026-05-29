---
kind: constraint
claim: "Guardian may only vote approve and post a summary comment; it must never trigger\
  \ an automatic merge \u2014 the author always clicks merge."
anchors:
- src/pr_guardian/decision/actions.py
- src/pr_guardian/decision/engine.py
tags:
- auto-approve
- merge-safety
- decision-engine
source: doc-import:docs/plan/01-philosophy.md
status: active
---
Guardian may only vote approve and post a summary comment; it must never trigger an automatic merge — the author always clicks merge.

This is an explicit safety boundary: auto-approve is distinct from auto-merge. Even when the decision engine resolves to the highest-confidence approval, the platform action is limited to casting an approval vote plus a summary comment. Merge authority stays with the PR author at all times.

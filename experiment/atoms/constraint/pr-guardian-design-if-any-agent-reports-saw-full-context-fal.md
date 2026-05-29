---
kind: constraint
claim: If any agent reports `saw_full_context = false` in its `evidence_basis`, the
  PR must be escalated to human review regardless of other verdict values, because
  an agent that lacked full context cannot be trusted when it produces no findings.
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/validator.py
- src/pr_guardian/agents/base.py
tags:
- saw_full_context
- escalation
- human-review
- silence
source: doc-import:docs/plan/pr-guardian-design.md
status: active
---
If any agent reports `saw_full_context = false` in its `evidence_basis`, the PR must be escalated to human review regardless of other verdict values, because an agent that lacked full context cannot be trusted when it produces no findings.

The auto-approve path requires ALL agents to have `saw_full_context = true`. The logic is: silence from a fully-informed agent is evidence of no issue; silence from a partially-informed agent is merely absence of evidence. Truncated diffs, missing file history, or context window limits can all cause `saw_full_context = false`.

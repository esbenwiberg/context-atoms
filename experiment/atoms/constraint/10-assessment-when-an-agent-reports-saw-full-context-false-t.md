---
kind: constraint
claim: 'When an agent reports saw_full_context: false, the decision engine must treat
  that agent''s output as untrusted.'
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/agents/base.py
tags:
- context-window
- trust
- large-pr
source: doc-import:docs/plan/10-assessment.md
status: active
---
When an agent cannot see the full diff (saw_full_context: false — triggered by large PRs exceeding context limits), the decision engine must treat that agent's findings as untrusted. The agent's silence on issues it could not see must not be interpreted as a clean signal. This constraint exists because partial-context analysis can produce misleadingly positive results; the engine must not auto-approve based on an incomplete scan.

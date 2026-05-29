---
kind: rationale
claim: Mechanical gates are designed to complete in under 2 minutes and run before
  AI agents are invoked, so any hard failure blocks the PR without spending LLM budget.
anchors:
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/mechanical/runner.py
tags:
- orchestration
- mechanical
- performance
- cost
source: doc-import:docs/plan/02-mechanical-gates.md
status: active
---
Mechanical gates are designed to complete in under 2 minutes and run before AI agents are invoked, so any hard failure blocks the PR without spending LLM budget. The ordering is intentional: deterministic checks are cheap and fast; running agents on a PR that has a hardcoded secret or critical CVE would waste tokens and obscure a clear signal. The gate stage must fully resolve (pass or hard-fail) before the orchestrator hands off to any agent.

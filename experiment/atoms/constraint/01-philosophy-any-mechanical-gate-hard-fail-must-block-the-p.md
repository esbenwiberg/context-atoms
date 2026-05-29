---
kind: constraint
claim: "Any mechanical gate hard-fail must block the PR and skip all AI agents \u2014\
  \ agents are only invoked after all mechanical checks pass."
anchors:
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/mechanical/runner.py
tags:
- pipeline-order
- mechanical-gates
- orchestration
source: doc-import:docs/plan/01-philosophy.md
status: active
---
Any mechanical gate hard-fail must block the PR and skip all AI agents — agents are only invoked after all mechanical checks pass.

Mechanical checks (Semgrep, Gitleaks, migration safety, PII scan, etc.) are deterministic and fast (<2 min). Running expensive AI agents on a PR that has already failed a deterministic check wastes compute and can produce misleading output. The orchestrator must short-circuit to a block decision on any hard mechanical failure without entering the triage or agent stages.

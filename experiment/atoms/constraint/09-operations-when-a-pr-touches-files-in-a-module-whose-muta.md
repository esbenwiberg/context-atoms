---
kind: constraint
claim: When a PR touches files in a module whose mutation survival score is below
  60%, the test quality agent must receive extra context about that module's coverage
  gap.
anchors:
- src/pr_guardian/agents/test_quality.py
- src/pr_guardian/core/orchestrator.py
tags:
- mutation-testing
- test-quality
- agent-context
- threshold
source: doc-import:docs/plan/09-operations.md
status: active
---
When a PR touches files in a module whose mutation survival score is below 60%, the test quality agent must receive extra context about that module's coverage gap. Mutation scores are stored per-module in .pr-guardian/mutation-scores.json and updated by the weekly mutation testing scheduled task. The 60% threshold is the design boundary below which test coverage is considered insufficient to validate correctness. The orchestrator is responsible for injecting this context before invoking the test quality agent.

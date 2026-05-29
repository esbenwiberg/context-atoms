---
kind: constraint
claim: The decision engine in `decision/` is the only place that mints verdicts; agents
  and mechanical gates return findings only.
anchors:
- src/pr_guardian/decision/
- src/pr_guardian/agents/
- src/pr_guardian/mechanical/
tags:
- decision
- verdict
- architecture
- pipeline
source: doc-import:ARCHITECTURE.md
status: active
---
The decision engine in `decision/` is the only place that mints verdicts (`APR` / `REV` / `BLK`); agents and mechanical gates return findings only.

Agents produce `AgentResult` objects with findings and certainty levels. Mechanical gates produce `MechanicalResult` objects with deterministic check outcomes. Neither layer makes an approve/request-changes/block call — that authority belongs exclusively to `decision/engine.py`, which performs weighted scoring and certainty validation before emitting a verdict.

`decision/` is pure logic over data with no IO. Introducing verdict logic in any upstream layer (agents, mechanical, orchestrator) breaks the single source of truth for review outcomes and makes the pipeline reasoning about verdicts impossible to audit in one place.

---
kind: rationale
claim: Agent findings use a `detected`/`suspected`/`uncertain` certainty enum instead
  of a confidence float so the decision engine can structurally enforce that agents
  show evidence before claiming high certainty.
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/validator.py
- src/pr_guardian/models/findings.py
- src/pr_guardian/agents/base.py
tags:
- certainty
- findings
- decision-engine
- evidence
source: doc-import:docs/plan/pr-guardian-design.md
status: active
---
Agent findings use a `detected`/`suspected`/`uncertain` certainty enum instead of a confidence float so the decision engine can structurally enforce that agents show evidence before claiming high certainty.

Each finding carries an `evidence_basis` object with fields: `saw_full_context`, `pattern_match`, `cwe_id`, `similar_code_in_repo`, `suggestion_is_concrete`, `cross_references`. The decision engine validates the certainty level against these fields — an agent cannot emit `certainty=detected` without meeting the evidence bar. A float would allow agents to self-report high confidence without accountability; the enum forces a discrete claim that the engine can reject.

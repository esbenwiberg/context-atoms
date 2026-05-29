---
kind: constraint
claim: 'The decision engine must validate and potentially downgrade agent certainty
  claims: ''detected'' requires 2+ evidence signals and ''suspected'' requires 1+
  signal, otherwise the claim is silently downgraded one level.'
anchors:
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/validator.py
- src/pr_guardian/models/findings.py
tags:
- certainty
- validation
- evidence
- downgrade
source: doc-import:docs/plan/05-decision-engine.md
status: active
---
The decision engine must validate and potentially downgrade agent certainty claims: 'detected' requires 2+ evidence signals and 'suspected' requires 1+ signal, otherwise the claim is silently downgraded one level. Agents cannot self-certify high certainty — they must show evidence. For 'detected': needs 2+ of {pattern_match+cwe_id, concrete suggestion, saw_full_context, cross_references>=1}; else downgraded to 'suspected'. For 'suspected': needs 1+ of {pattern_match, saw_full_context, concrete suggestion}; else downgraded to 'uncertain'. The validated certainty (not the agent's claimed certainty) is what feeds scoring and override rules.

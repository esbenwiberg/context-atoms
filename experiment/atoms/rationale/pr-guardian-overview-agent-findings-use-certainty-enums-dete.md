---
kind: rationale
claim: Agent findings use certainty enums (detected/suspected/uncertain) instead of
  confidence floats so the decision engine can validate and downgrade unsubstantiated
  claims.
anchors:
- src/pr_guardian/models/findings.py
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/validator.py
tags:
- certainty
- findings
- decision-engine
- agent-trust
source: doc-import:docs/plan/pr-guardian-overview.md
status: active
---
Agent findings use certainty enums (detected/suspected/uncertain) instead of confidence floats so the decision engine can validate and downgrade unsubstantiated claims. Each certainty level requires structured evidence (CWE, pattern, cross-refs); if evidence is insufficient for the claimed level, the engine downgrades it before scoring. This was chosen over floats because a float is opaque — agents could inflate confidence without providing verifiable evidence. Enums force agents to commit to a tier that the deterministic engine can independently audit.

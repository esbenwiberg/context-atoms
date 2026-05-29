---
kind: rationale
claim: The certainty field on findings is an enum (detected | suspected | uncertain)
  rather than a float probability to avoid unreliable LLM-generated numeric confidence
  values.
anchors:
- src/pr_guardian/models/findings.py
- src/pr_guardian/decision/validator.py
tags:
- certainty
- findings
- llm-reliability
source: doc-import:docs/plan/04-ai-agents.md
status: active
---
The certainty field on findings is an enum (detected | suspected | uncertain) rather than a float probability to avoid unreliable LLM-generated numeric confidence values. 'detected' means a concrete pattern with a CWE and specific fix; 'suspected' means it looks problematic but needs more context; 'uncertain' means the area is risky but no specific issue can be pinpointed. The decision engine validates certainty against the evidence_basis sub-object rather than trusting a raw number from the LLM.

---
kind: rationale
claim: Agents use certainty enums (`detected` / `suspected` / `uncertain`) instead
  of confidence floats because the decision engine must be able to validate that each
  claim is backed by structured evidence.
anchors:
- src/pr_guardian/decision/types.py
- src/pr_guardian/decision/validator.py
- src/pr_guardian/decision/engine.py
- src/pr_guardian/models/findings.py
tags:
- certainty
- evidence
- findings
- decision-engine
source: doc-import:docs/plan/01-philosophy.md
status: active
---
Agents use certainty enums (`detected` / `suspected` / `uncertain`) instead of confidence floats because the decision engine must be able to validate that each claim is backed by structured evidence.

A float like 0.85 is unverifiable — there is no way for downstream logic to confirm the number reflects real evidence rather than hallucination. The three-value enum forces agents to declare the strength of their finding explicitly, and the decision engine can then reject any finding marked `detected` that lacks a corresponding evidence_basis, preventing agents from overstating certainty without showing their work.

---
kind: constraint
claim: "LLM escalation must never lower a trust tier \u2014 path rules set an immutable\
  \ floor, and agent findings can only raise the tier to MANDATORY_HUMAN or above."
anchors:
- src/pr_guardian/triage/trust_escalation.py
- src/pr_guardian/triage/trust_classifier.py
tags:
- trust-tier
- escalation
- invariant
- one-way
source: doc-import:docs/plan/tiered-trust.md
status: active
---
LLM escalation must never lower a trust tier — path rules set an immutable floor, and agent findings can only raise the tier to MANDATORY_HUMAN or above.

Escalation triggers and their minimum post-escalation tier:
- Security-category finding (auth, permission, token, credential, encryption, RBAC, SQL injection) in a file classified below MANDATORY_HUMAN → MANDATORY_HUMAN
- Any agent verdict of flag_human → MANDATORY_HUMAN
- Critical severity + detected certainty finding → MANDATORY_HUMAN
- Repo risk class = critical → MANDATORY_HUMAN

A file matched as human_primary by path rules stays human_primary even if agents find nothing. The LLM never chooses a tier directly — it produces findings with categories and severities, and deterministic escalation rules interpret those findings. This keeps the system predictable and prevents the AI from silently reducing oversight.

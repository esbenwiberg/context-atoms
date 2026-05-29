---
kind: rationale
claim: The `architecture_intent` agent is split into two identities (`intent` and
  `architecture`) because they require different anchor sources and opposing missing-anchor
  semantics.
anchors:
- src/pr_guardian/agents/architecture_intent.py
- src/pr_guardian/agents/base.py
- src/pr_guardian/core/orchestrator.py
tags:
- agents
- architecture
- intent
- split
- anchors
source: doc-import:docs/decisions/ADR-006-split-verifier-agent-identity.md
status: active
---
The `architecture_intent` agent is split into two identities (`intent` and `architecture`) because they require different anchor sources and opposing missing-anchor semantics. `intent` treats a missing PR-author claim as a problem on medium/high-risk changes. `architecture` must skip entirely — returning a PASS with explanation — when no architecture ground truth exists, because attempting to verify without anchors produces subjective noise. A single combined agent cannot express both behaviors cleanly. Rejected alternative: keep one agent and use better prompt instructions (does not solve the structural anchor difference).

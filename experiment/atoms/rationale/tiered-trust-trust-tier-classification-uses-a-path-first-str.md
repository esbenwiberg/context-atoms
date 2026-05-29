---
kind: rationale
claim: Trust tier classification uses a path-first strategy with LLM-only escalation
  because path patterns are deterministic, zero-cost, and auditable, while LLM agents
  handle cases where naming conventions fail (e.g., auth logic in src/utils/helpers.py).
anchors:
- src/pr_guardian/triage/trust_classifier.py
- src/pr_guardian/triage/trust_escalation.py
tags:
- trust-tier
- classification
- path-matching
- llm-escalation
source: doc-import:docs/plan/tiered-trust.md
status: active
---
Trust tier classification uses a path-first strategy with LLM-only escalation because path patterns are deterministic, zero-cost, and auditable, while LLM agents handle cases where naming conventions fail (e.g., auth logic in src/utils/helpers.py).

Stage 0 matches each changed file against config-driven path patterns (e.g., `**/auth/**` → human_primary). The PR-level tier is the highest (least trusting) tier across all files. This runs in microseconds with zero API calls and produces an auditable answer: 'this was flagged because it matched X pattern'.

After agents run (stages 1–3), their findings are inspected for trust-relevant signals: security-category findings in low-tier files, agent verdict flag_human, or critical+detected severity findings. These can only raise the tier, never lower it.

Rejected alternative: a pure LLM classification call. This would add latency, cost, and a black-box decision with no auditable path. Path rules also need to influence which agents run, so they must resolve before agents execute.

---
kind: constraint
claim: "Modules in `src/pr_guardian/mechanical/` must never make LLM calls \u2014\
  \ all checks are deterministic/static-analysis only."
anchors:
- src/pr_guardian/mechanical/
tags:
- mechanical
- llm
- architecture
- layer-rule
source: doc-import:CONTRIBUTING.md
status: active
---
Modules in `src/pr_guardian/mechanical/` must never make LLM calls — all checks are deterministic/static-analysis only.
The mechanical layer is explicitly separated from the agent/LLM layer. Adding an LLM call inside any file under `src/pr_guardian/mechanical/` violates the architectural boundary that keeps mechanical checks fast, cost-free, and side-effect-free.

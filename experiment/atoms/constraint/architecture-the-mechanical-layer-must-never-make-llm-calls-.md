---
kind: constraint
claim: The `mechanical/` layer must never make LLM calls; it is restricted to deterministic
  checks only, enforced by import-linter.
anchors:
- src/pr_guardian/mechanical/
tags:
- mechanical
- llm
- layers
- determinism
source: doc-import:ARCHITECTURE.md
status: active
---
The `mechanical/` layer must never make LLM calls; it is restricted to deterministic checks only, enforced by import-linter.

Mechanical gates (semgrep, gitleaks, dep risk, PII, migration safety) are deterministic by design so their results are reproducible and auditable without model variance. Any logic that requires a model belongs in `agents/`, not `mechanical/`. The import-linter rule in `pyproject.toml` statically enforces this boundary and will fail CI if violated.

If a new check feels like it needs an LLM to reason about the code, it is an agent finding, not a mechanical gate.

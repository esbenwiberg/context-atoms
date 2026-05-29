---
kind: constraint
claim: The `mechanical/` layer must never import from `llm/`; deterministic gates
  must remain deterministic, and any nuance they uncover must be escalated through
  triage rather than resolved via an LLM call.
anchors:
- src/pr_guardian/mechanical/
- src/pr_guardian/llm/
- pyproject.toml
tags:
- architecture
- import-linter
- determinism
- mechanical
source: doc-import:CLAUDE.md
status: active
---
The `mechanical/` layer must never import from `llm/`; deterministic gates must remain deterministic, and any nuance they uncover must be escalated through triage rather than resolved via an LLM call.

This constraint is enforced at CI time via `import-linter` (configured in `pyproject.toml`). Violations break the build.

The mechanical gates (semgrep, gitleaks, dep checks, PII scanner) are designed to be fully reproducible and side-effect-free. Mixing LLM calls into them would make their outputs non-deterministic and untestable. When a mechanical check detects something ambiguous, the correct path is to surface it as a finding and let triage decide whether an agent should examine it further — not to call an LLM inline.

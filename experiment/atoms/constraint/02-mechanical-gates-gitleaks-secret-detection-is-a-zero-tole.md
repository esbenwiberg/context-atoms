---
kind: constraint
claim: "Gitleaks secret detection is a zero-tolerance hard block \u2014 any detected\
  \ secret immediately blocks the PR with no severity threshold and no exceptions."
anchors:
- src/pr_guardian/mechanical/gitleaks.py
tags:
- security
- secrets
- gitleaks
- blocking
source: doc-import:docs/plan/02-mechanical-gates.md
status: active
---
Gitleaks secret detection is a zero-tolerance hard block — any detected secret immediately blocks the PR with no severity threshold and no exceptions. Unlike Semgrep (blocks on HIGH, warns on MEDIUM) or the PII scanner (tiered by data type), Gitleaks has a binary outcome: detected → block. The scanner runs on the diff only, not the full history, on every PR.

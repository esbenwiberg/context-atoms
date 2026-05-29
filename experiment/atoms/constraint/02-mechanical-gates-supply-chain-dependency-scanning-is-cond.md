---
kind: constraint
claim: 'Supply chain dependency scanning is conditional: it only runs when package.json,
  requirements.txt, or *.csproj files are part of the PR diff.'
anchors:
- src/pr_guardian/mechanical/deps.py
tags:
- supply-chain
- dependencies
- conditional-execution
source: doc-import:docs/plan/02-mechanical-gates.md
status: active
---
Supply chain dependency scanning is conditional: it only runs when package.json, requirements.txt, or *.csproj files are part of the PR diff. PRs that do not touch dependency manifests skip this check entirely. This avoids false-positive noise on unrelated changes and keeps the mechanical stage fast. The gate blocks on critical CVEs and warns on medium severity.

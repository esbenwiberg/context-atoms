---
kind: constraint
claim: AI coding agents must append their model name (e.g. CLAUDE, CODEX) to the end
  of every PR title and commit message.
anchors:
- CLAUDE.md
tags:
- git
- agents
- commit-conventions
source: doc-import:CLAUDE.md#development-guidelines
status: active
---
AI coding agents must append their model name (e.g. CLAUDE, CODEX) to the end of every PR title and commit message. This applies in addition to the Conventional Commits format required for PR titles. Example: 'feat: add BigQuery TIMESTAMP support [CLAUDE]'. Human contributors are not subject to this rule.

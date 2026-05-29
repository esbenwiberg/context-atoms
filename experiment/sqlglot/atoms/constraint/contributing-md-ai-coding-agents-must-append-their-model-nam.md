---
kind: constraint
claim: AI coding agents must append their model name (e.g., CLAUDE, CODEX) to the
  end of every pull request title.
anchors:
- CONTRIBUTING.md
tags:
- pr
- ai-agents
- git
source: doc-import:CONTRIBUTING.md
status: active
---
AI coding agents must append their model name (e.g., CLAUDE, CODEX) to the end of every pull request title. This is stated as an IMPORTANT directive at the top of CONTRIBUTING.md, addressed specifically to agents. Example: 'Fix Snowflake date parsing [CLAUDE]'. Failure to do so violates the project's contribution conventions for automated contributors.

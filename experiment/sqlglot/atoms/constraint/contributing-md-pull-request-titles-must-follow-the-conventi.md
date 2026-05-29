---
kind: constraint
claim: Pull request titles must follow the Conventional Commits specification.
anchors:
- CONTRIBUTING.md
tags:
- pr
- commits
- git
source: doc-import:CONTRIBUTING.md
status: active
---
Pull request titles must follow the Conventional Commits specification (https://www.conventionalcommits.org/en/v1.0.0/). This is called out in the PR submission checklist in CONTRIBUTING.md. Examples of valid prefixes: feat:, fix:, refactor:, test:, docs:. This constraint applies in addition to the agent-model-name suffix requirement.

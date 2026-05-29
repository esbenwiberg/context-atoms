---
kind: constraint
claim: 'Commit messages must follow Conventional Commits format: `type(scope): subject`
  (e.g. `fix(daemon): preserve pod status transition`).'
anchors:
- .githooks/commit-msg
tags:
- git
- commits
- convention
source: doc-import:CONTRIBUTING.md
status: active
---
Commit messages must follow Conventional Commits format: `type(scope): subject` (e.g. `fix(daemon): preserve pod status transition`). Branch names should be short and descriptive, typically `feat/<topic>`, `fix/<topic>`, or `docs/<topic>`. This format is enforced at commit time via the `.githooks/commit-msg` hook.

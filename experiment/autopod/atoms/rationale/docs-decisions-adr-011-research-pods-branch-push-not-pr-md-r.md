---
kind: rationale
claim: Research artifact sessions push a branch only and skip PR creation because
  build/smoke/AI-review validation is meaningless for non-code artifacts like Markdown
  files.
anchors:
- packages/daemon/src/interfaces/worktree-manager.ts
- packages/daemon/src/interfaces/pr-manager.ts
- packages/daemon/src/db/migrations/040_research_repos.sql
tags:
- research
- pods
- pr
- validation
- artifacts
source: doc-import:docs/decisions/ADR-011-research-pods-branch-push-not-pr.md
status: active
---
Research artifact sessions push a branch only and skip PR creation because build/smoke/AI-review validation is meaningless for non-code artifacts like Markdown files. When `profile.repoUrl` is set for an artifact/research session the worktreeManager push path is reused but the PR manager is bypassed entirely — no PR is opened and no validation pipeline runs. The rejected alternative was treating research sessions identically to regular code sessions (branch → build → smoke → AI review → PR), which was discarded because none of those gates apply to document content. No automated merge is intentional: research artifacts must not auto-merge to main.

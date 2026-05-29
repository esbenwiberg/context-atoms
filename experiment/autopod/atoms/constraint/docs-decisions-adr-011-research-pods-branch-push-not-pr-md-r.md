---
kind: constraint
claim: Research artifact sessions must push to branch `research/<sessionId>` and must
  never trigger PR creation or any validation phase.
anchors:
- packages/daemon/src/interfaces/worktree-manager.ts
- packages/daemon/src/interfaces/pr-manager.ts
- packages/daemon/src/db/migrations/040_research_repos.sql
tags:
- research
- pods
- branch-naming
- pr
- validation
source: doc-import:docs/decisions/ADR-011-research-pods-branch-push-not-pr.md
status: active
---
Research artifact sessions must push to branch `research/<sessionId>` and must never trigger PR creation or any validation phase. The branch naming convention `research/<sessionId>` is the canonical delivery vehicle — users browse artifacts directly in GitHub/ADO via this branch. Consistent with workspace pod behavior, which is also branch-push only. Code paths that handle post-push flow must branch on session type and route research sessions away from the PR manager and validation engine entirely.

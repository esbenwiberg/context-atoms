---
kind: constraint
claim: gh pr create must always include --head <branch> because git worktrees do not
  track remote branches.
anchors:
- CLAUDE.md
tags:
- git
- worktrees
- pr
source: doc-import:CLAUDE.md#pr-workflow
status: active
---
gh pr create must always include --head <branch> because git worktrees do not track remote branches. Without the explicit --head flag, the CLI cannot infer the correct source branch from a worktree checkout, causing PRs to target the wrong branch or fail entirely. Always run `git push -u origin <branch>` before calling gh pr create.

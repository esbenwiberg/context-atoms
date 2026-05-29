---
kind: rationale
claim: PRs must be created with an explicit `--head <branch>` flag because worktrees
  do not always track remote branches.
anchors:
- .githooks/pre-push
tags:
- git
- worktree
- pr
- github
source: doc-import:CONTRIBUTING.md
status: active
---
PRs must be created with an explicit `--head <branch>` flag because worktrees do not always track remote branches. The recommended command is `gh pr create --head <branch>`. Without `--head`, `gh pr create` may fail or target the wrong branch when run from a worktree, since worktrees lack the remote-tracking refs that a normal clone has.

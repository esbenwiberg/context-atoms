---
kind: constraint
claim: When `processSession()` finds a `recoveryWorktreePath` set on a pod, it must
  skip worktree creation and derive `bareRepoPath` from that existing path; every
  other setup step must run normally.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/db/migrations/015_recovery_worktree_path.sql
tags:
- recovery
- constraint
- pod-manager
- worktree
source: doc-import:docs/decisions/ADR-007-local-recovery-requeue-not-resume.md
status: active
---
When `processSession()` finds a `recoveryWorktreePath` set on a pod, it must skip worktree creation and derive `bareRepoPath` from that existing path; every other setup step must run normally.

This conditional is intentionally placed at the top of `processSession()` (worktree branch) and at the bottom (spawn vs. resume), not scattered throughout. All intermediate setup — network policy, skills, CLAUDE.md, credentials, registry — must execute on every recovery run just as on a fresh run.

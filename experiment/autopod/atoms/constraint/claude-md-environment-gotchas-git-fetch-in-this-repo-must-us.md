---
kind: constraint
claim: Git fetch in this repo must use an explicit refspec rather than a wildcard
  because wildcard fetches fail on Azure SMB mounts.
anchors:
- packages/daemon/src/interfaces/worktree-manager.ts
- .github/workflows/ci.yml
tags:
- git
- azure
- ci
- worktree
source: doc-import:CLAUDE.md#environment-gotchas
status: active
---
Git fetch in this repo must use an explicit refspec rather than a wildcard because wildcard fetches fail on Azure SMB mounts. Always use: `git fetch origin +refs/heads/main:refs/remotes/origin/main`. Wildcard forms (e.g. `git fetch origin`) will silently fail or error on the Azure File Share backing the sandbox. Also: `chmod` warnings on `config.lock` during push are expected and can be ignored on Azure SMB.

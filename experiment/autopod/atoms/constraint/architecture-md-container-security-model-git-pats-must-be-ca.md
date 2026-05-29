---
kind: constraint
claim: Git PATs must be cached in-memory on the daemon host only and must never be
  written to any container filesystem.
anchors:
- packages/daemon/src/crypto/credentials-cipher.ts
- packages/daemon/src/profiles/profile-pat.ts
- packages/daemon/src/crypto/pod-tokens.ts
tags:
- secrets
- security
- git
- pat
source: doc-import:ARCHITECTURE.md#container-security-model
status: active
---
Git PATs must be cached in-memory on the daemon host only and must never be written to any container filesystem. Repos are cloned as bare repos with auth baked into the URL, then the remote URL is immediately stripped via `git remote set-url` before the container gets access. This ensures that even if a container is compromised, the attacker cannot read PAT material from disk or from git config. Any code path that persists PATs (e.g. to SQLite) must use the credentials cipher and must target daemon-side storage only.

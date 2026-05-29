---
kind: rationale
claim: "GitHub App auth is preferred over PATs because it provides an org-owned identity\
  \ with short-lived rotating tokens, a 3\xD7 higher rate limit (15k vs 5k req/hr),\
  \ and granular per-repo permission scoping."
anchors:
- src/pr_guardian/platform/github.py
tags:
- github
- auth
- rate-limits
- github-app
source: doc-import:docs/plan/11-external-api-and-auth.md
status: active
---
GitHub App auth is preferred over PATs because it provides an org-owned identity with short-lived rotating tokens, a 3× higher rate limit (15k vs 5k req/hr), and granular per-repo permission scoping. GitHub does not accept Entra ID tokens, so a GitHub App is the closest equivalent to a service principal. Installation tokens last 1 hour and auto-rotate; the private key can be stored in Azure Key Vault. The migration strategy maintains backward compatibility: if GITHUB_APP_ID + GITHUB_APP_PRIVATE_KEY + GITHUB_APP_INSTALLATION_ID are set, use GitHub App auth; else fall back to GITHUB_TOKEN PAT; else error.

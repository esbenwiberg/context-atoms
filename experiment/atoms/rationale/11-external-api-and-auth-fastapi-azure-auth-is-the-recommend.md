---
kind: rationale
claim: '`fastapi-azure-auth` is the recommended library for Entra ID JWT validation
  over manual PyJWT because it handles OIDC discovery, JWKS key rotation, and nonce
  quirks out of the box.'
anchors:
- src/pr_guardian/auth/dependencies.py
tags:
- auth
- entra-id
- jwt
- library-choice
- fastapi
source: doc-import:docs/plan/11-external-api-and-auth.md
status: active
---
`fastapi-azure-auth` is the recommended library for Entra ID JWT validation over manual PyJWT because it handles OIDC discovery, JWKS key rotation, and nonce quirks out of the box. Manual PyJWT is only preferred if heavy customisation is needed. The validation pipeline must: extract the Bearer token, fetch + cache the OIDC discovery doc from `https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration`, validate RS256 signature via JWKS kid matching, check iss/aud/exp/nbf, then distinguish delegated tokens (scp claim) from app-only tokens (roles claim + oid==sub) to enforce per-endpoint permission requirements.

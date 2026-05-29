---
kind: rationale
claim: GitHub CI authenticates to Dataverse via OIDC token exchange (ClientAssertionCredential)
  rather than a long-lived client secret so no durable credential is stored on the
  runner.
anchors:
- .github/workflows/build-and-smoke.yml
- tools/lib/dataverse-client.mjs
- tools/lib/github-oidc.mjs
tags:
- ci
- auth
- dataverse
- security
source: doc-import:README.md
status: active
---
GitHub CI authenticates to Dataverse via OIDC token exchange (ClientAssertionCredential) rather than a long-lived client secret so no durable credential is stored on the runner. The workflow is granted `permissions: id-token: write`; the runner's OIDC token is exchanged for an Entra access token via the app registration's federated-credential entry. Only the three non-secret config values (tenant ID, client ID, Dataverse URL) are written to `.env.local` from repo secrets. Local runs use `ClientSecretCredential` via `.env.local` with a `DATAVERSE_CLIENT_SECRET` the developer supplies.

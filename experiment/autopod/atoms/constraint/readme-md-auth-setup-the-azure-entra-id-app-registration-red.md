---
kind: constraint
claim: The Azure Entra ID app registration redirect URI must be set to `http://localhost`
  to support the PKCE flow used by autopod.
anchors:
- packages/cli/src/auth/msal-client.ts
- .env.example
tags:
- auth
- azure
- pkce
- entra
source: doc-import:README.md#auth-setup
status: active
---
The Azure Entra ID app registration redirect URI must be set to `http://localhost` to support the PKCE flow used by autopod. PKCE (Proof Key for Code Exchange) is the auth flow autopod uses for interactive logins. The redirect URI in the Azure portal registration must match exactly what the MSAL client sends; any other value will cause the auth code exchange to fail.

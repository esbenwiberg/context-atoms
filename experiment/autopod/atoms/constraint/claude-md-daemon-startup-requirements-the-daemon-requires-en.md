---
kind: constraint
claim: The daemon requires ENTRA_CLIENT_ID and ENTRA_TENANT_ID environment variables
  to be set; placeholder values are acceptable in dev but the keys must be present.
anchors:
- packages/daemon/src/index.ts
tags:
- daemon
- startup
- auth
- env-vars
- entra
source: doc-import:CLAUDE.md#daemon-startup-requirements
status: active
---
The daemon requires ENTRA_CLIENT_ID and ENTRA_TENANT_ID environment variables to be set; placeholder values are acceptable in dev but the keys must be present. These drive the Entra (Azure AD) authentication module. Missing vars will cause startup failure in production; in dev the values are not validated because auth is stubbed.

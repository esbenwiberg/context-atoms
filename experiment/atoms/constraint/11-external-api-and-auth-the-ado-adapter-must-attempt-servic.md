---
kind: constraint
claim: 'The ADO adapter must attempt service-principal Bearer auth before PAT fallback:
  use SP if ADO_CLIENT_ID + ADO_TENANT_ID + ADO_CLIENT_SECRET are all set, fall back
  to PAT if only ADO_PAT is set, and error if neither is present.'
anchors:
- src/pr_guardian/platform/ado.py
tags:
- ado
- auth
- service-principal
- env-vars
- migration
source: doc-import:docs/plan/11-external-api-and-auth.md
status: active
---
The ADO adapter must attempt service-principal Bearer auth before PAT fallback: use SP if ADO_CLIENT_ID + ADO_TENANT_ID + ADO_CLIENT_SECRET are all set, fall back to PAT if only ADO_PAT is set, and error if neither is present. SP auth uses MSAL client-credentials flow against scope `499b84ac-1321-427f-aa17-267ca6975798/.default` (the ADO resource). MSAL caches the ~1-hour token automatically. The SP must be added to the ADO org via the Enterprise Applications Object ID (not the App Registrations App ID) and granted Code Read/Write + PR Contribute permissions.

---
kind: rationale
claim: Managed Identity is used for the daemon's Azure resource access so that no
  credentials ever appear in code or config.
anchors:
- infra/main.bicep
- infra/modules/identity.bicep
tags:
- azure
- auth
- security
- managed-identity
source: doc-import:README.md#deployment-azure
status: active
---
Managed Identity is used for the daemon's Azure resource access so that no credentials ever appear in code or config. This was a deliberate design choice rejecting alternatives like service principal secrets or connection strings stored in env vars. The Managed Identity is provisioned via Bicep and grants the Container App access to ACR and Key Vault without any secret material being stored anywhere in the deployment.

---
kind: constraint
claim: "All secrets (API keys, PATs, webhook URLs) must be stored in Azure Key Vault\
  \ \u2014 never hardcoded or placed in environment variables directly."
anchors:
- infra/modules/keyvault.bicep
- infra/parameters/dev.bicepparam
- infra/parameters/prod.bicepparam
tags:
- secrets
- keyvault
- azure
- security
source: doc-import:README.md#deployment-azure
status: active
---
All secrets (API keys, PATs, webhook URLs) must be stored in Azure Key Vault — never hardcoded or placed in environment variables directly. Key Vault is the single source of truth for sensitive values in both dev and prod environments. The daemon reads secrets from Key Vault at runtime via Managed Identity, meaning no secret material touches the Bicep parameter files or container environment config.

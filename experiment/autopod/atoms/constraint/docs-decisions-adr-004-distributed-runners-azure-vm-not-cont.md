---
kind: constraint
claim: When running on Azure File Share (SMB) mounts, git fetch must use an explicit
  refspec (`git fetch origin +refs/heads/main:refs/remotes/origin/main`) because wildcard
  fetches fail silently on SMB.
anchors:
- infra/main.bicep
- infra/modules/container-apps.bicep
tags:
- azure
- git
- smb
- infra
source: doc-import:docs/decisions/ADR-004-distributed-runners-azure-vm-not-container-apps.md
status: active
---
When running on Azure File Share (SMB) mounts, git fetch must use an explicit refspec (`git fetch origin +refs/heads/main:refs/remotes/origin/main`) because wildcard fetches fail silently on SMB. This constraint is documented in CLAUDE.md and is the primary technical reason Azure Container Apps and App Service were rejected as daemon hosts — both mandate Azure Files for persistent storage, making any code path that performs a wildcard git fetch unreliable.

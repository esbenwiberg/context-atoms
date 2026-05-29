---
kind: rationale
claim: The Azure daemon deployment uses a Standard_B1s Burstable VM with a managed
  disk rather than Container Apps, App Service, or ACI because SMB-backed Azure Files
  storage is hostile to git operations and SQLite WAL mode, and those platforms also
  lack Docker socket access.
anchors:
- infra/main.bicep
- infra/modules/container-apps.bicep
- infra/parameters/dev.bicepparam
- infra/parameters/prod.bicepparam
tags:
- azure
- infra
- sqlite
- docker
- git
source: doc-import:docs/decisions/ADR-004-distributed-runners-azure-vm-not-container-apps.md
status: active
---
The Azure daemon deployment uses a Standard_B1s Burstable VM with a managed disk rather than Container Apps, App Service, or ACI because SMB-backed Azure Files storage is hostile to git operations and SQLite WAL mode, and those platforms also lack Docker socket access. Container Apps and App Service both rely on Azure Files (SMB) for persistent state; bare repo caches require many git operations, and SMB mounts cause silent failures and contention. ACI has the same storage problem and costs ~$30+/mo for 24/7 use. The B1s VM at ~$8–15/mo runs git and SQLite on local SSD with no SMB indirection, supports native Docker socket for the local-docker executor, and uses the same Docker image as the Pi deployment for symmetric deploys. Azure Backup on the managed disk provides daily snapshots. The tradeoff is that it is not fully managed: the user must apply OS patches, manage TLS certs, and rotate the Tailscale credential.

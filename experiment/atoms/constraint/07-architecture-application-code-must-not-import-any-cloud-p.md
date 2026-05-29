---
kind: constraint
claim: Application code must not import any cloud-provider hosting SDK so the same
  Docker image runs on Azure Container Apps, on-prem Docker, and any k8s cluster.
anchors:
- src/pr_guardian/
tags:
- hosting
- portability
- docker
source: doc-import:docs/plan/07-architecture.md
status: active
---
Application code must not import any cloud-provider hosting SDK so the same Docker image runs on Azure Container Apps, on-prem Docker, and any k8s cluster. All three deployment profiles (Cloud/Azure, Hybrid, On-prem) use the identical image; only env vars differ. Any Azure-specific SDK import (e.g. `azure-identity`, `azure-mgmt-*`) inside `src/pr_guardian/` would violate this invariant. Infra-level concerns (ACR push, Bicep templates) live exclusively under `infra/azure/`.

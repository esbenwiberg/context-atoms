---
kind: rationale
claim: PR Guardian runs as a hosted container service outside CI pipelines so it consumes
  zero pipeline agents and can maintain a persistent cross-repo feedback loop.
anchors:
- src/pr_guardian/main.py
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/api/webhooks.py
tags:
- architecture
- deployment
- ci-native
- feedback-loop
source: doc-import:docs/plan/pr-guardian-overview.md
status: active
---
PR Guardian runs as a hosted container service outside CI pipelines so it consumes zero pipeline agents and can maintain a persistent cross-repo feedback loop. Webhooks from Azure DevOps and GitHub drive reviews; the service is always warm and shares one image across cloud, hybrid, and on-prem deployments. The CI-native alternative was rejected because: each review would consume a pipeline agent slot, the process would be ephemeral (no persistent feedback store), and multi-platform support would require duplicating pipeline definitions per platform.

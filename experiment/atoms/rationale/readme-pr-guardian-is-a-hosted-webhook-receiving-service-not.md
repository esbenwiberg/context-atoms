---
kind: rationale
claim: PR Guardian is a hosted webhook-receiving service, not a CI step, so it runs
  independently of the repo's own pipeline.
anchors:
- src/pr_guardian/api/webhooks.py
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/main.py
tags:
- architecture
- webhook
- hosted-service
source: doc-import:README.md
status: active
---
PR Guardian is architected as a standalone hosted service that receives GitHub or Azure DevOps webhook events, not as a job embedded in the target repo's CI pipeline. This shapes every integration point: auth, network topology, secret management, and deployment all belong to the Guardian service rather than to the reviewed repos. The trade-off accepted is operational overhead of running a separate service in exchange for isolation and the ability to review any repo without modifying its CI config.

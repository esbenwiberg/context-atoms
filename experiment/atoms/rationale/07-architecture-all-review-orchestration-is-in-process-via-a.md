---
kind: rationale
claim: All review orchestration is in-process via asyncio; core/queue.py is a thin
  asyncio task manager rather than an external message queue.
anchors:
- src/pr_guardian/core/queue.py
- src/pr_guardian/core/orchestrator.py
tags:
- queue
- asyncio
- architecture
source: doc-import:docs/plan/07-architecture.md
status: active
---
All review orchestration is in-process via asyncio; core/queue.py is a thin asyncio task manager rather than an external message queue. The design avoids the operational overhead of Redis/RabbitMQ/SQS while still providing cancellation support for long-running reviews. Rejected alternative: external broker — adds infra to manage and complicates the hosting-agnostic constraint. The trade-off is that scale-out is limited to the concurrency of a single process, which is acceptable given the Azure Container App HTTP-scaling rules (maxReplicas: 5, concurrentRequests: 3).

---
kind: rationale
claim: PR Guardian deliberately uses an in-process asyncio queue for concurrency and
  dedup instead of an external message broker.
anchors:
- src/pr_guardian/core/queue.py
- src/pr_guardian/core/orchestrator.py
tags:
- architecture
- concurrency
- queue
source: doc-import:docs/plan/08-implementation.md
status: active
---
PR Guardian deliberately uses an in-process asyncio queue for concurrency and dedup instead of an external message broker. The entire review pipeline runs in one process with no external message queues and no pipeline artifacts on disk. In-process asyncio handles dedup (repo+pr_id+head_sha), stale-cancellation of in-flight reviews for the same PR, and worker concurrency. The database is the sole persistent record of everything. External brokers (e.g. Redis, Celery) were implicitly rejected to keep the deployment footprint minimal.

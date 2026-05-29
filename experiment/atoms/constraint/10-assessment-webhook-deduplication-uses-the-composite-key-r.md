---
kind: constraint
claim: Webhook deduplication uses the composite key (repo, pr_id, head_sha), and a
  new push to the same PR must cancel the in-flight review and restart from scratch.
anchors:
- src/pr_guardian/api/webhooks.py
- src/pr_guardian/core/queue.py
- src/pr_guardian/decision/dedup.py
tags:
- webhook
- dedup
- concurrency
- cancel-restart
source: doc-import:docs/plan/10-assessment.md
status: active
---
Webhook deduplication is keyed on (repo, pr_id, head_sha). When a new push arrives for a PR that already has a review in flight, the existing review must be cancelled and a full re-run started — not merged or patched. Partial results from the cancelled run must not influence the new review. This guarantees that every completed review reflects a single consistent commit state and prevents stale findings from bleeding across pushes.

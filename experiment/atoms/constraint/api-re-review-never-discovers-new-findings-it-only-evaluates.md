---
kind: constraint
claim: Re-review never discovers new findings; it only evaluates whether non-dismissed
  findings from the original review are still valid.
anchors:
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/api/review.py
tags:
- re-review
- findings
- pipeline
source: doc-import:docs/api.md
status: active
---
Re-review never discovers new findings; it only evaluates whether non-dismissed findings from the original review are still valid. The re-review flow is: (1) fetch the incremental diff since the last reviewed commit, (2) collect non-dismissed findings from the original review, (3) ask each agent whether those findings are still valid. Each finding is marked `kept`, `resolved`, or `updated`. No new findings are emitted. This is by design to prevent hallucination and to keep re-review cheaper and faster than a full pipeline run.

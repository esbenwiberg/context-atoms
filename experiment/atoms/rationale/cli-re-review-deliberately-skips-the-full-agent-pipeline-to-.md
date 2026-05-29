---
kind: rationale
claim: '`re-review` deliberately skips the full agent pipeline to be cheaper/faster
  and to prevent agents from hallucinating new findings.'
anchors:
- src/pr_guardian/cli.py
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/core/repo_review.py
tags:
- re-review
- cost
- hallucination
- agent-pipeline
source: doc-import:docs/cli.md
status: active
---
`re-review` deliberately skips the full agent pipeline to be cheaper/faster and to prevent agents from hallucinating new findings. Instead of re-running full analysis, it: (1) fetches only the incremental diff since the last reviewed commit, (2) collects non-dismissed findings from the original review, and (3) asks each agent only whether those specific findings are still valid. Each finding is then marked `kept`, `resolved`, or `updated`. When no new commits exist since the last review, agents re-evaluate findings purely on their own merits — intended as a false-positive catch pass. The constraint is: re-review MUST NOT surface net-new findings; its output domain is strictly the set of existing non-dismissed findings from the original review.

---
kind: rationale
claim: The human review interface groups diffs into chapters by file concern rather
  than by AI agent because the human's job is to verify and judge automation output,
  not re-discover bugs.
anchors:
- src/pr_guardian/dashboard/human_review.html
- src/pr_guardian/dashboard/human_wizard.html
- REVIEW_INTERFACE_DESIGN.md
tags:
- human-review
- ux
- ai-pipeline
source: doc-import:docs/human-review-design.md
status: active
---
The human review interface groups diffs into chapters by file concern rather than by AI agent because the human's job is to verify and judge automation output, not re-discover bugs. By the time a human reviewer sees a PR, SAST and 6 AI agents have already run. Grouping findings by agent (as review_detail.html does) reflects the pipeline structure, not the reviewer's mental model. The chapter view reflects files and code — what a human actually thinks about. The original four concepts (A–D) all presented files and let the reviewer decide where to go; for 50+ file PRs this is the wrong model because it forces the reviewer to manage their own attention budget instead of the interface doing it.

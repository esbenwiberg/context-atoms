---
kind: constraint
claim: Work must be committed and pushed incrementally rather than batched at the
  end of a task.
anchors:
- CLAUDE.md
tags:
- git
- workflow
source: doc-import:CLAUDE.md#pr-workflow
status: active
---
Work must be committed and pushed incrementally rather than batched at the end of a task. This ensures in-progress state is recoverable if a pod or agent dies mid-task, and keeps individual commits reviewable. Do not accumulate all changes into a single end-of-task commit.

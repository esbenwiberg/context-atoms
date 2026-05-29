---
kind: rationale
claim: A separate AI reviewer evaluates screenshots and build/test output independently
  because agent self-reports of task completion are not trusted.
anchors:
- packages/daemon/src/providers/memory-reviewer.ts
- packages/daemon/src/pods/quality-score.ts
- packages/daemon/src/pods/quality-score-recorder.ts
- packages/daemon/src/pods/quality-signals.ts
- packages/daemon/src/db/migrations/058_reviewer_model.sql
tags:
- reviewer
- quality
- trust-model
- design-philosophy
source: doc-import:README.md#why-autopod
status: active
---
A separate AI reviewer evaluates screenshots and build/test output independently because agent self-reports of task completion are not trusted. When the coding agent declares it is done, autopod builds the project, runs the test suite, launches the app, takes real browser screenshots, and passes those artefacts to a distinct reviewer model that asks whether the result looks correct. This reviewer is intentionally decoupled from the coding agent to avoid self-serving confirmation bias. The quality score pipeline, reviewer model configuration (migration 058), and screenshot infrastructure all exist to serve this verification step — not as optional observability, but as the primary gate before structured feedback or approval is issued.

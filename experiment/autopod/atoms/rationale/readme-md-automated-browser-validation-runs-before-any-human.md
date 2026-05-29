---
kind: rationale
claim: Automated browser validation runs before any human notification is sent so
  that reviewers only receive results that have already passed quality checks, not
  raw agent output.
anchors:
- packages/daemon/src/pods/preview-supervisor.ts
- packages/daemon/src/pods/quality-score.ts
- packages/daemon/src/pods/quality-score-recorder.ts
- packages/daemon/src/notifications/notification-service.ts
tags:
- validation
- browser-qa
- human-in-the-loop
- quality
source: doc-import:README.md
status: active
---
Automated browser validation runs before any human notification is sent so that reviewers only receive results that have already passed quality checks, not raw agent output. The design principle is 'only bother you when there's something worth reviewing': the validation pipeline (screenshots, quality scores, browser QA) acts as a filter that absorbs low-quality outputs before they reach the human review queue. This is why quality scoring and the preview supervisor sit between agent completion and PR/notification emission rather than running in parallel with them. Rejected alternative: notifying on every agent completion would flood reviewers and defeat the purpose of autonomous operation.

---
kind: rationale
claim: "The composite quality score (0\u2013100) is derived from four signals: read:edit\
  \ ratio, blind edits, validation pass, and fix attempt count."
anchors:
- packages/daemon/src/pods/quality-score.ts
- packages/daemon/src/pods/quality-signals.ts
- packages/daemon/src/pods/quality-score-recorder.ts
- packages/daemon/src/pods/quality-score-repository.ts
tags:
- quality
- scoring
- signals
source: doc-import:ARCHITECTURE.md#analytics
status: active
---
The composite quality score (0–100) is derived from four signals: read:edit ratio, blind edits, validation pass, and fix attempt count.

These four were chosen because they are directly observable from pod execution without human review: read:edit ratio proxies whether the agent understood the codebase before changing it; blind edits flags writes to files never read; validation pass captures whether the automated gate accepted the output; fix attempt count measures how much rework was needed. Together they approximate implementation quality without requiring a reviewer.

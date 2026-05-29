---
kind: constraint
claim: "The validation pipeline must execute phases in strict order: lint \u2192 SAST\
  \ \u2192 build \u2192 test \u2192 health \u2192 pages \u2192 AC \u2192 facts \u2192\
  \ review."
anchors:
- packages/daemon/src/pods/pod-manager.ts
tags:
- validation
- ordering
- pipeline
source: doc-import:ARCHITECTURE.md#orchestration-loop
status: active
---
The validation pipeline must execute phases in strict order: lint → SAST → build → test → health → pages → AC → facts → review. Earlier phases (lint, SAST) are cheap and catch surface errors fast; later phases (AC, facts, review) depend on a successfully built and tested artifact. Reordering would waste compute running expensive checks against code that wouldn't compile, and would produce misleading review feedback.

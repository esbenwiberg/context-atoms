---
kind: constraint
claim: "The multi-phase validation pipeline must execute phases in the fixed order:\
  \ Lint \u2192 SAST \u2192 Build \u2192 Test \u2192 Health \u2192 Smoke \u2192 AC\
  \ \u2192 Facts \u2192 AI review, so cheaper/faster checks fail fast before expensive\
  \ ones run."
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/validation-repository.ts
tags:
- validation
- phase-order
- fail-fast
source: doc-import:README.md#features
status: active
---
The multi-phase validation pipeline must execute phases in the fixed order: Lint → SAST → Build → Test → Health → Smoke → AC → Facts → AI review, so cheaper/faster checks fail fast before expensive ones run. The ordering is intentional: static analysis (lint, SAST) runs before compilation (build) which runs before execution (test, health, smoke) which runs before AI-based review. Reordering phases — e.g. running the AI review step early to get faster feedback — would waste LLM tokens on code that hasn't even compiled. The state machine must treat this sequence as invariant.

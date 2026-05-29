---
kind: rationale
claim: "Validation uses two independent loops \u2014 an inner agent self-validation\
  \ loop and an outer independent-reviewer loop \u2014 so issues are caught before\
  \ an unrelated model grades the work."
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/validation-repository.ts
tags:
- validation
- architecture
- review
source: doc-import:README.md#how-it-works
status: active
---
Validation uses two independent loops — an inner agent self-validation loop and an outer independent-reviewer loop — so issues are caught before an unrelated model grades the work.

Inner loop: while the agent is still developing, it can invoke `validate_in_browser` via MCP to open a real browser inside its own container and verify acceptance criteria. This surfaces problems (broken pages, failing assertions) before the outer loop runs.

Outer loop: after the agent finishes, an independent reviewer model receives the diff, original task, contract, and findings from all prior attempts, and produces a pass/fail decision. The nine-phase sequence is: Lint → SAST → Build → Test → Health check → Smoke pages → AC validation → Required facts → AI task review. Each phase must pass before the next runs.

The two-loop separation is intentional: self-validation gives fast feedback to the agent; independent review prevents the agent from gaming its own grade.

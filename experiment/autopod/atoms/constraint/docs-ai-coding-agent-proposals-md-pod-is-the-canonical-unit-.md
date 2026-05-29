---
kind: constraint
claim: '"Pod" is the canonical unit of orchestration; any reference to "session",
  `processSession()`, or `packages/daemon/src/sessions/*` in documentation is legacy
  and should be read as referring to the current pod model and `processPod()` entry
  point.'
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/reconciler.ts
tags:
- naming
- pod
- orchestration
- legacy
- terminology
source: doc-import:docs/ai-coding-agent-proposals.md
status: active
---
"Pod" is the canonical unit of orchestration; any reference to "session", `processSession()`, or `packages/daemon/src/sessions/*` in documentation is legacy and should be read as referring to the current pod model and `processPod()` entry point.

The codebase underwent a pod-first rename: the top-level orchestration entry point is now `processPod()` (not `processSession()`), and all pod lifecycle, state machine, and reconciliation logic lives under `packages/daemon/src/pods/`. There is no `packages/daemon/src/sessions/` directory in the current tree. When reading older design docs or proposals that use session terminology, mentally substitute "pod" for "session" throughout.

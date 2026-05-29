---
kind: constraint
claim: Deterministic check steps (lint, build, test, typecheck) in a blueprint must
  be executed by the harness/walker directly, never delegated to the agent runtime,
  so the agent cannot skip or ignore failures.
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- blueprint
- deterministic
- harness
- invariant
- safety
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-2-blueprint-workflow-system-subsumes-tiered-validat
status: active
---
Deterministic check steps (lint, build, test, typecheck) in a blueprint must be executed by the harness/walker directly, never delegated to the agent runtime, so the agent cannot skip or ignore failures. This is the core reliability guarantee of the blueprint design: the harness enforces the step sequence and the agent has no mechanism to bypass a check gate. The `check` step type fans out to every declared stack using each stack's configured `cwd` and `commands.<check>`, and the `deterministic` step type runs `execInContainer(command)` directly. Agentic steps that follow a failed check only run when `condition: previous_failed` is set, keeping the agent's scope bounded to reacting to harness-reported failures.

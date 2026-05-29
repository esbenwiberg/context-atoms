---
kind: constraint
claim: "Autopod validation must proceed in a fixed phase order \u2014 build, health\
  \ check, smoke test, AI review \u2014 and each phase must pass before the next starts."
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/db/migrations/086_profile_skip_validation_phases.sql
tags:
- validation
- phases
- ordering
- autopod
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#3-validation-feedback-loops
status: active
---
Autopod validation must proceed in a fixed phase order — build, health check, smoke test, AI review — and each phase must pass before the next starts. This gate structure ensures cheap failures (build errors) are caught before expensive ones (AI review tokens). Profiles may skip specific phases via profile_skip_validation_phases, but the ordering of remaining phases is invariant. Adding a new validation phase requires inserting it at the correct position in the state machine, not appending it arbitrarily.

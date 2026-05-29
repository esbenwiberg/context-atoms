---
kind: rationale
claim: Blueprint steps are typed as either 'deterministic' (daemon executes a shell
  command directly in the container, bypassing the agent) or 'agentic' (agent gets
  control with a scoped prompt) because mixing the two responsibilities inside a single
  agentic phase was the root cause of unreliable validation.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/profiles/profile-store.ts
tags:
- blueprints
- step-types
- architecture
- deterministic
- agentic
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#4-blueprints-execplans-structured-task-decomposition
status: active
---
Blueprint steps are typed as either 'deterministic' (daemon executes a shell command directly in the container, bypassing the agent) or 'agentic' (agent gets control with a scoped prompt) because mixing the two responsibilities inside a single agentic phase was the root cause of unreliable validation. Deterministic steps capture stdout/stderr and feed failures automatically to the next agentic step as a correction; they are never left to agent discretion. Agentic steps run until the agent signals completion or hits a timeout. The conditional 'previous_failed' mechanism on agentic steps allows fix loops without always spawning them. This design was directly informed by Stripe's blueprint pattern of wiring deterministic nodes with agentic nodes rather than delegating all orchestration to the AI.

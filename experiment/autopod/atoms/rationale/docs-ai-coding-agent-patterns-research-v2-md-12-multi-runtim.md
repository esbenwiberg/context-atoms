---
kind: rationale
claim: The `Runtime` interface abstraction exists so that infrastructure investment
  pays dividends regardless of which LLM is in use, deliberately making the model
  less important than the surrounding harness.
anchors:
- packages/daemon/src/interfaces/runtime-registry.ts
- packages/daemon/src/runtimes/claude-runtime.ts
- packages/daemon/src/runtimes/codex-runtime.ts
- packages/daemon/src/runtimes/copilot-runtime.ts
- packages/daemon/src/runtimes/runtime-registry.ts
tags:
- architecture
- multi-runtime
- model-agnostic
- abstraction
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#12-multi-runtime-model-agnostic-architecture
status: active
---
The Runtime interface abstraction exists so that infrastructure investment pays dividends regardless of which LLM is in use, deliberately making the model less important than the surrounding harness. The design philosophy is: 'The model does not run the system; the system runs the model.' This means Claude, Codex, and Copilot are all interchangeable at the runtime layer — the harness (scheduling, validation, state machine, security scanning, etc.) operates independently of which model executes inside. Rejected alternative: tight coupling to a single provider would make every model upgrade or switch a cross-cutting infrastructure change.

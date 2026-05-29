---
kind: rationale
claim: Blueprint `check` steps fan out across all declared stacks in parallel without
  short-circuiting so the agent sees the complete failure surface in a single round-trip
  rather than discovering per-stack failures iteratively.
anchors:
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/profiles/profile-validator.ts
- packages/daemon/src/profiles/inheritance.ts
tags:
- blueprint
- fanout
- parallel
- check
- design-decision
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-2-blueprint-workflow-system-subsumes-tiered-validat
status: active
---
Blueprint `check` steps fan out across all declared stacks in parallel without short-circuiting so the agent sees the complete failure surface in a single round-trip rather than discovering per-stack failures iteratively. Without this, an agent fixes node lint, re-runs, then discovers dotnet lint also fails — paying the full round-trip cost once per stack. Parallel fanout collapses N sequential agent-fix-recheck loops into one. Failures are reported per-stack so error messages remain attributable (e.g., `dotnet lint failed at src/Api/Foo.cs:42`). Changed-files gating (v1) further constrains this: if no files under a stack's `cwd` changed relative to the session base branch, that stack is skipped entirely to avoid pure latency on unaffected stacks.

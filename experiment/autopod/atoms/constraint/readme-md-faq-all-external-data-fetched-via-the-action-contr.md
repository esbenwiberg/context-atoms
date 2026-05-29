---
kind: constraint
claim: All external data fetched via the action control plane (GitHub issues/PRs,
  ADO work items, Azure logs) must be PII-stripped and scanned for prompt injection
  before it reaches an agent.
anchors:
- packages/daemon/src/actions/
- packages/daemon/src/security/detectors/injection-detector.ts
- packages/daemon/src/security/detectors/pii-detector.ts
tags:
- security
- actions
- pii
- prompt-injection
source: doc-import:README.md#faq
status: active
---
All external data fetched via the action control plane must be PII-stripped and scanned for prompt injection before it reaches an agent. This applies to every action handler that retrieves content from third-party systems (GitHub issues/PRs, Azure DevOps work items, Azure application logs). The security pipeline must run on action responses before they are forwarded to the agent runtime — bypassing or short-circuiting these checks for any action handler breaks this invariant.

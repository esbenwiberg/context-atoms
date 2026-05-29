---
kind: constraint
claim: All external data ingested via the action control plane (GitHub issues, ADO
  work items, app logs) must pass through PII stripping and prompt-injection quarantine
  before being exposed to agent containers.
anchors:
- packages/daemon/src/actions/
- packages/daemon/src/security/detectors/pii-detector.ts
- packages/daemon/src/security/detectors/injection-detector.ts
- packages/daemon/src/actions/policy-resolver.ts
tags:
- security
- pii
- prompt-injection
- actions
source: doc-import:README.md#features
status: active
---
All external data ingested via the action control plane must pass through PII stripping and prompt-injection quarantine before being exposed to agent containers. This applies to every action source — GitHub issues, ADO work items, Azure logs — regardless of how trusted the source appears. The two detectors (PII and injection) are not optional filters; they are mandatory gates in the action pipeline. Bypassing them to speed up data delivery is not acceptable, as the threat model assumes untrusted content can appear in any external system the agent reads from.

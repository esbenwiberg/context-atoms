---
kind: constraint
claim: Inbound webhook trigger endpoints must verify payload authenticity with HMAC
  signatures before spawning any session.
anchors:
- packages/daemon/src/api/routes/scheduled-jobs.ts
- packages/daemon/src/api/ssrf-guard.ts
tags:
- webhooks
- security
- hmac
- triggers
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-6-scheduled-event-triggered-sessions
status: active
---
Inbound webhook trigger endpoints must verify payload authenticity with HMAC signatures before spawning any session. The proposal specifies the `/api/triggers/webhook/:triggerId` endpoint 'accepts inbound POSTs (with HMAC-verified signatures)' before matching against trigger definitions. This is a security invariant: unauthenticated webhook calls must be rejected prior to any prompt-template interpolation or session creation, preventing arbitrary actors from spawning pods by hitting a publicly reachable endpoint.

---
kind: rationale
claim: Container-level isolation (seccomp, network bounds, HAProxy) is the primary
  reliability layer because agents will drift from instructions over time and only
  constraints they cannot bypass are durable.
anchors:
- packages/daemon/src/containers/seccomp-profile.json
- packages/daemon/src/containers/docker-bounds.ts
- packages/daemon/src/containers/haproxy-config.ts
- packages/daemon/src/containers/haproxy-deny-stream.ts
- packages/daemon/src/containers/docker-network-manager.ts
tags:
- security
- containment
- agent-reliability
- network-policy
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#15-key-quotes-worth-remembering
status: active
---
Container-level isolation (seccomp, network bounds, HAProxy) is the primary reliability layer because agents will drift from instructions over time and only constraints they cannot bypass are durable. seccomp-profile.json restricts syscalls at kernel level; docker-bounds.ts enforces resource limits; haproxy-config.ts and haproxy-deny-stream.ts gate egress traffic. These controls are the "walls" that compound into system-wide reliability — an agent cannot circumvent a network deny rule it cannot see. Runtime-enforced containment is chosen over prompt-level policy because prompt compliance degrades across long-running, stateful agent sessions.

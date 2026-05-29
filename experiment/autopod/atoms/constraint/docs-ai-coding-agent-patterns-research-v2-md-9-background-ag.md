---
kind: constraint
claim: "Every pod must receive its own ephemeral token with per-project RBAC and be\
  \ network-isolated from all other running pods \u2014 sharing credentials or collapsing\
  \ network boundaries across pods violates the core isolation invariant."
anchors:
- packages/daemon/src/crypto/pod-tokens.ts
- packages/daemon/src/crypto/credentials-cipher.ts
- packages/daemon/src/containers/docker-network-manager.ts
tags:
- security
- isolation
- tokens
- network-policy
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#9-background-agent-infrastructure-patterns-ona-ramp
status: active
---
Every pod must receive its own ephemeral token with per-project RBAC and be network-isolated from all other running pods — sharing credentials or collapsing network boundaries across pods violates the core isolation invariant. This maps directly to the industry-identified 'Isolation and security' layer: ephemeral tokens per environment, RBAC per project, and network isolation between sessions are listed as non-negotiable for production agent infrastructure. The encrypted credentials store and per-pod token generation exist to enforce this; any change that reuses tokens across pods or flattens the network policy between concurrent pods breaks this guarantee.

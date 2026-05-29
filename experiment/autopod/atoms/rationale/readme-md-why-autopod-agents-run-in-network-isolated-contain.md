---
kind: rationale
claim: Agents run in network-isolated containers with firewall rules because they
  are treated as untrusted by default, not as cooperative tools.
anchors:
- packages/daemon/src/containers/docker-network-manager.ts
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/db/migrations/004_network_policy.sql
- packages/daemon/src/containers/haproxy-config.ts
tags:
- security
- containers
- network-policy
- design-philosophy
source: doc-import:README.md#why-autopod
status: active
---
Agents run in network-isolated containers with firewall rules because they are treated as untrusted by default, not as cooperative tools. The design premise is adversarial: the agent cannot be assumed to stay in scope, avoid side-effects, or report honestly. Network isolation, seccomp profiles, and HAProxy-enforced egress rules exist to contain blast radius, not merely to sandbox for reproducibility. Alternative approaches (trusting agent output, running in the host environment) were implicitly rejected in favour of this locked-down model. Any relaxation of network policy must be explicit and audited — the default is deny, not allow.

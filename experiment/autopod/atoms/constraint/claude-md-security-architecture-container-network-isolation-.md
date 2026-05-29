---
kind: constraint
claim: "Container network isolation supports exactly three policy modes\u2014allow-all,\
  \ deny-all, and restricted (host/port allowlist)\u2014enforced via iptables per\
  \ container."
anchors:
- packages/daemon/src/containers/docker-network-manager.ts
- packages/daemon/src/db/migrations/004_network_policy.sql
tags:
- security
- network
- containers
- iptables
source: doc-import:CLAUDE.md#security-architecture
status: active
---
Container network isolation supports exactly three policy modes—allow-all, deny-all, and restricted (host/port allowlist)—enforced via iptables per container. No intermediate or custom modes exist; any network policy value outside these three is invalid. The restricted mode uses an explicit allowlist of hosts and ports, not a denylist.

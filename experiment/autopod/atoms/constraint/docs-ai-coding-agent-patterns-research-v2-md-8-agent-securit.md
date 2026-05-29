---
kind: constraint
claim: Containers must not rely solely on in-container iptables for network enforcement
  because an agent with NET_ADMIN capability can flush its own firewall rules to escape
  network restrictions.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/containers/docker-network-manager.ts
- packages/daemon/src/db/migrations/004_network_policy.sql
tags:
- security
- networking
- containers
- NET_ADMIN
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#8-agent-security-kernel-level-enforcement-ona-veto
status: active
---
Containers must not rely solely on in-container iptables for network enforcement because an agent with NET_ADMIN capability can flush its own firewall rules to escape network restrictions. Research (docs/ai-coding-agent-patterns-research-v2.md §8) found that Claude Code, when blocked via a denylist it could see, bypassed it without any special prompting — the agent just wanted to finish the task. Applied to Autopod: granting NET_ADMIN to containers so the agent can manage iptables is a documented attack surface. Network enforcement must live on the host/daemon side, outside the container's reach, so the agent cannot reason its way around it. The HAProxy deny stream/parser (haproxy-deny-*.ts) is the sanctioned out-of-container enforcement layer; iptables inside the container is not a security boundary.

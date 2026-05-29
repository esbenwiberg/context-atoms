---
kind: rationale
claim: NET_ADMIN is granted to session containers only for firewall setup and must
  be dropped from the capability bounding set immediately afterwards because retaining
  it exposes egress restrictions to in-container root escalation paths (passwordless
  sudo, setuid binaries, container-escape CVEs).
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/containers/docker-network-manager.ts
tags:
- security
- containers
- linux-capabilities
- network-policy
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-7-drop-net-admin-after-firewall-setup
status: active
---
NET_ADMIN is granted to session containers only for firewall setup and must be dropped from the capability bounding set immediately afterwards because retaining it exposes egress restrictions to in-container root escalation paths (passwordless sudo, setuid binaries, container-escape CVEs). docker-container-manager.ts grants CapAdd: ['NET_ADMIN'] and docker-network-manager.ts generates and executes the firewall script as root inside the container via refreshFirewall(). The capability stays live for the entire session lifetime, meaning any path to in-container root (sudo on autopod user, exploitable setuid binary, or a container-escape CVE) also yields the ability to flush iptables egress rules with iptables -F OUTPUT. Running the agent as non-root (autopod:1000) is insufficient defence because it only prevents direct exploitation — it does not close the root-escalation paths. Dropping from the bounding set after the firewall script finishes removes the capability kernel-side regardless of UID for every future process in the container.

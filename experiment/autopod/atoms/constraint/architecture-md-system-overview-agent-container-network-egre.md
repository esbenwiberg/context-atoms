---
kind: constraint
claim: Agent container network egress must flow through HAProxy (SNI proxy) and iptables;
  containers must not bypass this firewall.
anchors:
- packages/daemon/src/containers/haproxy-config.ts
- packages/daemon/src/containers/haproxy-deny-stream.ts
- packages/daemon/src/containers/docker-network-manager.ts
tags:
- security
- network
- egress
- haproxy
- iptables
source: doc-import:ARCHITECTURE.md#system-overview
status: active
---
Agent container network egress must flow through HAProxy (SNI proxy) and iptables; containers must not bypass this firewall. HAProxy operates as an SNI-level proxy (not full TLS termination) so the daemon can apply allowlist/denylist policy per destination hostname without decrypting traffic. iptables rules enforce that no TCP connection can leave the container without transiting HAProxy. Any change that grants containers direct internet access removes the egress control guarantee.

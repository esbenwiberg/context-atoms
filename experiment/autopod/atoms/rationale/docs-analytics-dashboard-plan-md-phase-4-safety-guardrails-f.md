---
kind: rationale
claim: "Firewall block logging via iptables LOG\u2192counters was deferred because\
  \ REJECT mode produces no observable signal and the infrastructure lift has no confirmed\
  \ user need."
anchors:
- packages/daemon/src/containers/docker-network-manager.ts
- packages/daemon/src/db/migrations/094_pods_network_policy_resolved.sql
tags:
- network-policy
- security
- deferred
source: doc-import:docs/analytics-dashboard-plan.md#phase-4-safety-guardrails
status: active
---
Firewall block logging via iptables LOG→counters was deferred because REJECT mode produces no observable signal and the infrastructure lift has no confirmed user need. The network policy distribution widget (% pods on allow-all / restricted / deny-all) covers the operator-grade visibility needed for now. Do not add iptables LOG plumbing or a counters table until a concrete user need is articulated — the cost/signal ratio is currently negative.

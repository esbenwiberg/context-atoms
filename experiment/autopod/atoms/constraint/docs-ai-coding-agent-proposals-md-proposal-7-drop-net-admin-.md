---
kind: constraint
claim: After all iptables rules are written, the firewall script must drop cap_net_admin
  from the Linux capability bounding set (via capsh --drop or prctl PR_CAPBSET_DROP),
  making it irreversible for all descendant processes regardless of UID.
anchors:
- packages/daemon/src/containers/docker-network-manager.ts
tags:
- security
- containers
- linux-capabilities
- firewall
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-7-drop-net-admin-after-firewall-setup
status: active
---
After all iptables rules are written, the firewall script must drop cap_net_admin from the Linux capability bounding set (via capsh --drop or prctl PR_CAPBSET_DROP), making it irreversible for all descendant processes regardless of UID. The bounding set drop must be the final step in every generated firewall script across all three modes (allow-all, deny-all, restricted). The drop line should be: `capsh --drop=cap_net_admin -- -c "exit 0" 2>/dev/null || true` — the || true guard makes it a silent no-op on images lacking capsh rather than a blocking failure, but base images should be audited to ensure capsh (libcap) or setpriv is present. This constraint is distinct from simply running the agent as non-root: non-root relies on the agent being unable to reach root, whereas the bounding set drop removes the capability at the kernel level regardless of what UID any process achieves.

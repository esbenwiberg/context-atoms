---
kind: rationale
claim: New pods start with restrictive network policies and are intended to earn expanded
  access over successful runs, because static wide-open policies give agents an attack
  surface from the first request.
anchors:
- packages/daemon/src/pods/runtime-network-defaults.ts
- packages/daemon/src/db/migrations/094_pods_network_policy_resolved.sql
- packages/daemon/src/pods/pod-repository.ts
tags:
- security
- networking
- trust
- network-policy
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#8-agent-security-kernel-level-enforcement-ona-veto
status: active
---
New pods start with restrictive network policies and are intended to earn expanded access over successful runs, because static wide-open policies give agents an attack surface from the first request. This follows the dynamic trust boundary model from §8: hard outer boundary (absolute limits set by the user/profile) plus a dynamic inner boundary that widens as the agent demonstrates trustworthy behavior and contracts on errors. The resolved network policy column (migration 094) captures the effective policy after profile inheritance is applied, which is the value that should be enforced — not a default permissive fallback. This design was motivated by the finding that authorised agents doing legitimate work can still cause unintended harm if given broad access upfront.

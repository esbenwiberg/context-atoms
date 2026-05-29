---
kind: constraint
claim: The resolved network policy must be snapshotted onto the pods row at launch
  time, not re-derived at query time, so analytics and audit always reflect the policy
  that was actually in effect.
anchors:
- packages/daemon/src/db/migrations/094_pods_network_policy_resolved.sql
- packages/daemon/src/pods/runtime-network-defaults.ts
- packages/daemon/src/pods/runtime-network-defaults.test.ts
tags:
- network-policy
- pods
- analytics
- audit
source: doc-import:docs/analytics-dashboard-plan.md#status
status: active
---
The resolved network policy must be snapshotted onto the pods row at launch time, not re-derived at query time, so analytics and audit always reflect the policy that was actually in effect. ADR-020 chose snapshot over live join because profile defaults, workspace overrides, and runtime-specific rules are collapsed through a resolver at pod start; storing the resolved form means the analytics dashboard and the audit trail are both reading the same immutable record. Any code that changes how network policy is resolved at runtime must also update the snapshot written to pods.network_policy_resolved.

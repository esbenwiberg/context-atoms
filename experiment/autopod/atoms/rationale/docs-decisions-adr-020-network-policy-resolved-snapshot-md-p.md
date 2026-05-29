---
kind: rationale
claim: pods.network_policy_resolved exists as a one-shot snapshot of the post-inheritance
  effective network policy written at provisioning because live profile joins produce
  historically drifting aggregates when profiles are edited after the fact.
anchors:
- packages/daemon/src/db/migrations/094_pods_network_policy_resolved.sql
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/profiles/inheritance.ts
tags:
- network-policy
- snapshot
- analytics
- historical-fidelity
source: doc-import:docs/decisions/ADR-020-network-policy-resolved-snapshot.md
status: active
---
pods.network_policy_resolved exists as a one-shot snapshot of the post-inheritance effective network policy written at provisioning because live profile joins produce historically drifting aggregates when profiles are edited after the fact.

Profiles are mutable: a profile's network_policy can change at any time. Aggregating historical pods via `pods.profile_id JOIN profiles` would attribute old pods to the *current* profile state, not the state when they ran. Additionally, a derived profile inherits network_policy via the extends chain (profiles/inheritance.ts), so the aggregator would have to re-resolve inheritance per row — against the current base profile, compounding drift.

Three options were considered: (A) aggregate over the live profile chain — cheap but drifts; (B) snapshot on the pods row at provisioning — chosen; (C) a separate pod_provisioning_log table — pure overhead for one field.

Option B matches the existing pattern for runtime, output_mode, and other profile-derived fields that are snapshotted on the pod row for historical fidelity. The Safety drill aggregator can then do a single-table read on pods with no JOIN or inheritance resolution.

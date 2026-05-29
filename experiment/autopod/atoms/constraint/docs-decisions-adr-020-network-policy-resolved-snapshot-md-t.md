---
kind: constraint
claim: The literal strings 'allow-all', 'restricted', and 'deny-all' stored in pods.network_policy_resolved
  must stay byte-for-byte identical to the values used in docker-network-manager.ts;
  renaming any value requires a coordinated data migration.
anchors:
- packages/daemon/src/containers/docker-network-manager.ts
- packages/daemon/src/db/migrations/094_pods_network_policy_resolved.sql
tags:
- network-policy
- string-contract
- safety-drill
- migration
source: doc-import:docs/decisions/ADR-020-network-policy-resolved-snapshot.md
status: active
---
The literal strings 'allow-all', 'restricted', and 'deny-all' stored in pods.network_policy_resolved must stay byte-for-byte identical to the values used in docker-network-manager.ts; renaming any value requires a coordinated data migration.

The Safety drill aggregator buckets historical pods by these exact strings. Any mismatch between the stored values and the strings docker-network-manager.ts uses causes bucket drift — pods would fall into a new bucket while existing stored rows stay in the old one, silently splitting what should be one cohort across two names.

Pre-migration pods (those with network_policy_resolved = NULL) are bucketed as 'unknown' by the aggregator. This is intentional and expected to dominate the distribution for the first ~30 days post-migration.

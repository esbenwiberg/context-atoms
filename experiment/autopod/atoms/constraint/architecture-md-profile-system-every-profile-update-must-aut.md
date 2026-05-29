---
kind: constraint
claim: Every profile update must auto-increment `version`, and when a pod is created
  the full resolved profile (with inherited values) is snapshotted into the pod record
  so any pod's config is permanently auditable.
anchors:
- packages/daemon/src/profiles/profile-store.ts
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/db/migrations/034_profile_version.sql
- packages/daemon/src/db/migrations/051_inheritable_columns.sql
tags:
- profiles
- versioning
- auditability
- pods
source: doc-import:ARCHITECTURE.md#profile-system
status: active
---
Every profile update must auto-increment `version`, and when a pod is created the full resolved profile (with inherited values) is snapshotted into the pod record so any pod's config is permanently auditable.

This means: mutating a profile field without bumping `version` breaks the audit trail. The snapshot in the pod record is the source of truth for what config produced that pod's output — do not read the live profile to reconstruct historical pod behavior.

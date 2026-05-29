---
kind: constraint
claim: Every profile mutation must auto-increment the profile's version counter, and
  each pod must snapshot the exact profile version in use at creation time.
anchors:
- packages/daemon/src/profiles/profile-store.ts
- packages/daemon/src/db/migrations/034_profile_version.sql
- packages/daemon/src/pods/pod-repository.ts
tags:
- profiles
- versioning
- reproducibility
- pods
source: doc-import:README.md#features
status: active
---
Every profile mutation must auto-increment the profile's version counter, and each pod must snapshot the exact profile version in use at creation time. This invariant ensures that historical pods remain reproducible and auditable — given a pod ID you can reconstruct exactly what profile configuration the agent ran with, even after the live profile has been updated many times since. Code that updates profile fields without bumping the version, or that launches pods without recording the current version, breaks the auditability guarantee.

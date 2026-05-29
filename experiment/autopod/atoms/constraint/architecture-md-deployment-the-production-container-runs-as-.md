---
kind: constraint
claim: The production container runs as non-root user autopod with UID 1000, so any
  mounted volumes (including /data) must be writable by that UID.
anchors:
- Dockerfile
- infra/modules/container-apps.bicep
tags:
- deployment
- security
- non-root
- permissions
source: doc-import:ARCHITECTURE.md#deployment
status: active
---
The production container runs as non-root user autopod with UID 1000, so any mounted volumes (including /data) must be writable by that UID. This is a security hardening measure to reduce the blast radius of container escape vulnerabilities. Infrastructure provisioning and volume configuration must account for this ownership requirement; failing to do so causes the daemon to crash at startup when it cannot write the SQLite database.

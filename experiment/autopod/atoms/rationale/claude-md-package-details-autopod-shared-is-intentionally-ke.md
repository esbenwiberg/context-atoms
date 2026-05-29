---
kind: rationale
claim: '@autopod/shared is intentionally kept zero-dependency so it can serve as the
  type backbone imported by every other package without introducing transitive dependency
  conflicts.'
anchors:
- packages/daemon/src/interfaces/index.ts
tags:
- shared
- types
- dependency-management
source: doc-import:CLAUDE.md#package-details
status: active
---
@autopod/shared is intentionally kept zero-dependency so it can serve as the type backbone imported by every other package without introducing transitive dependency conflicts. All cross-package types (pod, profile, runtime, actions, escalation, validation, events, injection, auth, model-provider, analytics, memory, etc.) live in src/types/ with one file per concern. Key exports are src/errors.ts (typed error hierarchy), src/constants.ts (POD_ID_LENGTH, CONTAINER_USER, VALID_STATUS_TRANSITIONS), and src/sanitize/ (PII/injection detection). Adding a runtime dependency to this package would force every consumer to resolve it, breaking the zero-dep contract.

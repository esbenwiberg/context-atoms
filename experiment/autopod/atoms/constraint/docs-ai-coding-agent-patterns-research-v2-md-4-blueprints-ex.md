---
kind: constraint
claim: The default blueprint must replicate the existing processSession() behavior
  exactly so that profiles without an explicit blueprint continue to work without
  modification.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/profiles/profile-store.ts
tags:
- blueprints
- backward-compatibility
- profiles
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#4-blueprints-execplans-structured-task-decomposition
status: active
---
The default blueprint must replicate the existing processSession() behavior exactly so that profiles without an explicit blueprint continue to work without modification. Blueprints are optional at the profile level; omitting one must be equivalent to using a blueprint that matches today's hardcoded flow (provision → agent codes → validate → merge). This backward-compatibility invariant must be preserved through all phases of blueprint implementation. Profiles reference blueprints by name, and the default (unnamed) blueprint is implicitly the legacy single-agentic-step flow.

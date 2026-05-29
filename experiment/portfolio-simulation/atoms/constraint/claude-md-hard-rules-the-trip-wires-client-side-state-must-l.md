---
kind: constraint
claim: Client-side state must live in in-memory Zustand only; localStorage must never
  be used as a source of truth.
anchors:
- src/state/store.ts
tags:
- state
- localStorage
- zustand
- dataverse
- sharing
source: doc-import:CLAUDE.md#hard-rules-the-trip-wires
status: active
---
Client-side state must live in in-memory Zustand only; localStorage must never be used as a source of truth. The sharing model for this app is Dataverse RBAC — persisting state in browser storage would bypass that model and create a divergent, non-sharable source of truth. All durable state goes to Dataverse; Zustand is the ephemeral UI layer only.

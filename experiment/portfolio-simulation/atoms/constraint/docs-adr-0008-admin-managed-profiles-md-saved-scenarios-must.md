---
kind: constraint
claim: Saved scenarios must carry a `pum_profilekey` column so they are scoped to
  the profile they were created under, preventing cross-profile data leakage.
anchors:
- src/scenarios/scenarioTypes.ts
- src/adapters/xrm/scenarioStore.ts
- src/scenarios/serializeScenario.ts
tags:
- scenarios
- profiles
- isolation
source: doc-import:docs/adr/0008-admin-managed-profiles.md
status: active
---
Saved scenarios must carry a `pum_profilekey` column so they are scoped to the profile they were created under, preventing cross-profile data leakage.

A `pum_profilekey` column is added to the `pum_scenario` Dataverse table. Every scenario read or write operation must filter or tag by this key. Loading scenarios from a different profile key must not surface rows belonging to another profile.

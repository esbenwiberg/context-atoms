---
kind: constraint
claim: Scenario persistence is the only persistence layer and must be backed by Dataverse
  RBAC via src/scenarios/ and src/adapters/xrm/scenarioStore.ts; all other store slices
  (weights, filters, overrides, panel state) are ephemeral.
anchors:
- src/scenarios/
- src/adapters/xrm/scenarioStore.ts
- src/state/store.ts
tags:
- persistence
- scenarios
- dataverse
- rbac
source: doc-import:docs/adr/0003-in-memory-zustand-no-browser-persistence.md
status: active
---
Scenario persistence is the only persistence layer and must be backed by Dataverse RBAC via src/scenarios/ and src/adapters/xrm/scenarioStore.ts; all other store slices (weights, filters, overrides, panel state) are ephemeral.

The no-browser-storage rule held the line until Dataverse-backed serialization was ready, allowing it to ship onto a clean canvas with no interim format to migrate from. Ranking weights, sort, filters, shortlist, constraint mode, heatmap overrides, and panel collapsed state are all lost on reload — only explicitly saved scenarios survive.

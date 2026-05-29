---
kind: constraint
claim: The analytics drill-in right pane must maintain its own independent scene state,
  separate from the fleet detail panel state.
anchors:
- packages/daemon/src/pods/event-bus.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- analytics
- ui-state
- navigation
source: doc-import:docs/analytics-dashboard-plan.md#vision
status: active
---
The analytics drill-in right pane must maintain its own independent scene state, separate from the fleet detail panel state. When a user clicks a card in the analytics grid, the right pane opens a deep view (histograms, tables, drill-down) without disturbing the fleet detail panel that is used elsewhere in the shell. The two right-pane contexts must not share or overwrite each other's state — they represent different navigation hierarchies active simultaneously.

---
kind: constraint
claim: "Within a series spec folder, advisory scope (touches, does_not_touch, require_sidecars)\
  \ must live in brief.md, while the runnable contract (depends_on, scenarios, required\
  \ facts, human review items) must live in contract.yaml \u2014 these concerns must\
  \ not be mixed across files."
anchors:
- packages/daemon/src/db/migrations/047_pod_series.sql
- packages/daemon/src/db/migrations/069_series_design_and_brief_scope.sql
- packages/daemon/src/pods/pod-manager.ts
tags:
- series
- spec-structure
- brief
- contract
source: doc-import:ARCHITECTURE.md#series-workflows
status: active
---
Within a series spec folder, advisory scope (touches, does_not_touch, require_sidecars) must live in brief.md, while the runnable contract (depends_on, scenarios, required facts, human review items) must live in contract.yaml — these concerns must not be mixed across files. brief.md is the human-readable task description the pod agent reads; contract.yaml is the machine-executable artifact used by the daemon for dependency resolution and validation gating. Keeping them separate allows the daemon to parse and act on contract.yaml without needing to interpret free-form task prose, and lets the spec authoring tools (e.g. /plan-feature) generate and validate each file independently.

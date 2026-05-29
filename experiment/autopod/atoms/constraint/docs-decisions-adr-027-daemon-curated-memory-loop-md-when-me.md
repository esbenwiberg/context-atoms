---
kind: constraint
claim: 'When memories are selected and injected before a pod starts, usage reporting
  at the MCP tool boundary is required: `report_plan` must state intended use and
  `report_task_summary` must report `applied`, `not_applicable`, or `harmful_stale`
  with a reason; missing or invalid payloads are rejected so the agent can retry.'
anchors:
- packages/daemon/src/pods/system-instructions-generator.ts
- packages/daemon/src/pods/pod-bridge-impl.ts
- packages/daemon/src/pods/memory-extraction.ts
tags:
- memory
- mcp
- reporting
- contract
source: doc-import:docs/decisions/ADR-027-daemon-curated-memory-loop.md
status: active
---
When memories are selected and injected before a pod starts, usage reporting at the MCP tool boundary is required: `report_plan` must state intended use and `report_task_summary` must report `applied`, `not_applicable`, or `harmful_stale` with a reason; missing or invalid payloads are rejected so the agent can retry. Pod lifecycle remains fail-soft: if a pod ends without final reporting the daemon records `not_reported` evidence rather than failing the pod. The injected prompt section is `Relevant Memory` (≤5 entries with reviewer rationale); the old 100-entry `Available Memory` index is removed from the prompt.

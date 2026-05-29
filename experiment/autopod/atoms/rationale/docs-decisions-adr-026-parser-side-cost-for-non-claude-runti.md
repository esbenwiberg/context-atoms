---
kind: rationale
claim: "Parser-side `costUsd` emission for non-Claude runtimes was chosen over read-time-only\
  \ aggregation because live-UX consumers (CLI `ap pod watch`, desktop activity feed)\
  \ render `AgentCompleteEvent.costUsd` directly from the event stream \u2014 not\
  \ from the database \u2014 so Codex pods would show nothing at completion time without\
  \ it."
anchors:
- packages/daemon/src/runtimes/codex-stream-parser.ts
- packages/daemon/src/pods/pod-manager.ts
tags:
- cost
- codex
- parser
- live-ux
- adr-026
source: doc-import:docs/decisions/ADR-026-parser-side-cost-for-non-claude-runtimes.md
status: active
---
Parser-side `costUsd` emission for non-Claude runtimes was chosen over read-time-only aggregation because live-UX consumers render `AgentCompleteEvent.costUsd` directly from the event stream, not from the database. CLI `ap pod watch` and the desktop activity feed consume the `AgentEvent` stream, so `effectiveCostUsd(pod)` running at read time cannot fix the live display gap. Option A (migrate stragglers to `effectiveCostUsd`, leave parser untouched) was rejected because it left the live UX asymmetric: Claude pods show a dollar figure on completion, Codex pods show nothing. Option B (compute in parser, emit on `AgentCompleteEvent`) fixes both the live display and the straggler read sites simultaneously, since `effectiveCostUsd`'s early return on `pod.costUsd > 0` self-heals them once the parser starts populating the column.

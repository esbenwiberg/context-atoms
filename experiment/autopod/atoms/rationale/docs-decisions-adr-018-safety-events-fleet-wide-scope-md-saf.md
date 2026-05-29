---
kind: rationale
claim: '`safety_events` is scoped fleet-wide across all six active detection sites
  rather than just issue-watcher because five of seven sites previously fired silently,
  making a single-source table produce misleading operator safety metrics.'
anchors:
- packages/daemon/src/safety/safety-events-repository.ts
- packages/daemon/src/db/migrations/092_safety_events.sql
- packages/daemon/src/actions/action-engine.ts
- packages/daemon/src/api/mcp-proxy-handler.ts
- packages/daemon/src/issue-watcher/issue-watcher-service.ts
- packages/daemon/src/pods/section-resolver.ts
- packages/daemon/src/pods/skill-resolver.ts
- packages/daemon/src/api/routes/pods.ts
- packages/daemon/src/pods/event-bus.ts
tags:
- safety
- adr
- fleet-wide
- detection
source: doc-import:docs/decisions/ADR-018-safety-events-fleet-wide-scope.md
status: active
---
`safety_events` is scoped fleet-wide across all six active detection sites rather than just issue-watcher because five of seven sites previously fired silently, making a single-source table produce misleading operator safety metrics. The seven sites are: action-engine (only one with prior durable record via `action_audit`), mcp-proxy-handler, issue-watcher, section-resolver, skill-resolver, POST /pods free-text, and event-bus (dead code in production — `event_payload` source value is reserved). Option A (issue-watcher only) was rejected because the operator success signal is "guardrails fired N times this month across all sources"; scoping to one source makes that claim false. Each active site inserts one row per pattern hit via `safetyEventsRepo.insert(...)`. The `event_payload` source enum value is reserved for when `event-bus.ts` content processing is wired in production (today `createEventBus(...)` at `index.ts:176` omits the `contentProcessing` option so that branch never runs).

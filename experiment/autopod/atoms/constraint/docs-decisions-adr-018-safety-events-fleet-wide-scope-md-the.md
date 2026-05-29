---
kind: constraint
claim: "The `source` enum on `safety_events` is append-only \u2014 values may be added\
  \ but never renamed or removed, as any change ripples through the aggregator, the\
  \ Swift Codable mirror, and the drill's `bySource` chart bucketing."
anchors:
- packages/daemon/src/safety/safety-events-repository.ts
- packages/daemon/src/pods/safety-aggregator.ts
- packages/daemon/src/db/migrations/092_safety_events.sql
tags:
- safety
- schema-contract
- enum
- breaking-change
source: doc-import:docs/decisions/ADR-018-safety-events-fleet-wide-scope.md
status: active
---
The `source` enum on `safety_events` is append-only — values may be added but never renamed or removed, as any change ripples through the aggregator, the Swift Codable mirror, and the drill's `bySource` chart bucketing. Valid values are `'action_response' | 'mcp_proxy' | 'issue_body' | 'claude_md_section' | 'skill_content' | 'pod_input' | 'event_payload'`. The aggregator uses these values for GROUP BY bucketing; renaming a value silently splits historical rows into two buckets. The Swift Codable mirror decodes the string directly, so a rename breaks deserialization on the mobile side without a coordinated migration.

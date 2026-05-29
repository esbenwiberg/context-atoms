---
kind: constraint
claim: Injection attempt detections must be persisted to a `safety_events` table (not
  remain log-only) by hooking into the issue-watcher-service detection path, so the
  safety analytics dashboard can query which patterns fired on which pods.
anchors:
- packages/daemon/src/safety/safety-events-repository.ts
- packages/daemon/src/issue-watcher/issue-watcher-service.ts
- packages/daemon/src/security/detectors/injection-detector.ts
tags:
- safety-events
- injection
- persistence
source: doc-import:docs/analytics-dashboard-plan.md#phase-4-safety-guardrails
status: active
---
Injection attempt detections must be persisted to a `safety_events` table (not remain log-only) by hooking into the issue-watcher-service detection path, so the safety analytics dashboard can query which patterns fired on which pods. Schema: (id, pod_id, type, pattern_name, severity, payload_excerpt, created_at). The write hook belongs in issue-watcher-service.ts. Without this persistence, the injection attempts list and trend sparklines in the safety hero card have no backing data.

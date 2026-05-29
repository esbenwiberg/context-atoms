---
kind: constraint
claim: '`node-cron` must NOT be used for job execution; only `cron-parser` is permitted,
  solely for validating cron expressions and computing the next `next_run_at` value.'
anchors:
- packages/daemon/src/scheduled-jobs/scheduled-job-scheduler.ts
- packages/daemon/src/scheduled-jobs/scheduled-job-repository.ts
tags:
- scheduler
- cron-parser
- node-cron
- dependency
source: doc-import:docs/decisions/ADR-012-scheduled-pods-db-driven-scheduler.md
status: active
---
`node-cron` must NOT be used for job execution; only `cron-parser` is permitted, solely for validating cron expressions and computing the next `next_run_at` value. The distinction matters because `node-cron` manages in-memory timer state that is lost on process restart, while `cron-parser` is a pure-computation library with no side effects. Any future code that needs to trigger recurring jobs must go through the DB-polling path, not by importing `node-cron`.

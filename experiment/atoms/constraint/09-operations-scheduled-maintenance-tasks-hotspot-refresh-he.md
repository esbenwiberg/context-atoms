---
kind: constraint
claim: "Scheduled maintenance tasks (hotspot refresh, health check, mutation testing)\
  \ run inside the Guardian service process \u2014 no external cron or job runner\
  \ is needed."
anchors:
- src/pr_guardian/core/maintenance.py
- src/pr_guardian/config/defaults.yml
tags:
- scheduler
- maintenance
- hotspot
- in-process
source: doc-import:docs/plan/09-operations.md
status: active
---
Scheduled maintenance tasks (hotspot refresh, health check, mutation testing) run inside the Guardian service process — no external cron or job runner is needed. The scheduler (APScheduler or equivalent) is configured via config/defaults.yml under scheduled_tasks: hotspot_refresh runs at 2 AM daily (timeout 30 min), health_check at 3 AM Sundays (timeout 60 min), mutation_testing at 4 AM Sundays (timeout 120 min). Results are stored in PostgreSQL keyed by repo + date. Adding an external scheduler (cron, Celery beat, etc.) would contradict this design.

---
kind: rationale
claim: Feedback and human-override data are stored in PostgreSQL (same database as
  reviews and findings) rather than in flat files, because the dashboard queries them
  directly with no file-sync step.
anchors:
- src/pr_guardian/persistence/storage.py
- alembic/versions/002_add_pipeline_log.py
tags:
- feedback
- storage
- postgresql
- dashboard
source: doc-import:docs/plan/09-operations.md
status: active
---
Feedback and human-override data are stored in PostgreSQL (same database as reviews and findings) rather than in flat files, because the dashboard queries them directly with no file-sync step. The feedback table captures per-PR data including agent verdicts, certainty downgrades, combined score, guardian decision, human outcome, human override flag, and post-merge incidents. A file-based approach was rejected because it would require a separate sync mechanism for the dashboard to read aggregate stats. Threshold auto-tuning also reads directly from this table and must not apply changes without human approval.

---
kind: constraint
claim: "Alembic migrations are append-only and sequentially numbered; a merged migration\
  \ must never be edited \u2014 new behavior requires a new migration file."
anchors:
- alembic/versions/
tags:
- migrations
- database
- append-only
source: doc-import:CLAUDE.md
status: active
---
Alembic migrations are append-only and sequentially numbered; a merged migration must never be edited — new behavior requires a new migration file.

The naming convention is `NNN_description.py` (e.g. `018_add_finding_lifecycle.py`). Editing a merged migration risks divergence between environments that have already applied it and those that haven't, breaking `alembic upgrade head` idempotency. Any schema change — including column widening, constraint additions, or data backfills — must be expressed as a new migration at the end of the sequence.

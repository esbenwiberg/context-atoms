---
kind: constraint
claim: 'Alembic migrations are append-only: merged migrations must never be mutated;
  schema state is reconstructed by sequential replay.'
anchors:
- alembic/versions/
tags:
- migrations
- database
- schema
source: doc-import:ARCHITECTURE.md
status: active
---
Alembic migrations are append-only: merged migrations must never be mutated; schema state is reconstructed by sequential replay.

When a schema change is needed, add a new numbered migration file — never edit an existing one in `alembic/versions/`. The canonical state of the database is the result of replaying all migrations from 001 onward. Editing a merged migration breaks replay for any environment that has already applied it, causing state divergence that cannot be automatically recovered.

Before touching the schema, read the last 3 migration files to understand the current shape.

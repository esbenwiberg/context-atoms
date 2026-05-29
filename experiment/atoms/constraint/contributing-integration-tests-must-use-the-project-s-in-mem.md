---
kind: constraint
claim: Integration tests must use the project's in-memory database mode rather than
  mocking the database layer.
anchors:
- tests/
- src/pr_guardian/persistence/database.py
tags:
- testing
- database
- integration
- no-mock
source: doc-import:CONTRIBUTING.md
status: active
---
Integration tests must use the project's in-memory database mode rather than mocking the database layer.
Mocking the DB layer allows schema mismatches and missing constraints to go undetected until production. The in-memory mode exists specifically to give tests a real SQLAlchemy/Alembic stack at near-zero cost. Prefer it wherever behaviour under real persistence semantics matters.

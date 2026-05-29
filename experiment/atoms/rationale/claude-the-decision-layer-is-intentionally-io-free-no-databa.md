---
kind: rationale
claim: The `decision/` layer is intentionally IO-free (no database, no HTTP, no platform
  calls) so that the scoring and verdict logic can be unit-tested in milliseconds
  and reasoned about independently of integration state.
anchors:
- src/pr_guardian/decision/
- pyproject.toml
tags:
- architecture
- import-linter
- testability
- decision-engine
source: doc-import:CLAUDE.md
status: active
---
The `decision/` layer is intentionally IO-free (no database, no HTTP, no platform calls) so that the scoring and verdict logic can be unit-tested in milliseconds and reasoned about independently of integration state.

This is enforced by `import-linter` in `pyproject.toml` and breaks CI if violated.

The decision engine is a pure function: it takes findings + config in and returns a verdict (APR/REV/BLK) out. This design was a deliberate trade-off — it sacrifices the ability to do lazy DB lookups inside scoring in exchange for complete isolation. Any data the engine needs must be passed in by the orchestrator before scoring begins. Adding IO to `decision/` is not a local change; it unravels the testability guarantee for the entire verdict path.

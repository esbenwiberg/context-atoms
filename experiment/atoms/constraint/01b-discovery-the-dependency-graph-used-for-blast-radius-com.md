---
kind: constraint
claim: The dependency graph used for blast-radius computation must never be computed
  per-PR; it must be a pre-computed nightly lookup from the database, with an empty-consumers
  fallback when no graph exists.
anchors:
- src/pr_guardian/discovery/blast_radius.py
- src/pr_guardian/discovery/dep_graph.py
tags:
- blast-radius
- dependency-graph
- performance
source: doc-import:docs/plan/01b-discovery.md
status: active
---
The dependency graph used for blast-radius computation must never be computed per-PR; it must be a pre-computed nightly lookup from the database, with an empty-consumers fallback when no graph exists.

Per-PR computation is explicitly ruled out as too slow. The graph is built nightly using language-specific import analysis (`dependency-cruiser` for JS/TS, `pydeps` for Python, Roslyn for C#) and stored in DB. If no graph is available (new repo), blast radius returns empty consumers and triage falls back to direct file classification only. Repos without static analysis tooling can declare `critical_consumers` mappings directly in `review.yml` as the highest-priority override.

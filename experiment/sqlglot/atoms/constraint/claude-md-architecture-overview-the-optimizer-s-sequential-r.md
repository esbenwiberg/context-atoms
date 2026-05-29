---
kind: constraint
claim: The optimizer's sequential rule pipeline has load-bearing order dependencies,
  so rules must not be reordered arbitrarily; `qualify` in particular must run before
  rules that depend on fully-resolved identifiers.
anchors:
- sqlglot/optimizer/optimizer.py
- sqlglot/optimizer/qualify.py
tags:
- optimizer
- rule-order
- qualify
- pipeline
source: doc-import:CLAUDE.md#architecture-overview
status: active
---
The optimizer's sequential rule pipeline has load-bearing order dependencies, so rules must not be reordered arbitrarily; `qualify` in particular must run before rules that depend on fully-resolved identifiers. `qualify` normalises identifiers and fully qualifies all tables and columns, which downstream rules such as `pushdown_predicates`, `pushdown_projections`, and `annotate_types` assume is already done. Adding a new optimizer pass without respecting this ordering will produce incorrect or partially-optimised output. The optimizer performs only logical rewrites — physical/performance planning is explicitly out of scope.

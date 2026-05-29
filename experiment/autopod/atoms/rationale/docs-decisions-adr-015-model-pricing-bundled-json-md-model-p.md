---
kind: rationale
claim: Model pricing is a bundled static JSON in @autopod/shared rather than a DB
  table or auto-fetched endpoint because pricing data is small, decays irregularly
  with no webhook, and the single-operator deployment has no multi-tenant override
  requirements.
anchors:
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- cost
- pricing
- architecture
source: doc-import:docs/decisions/ADR-015-model-pricing-bundled-json.md
status: active
---
Model pricing is a bundled static JSON in @autopod/shared rather than a DB table or auto-fetched endpoint because pricing data is small, decays irregularly with no webhook, and the single-operator deployment has no multi-tenant override requirements. Three properties drove the decision: (1) prices change without a push signal so any auto-fetch becomes its own integration to maintain; (2) the full catalog is a few dozen models × two numbers each, comfortably in one small JSON file; (3) Esben is the sole operator, so there is no per-org override scenario. Rejected alternatives: a database table (unnecessary migration + admin UI overhead), a scheduled polling job (complexity for no gain given solo usage), an admin endpoint (same).

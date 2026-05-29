---
kind: rationale
claim: No POST /pods/analytics/simulate daemon endpoint exists because the what-if
  simulator runs client-side on the byModel[] payload the analytics endpoint already
  returns.
anchors:
- packages/daemon/src/api/routes/
tags:
- analytics
- simulator
- architecture
source: doc-import:docs/decisions/ADR-023-simulator-client-side-naive-projection.md
status: active
---
No POST /pods/analytics/simulate daemon endpoint exists because the what-if simulator runs client-side on the byModel[] payload the analytics endpoint already returns. Option A (server endpoint with identical naïve math) was rejected in ADR-023: it imposes HTTP round-trip latency on every slider tick with no accuracy improvement, adds a new endpoint/error path/DB hit per exploration, and the master plan had already tagged the server endpoint as deferrable. Client-side weighted-average math over <10 models runs in microseconds and enables immediate feedback on slider drag with no network dependency. If a future CLI or non-desktop surface needs simulation, the math must be re-derived in that language — formulas are documented in ADR-023 and specs/analytics-models/briefs/03-add-models-what-if-simulator.md.

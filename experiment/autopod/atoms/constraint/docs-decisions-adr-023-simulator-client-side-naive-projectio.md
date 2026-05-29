---
kind: constraint
claim: The completeCostUsd field in the byModel[] wire payload exists specifically
  for the what-if simulator's cost-per-PR projection math and must not be removed.
anchors:
- packages/daemon/src/api/wire-serializers.ts
- packages/daemon/src/api/schemas.ts
tags:
- analytics
- simulator
- wire-contract
source: doc-import:docs/decisions/ADR-023-simulator-client-side-naive-projection.md
status: active
---
The completeCostUsd field in the byModel[] wire payload exists specifically for the what-if simulator's cost-per-PR projection math and must not be removed. Per ADR-023: 'The simulator's byModel[] consumption is verbatim — adding a new field for the simulator means adding it to the wire contract first. Today this includes completeCostUsd which exists specifically for the projection math.' Dropping or renaming this field silently breaks the client-side projected cost-per-PR axis without any daemon-side test failure, since the computation lives in the desktop app.

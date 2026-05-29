---
kind: rationale
claim: buildContributions uses a layered render-time carving pattern borrowed from
  PowerHeatmap's allocationBreakdownProcessor, parameterised on two pure primitives
  so all math stays in src/math/.
anchors:
- src/heatmap/buildContributions.ts
- src/math/
tags:
- heatmap
- prior-art
- architecture
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#references
status: active
---
buildContributions uses a layered render-time carving pattern borrowed from PowerHeatmap's allocationBreakdownProcessor (sibling Projectum repo). The key architectural decision was to parameterise the carving logic on two pure primitives rather than embedding calculation logic inside the heatmap module, keeping all math in src/math/ and making the heatmap layer a pure renderer over pre-computed data.

---
kind: rationale
claim: The `curve` front/back/even weighting on Resource was removed because it was
  a POC-era synthesis to generate demand shape from monthly totals; with `pum_propose`
  spans flowing through directly, the data is the curve and the field has no input.
anchors:
- src/adapters/xrm/index.ts
- src/adapters/xrm/mappers.ts
- specs/demand-distribution-spans/design.md
tags:
- dataverse
- resource
- adr
- poc-cleanup
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#alternatives-considered
status: active
---
The `curve` front/back/even weighting on Resource was removed because it was a POC-era synthesis to generate demand shape from monthly totals; with `pum_propose` spans flowing through directly, the data is the curve and the field has no input. The curve property existed only to synthesise a temporal distribution when upstream rows did not carry one. Once the adapter reads continuous `pum_propose` spans, the curve weighting is both redundant and without a valid input signal.

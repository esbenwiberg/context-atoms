---
kind: constraint
claim: Every bundle-size budget raise must update the constants in `tools/check-bundle-size.mjs`
  AND add an inline note in the file's comment header recording the date, driving
  feature, new measurements, and remaining headroom; a raise without this note is
  a process bug and must be reverted or amended.
anchors:
- tools/check-bundle-size.mjs
tags:
- bundle-size
- process
- audit-trail
- constraint
source: doc-import:docs/adr/0005-bundle-size-budget.md
status: active
---
Every bundle-size budget raise must update the constants in `tools/check-bundle-size.mjs` AND add an inline note in the file's comment header recording the date, driving feature, new measurements, and remaining headroom; a raise without this note is a process bug and must be reverted or amended.

The comment header in `tools/check-bundle-size.mjs` is the canonical audit trail — it functions as a running perf diary readable via git blame. The raise must also be justified in the commit message with the feature that drove it. Before raising, `npm run bundle:viz` (rollup-plugin-visualizer, local-only treemap) should be used to confirm there is no obvious fat to cut first. The discipline of the note IS the decision — silent raises undermine the entire gate.

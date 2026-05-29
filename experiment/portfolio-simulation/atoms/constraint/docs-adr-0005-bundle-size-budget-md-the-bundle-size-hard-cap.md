---
kind: constraint
claim: The bundle-size hard cap is the Dataverse Web Resource upload limit (5 MB)
  applied to the raw `dist/index.html` artifact; gzip size is not gated because Dataverse
  enforces upload size on the uncompressed artifact, and a 2 MB soft warning sits
  below the hard cap.
anchors:
- tools/check-bundle-size.mjs
tags:
- bundle-size
- dataverse
- performance
- ci-gate
source: doc-import:docs/adr/0005-bundle-size-budget.md
status: active
---
The bundle-size hard cap is the Dataverse Web Resource upload limit (5 MB) applied to the raw `dist/index.html` artifact; gzip size is not gated because Dataverse enforces upload size on the uncompressed artifact, and a 2 MB soft warning sits below the hard cap.

The artifact is a single inlined HTML file with no code-splitting or lazy-loading — every byte lands on the customer's first paint on every page load inside the xPM model-driven app iframe. The hard cap constant `RAW_BUDGET_BYTES` and the warning threshold both live at the top of `tools/check-bundle-size.mjs`. Gzip was previously gated but was removed (2026-05-24 revision) because Dataverse upload enforcement is on the raw file, not its compressed form. The 2 MB warning preserves deliberate-raise discipline without failing builds on normal feature growth.

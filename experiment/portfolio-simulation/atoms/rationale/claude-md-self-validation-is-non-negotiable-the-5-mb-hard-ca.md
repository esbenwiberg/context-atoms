---
kind: rationale
claim: The 5 MB hard cap on dist/index.html exists because Dataverse Web Resource
  uploads cannot exceed 5 MB; 2 MB is a soft warning threshold.
anchors:
- tools/check-bundle-size.mjs
tags:
- bundle-size
- dataverse
- ci-gate
source: doc-import:CLAUDE.md#self-validation-is-non-negotiable
status: active
---
The 5 MB hard cap on dist/index.html exists because Dataverse Web Resource uploads cannot exceed 5 MB; 2 MB is a soft warning threshold. The build gate in tools/check-bundle-size.mjs enforces both limits. Gzip size is reported but not gated. Any warning should be investigated before merging. When raising either limit, bump both numbers in the tool and note the new baseline and reason in the commit message.

---
kind: constraint
claim: The build must produce a single-file dist/index.html with no dynamic chunks,
  enforced by vite-plugin-singlefile and CI.
anchors:
- vite.config.ts
- .github/workflows/build-and-smoke.yml
tags:
- build
- single-bundle
- dataverse
- no-dynamic-chunks
source: doc-import:CLAUDE.md#conventions
status: active
---
The build must produce a single-file dist/index.html with no dynamic chunks, enforced by vite-plugin-singlefile and CI. This constraint exists because the output is deployed as a Dataverse Web Resource, which must be a self-contained HTML file. Introducing dynamic imports or code splitting will break the deployment target.

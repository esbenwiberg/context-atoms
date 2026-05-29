---
kind: rationale
claim: "The `validator` package holds only types for Playwright smoke test script\
  \ generation and result parsing \u2014 execution lives in `daemon` \u2014 to decouple\
  \ the type contract from the Playwright runtime."
anchors:
- packages/daemon/package.json
tags:
- validator
- playwright
- architecture
- separation-of-concerns
source: doc-import:CLAUDE.md#architecture
status: active
---
The `validator` package holds only types for Playwright smoke test script generation and result parsing — execution lives in `daemon` — to decouple the type contract from the Playwright runtime. This means consumers of the validator's types (e.g. the CLI) do not pull in Playwright as a transitive dependency, and the execution boundary stays clearly inside the daemon where container orchestration already lives.

---
kind: constraint
claim: The smoke-fixture Playwright tests rely on `playwright.fixture.config.ts` owning
  the vite-preview server lifecycle; tests must not spawn or manage their own dev
  server.
anchors:
- playwright.fixture.config.ts
- tests/smoke-fixture
tags:
- testing
- playwright
- smoke
- vite
- lifecycle
source: doc-import:CLAUDE.md#where-context-lives
status: active
---
The smoke-fixture Playwright tests rely on `playwright.fixture.config.ts` owning the vite-preview server lifecycle; tests must not spawn or manage their own dev server. The `webServer` option in `playwright.fixture.config.ts` starts and stops the vite-preview process around the test run. Individual specs in `tests/smoke-fixture/` must not replicate this setup or assume a separately-running server, or the process lifecycle will be undefined and tests will flake.

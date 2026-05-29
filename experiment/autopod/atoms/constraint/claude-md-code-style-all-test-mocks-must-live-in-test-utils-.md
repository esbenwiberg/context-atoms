---
kind: constraint
claim: All test mocks must live in `test-utils/mock-helpers.ts` rather than being
  defined inline or scattered across individual test files.
anchors:
- packages/daemon/src/test-utils/mock-helpers.ts
tags:
- testing
- mocks
- organisation
source: doc-import:CLAUDE.md#code-style
status: active
---
All test mocks must live in `packages/daemon/src/test-utils/mock-helpers.ts` rather than being defined inline or scattered across individual test files. This is the single source of truth for shared mock factories and stubs. Test files co-located with source (foo.ts → foo.test.ts) import from this central file. Defining a one-off mock inside a test file violates this convention even for simple cases.

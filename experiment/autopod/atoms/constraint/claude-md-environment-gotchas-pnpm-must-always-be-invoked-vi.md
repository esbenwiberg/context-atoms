---
kind: constraint
claim: pnpm must always be invoked via `npx pnpm` because pnpm is not installed globally
  in the sandbox.
anchors:
- package.json
- .github/workflows/ci.yml
tags:
- pnpm
- tooling
- sandbox
- cli
source: doc-import:CLAUDE.md#environment-gotchas
status: active
---
pnpm must always be invoked via `npx pnpm` because pnpm is not installed globally in the sandbox. Any bare `pnpm` command (e.g. `pnpm install`, `pnpm run build`) will fail with 'command not found'. Every script, Makefile target, or agent command that invokes pnpm must prefix it with `npx`.

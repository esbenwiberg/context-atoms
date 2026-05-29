---
kind: rationale
claim: "Ports-and-adapters with math purity was chosen because the math IP is the\
  \ load-bearing asset \u2014 empirically tuned and locked in by parity tests \u2014\
  \ so leaking it into React or platform code would make it untestable in isolation,\
  \ lock it to xPM, and make refactors risky."
anchors:
- src/math/**
- src/adapters/types.ts
- src/adapters/index.ts
- .dependency-cruiser.cjs
- tests/parity
tags:
- architecture
- math-purity
- ports-and-adapters
- adr
source: doc-import:docs/adr/0002-ports-and-adapters-with-math-purity.md
status: active
---
Ports-and-adapters with math purity was chosen because the math IP is the load-bearing asset — empirically tuned and locked in by parity tests — so leaking it into React or platform code would make it untestable in isolation, lock it to xPM, and make refactors risky.

Alternatives rejected:
- Hexagonal-by-convention without tooling: conventions silently rot under deadline pressure.
- Layered architecture: doesn't capture the 'math IP is the asset' invariant — still allows React to leak into the domain.
- Single-package monolith: dev-time fixture adapter and prod-time xrm adapter would tangle with view code, making adapter swaps a refactor instead of a wiring change.

The invariant is enforced at build time via `dependency-cruiser` (`npm run arch:check`, part of `npm run verify` and CI). If a math module legitimately needs new capability (e.g. async I/O), the impure part must live in an adapter or platform module — not relax the rule.

---
kind: constraint
claim: src/math/ modules must never import React, DOM globals, or platform/adapter
  code; this purity is enforced by dependency-cruiser.
anchors:
- src/math
- .dependency-cruiser.cjs
tags:
- architecture
- ports-and-adapters
- math-purity
source: doc-import:CLAUDE.md#self-validation-is-non-negotiable
status: active
---
src/math/ modules must never import React, DOM globals, or platform/adapter code; this purity is enforced by dependency-cruiser. The arch:check gate (npm run arch:check) additionally forbids math and view layers from importing adapter implementations, and rejects circular deps. These rules encode the ports-and-adapters seam: math is a pure computation layer with no side-effects or framework coupling.

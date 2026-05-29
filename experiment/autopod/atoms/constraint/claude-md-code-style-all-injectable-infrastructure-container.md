---
kind: constraint
claim: All injectable infrastructure (ContainerManager, Runtime, WorktreeManager,
  ValidationEngine) must be defined as TypeScript interfaces, not concrete classes.
anchors:
- packages/daemon/src/interfaces/container-manager.ts
- packages/daemon/src/interfaces/runtime-registry.ts
- packages/daemon/src/interfaces/validation-engine.ts
- packages/daemon/src/interfaces/worktree-manager.ts
- packages/daemon/src/interfaces/
tags:
- dependency-injection
- interfaces
- architecture
source: doc-import:CLAUDE.md#code-style
status: active
---
All injectable infrastructure must be defined as TypeScript interfaces, not concrete classes. This applies to ContainerManager, Runtime, WorktreeManager, ValidationEngine, and any future infrastructure boundary. Concrete implementations live elsewhere; tests receive mock implementations satisfying the interface. Adding a new injectable service requires a matching interface file in packages/daemon/src/interfaces/ before wiring it up.

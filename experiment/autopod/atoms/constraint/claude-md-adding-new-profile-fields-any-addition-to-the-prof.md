---
kind: constraint
claim: Any addition to the Profile type must follow the /add-profile-field skill checklist
  because the change spans ~11 layers and skipping one is the top cause of shipping
  broken fields.
anchors:
- .agents/skills/add-profile-field/SKILL.md
- .claude/skills/add-profile-field/SKILL.md
- packages/daemon/src/profiles/profile-store.ts
- packages/daemon/src/profiles/profile-validator.ts
tags:
- profile
- checklist
- multi-layer
source: doc-import:CLAUDE.md#adding-new-profile-fields
status: active
---
Any addition to the Profile type must follow the /add-profile-field skill checklist because the change spans ~11 layers and skipping one is the top cause of shipping broken fields.

The ~11 layers are: shared types, daemon migration, profile-store, profile-validator, 6 desktop layers, and the CLI. The canonical failure mode is a field that the daemon validates correctly but the desktop cannot render, which ships silently without the checklist.

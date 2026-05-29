---
kind: rationale
claim: The 'artifact' OutputMode was chosen to implement research pods rather than
  adding a new 'research' value because 'artifact' already had scaffolding in system-instructions-generator.ts
  and was originally added anticipating this use case.
anchors:
- packages/daemon/src/pods/system-instructions-generator.ts
- packages/cli/src/commands/research.ts
tags:
- output-mode
- research
- artifact
- adr
source: doc-import:docs/decisions/ADR-009-research-pods-reuse-artifact-outputmode.md
status: active
---
The 'artifact' OutputMode was chosen to implement research pods rather than adding a new 'research' value because 'artifact' already had scaffolding in system-instructions-generator.ts and was originally added anticipating this use case. Adding a 'research' value to OutputMode was explicitly rejected: it would duplicate the concept and abandon existing artifact-mode branches in system-instructions-generator.ts (lines 161-182, 346-358, 500-515). The existing scaffolding is the starting point, not a rewrite. Any future non-research artifact use cases also benefit from the same implementation.

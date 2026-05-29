---
kind: constraint
claim: 'The CLI command ''ap research'' must use outputMode: ''artifact'' internally;
  no ''research'' literal must ever be added to the OutputMode union type.'
anchors:
- packages/cli/src/commands/research.ts
- packages/daemon/src/pods/system-instructions-generator.ts
tags:
- output-mode
- research
- artifact
- type-invariant
source: doc-import:docs/decisions/ADR-009-research-pods-reuse-artifact-outputmode.md
status: active
---
The CLI command 'ap research' must use outputMode: 'artifact' internally; no 'research' literal must ever be added to the OutputMode union type. The user-facing name ('research') and the internal representation ('artifact') are intentionally different — this is not a naming inconsistency to be 'fixed'. OutputMode remains 'pr' | 'artifact' | 'workspace' with no additions for research functionality.

---
kind: constraint
claim: ADR numbers are globally monotonic and must never be reused, even after a decision
  is superseded.
anchors:
- .agents/skills/plan-feature/SKILL.md
- .claude/skills/plan-feature/SKILL.md
tags:
- adr
- numbering
- docs
source: doc-import:docs/decisions/README.md
status: active
---
ADR numbers are globally monotonic and must never be reused, even after a decision is superseded. Each ADR lives forever under its original `ADR-NNN` identifier so that references from spec folders and other ADRs remain stable over time. A superseded ADR updates its status to `Superseded by ADR-MMM` but retains its file and number.

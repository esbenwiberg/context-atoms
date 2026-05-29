---
kind: rationale
claim: Spec folders (specs/<feature>/) reference only ADR IDs in design.md rather
  than embedding full ADR text, so the canonical decision record remains in docs/decisions/
  and can evolve without touching specs.
anchors:
- .agents/skills/plan-feature/SKILL.md
- .claude/skills/plan-feature/SKILL.md
tags:
- adr
- spec
- plan-feature
source: doc-import:docs/decisions/README.md
status: active
---
Spec folders (specs/<feature>/) reference only ADR IDs in design.md rather than embedding full ADR text, so the canonical decision record remains in docs/decisions/ and can evolve without touching specs. This indirection avoids duplication drift: if consequences or context are revised after acceptance, only the ADR file changes. The planning tool (/plan-feature) is responsible for writing new ADRs here whenever a planning interview surfaces a hard-to-reverse or surprising decision.

---
kind: constraint
claim: 'References to curve: or Resource.curve are banned from src/ and docs/adr/
  to prevent resurrection of the deleted demand-curve model.'
anchors:
- tools/check-bans.mjs
- tests/tools/check-bans.spec.ts
tags:
- demand
- curve
- ban
- deleted-model
source: doc-import:docs/adr/0011-demand-distribution-and-override-spans.md#enforcement
status: active
---
References to curve: or Resource.curve are banned from src/ and docs/adr/ to prevent resurrection of the deleted demand-curve model. The ban is enforced by tools/check-bans.mjs. ADR-0011 itself is excluded from the grep so it can name the deleted symbols in prose; any future ADR that legitimately needs to mention these symbols must fence the line in a comment or add itself to the rule's exclude list.

---
kind: rationale
claim: "`config_policy` is a distinct `StickyTriggerKind` rather than reusing `path_risk`\
  \ because config-consent violations must surface as a structural semantic in the\
  \ wizard, audit payload, and future reviewers\u2014not be hidden behind path-risk\
  \ semantics."
anchors:
- src/pr_guardian/decision/types.py
- src/pr_guardian/decision/engine.py
tags:
- sticky-trigger
- auto-approve
- config-policy
- decision
source: doc-import:docs/decisions/ADR-005-final-auto-approval-gate.md
status: active
---
`config_policy` is a distinct `StickyTriggerKind` rather than reusing `path_risk` because config-consent violations must surface as a structural semantic in the wizard, audit payload, and future reviewers—not be hidden behind path-risk semantics.

ADR-002 made the sticky-trigger kind set closed. The auto-approve policy needed a structural reason (missing/invalid consent, root `review.yml` edits) that is neither path-risk nor finding-derived. Reusing `path_risk` would obscure those semantics everywhere the kind is inspected: the human review wizard, the stored audit record, and any future code reading the trigger set. Future structural trigger kinds still require an ADR update before being added.

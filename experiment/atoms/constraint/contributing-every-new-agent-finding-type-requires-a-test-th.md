---
kind: constraint
claim: Every new agent finding type requires a test that proves the evidence anchor
  format (file + line + quote) round-trips correctly through storage.
anchors:
- src/pr_guardian/agents/
- src/pr_guardian/models/findings.py
- tests/
tags:
- testing
- findings
- agents
- evidence-anchor
source: doc-import:CONTRIBUTING.md
status: active
---
Every new agent finding type requires a test that proves the evidence anchor format (file + line + quote) round-trips correctly through storage.
This invariant guards against silent data loss in the evidence anchor fields. A finding that loses its file/line/quote reference cannot be used for inline comments, human review, or audit trails. The round-trip test must cover serialisation → storage → retrieval of these three fields.

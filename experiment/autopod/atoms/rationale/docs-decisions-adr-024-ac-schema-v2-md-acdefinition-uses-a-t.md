---
kind: rationale
claim: AcDefinition uses a typed `polarity` enum ('expect-output'|'expect-no-output'|'exit-zero')
  instead of prose pass/fail strings because regex-scanning the `pass:` value against
  a NEGATIVE_HINTS table was silently incorrect on small typos and the alternative
  of just tightening the regex was rejected as leaving the fragility intact.
anchors:
- packages/daemon/src/db/migrations/101_pod_contract.sql
- packages/daemon/src/db/migrations/104_remove_acceptance_criteria.sql
- packages/daemon/src/pods/validation-repository.ts
tags:
- acceptance-criteria
- ac-schema
- polarity
- validation
source: doc-import:docs/decisions/ADR-024-ac-schema-v2.md
status: active
---
AcDefinition uses a typed `polarity` enum instead of prose pass/fail strings because regex-scanning prose for polarity was brittle and silently wrong on typos. The old shape `{ type, test, pass, fail }` had `executeCmdChecks` regex-scan the `pass:` value against a `NEGATIVE_HINTS` table to decide between expect-output and expect-no-output. The alternative of keeping prose and tightening the regex was explicitly rejected (ADR-024 alternative 1) because it would have fixed the immediate firing bug while leaving both the overloaded `test` field and the fragility intact. `polarity` as an explicit enum is strictly more constrained: the valid values are 'expect-output', 'expect-no-output', and 'exit-zero', and it is only valid when `type === 'cmd'`.

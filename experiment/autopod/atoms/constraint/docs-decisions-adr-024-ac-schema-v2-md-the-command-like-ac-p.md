---
kind: constraint
claim: The `COMMAND_LIKE_AC_PATTERNS` banlist in `classifyAcTypes` must only override
  ACs whose declared type is `cmd` or absent; ACs with an explicitly declared `web`
  or `api` type must pass through unchanged.
anchors:
- packages/daemon/src/pods/validation-repository.ts
- packages/daemon/src/pods/pod-bridge-validation.test.ts
tags:
- acceptance-criteria
- classifyAcTypes
- ac-type
- banlist
source: doc-import:docs/decisions/ADR-024-ac-schema-v2.md
status: active
---
The `COMMAND_LIKE_AC_PATTERNS` banlist must only fire when the declared AC type is `cmd` or absent — it must never reclassify a declared `web` or `api` AC. The pre-existing bug (pod `confidential-loon`) occurred because the banlist ran against every AC regardless of declared type: two ACs with `type: web` and outcome text starting with `/pr-dashboard` matched the slash-command regex `/^\/[a-z]/i` and were silently force-converted to `type: 'none'`, so they never fired. The fix has two parts: (1) tighten the regex to require single-token criteria (`/^\/[a-z][a-z0-9-]*\s*$/i`) so outcomes like `/pr-dashboard renders with header` are not caught, and (2) gate the override so it only applies when the declared type is `cmd` or absent. A declared `web` or `api` type is now load-bearing and must be trusted.

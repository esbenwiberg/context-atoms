---
kind: constraint
claim: "`payload_excerpt` in `safety_events` must always contain post-sanitize text\
  \ (\u2264256 chars); storing the pre-sanitize raw input is explicitly prohibited\
  \ because it re-introduces the data leakage the sanitizer was designed to prevent."
anchors:
- packages/daemon/src/safety/safety-events-repository.ts
- packages/daemon/src/db/migrations/092_safety_events.sql
- packages/daemon/src/security/detectors/pii-detector.ts
- packages/daemon/src/security/detectors/injection-detector.ts
tags:
- safety
- pii
- sanitization
- data-handling
source: doc-import:docs/decisions/ADR-018-safety-events-fleet-wide-scope.md
status: active
---
`payload_excerpt` in `safety_events` must always contain post-sanitize text (≤256 chars); storing the pre-sanitize raw input is explicitly prohibited because it re-introduces the data leakage the sanitizer was designed to prevent. The field is TEXT NULL — NULL is valid when no excerpt is needed. The 256-char cap is enforced at write time. Writers must pass the sanitized/redacted output of `processContent`/`processContentDeep`, never the original untrusted string. This is a hard invariant: the security value of logging detections is nullified if the log itself becomes a leakage vector.

---
kind: constraint
claim: profile.reviewerModel is the authoritative model for ask_ai escalations and
  AI task review; escalation.askAi.model exists solely for legacy wire compatibility
  and must not be used as a source of truth.
anchors:
- packages/daemon/src/profiles/profile-store.ts
- packages/daemon/src/pods/system-instructions-generator.ts
tags:
- escalation
- model
- legacy
source: doc-import:README.md#profile-deep-dive
status: active
---
profile.reviewerModel is the authoritative model for ask_ai escalations and AI task review; escalation.askAi.model exists solely for legacy wire compatibility and must not be used as a source of truth. Any code that needs to resolve which model handles reviewer tasks must read reviewerModel. escalation.askAi.model is preserved on the wire format to avoid breaking older clients but should never override reviewerModel when both are present.

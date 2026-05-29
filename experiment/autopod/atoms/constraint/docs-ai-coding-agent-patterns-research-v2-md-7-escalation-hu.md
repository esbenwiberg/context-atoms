---
kind: constraint
claim: CI and validation retry caps must be finite and prominently configurable in
  profile config, with two rounds as the recommended upper bound, because unbounded
  retries mask systemic harness deficiencies rather than fixing them.
anchors:
- packages/daemon/src/db/migrations/076_profile_loop_tunables.sql
- packages/daemon/src/profiles/profile-store.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- retry-policy
- ci
- validation
- profile-config
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#7-escalation-human-oversight-agent-to-agent-review
status: active
---
CI and validation retry caps must be finite and prominently configurable in profile config, with two rounds as the recommended upper bound, because unbounded retries mask systemic harness deficiencies rather than fixing them. When a pod fails repeatedly on similar issues, the correct response is to surface patterns to profile owners suggesting harness improvements (better instructions, additional tools, different validation strategy) — not to keep retrying. This principle ('fix the harness, not the prompt') is modelled on Stripe's hard two-round CI cap. The loop tunables migration (076) introduced this surface; the constraint is that these caps should never be left as unlimited defaults in production profiles.

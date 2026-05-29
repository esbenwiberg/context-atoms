---
kind: rationale
claim: "Auto-spillover to ACI was explicitly rejected because placement is deliberate\
  \ \u2014 users pick hardware based on repo size and cost \u2014 and silent rerouting\
  \ would waste money (ACI is billed per minute) or time (wrong CPU class)."
anchors:
- packages/daemon/src/pods/pod-queue.ts
- packages/daemon/src/pods/runtime-resolver.ts
- packages/daemon/src/containers/aci-container-manager.ts
tags:
- scheduling
- placement
- ACI
- cost
- rejected-alternative
source: doc-import:docs/decisions/ADR-005-distributed-runners-no-auto-spillover.md
status: active
---
Auto-spillover to ACI was explicitly rejected because placement is deliberate. Users choose a specific runner (e.g. their laptop) intentionally — heavy repos run locally on purpose; scheduled jobs target ACI on purpose. Surprise rerouting would silently execute on the wrong hardware, wasting ACI per-minute billing or incurring wrong-CPU-class time penalties. Two other alternatives were also rejected: fail-fast loses the 'my laptop wakes up in 15 min, just wait' use case; per-profile policy (option 4) was deemed over-engineered for v1 and deferred — it can be added later without breaking changes if a real use case appears.

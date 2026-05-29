---
kind: constraint
claim: The sleep-detector tick interval (30 s) must remain strictly shorter than the
  watchdog tick interval (60 s), because the 60 s wake-grace window granted to watchdogs
  must be larger than the watchdog's own polling interval or the watchdog will fire
  before the grace window suppression takes effect.
anchors:
- packages/daemon/src/pods/sleep-detector.ts
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/runtimes/stream-grace.ts
tags:
- sleep-recovery
- timing
- watchdog
- invariant
source: doc-import:docs/decisions/ADR-021-sleep-recovery-via-reconcile-on-wake.md
status: active
---
The sleep-detector tick interval (30 s) must remain strictly shorter than the watchdog tick interval (60 s), because the 60 s wake-grace window granted to watchdogs must be larger than the watchdog's own polling interval or the watchdog will fire before the grace window suppression takes effect. startStuckPodWatchdog (pod-manager.ts) and withIdleLivenessProbe (stream-grace.ts) both subscribe to host.resumed and suppress failure paths for 60 s; if the watchdog's tick is also 60 s it may evaluate before the suppression is registered. Changing AUTOPOD_SLEEP_DETECT_THRESHOLD_MS, the watchdog interval, or the grace window must preserve the ordering: detect-tick < watchdog-tick <= grace-window.

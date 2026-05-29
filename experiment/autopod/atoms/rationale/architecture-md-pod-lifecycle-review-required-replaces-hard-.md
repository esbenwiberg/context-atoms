---
kind: rationale
claim: '`review_required` replaces hard failure once `maxPrFixAttempts` are exhausted
  so that in-progress work is never silently discarded.'
anchors:
- packages/daemon/src/pods/pod-repository.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- pod-lifecycle
- review
- human-in-the-loop
source: doc-import:ARCHITECTURE.md#pod-lifecycle
status: active
---
`review_required` replaces hard failure once `maxPrFixAttempts` are exhausted so that in-progress work is never silently discarded. It is a durable human-attention signal — the pod stays visible and actionable rather than disappearing into a terminal `failed` state. From `review_required` a pod can re-enter `running` if a human intervenes.

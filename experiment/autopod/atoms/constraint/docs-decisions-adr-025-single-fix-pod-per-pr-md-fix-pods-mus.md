---
kind: constraint
claim: Fix pods must complete after git push without calling approveSession; merge
  ownership belongs exclusively to the parent pod's merge poller, which actively re-attempts
  the merge after a fix pod pushes.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/state-machine.ts
tags:
- fix-pod
- merge
- ownership
- invariant
source: doc-import:docs/decisions/ADR-025-single-fix-pod-per-pr.md
status: active
---
Fix pods must complete after git push without calling approveSession; merge ownership belongs exclusively to the parent pod's merge poller, which actively re-attempts the merge after a fix pod pushes. Previously both the parent's startMergePolling and the fix pod's approveSession path called mergePr, creating ambiguous ownership. Under the new design the parent's poller is the sole merge actor — it watches PR state and calls mergeQueue.enqueueMerge(parent) when the PR becomes mergeable after the fix pod's push. Any call to approveSession from within a fix pod's lifecycle is incorrect and re-introduces the dual-ownership bug.

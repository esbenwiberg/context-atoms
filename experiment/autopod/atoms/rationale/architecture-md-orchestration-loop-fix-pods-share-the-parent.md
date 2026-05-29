---
kind: rationale
claim: Fix pods share the parent pod's branch and track their ancestor chain via `linkedPodId`
  specifically to enable UI drill-down across the fix hierarchy.
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/pod-repository.ts
tags:
- fix-pods
- linkedPodId
- ui
- ancestry
source: doc-import:ARCHITECTURE.md#orchestration-loop
status: active
---
Fix pods share the parent pod's branch and track their ancestor chain via `linkedPodId` specifically to enable UI drill-down across the fix hierarchy. When CI fails after merge, a fix pod is spawned on the same branch so it can push remediation commits without rebasing. The `linkedPodId` foreign key preserves the parent→child relationship so the UI can render a drill-down from the original task through each successive fix pod. Without this link the fix pods would appear as unrelated top-level work items.

---
kind: rationale
claim: "The fleet/batch pattern \u2014 creating N sessions across N repos with the\
  \ same task, monitoring them as a group, and supporting phased rollouts \u2014 is\
  \ the identified missing capability for enterprise-scale migrations."
anchors:
- packages/daemon/src/pods/pod-manager.ts
- packages/daemon/src/pods/pod-queue.ts
- packages/daemon/src/api/routes/pods.ts
- packages/daemon/src/scheduled-jobs/
tags:
- fleet
- batch
- enterprise
- migrations
- gap-analysis
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#11-automation-patterns-triggers-code-review-spec-to-ship-doc
status: active
---
The fleet/batch pattern — creating N sessions across N repos with the same task, monitoring them as a group, and supporting phased rollouts — is the identified missing capability for enterprise-scale migrations. Research notes that autopod handles single-session orchestration well, but enterprise migration use cases (reactive security fixes, strategic cloud migrations, continuous standardization) require: batch session creation across hundreds of repos, a dashboard showing cross-session progress, phased rollout gates (pilot 5 repos → review → scale to 500), and shared profile config enforcing consistent standards across all sessions. These are architectural additions, not incremental feature flags.

---
kind: constraint
claim: "The pricing catalog must be updated manually only \u2014 no auto-fetch, no\
  \ scheduled job, no admin endpoint \u2014 and a model key absent from the catalog\
  \ must log a warning and return $0 rather than throw."
anchors:
- packages/daemon/src/pods/cost-aggregation.ts
tags:
- pricing
- refresh-policy
- error-handling
source: doc-import:docs/decisions/ADR-015-model-pricing-bundled-json.md
status: active
---
The pricing catalog must be updated manually only — no auto-fetch, no scheduled job, no admin endpoint — and a model key absent from the catalog must log a warning and return $0 rather than throw. Manual refresh (edit JSON, rebuild, redeploy) is an explicit commitment, not an oversight; a follow-up ADR is required to change this stance. The $0-with-warning behaviour for unknown models is acceptable because the daemon already requires pod.model to be set on terminal pods (see quality-score-recorder.ts). A unit test should assert every model present in pod.model fixture rows has a pricing entry to surface catalog drift early.

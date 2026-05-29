---
kind: constraint
claim: "The what-if simulator must visibly flag in the UI that its projections use\
  \ a na\xEFve assumption (historical per-model averages applied uniformly, no interaction\
  \ effects)."
anchors:
- packages/daemon/src/api/routes/pods.ts
tags:
- analytics
- what-if
- ui
- models
source: doc-import:docs/analytics-dashboard-plan.md#phase-6-models-leaderboard-what-if
status: active
---
The what-if simulator must visibly flag in the UI that its projections use a naïve assumption (historical per-model averages applied uniformly, no interaction effects). The simulator lets users drag a slider to redirect a % of pods from one model to another and projects the delta in cost/quality/success rate. Because the math assumes each model's historical averages hold independently under the redirect, results will not capture compounding effects, task-type skew, or model-capability mismatch. The UI must surface this caveat — not bury it — so decision-makers understand the confidence level of the projection.

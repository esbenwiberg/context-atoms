---
kind: rationale
claim: Stage 0 Discovery was introduced as an explicit first step because language
  detection, config loading, and diff parsing were previously scattered across later
  stages, creating a sequencing contradiction where Stage 1 (Mechanical Gates) needed
  the language map before Stage 2 (where detection was defined) had run.
anchors:
- src/pr_guardian/discovery/
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/models/context.py
tags:
- orchestration
- stage-ordering
- review-pipeline
source: doc-import:docs/plan/01b-discovery.md
status: active
---
Stage 0 Discovery was introduced as an explicit first step because language detection, config loading, and diff parsing were previously scattered across later stages, creating a sequencing contradiction where Stage 1 (Mechanical Gates) needed the language map before Stage 2 (where detection was defined) had run.

The single output — `ReviewContext` — is built once and consumed by all four downstream stages. Every field is deterministic: no heuristics, no scoring, no decisions. The stage must complete in under 5 seconds with no AI calls.

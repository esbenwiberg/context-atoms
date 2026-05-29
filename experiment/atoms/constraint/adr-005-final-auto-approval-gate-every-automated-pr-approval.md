---
kind: constraint
claim: Every automated PR approval path must pass through the final auto-approval
  gate before any platform side effects (e.g. `approve_pr()`); manual human verdict
  approvals are explicitly exempt.
anchors:
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/decision/engine.py
- src/pr_guardian/decision/actions.py
tags:
- auto-approve
- gate
- invariant
- platform-side-effects
source: doc-import:docs/decisions/ADR-005-final-auto-approval-gate.md
status: active
---
Every automated PR approval path must pass through the final auto-approval gate before any platform side effects (e.g. `approve_pr()`); manual human verdict approvals are explicitly exempt.

Prior to this decision, two re-review branches could reach `Decision.AUTO_APPROVE` without re-running target-branch config consent, hotspot checks, or root config edit policy. The gate evaluates: target-branch config consent, current-path root `review.yml` edits, respected hotspot hits, hotspot lookup failures, and existing structural triggers. Re-review orchestration must carry enough context to run the same gate even when agent work is skipped or minimal.

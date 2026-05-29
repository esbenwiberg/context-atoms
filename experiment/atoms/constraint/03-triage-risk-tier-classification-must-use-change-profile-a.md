---
kind: constraint
claim: Risk tier classification must use change_profile and blast_radius as primary
  signals; line count is only a tiebreaker within the same tier, never the primary
  driver.
anchors:
- src/pr_guardian/triage/classifier.py
- src/pr_guardian/discovery/blast_radius.py
- src/pr_guardian/discovery/change_profile.py
tags:
- triage
- risk-tier
- blast-radius
source: doc-import:docs/plan/03-triage.md
status: active
---
Risk tier classification must use change_profile and blast_radius as primary signals; line count is only a tiebreaker within the same tier, never the primary driver. Rationale: 5 lines adding bypassAuth to middleware is catastrophic; 500 lines of unit tests is near-zero risk. Blast radius propagates security classification transitively — a 3-line change to a shared util imported by auth and payment code must be rated HIGH even if the file itself matches no security-surface pattern. Line count may only inform agent timeouts or context window sizes within an already-established tier.

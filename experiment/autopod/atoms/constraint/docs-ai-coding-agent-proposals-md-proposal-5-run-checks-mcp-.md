---
kind: constraint
claim: Every brief executed under /exec must call run_checks (at minimum lint + typecheck)
  before signaling completion and must fix all failures in its own file surface before
  handing back control.
anchors:
- .claude/skills/prep/SKILL.md
- .agents/skills/prep/SKILL.md
tags:
- exec
- brief
- validation
- non-negotiable
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-5-run-checks-mcp-tool-self-validating-briefs
status: active
---
Every brief executed under /exec must call run_checks (at minimum lint + typecheck) before signaling completion and must fix all failures in its own file surface before handing back control. This is framed as a non-negotiable in the /exec skill text, equivalent in weight to the existing 'always push before handover' rules — not a suggestion. Tiering: lint + typecheck run per brief (fast, cheap, catches ~80% of regressions); full build + test run once at the end of the /exec session, not after every brief. Briefs may opt into heavier checks via their own logic. The rationale mirrors Stripe's finding that 'linting, test execution, pushing should never be left to vibes' — the blueprint walker enforces this at session level; run_checks enforces it at the sub-task level.

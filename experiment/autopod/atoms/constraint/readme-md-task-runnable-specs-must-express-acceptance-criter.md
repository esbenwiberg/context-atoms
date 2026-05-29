---
kind: constraint
claim: "Runnable specs must express acceptance criteria exclusively through contract.yaml\
  \ scenarios, required_facts, and human_review items \u2014 brief frontmatter acceptance_criteria\
  \ and markdown ## Acceptance Criteria sections are no longer accepted."
anchors:
- .agents/skills/prep/SKILL.md
- .claude/skills/prep/SKILL.md
- .agents/skills/plan-feature/SKILL.md
- .claude/skills/plan-feature/SKILL.md
tags:
- spec-format
- contract
- acceptance-criteria
source: doc-import:README.md#task
status: active
---
Runnable specs must express acceptance criteria exclusively through contract.yaml scenarios, required_facts, and human_review items — brief frontmatter acceptance_criteria and markdown ## Acceptance Criteria sections are no longer accepted.

This means any spec folder must contain a contract.yaml at its root. The contract.yaml drives automated proof via required_facts (each with a kind, artifact path, and test command) that map to scenario IDs. Human-gated sign-off goes in the human_review list. Writing acceptance criteria anywhere else (frontmatter or markdown body) will be ignored or rejected by the harness.

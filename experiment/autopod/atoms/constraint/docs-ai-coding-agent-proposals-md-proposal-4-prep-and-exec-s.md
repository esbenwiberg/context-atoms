---
kind: constraint
claim: Brief templates must include a `## Context & Orientation` section that explains
  the relevant codebase to a reader assumed to be a complete beginner with only the
  working tree and the single plan file.
anchors:
- .claude/skills/prep/SKILL.md
- .agents/skills/prep/SKILL.md
- .claude/skills/plan-feature/SKILL.md
- .agents/skills/plan-feature/SKILL.md
tags:
- brief
- prep
- subagent
- orientation
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-4-prep-and-exec-skill-improvements
status: active
---
Brief templates must include a `## Context & Orientation` section that explains the relevant codebase to a reader assumed to be a complete beginner with only the working tree and the single plan file.

This section should cover: key file paths, module purposes, and how relevant parts connect. The constraint exists because executing subagents have no carry-over familiarity with the codebase — every brief is their entire world. Omitting orientation degrades effectiveness on complex briefs touching unfamiliar areas.

The design principle (from OpenAI ExecPlan methodology): "Treat the reader as a complete beginner to the repository who has only the current working tree and the single plan file."

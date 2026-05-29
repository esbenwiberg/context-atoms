---
kind: rationale
claim: progress.md is kept separate from handovers because handovers are forward-looking
  (briefing the next subagent) while progress.md is backward-looking (audit trail
  of what was done), so neither replaces the other.
anchors:
- .claude/skills/prep/SKILL.md
- .agents/skills/prep/SKILL.md
tags:
- exec
- progress
- handover
- audit-trail
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-4-prep-and-exec-skill-improvements
status: active
---
progress.md is kept separate from handovers because handovers are forward-looking (briefing the next subagent) while progress.md is backward-looking (audit trail of what was done), so neither replaces the other.

Handovers remain the mechanism for subagent context transfer. progress.md sits alongside them and is updated after each brief completes with: timestamped checkboxes (`[x] (2026-04-12 14:30Z) Completed step 1`), a Surprises & Discoveries section for unexpected behaviors, and a Decision Log with rationale and date per decision.

The separation is intentional — conflating the two would either bloat handovers with history or strip progress.md of its audit-trail purpose.

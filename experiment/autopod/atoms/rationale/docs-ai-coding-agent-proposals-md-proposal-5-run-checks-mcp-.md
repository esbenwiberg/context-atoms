---
kind: rationale
claim: run_checks gates validation at the brief/sub-task level rather than the harness
  level because /exec dispatches briefs concurrently, leaving no coherent 'between
  briefs' window where the harness could insert a deterministic gate without seeing
  in-flight changes from sibling briefs.
anchors:
- .claude/skills/prep/SKILL.md
- .agents/skills/prep/SKILL.md
tags:
- exec
- concurrency
- validation
- brief
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-5-run-checks-mcp-tool-self-validating-briefs
status: active
---
run_checks gates validation at the brief/sub-task level rather than the harness level because /exec dispatches briefs concurrently, leaving no coherent 'between briefs' window where the harness could insert a deterministic gate without seeing in-flight changes from sibling briefs. A blueprint walker gates between agentic steps in a single session, but a long /exec run is one giant agentic step from the harness perspective. If two briefs call run_checks concurrently and both see the same workspace, failures caused by a sibling brief's in-flight changes would spuriously block completion. The scoped-reporting mitigation: run_checks results include stack and file path of each failure, so a brief's subagent can filter 'errors under files I own' from 'errors caused by a sibling brief' and complete if its own surface is clean. Full workspace isolation per brief (separate worktrees) was explicitly ruled out of scope as a much larger change.

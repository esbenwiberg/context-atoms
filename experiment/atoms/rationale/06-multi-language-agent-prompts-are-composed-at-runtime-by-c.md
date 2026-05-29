---
kind: rationale
claim: "Agent prompts are composed at runtime by concatenating a universal base prompt\
  \ with per-language sections, so adding support for a new language requires only\
  \ new prompt files and config \u2014 no code changes."
anchors:
- src/pr_guardian/agents/prompt_composer.py
- prompts/
tags:
- prompt-engineering
- extensibility
- multi-language
source: doc-import:docs/plan/06-multi-language.md
status: active
---
Agent prompts are composed at runtime by concatenating a universal base prompt with per-language sections, so adding support for a new language requires only new prompt files and config — no code changes.

The composition formula is: AGENT_PROMPT = base.md + Σ(language.md for each language in PR). When a PR spans more than one language a cross-language concerns section is appended automatically.

Alternative considered and rejected: one monolithic prompt per agent that tries to cover all languages. That approach was rejected because it causes prompt bloat on single-language PRs and makes adding a language a code-change-plus-prompt-change rather than prompt-change-only.

New prompt files follow the path pattern `prompts/<agent_type>/<lang>.md`. Missing language files are silently skipped (graceful degradation), so partial language coverage is always valid.

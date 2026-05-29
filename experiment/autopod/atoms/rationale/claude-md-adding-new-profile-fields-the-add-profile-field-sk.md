---
kind: rationale
claim: The /add-profile-field skill exists because profile-field additions have a
  uniquely wide blast radius (11 layers) where each layer can fail independently and
  silently.
anchors:
- .agents/skills/add-profile-field/SKILL.md
- .claude/skills/add-profile-field/SKILL.md
tags:
- profile
- skill
- blast-radius
source: doc-import:CLAUDE.md#adding-new-profile-fields
status: active
---
The /add-profile-field skill exists because profile-field additions have a uniquely wide blast radius (11 layers) where each layer can fail independently and silently.

Rejected alternative: ad-hoc per-PR checklists in PR descriptions. Those rot and are not enforced. The skill centralises verification steps and makes omission visible. The specific risk being guarded against is daemon-validates-but-desktop-cannot-render, a class of bug that does not surface in unit tests scoped to either side alone.

---
kind: rationale
claim: comment_mode tri-state (none/summary/inline) replaced post_comment bool because
  the three posting modes are mutually exclusive, and two separate booleans would
  allow callers to set both true, creating an undefined combined state.
anchors:
- src/pr_guardian/models/pr.py
- src/pr_guardian/persistence/models.py
- src/pr_guardian/api/review.py
tags:
- comment-mode
- api-design
- mutual-exclusion
source: doc-import:docs/decisions/ADR-001-inline-comment-mode-tristate.md
status: active
---
comment_mode tri-state (none/summary/inline) replaced post_comment bool because the three posting modes are mutually exclusive, and two separate booleans would allow callers to set both true, creating an undefined combined state.

The original field was `post_comment: bool = False`. When inline comments were added as a third mode (per-finding inline comments + final summary), this could not be expressed as a boolean alongside a hypothetical `inline_comments: bool` without risking callers passing both as true — an undefined state with no clear resolution.

The chosen type is `comment_mode: Literal["none", "summary", "inline"] = "none"`. The default "none" deliberately matches the previous `False` default so callers that omitted the field retain the same behaviour. The value is persisted as a string column on ReviewRow so re-review operations can inherit the original posting intent without additional logic.

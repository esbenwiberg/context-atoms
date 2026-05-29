"""Format matched atoms into a system-prompt block.

Flat injection: kind-grouped for readability ONLY (rationale then constraint) —
this is presentation, not the kind-*ordering* mechanism the selector would do.
No ranking, no token budgeting. The block is appended to the agent's system
prompt verbatim (`claude -p --append-system-prompt`).
"""
from __future__ import annotations

from .schema import Atom

_HEADER = (
    "# Repository context\n"
    "The following atoms capture intent and constraints relevant to the files "
    "you are likely to touch. They are guidance, not strict spec — use them to "
    "understand *why* things are the way they are.\n"
)


def render(atoms: list[Atom], show_anchors: bool = True) -> str:
    """Render matched atoms as a prompt block.

    show_anchors=False omits the anchor file paths. The experiment uses this so
    arm A receives intent/constraint *content* without a free "edit these files"
    location hint — isolating the intent effect from a file-pointer effect.
    """
    if not atoms:
        return ""
    lines = [_HEADER]
    for kind, label in (("rationale", "Rationale"), ("constraint", "Constraints")):
        group = [a for a in atoms if a.kind == kind]
        if not group:
            continue
        lines.append(f"\n## {label}")
        for a in group:
            lines.append(f"\n- **{a.claim}**")
            body = a.body.strip()
            if body:
                lines.append(f"  {body.splitlines()[0]}")
            if show_anchors:
                lines.append(f"  _(anchors: {', '.join(a.anchor_paths())})_")
    return "\n".join(lines).strip() + "\n"

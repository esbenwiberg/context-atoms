"""Flat anchor-match selector — the ONLY selection logic the experiment uses.

Given the set of changed files for a task, return atoms whose anchors intersect
those files. No tag scoring, no per-link graph traversal, no kind ordering, no
relevance/token-budget ranking. Those are the *mechanism* and are deliberately
NOT built until the bet is proven (docs/design/experiment/plan.md).

This is step 1 of the eventual selector (anchor ∩ envelope.files) and nothing
more.
"""
from __future__ import annotations

import re

from .schema import Atom


def _anchor_to_regex(anchor: str) -> re.Pattern[str]:
    """Translate a path/glob anchor into a full-match regex.

    Supports `**` (any depth, incl. zero segments), `*` (within a segment) and
    `?`. A bare directory path (no wildcard, no extension-looking tail) also
    matches anything beneath it.
    """
    a = anchor.strip().rstrip("/")
    out = []
    i = 0
    while i < len(a):
        c = a[i]
        if c == "*":
            if a[i : i + 2] == "**":
                out.append(".*")
                i += 2
                if a[i : i + 1] == "/":
                    i += 1
                continue
            out.append("[^/]*")
        elif c == "?":
            out.append("[^/]")
        else:
            out.append(re.escape(c))
        i += 1
    # Also allow matching everything beneath a directory-style anchor.
    pattern = "".join(out)
    return re.compile(rf"^{pattern}(/.*)?$")


def select(atoms: list[Atom], changed_files: list[str]) -> list[Atom]:
    """Return atoms with >=1 anchor matching >=1 changed file. Order preserved."""
    files = [f.strip().lstrip("./") for f in changed_files if f.strip()]
    matched: list[Atom] = []
    for atom in atoms:
        if atom.status != "active":
            continue
        patterns = [_anchor_to_regex(a) for a in atom.anchor_paths()]
        if any(p.match(f) for p in patterns for f in files):
            matched.append(atom)
    return matched

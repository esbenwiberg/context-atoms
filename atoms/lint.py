"""Shape lint for atoms — the validator from docs/design/experiment/extractor.md.

Rules (reject = skip, not abort, at extraction time):
  - all required frontmatter fields present and non-empty
  - kind in {rationale, constraint}
  - total file length <= 30 lines (incl. frontmatter)
  - body has at most one H2 heading (multi-fact tell)
  - every anchor resolves to a real path/glob in the target repo (path-only v0)
  - claim is unique within the linted set

`anchor_root` is the repo the anchors point INTO (the pilot repo), which is NOT
the repo the atoms are stored in.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .schema import KINDS, REQUIRED_FIELDS, Atom

MAX_LINES = 30
_H2_RE = re.compile(r"^##\s", re.MULTILINE)


@dataclass
class Finding:
    atom: str  # identifier (path or claim)
    rule: str
    message: str


def _atom_id(a: Atom) -> str:
    return str(a.path) if a.path else (a.claim[:48] or "<unknown>")


def _anchor_resolves(anchor: str, anchor_root: Path) -> bool:
    path = anchor.split("#", 1)[0].strip()
    if not path:
        return False
    # Glob pattern (contains wildcard) -> any match counts.
    if any(ch in path for ch in "*?[]"):
        return any(anchor_root.glob(path))
    return (anchor_root / path).exists()


def lint_atom(a: Atom, anchor_root: Path, total_lines: int | None = None) -> list[Finding]:
    out: list[Finding] = []
    aid = _atom_id(a)

    for f in REQUIRED_FIELDS:
        val = getattr(a, f, None)
        if val in (None, "", []):
            out.append(Finding(aid, "required-field", f"missing/empty field: {f}"))

    if a.kind and a.kind not in KINDS:
        out.append(Finding(aid, "kind", f"kind must be one of {KINDS}, got {a.kind!r}"))

    if total_lines is None:
        total_lines = len(a.to_markdown().splitlines())
    if total_lines > MAX_LINES:
        out.append(Finding(aid, "length", f"{total_lines} lines > {MAX_LINES}"))

    h2_count = len(_H2_RE.findall(a.body))
    if h2_count > 1:
        out.append(Finding(aid, "single-fact", f"{h2_count} H2 headings (expect <=1)"))

    for anchor in a.anchors:
        if not _anchor_resolves(anchor, anchor_root):
            out.append(Finding(aid, "anchor", f"anchor does not resolve: {anchor}"))

    return out


def lint_set(atoms: list[Atom], anchor_root: Path) -> list[Finding]:
    out: list[Finding] = []
    seen: dict[str, str] = {}
    for a in atoms:
        out.extend(lint_atom(a, anchor_root))
        key = a.claim.strip().lower()
        if key and key in seen:
            out.append(Finding(_atom_id(a), "duplicate-claim", f"same claim as {seen[key]}"))
        elif key:
            seen[key] = _atom_id(a)
    return out

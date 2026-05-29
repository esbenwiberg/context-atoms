"""Atom model + frontmatter (de)serialization.

An atom is a small markdown file: YAML frontmatter + short body. One claim per
atom. Fields per docs/design/design.md:

    kind     rationale | constraint            (required)
    claim    one-sentence summary              (required)
    anchors  list of repo paths/globs          (required, >=1)
    tags     closed-vocab-ish list             (optional)
    links    list of atom-id references        (optional; NOT populated at v0)
    source   provenance, e.g. doc-import:ADR-7 (required)
    status   active | superseded | ...         (required, default "active")

Anchors may carry a `#symbol` suffix; at v0 we resolve path-only and ignore the
symbol (open-questions item 2 defers tree-sitter).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

KINDS = ("rationale", "constraint")
REQUIRED_FIELDS = ("kind", "claim", "anchors", "source", "status")

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)


@dataclass
class Atom:
    kind: str
    claim: str
    anchors: list[str]
    source: str
    status: str = "active"
    tags: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    body: str = ""
    path: Path | None = None  # where it lives on disk, if loaded

    # --- anchors -----------------------------------------------------------
    def anchor_paths(self) -> list[str]:
        """Anchor strings with any `#symbol` suffix stripped (path-only v0)."""
        return [a.split("#", 1)[0] for a in self.anchors]

    # --- (de)serialization -------------------------------------------------
    def to_markdown(self) -> str:
        fm: dict[str, Any] = {
            "kind": self.kind,
            "claim": self.claim,
            "anchors": self.anchors,
        }
        if self.tags:
            fm["tags"] = self.tags
        if self.links:
            fm["links"] = self.links
        fm["source"] = self.source
        fm["status"] = self.status
        front = yaml.safe_dump(fm, sort_keys=False, default_flow_style=False).strip()
        body = self.body.strip()
        return f"---\n{front}\n---\n{body}\n"


def parse_atom(text: str, path: Path | None = None) -> Atom:
    """Parse atom markdown into an Atom. Raises ValueError on malformed input."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no YAML frontmatter block found")
    raw_front, body = m.group(1), m.group(2)
    try:
        data = yaml.safe_load(raw_front) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"invalid YAML frontmatter: {e}") from e
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")

    def as_list(v: Any) -> list[str]:
        if v is None:
            return []
        if isinstance(v, str):
            return [v]
        return [str(x) for x in v]

    return Atom(
        kind=str(data.get("kind", "")),
        claim=str(data.get("claim", "")),
        anchors=as_list(data.get("anchors")),
        source=str(data.get("source", "")),
        status=str(data.get("status", "active")),
        tags=as_list(data.get("tags")),
        links=as_list(data.get("links")),
        body=body.strip(),
        path=path,
    )


def load_atoms(root: Path) -> list[Atom]:
    """Load every *.md atom under root (recursively)."""
    atoms: list[Atom] = []
    for p in sorted(Path(root).rglob("*.md")):
        try:
            atoms.append(parse_atom(p.read_text(encoding="utf-8"), path=p))
        except ValueError:
            # Not an atom (no frontmatter) — skip silently; lint reports separately.
            continue
    return atoms

"""Unit tests for the pure-function core: schema roundtrip, lint, select."""
from __future__ import annotations

from pathlib import Path

from atoms.inject import render
from atoms.lint import lint_set
from atoms.schema import Atom, parse_atom
from atoms.select import _anchor_to_regex, select


def _atom(**kw) -> Atom:
    base = dict(
        kind="rationale",
        claim="X is chosen over Y",
        anchors=["src/foo.py"],
        source="doc-import:ADR-1",
        status="active",
    )
    base.update(kw)
    return Atom(**base)


# --- schema ---------------------------------------------------------------
def test_roundtrip():
    a = _atom(tags=["t1"], body="X is chosen over Y because reasons.")
    back = parse_atom(a.to_markdown())
    assert back.kind == a.kind
    assert back.claim == a.claim
    assert back.anchors == a.anchors
    assert back.tags == ["t1"]
    assert "because reasons" in back.body


def test_parse_requires_frontmatter():
    import pytest

    with pytest.raises(ValueError):
        parse_atom("no frontmatter here")


def test_anchor_paths_strip_symbol():
    a = _atom(anchors=["src/foo.py#bar", "pkg/**"])
    assert a.anchor_paths() == ["src/foo.py", "pkg/**"]


# --- anchor matching ------------------------------------------------------
def test_exact_match():
    assert _anchor_to_regex("src/foo.py").match("src/foo.py")
    assert not _anchor_to_regex("src/foo.py").match("src/foo_other.py")


def test_dir_prefix_match():
    r = _anchor_to_regex("src/recovery")
    assert r.match("src/recovery/handler.py")
    assert r.match("src/recovery")
    assert not r.match("src/recovery_utils.py")


def test_globstar_match():
    r = _anchor_to_regex("packages/**/recovery.py")
    assert r.match("packages/a/b/recovery.py")
    assert r.match("packages/recovery.py")
    assert not r.match("packages/a/other.py")


def test_single_star_within_segment():
    r = _anchor_to_regex("src/*.py")
    assert r.match("src/foo.py")
    assert not r.match("src/sub/foo.py")


# --- select ---------------------------------------------------------------
def test_select_matches_intersection():
    atoms = [
        _atom(claim="a", anchors=["src/foo.py"]),
        _atom(claim="b", anchors=["src/bar/**"]),
        _atom(claim="c", anchors=["unrelated/x.py"]),
    ]
    got = select(atoms, ["src/foo.py", "src/bar/deep/x.py"])
    assert {a.claim for a in got} == {"a", "b"}


def test_select_skips_non_active():
    atoms = [_atom(claim="old", anchors=["src/foo.py"], status="superseded")]
    assert select(atoms, ["src/foo.py"]) == []


def test_select_empty_when_no_files():
    atoms = [_atom(anchors=["src/foo.py"])]
    assert select(atoms, []) == []


# --- lint -----------------------------------------------------------------
def test_lint_clean(tmp_path: Path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "foo.py").write_text("x = 1\n")
    findings = lint_set([_atom(body="X is chosen over Y.")], tmp_path)
    assert findings == []


def test_lint_bad_kind(tmp_path: Path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "foo.py").write_text("x\n")
    findings = lint_set([_atom(kind="intent")], tmp_path)
    assert any(f.rule == "kind" for f in findings)


def test_lint_unresolved_anchor(tmp_path: Path):
    findings = lint_set([_atom(anchors=["does/not/exist.py"])], tmp_path)
    assert any(f.rule == "anchor" for f in findings)


def test_lint_duplicate_claim(tmp_path: Path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "foo.py").write_text("x\n")
    findings = lint_set([_atom(claim="same"), _atom(claim="same")], tmp_path)
    assert any(f.rule == "duplicate-claim" for f in findings)


def test_lint_too_long(tmp_path: Path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "foo.py").write_text("x\n")
    findings = lint_set([_atom(body="\n".join(f"line {i}" for i in range(40)))], tmp_path)
    assert any(f.rule == "length" for f in findings)


# --- inject ---------------------------------------------------------------
def test_render_groups_by_kind():
    atoms = [
        _atom(kind="rationale", claim="why-thing", body="why-thing because."),
        _atom(kind="constraint", claim="must-hold", body="must-hold always."),
    ]
    out = render(atoms)
    assert "## Rationale" in out and "## Constraints" in out
    assert "why-thing" in out and "must-hold" in out


def test_render_empty():
    assert render([]) == ""

"""Tool-neutral CLI: init / new / lint / select / inject.

Deliberately small. No selector, no graph, no MCP — see package docstring.
Anchors point INTO a target repo (`--anchor-root`), which may differ from where
atoms are stored (`--atoms-dir`).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from .inject import render
from .lint import lint_set
from .schema import Atom, load_atoms

_TEMPLATE = """\
---
kind: {kind}
claim: ONE-SENTENCE claim goes here
anchors:
  - path/to/file_or_glob
source: human-prep
status: active
---
First sentence restates the claim. Then <=29 more lines of why/what-invariant.
"""


def _changed_files(diff_ref: str, repo: Path) -> list[str]:
    """Files changed vs a git ref (e.g. 'HEAD', 'main', or a SHA range)."""
    args = ["git", "-C", str(repo), "diff", "--name-only", diff_ref]
    out = subprocess.run(args, capture_output=True, text=True, check=True).stdout
    return [l for l in out.splitlines() if l.strip()]


def cmd_init(args: argparse.Namespace) -> int:
    base = Path(args.atoms_dir)
    for sub in ("rationale", "constraint"):
        (base / sub).mkdir(parents=True, exist_ok=True)
    print(f"scaffolded {base}/{{rationale,constraint}}/")
    return 0


def cmd_new(args: argparse.Namespace) -> int:
    base = Path(args.atoms_dir) / args.kind
    base.mkdir(parents=True, exist_ok=True)
    dest = base / f"{args.slug}.md"
    if dest.exists() and not args.force:
        print(f"refusing to overwrite {dest} (use --force)", file=sys.stderr)
        return 1
    dest.write_text(_TEMPLATE.format(kind=args.kind), encoding="utf-8")
    print(f"created {dest}")
    return 0


def cmd_lint(args: argparse.Namespace) -> int:
    atoms = load_atoms(Path(args.atoms_dir))
    findings = lint_set(atoms, Path(args.anchor_root))
    for f in findings:
        print(f"{f.atom}: [{f.rule}] {f.message}")
    print(f"\n{len(atoms)} atoms, {len(findings)} findings", file=sys.stderr)
    return 1 if findings else 0


def _resolve_files(args: argparse.Namespace) -> list[str]:
    if args.files:
        return args.files
    if args.diff:
        return _changed_files(args.diff, Path(args.anchor_root))
    return []


def cmd_select(args: argparse.Namespace) -> int:
    from .select import select

    atoms = load_atoms(Path(args.atoms_dir))
    files = _resolve_files(args)
    matched = select(atoms, files)
    for a in matched:
        print(f"{a.kind}\t{a.path}\t{a.claim}")
    print(f"\n{len(matched)}/{len(atoms)} atoms match {len(files)} files", file=sys.stderr)
    return 0


def cmd_inject(args: argparse.Namespace) -> int:
    from .select import select

    atoms = load_atoms(Path(args.atoms_dir))
    files = _resolve_files(args)
    matched = select(atoms, files)
    sys.stdout.write(render(matched))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="atoms", description="context-atoms v0 CLI")
    p.add_argument("--atoms-dir", default="docs/context", help="where atoms live")
    p.add_argument("--anchor-root", default=".", help="repo the anchors point into")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="scaffold atom dirs").set_defaults(func=cmd_init)

    n = sub.add_parser("new", help="create an atom from template")
    n.add_argument("kind", choices=("rationale", "constraint"))
    n.add_argument("slug")
    n.add_argument("--force", action="store_true")
    n.set_defaults(func=cmd_new)

    sub.add_parser("lint", help="shape-check atoms").set_defaults(func=cmd_lint)

    for name, fn in (("select", cmd_select), ("inject", cmd_inject)):
        s = sub.add_parser(name, help=f"{name} atoms by changed files")
        s.add_argument("--files", nargs="*", help="explicit changed file paths")
        s.add_argument("--diff", help="git ref to diff against (e.g. HEAD, main)")
        s.set_defaults(func=fn)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

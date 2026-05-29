"""Stage 1 — doc-import atom extractor.

Walk the pilot repo's docs, ask Sonnet (via `claude -p`) for 0-3 atoms per
source, validate shape + anchor resolution, write survivors to the atoms dir.
No hand-authoring. No links graph. Path-only anchors. See
docs/design/experiment/extractor.md.

Run:  python -m experiment.extract --repo ~/repos/pr-guardian --out experiment/atoms
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from atoms.lint import lint_atom  # noqa: E402
from atoms.schema import Atom  # noqa: E402
from experiment.claude_cli import extract_json_block, text_call  # noqa: E402

# Source priority (docs/design/experiment/extractor.md). Globs relative to repo.
SOURCE_GLOBS = [
    "docs/decisions/*.md",
    "docs/adr/*.md",
    "ARCHITECTURE.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "README.md",
    "docs/plan/*.md",
    "docs/*.md",
]

PROMPT = """\
You are extracting atomic context for AI coding agents from a source document.

Propose 0-3 atoms. Return a STRICT JSON array (no prose, no markdown fences).
Each atom is an object:
  {{"kind": "rationale"|"constraint",
    "claim": "<one sentence>",
    "anchors": ["<repo-relative path or glob>", ...],
    "tags": ["<short>", ...],
    "body": "<<=25 lines; first sentence restates the claim>"}}

Each atom MUST:
- State ONE claim. kind=rationale (why a thing exists / was chosen, incl. rejected
  alternatives) OR kind=constraint (an invariant the code must maintain).
- Use anchors chosen ONLY from the repo file list below. Pick the files/dirs the
  claim is actually about. Use a directory or glob if it spans many files.
- Be concrete and recoverable-from-docs, NOT from code.

Return [] (empty array) if the source is purely procedural (how to run X),
status/progress, or trivially recoverable by grepping the code.

=== REPO FILE LIST (anchors MUST come from here) ===
{filelist}

=== SOURCE: {source_path} ===
{source_text}
"""


def repo_file_list(repo: Path, limit: int = 600) -> str:
    out = subprocess.run(
        ["git", "-C", str(repo), "ls-files"], capture_output=True, text=True
    ).stdout
    files = [f for f in out.splitlines() if f and not f.startswith("docs/")]
    # Bias toward source dirs to keep the list focused and within token budget.
    files.sort(key=lambda f: (not f.startswith(("src/", "alembic/")), f))
    return "\n".join(files[:limit])


def gather_sources(repo: Path) -> list[Path]:
    seen: dict[Path, None] = {}
    for g in SOURCE_GLOBS:
        for p in sorted(repo.glob(g)):
            if p.is_file() and p not in seen:
                seen[p] = None
    return list(seen)


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60] or "atom"


def chunks_for(source: Path, repo: Path, max_lines: int = 220) -> list[tuple[str, str]]:
    """Yield (label, text) chunks. Large docs are split on H2 headers so few-but-big
    files (common in OSS repos) produce proportionally more extraction calls."""
    rel = str(source.relative_to(repo))
    text = source.read_text(encoding="utf-8", errors="replace")
    if len(text.splitlines()) <= max_lines:
        return [(rel, text[:12000])]
    # split on H2 boundaries, keeping the header with its section
    parts = re.split(r"(?m)^(?=##\s)", text)
    chunks: list[tuple[str, str]] = []
    for part in parts:
        part = part.strip()
        if len(part) < 80:  # skip tiny preambles/sections
            continue
        m = re.match(r"##\s+(.+)", part)
        label = f"{rel}#{slugify(m.group(1))}" if m else rel
        chunks.append((label, part[:12000]))
    return chunks or [(rel, text[:12000])]


def extract_text(label: str, text: str, filelist: str, model: str) -> tuple[list[dict], float]:
    prompt = PROMPT.format(filelist=filelist, source_path=label, source_text=text)
    res = text_call(prompt, model=model)
    if res.is_error:
        print(f"  ! claude error on {label}: {res.raw}", file=sys.stderr)
        return [], res.cost_usd
    try:
        data = extract_json_block(res.text)
    except ValueError:
        print(f"  ! unparseable response on {label}", file=sys.stderr)
        return [], res.cost_usd
    if not isinstance(data, list):
        return [], res.cost_usd
    return data, res.cost_usd


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--limit-sources", type=int, default=0, help="0 = all")
    args = ap.parse_args(argv)

    repo = args.repo.expanduser().resolve()
    out = args.out.resolve()
    for sub in ("rationale", "constraint"):
        (out / sub).mkdir(parents=True, exist_ok=True)

    filelist = repo_file_list(repo)
    sources = gather_sources(repo)
    if args.limit_sources:
        sources = sources[: args.limit_sources]
    chunks: list[tuple[str, str]] = []
    for src in sources:
        chunks.extend(chunks_for(src, repo))
    print(f"sources: {len(sources)} -> {len(chunks)} chunks  repo: {repo}", file=sys.stderr)

    kept = 0
    rejected = 0
    seen_claims: set[str] = set()
    total_cost = 0.0
    manifest = []

    for rel, text in chunks:
        raw_atoms, cost = extract_text(rel, text, filelist, args.model)
        total_cost += cost
        print(f"[{rel}] -> {len(raw_atoms)} proposed (${total_cost:.3f} cum)", file=sys.stderr)
        for i, ra in enumerate(raw_atoms):
            try:
                atom = Atom(
                    kind=str(ra.get("kind", "")),
                    claim=str(ra.get("claim", "")).strip(),
                    anchors=[str(a) for a in (ra.get("anchors") or [])],
                    tags=[str(t) for t in (ra.get("tags") or [])],
                    source=f"doc-import:{rel}",
                    status="active",
                    body=str(ra.get("body", "")).strip(),
                )
            except Exception as e:  # noqa: BLE001
                print(f"    skip (construct): {e}", file=sys.stderr)
                rejected += 1
                continue
            ckey = atom.claim.lower()
            if ckey in seen_claims:
                rejected += 1
                continue
            findings = lint_atom(atom, repo)
            if findings:
                rejected += 1
                print(f"    reject {atom.claim[:40]!r}: "
                      + "; ".join(f.message for f in findings), file=sys.stderr)
                continue
            seen_claims.add(ckey)
            dest = out / atom.kind / f"{slugify(rel + '-' + atom.claim)}.md"
            dest.write_text(atom.to_markdown(), encoding="utf-8")
            manifest.append({"file": str(dest.relative_to(out)), "source": str(rel),
                             "kind": atom.kind, "claim": atom.claim})
            kept += 1

    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nKEPT {kept}  REJECTED {rejected}  COST ${total_cost:.3f}", file=sys.stderr)
    if kept < 15:
        print(f"\n*** STAGE-1 KILL: only {kept} atoms (<15). Pilot too doc-sparse "
              f"OR extractor too strict. ***", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Shared git-worktree + pytest plumbing for Stages 2 and 3.

Everything runs in isolated `git worktree` checkouts so the pilot repo's real
working tree is never touched. Tests run with PYTHONPATH pointed at the
worktree's src so the *checked-out* source wins over any editable install in the
shared venv.
"""
from __future__ import annotations

import os
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path

BENCH_ROOT = Path("/tmp/ca-bench")


def git(repo: Path, *args: str, check: bool = True) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


@dataclass
class Worktree:
    path: Path
    repo: Path

    def __enter__(self) -> "Worktree":
        return self

    def __exit__(self, *exc) -> None:
        self.remove()

    def remove(self) -> None:
        subprocess.run(
            ["git", "-C", str(self.repo), "worktree", "remove", str(self.path), "--force"],
            capture_output=True, text=True,
        )


def add_worktree(repo: Path, sha: str, label: str = "") -> Worktree:
    BENCH_ROOT.mkdir(parents=True, exist_ok=True)
    name = f"{label}-{uuid.uuid4().hex[:8]}" if label else uuid.uuid4().hex[:8]
    path = BENCH_ROOT / name
    git(repo, "worktree", "add", "-q", "--detach", str(path), sha)
    return Worktree(path=path, repo=repo)


def checkout_paths_from(wt: Worktree, sha: str, paths: list[str]) -> None:
    """Bring specific paths from another commit into the worktree (e.g. the PR's tests)."""
    if paths:
        subprocess.run(
            ["git", "-C", str(wt.path), "checkout", sha, "--", *paths],
            capture_output=True, text=True, check=False,
        )


@dataclass
class PytestResult:
    passed: bool          # True iff exit code 0 (all selected tests passed)
    returncode: int
    n_passed: int
    n_failed: int
    n_error: int
    stdout: str


def prepare_worktree(wt: Worktree, files: dict[str, str]) -> None:
    """Synthesize files into a fresh worktree (e.g. a version stub)."""
    for rel, content in (files or {}).items():
        dest = wt.path / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")


def run_pytest(wt: Worktree, venv_python: Path, test_targets: list[str],
               timeout: int = 300, pythonpath: Path | None = None) -> PytestResult:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(pythonpath if pythonpath is not None else wt.path / "src")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    args = [str(venv_python), "-m", "pytest", "-q", "-p", "no:cacheprovider", *test_targets]
    try:
        r = subprocess.run(args, cwd=str(wt.path), env=env, capture_output=True,
                           text=True, timeout=timeout)
        out = r.stdout + "\n" + r.stderr
        rc = r.returncode
    except subprocess.TimeoutExpired:
        return PytestResult(False, -9, 0, 0, 0, "TIMEOUT")
    return PytestResult(
        passed=(rc == 0),
        returncode=rc,
        n_passed=_count(out, "passed"),
        n_failed=_count(out, "failed"),
        n_error=_count(out, "error"),
        stdout=out[-4000:],
    )


_ANSI = None


def _count(summary: str, word: str) -> int:
    import re
    global _ANSI
    if _ANSI is None:
        _ANSI = re.compile(r"\x1b\[[0-9;]*m")
    clean = _ANSI.sub("", summary)
    # match singular or plural (passed, failed, error/errors) anywhere
    m = re.findall(rf"(\d+) {word}s?\b", clean)
    return int(m[-1]) if m else 0

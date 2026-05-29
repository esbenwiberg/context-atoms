"""Per-repo profiles so the harness is genuinely repo-agnostic.

A profile captures everything repo-specific the stages need: where source vs test
files live, how to put the checked-out source on the import path, which venv runs
the tests, and any files that must be synthesized into each worktree (e.g. a
setuptools_scm version stub that only exists after install).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Profile:
    name: str
    repo: Path
    venv_python: Path
    src_prefixes: tuple[str, ...]
    test_prefixes: tuple[str, ...]
    pythonpath_subdir: str  # relative to the worktree; "src" or "." etc.
    prepare_files: dict[str, str] = field(default_factory=dict)

    def is_src(self, path: str) -> bool:
        return path.endswith(".py") and path.startswith(self.src_prefixes)

    def is_test(self, path: str) -> bool:
        return path.endswith(".py") and (
            path.startswith(self.test_prefixes) or Path(path).name.startswith("test")
        )

    def pythonpath(self, worktree: Path) -> Path:
        return (worktree / self.pythonpath_subdir).resolve()


_HOME = Path("~").expanduser()

PROFILES: dict[str, Profile] = {
    "pr-guardian": Profile(
        name="pr-guardian",
        repo=_HOME / "repos/pr-guardian",
        venv_python=_HOME / "repos/pr-guardian/.venv/bin/python",
        src_prefixes=("src/",),
        test_prefixes=("tests/",),
        pythonpath_subdir="src",
    ),
    "sqlglot": Profile(
        name="sqlglot",
        repo=_HOME / "repos/sqlglot",
        venv_python=_HOME / "repos/sqlglot/.venv/bin/python",
        src_prefixes=("sqlglot/",),
        test_prefixes=("tests/",),
        pythonpath_subdir=".",
        prepare_files={
            "sqlglot/_version.py": '__version__ = "0.0.0"\n__version_tuple__ = (0, 0, 0)\n',
        },
    ),
}


def get(name: str) -> Profile:
    if name not in PROFILES:
        raise SystemExit(f"unknown profile {name!r}; have {list(PROFILES)}")
    return PROFILES[name]

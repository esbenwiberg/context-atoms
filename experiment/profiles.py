"""Per-repo profiles so the harness is genuinely repo-AND-language-agnostic.

A profile captures everything repo-specific the stages need: how to tell source
from test files, which test runner to invoke and how, how to put the checked-out
code on the import/resolution path, and any files/symlinks that must be
synthesized into each isolated worktree (a setuptools_scm version stub for
Python; a node_modules symlink for node so we skip a per-run `npm ci`).

Two runners supported: pytest (Python) and vitest (node/TS). Pass/fail is the
test command's exit code in both cases.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fnmatch import fnmatch
from pathlib import Path


@dataclass
class Profile:
    name: str
    repo: Path
    runner: str  # "pytest" | "vitest"
    src_prefixes: tuple[str, ...]
    src_exts: tuple[str, ...]
    test_prefixes: tuple[str, ...] = ()
    test_globs: tuple[str, ...] = ()  # basename fnmatch patterns, e.g. "*.spec.ts"
    # pytest
    venv_python: Path | None = None
    pythonpath_subdir: str = "src"
    # worktree prep
    prepare_files: dict[str, str] = field(default_factory=dict)
    prepare_symlinks: dict[str, Path] = field(default_factory=dict)  # wt-rel -> abs target

    # --- file classification ---------------------------------------------
    def is_test(self, path: str) -> bool:
        name = Path(path).name
        if self.test_globs and any(fnmatch(name, g) for g in self.test_globs):
            return True
        if self.test_prefixes and path.startswith(self.test_prefixes):
            return path.endswith(self.src_exts)
        return False

    def is_src(self, path: str) -> bool:
        return (
            path.endswith(self.src_exts)
            and path.startswith(self.src_prefixes)
            and not self.is_test(path)
        )

    # --- execution -------------------------------------------------------
    def test_argv(self, worktree: Path, targets: list[str]) -> list[str]:
        if self.runner == "pytest":
            return [str(self.venv_python), "-m", "pytest", "-q",
                    "-p", "no:cacheprovider", *targets]
        if self.runner == "vitest":
            return [str(worktree / "node_modules/.bin/vitest"), "run", *targets]
        raise ValueError(f"unknown runner {self.runner!r}")

    def test_env_pythonpath(self, worktree: Path) -> Path | None:
        if self.runner == "pytest":
            return (worktree / self.pythonpath_subdir).resolve()
        return None

    def test_cmd_str(self, test_files: list[str]) -> str:
        """Human-runnable command string for the agent prompt."""
        files = " ".join(test_files)
        if self.runner == "pytest":
            return f"PYTHONPATH={self.pythonpath_subdir} {self.venv_python} -m pytest {files} -q"
        return f"npx vitest run {files}"


_HOME = Path("~").expanduser()

PROFILES: dict[str, Profile] = {
    "pr-guardian": Profile(
        name="pr-guardian",
        repo=_HOME / "repos/pr-guardian",
        runner="pytest",
        src_prefixes=("src/",),
        src_exts=(".py",),
        test_prefixes=("tests/",),
        test_globs=("test_*.py",),
        venv_python=_HOME / "repos/pr-guardian/.venv/bin/python",
        pythonpath_subdir="src",
    ),
    "sqlglot": Profile(
        name="sqlglot",
        repo=_HOME / "repos/sqlglot",
        runner="pytest",
        src_prefixes=("sqlglot/",),
        src_exts=(".py",),
        test_prefixes=("tests/",),
        test_globs=("test_*.py",),
        venv_python=_HOME / "repos/sqlglot/.venv/bin/python",
        pythonpath_subdir=".",
        prepare_files={
            "sqlglot/_version.py": '__version__ = "0.0.0"\n__version_tuple__ = (0, 0, 0)\n',
        },
    ),
    "portfolio-simulation": Profile(
        name="portfolio-simulation",
        repo=_HOME / "repos/portfolio-simulation",
        runner="vitest",
        src_prefixes=("src/",),
        src_exts=(".ts", ".tsx"),
        test_prefixes=("tests/",),
        test_globs=("*.spec.ts", "*.test.ts", "*.spec.tsx", "*.test.tsx"),
        prepare_symlinks={
            "node_modules": _HOME / "repos/portfolio-simulation/node_modules",
        },
    ),
}


def get(name: str) -> Profile:
    if name not in PROFILES:
        raise SystemExit(f"unknown profile {name!r}; have {list(PROFILES)}")
    return PROFILES[name]

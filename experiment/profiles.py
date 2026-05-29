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
    # monorepo: run the test command from this subdir (vitest); targets are
    # relativized to it. "" = repo root.
    package_dir: str = ""
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
    def test_cwd(self, worktree: Path) -> Path:
        return worktree / self.package_dir if self.package_dir else worktree

    def _rel_targets(self, targets: list[str]) -> list[str]:
        """Strip the package_dir prefix so targets are relative to the runner cwd."""
        if not self.package_dir:
            return targets
        pref = self.package_dir.rstrip("/") + "/"
        return [t[len(pref):] if t.startswith(pref) else t for t in targets]

    def test_argv(self, worktree: Path, targets: list[str]) -> list[str]:
        if self.runner == "pytest":
            return [str(self.venv_python), "-m", "pytest", "-q",
                    "-p", "no:cacheprovider", *targets]
        if self.runner == "vitest":
            vitest = self.test_cwd(worktree) / "node_modules/.bin/vitest"
            return [str(vitest), "run", *self._rel_targets(targets)]
        raise ValueError(f"unknown runner {self.runner!r}")

    def test_env_pythonpath(self, worktree: Path) -> Path | None:
        if self.runner == "pytest":
            return (worktree / self.pythonpath_subdir).resolve()
        return None

    def test_cmd_str(self, test_files: list[str]) -> str:
        """Human-runnable command string for the agent prompt."""
        if self.runner == "pytest":
            files = " ".join(test_files)
            return f"PYTHONPATH={self.pythonpath_subdir} {self.venv_python} -m pytest {files} -q"
        files = " ".join(self._rel_targets(test_files))
        prefix = f"cd {self.package_dir} && " if self.package_dir else ""
        return f"{prefix}npx vitest run {files}"


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
    "autopod-daemon": Profile(
        name="autopod-daemon",
        repo=_HOME / "repos/autopod",
        runner="vitest",
        package_dir="packages/daemon",
        src_prefixes=("packages/daemon/src/",),
        src_exts=(".ts", ".tsx"),
        test_globs=("*.test.ts", "*.test.tsx"),  # colocated in src/ -> glob only
        prepare_symlinks={
            "node_modules": _HOME / "repos/autopod/node_modules",
            "packages/daemon/node_modules": _HOME / "repos/autopod/packages/daemon/node_modules",
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

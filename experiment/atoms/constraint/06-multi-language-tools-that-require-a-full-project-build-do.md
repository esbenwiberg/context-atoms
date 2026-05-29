---
kind: constraint
claim: "Tools that require a full project build (dotnet build, tsc --noEmit) must\
  \ NOT be invoked in-process by the mechanical runner \u2014 Guardian consumes those\
  \ results from the repo's own CI pipeline via platform API status checks."
anchors:
- src/pr_guardian/mechanical/runner.py
- src/pr_guardian/platform/protocol.py
tags:
- mechanical
- ci-integration
- tool-dispatch
source: doc-import:docs/plan/06-multi-language.md
status: active
---
Tools that require a full project build (dotnet build, tsc --noEmit) must NOT be invoked in-process by the mechanical runner — Guardian consumes those results from the repo's own CI pipeline via platform API status checks.

Only tools that can operate on individual files or a cloned repo without a full build toolchain may run in-process. The distinction is: if a tool needs the project's dependency graph resolved (e.g. NuGet restore, node_modules), it belongs in CI. If it can lint/scan source files directly (semgrep, ruff, gitleaks, shellcheck), it runs in-process.

This keeps Guardian's container image lean and avoids per-language SDK installation sprawl. Adding a new in-process tool must satisfy this constraint — if it needs a build step, it must be wired as a CI status check consumer instead.

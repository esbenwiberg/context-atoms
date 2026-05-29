---
kind: constraint
claim: The `shared` package must maintain zero heavy runtime dependencies because
  every other package in the monorepo depends on it.
anchors:
- package.json
tags:
- shared
- dependencies
- architecture
source: doc-import:CLAUDE.md#architecture
status: active
---
The `shared` package must maintain zero heavy runtime dependencies because every other package in the monorepo depends on it. Its purpose is limited to types, errors, constants, and sanitization. Introducing a heavy dep here (e.g. a database driver, HTTP framework, or SDK) would force that transitive cost onto all consumers including the CLI and escalation-mcp.

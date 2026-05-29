---
kind: constraint
claim: '`@autopod/shared` must carry zero heavy dependencies because it is imported
  by every other package (daemon, cli, validator, escalation-mcp).'
anchors:
- .dependency-cruiser.cjs
tags:
- shared
- dependencies
- architecture
source: doc-import:ARCHITECTURE.md#packages
status: active
---
`@autopod/shared` must carry zero heavy dependencies because it is imported by every other package (daemon, cli, validator, escalation-mcp).

Adding a heavy transitive dep to shared bloats every downstream consumer. The package's role is limited to: shared TypeScript types, error classes, constants, and PII/injection sanitization utilities. Anything requiring a heavy runtime (DB drivers, HTTP clients, AI SDKs) belongs in the package that actually uses it, not in shared.

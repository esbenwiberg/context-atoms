---
kind: constraint
claim: Changes to the `pum_portfoliosimulationprofile` Dataverse schema or admin-profiles
  UX must be preceded by reading `specs/admin-managed-profiles/` and ADR 0008.
anchors:
- specs/admin-managed-profiles/design.md
- specs/admin-managed-profiles/purpose.md
- specs/admin-managed-profiles/briefs/01-profile-schema-and-default-seed/brief.md
tags:
- dataverse
- admin-profiles
- schema
- adr
source: doc-import:CLAUDE.md#where-context-lives
status: active
---
Changes to the `pum_portfoliosimulationprofile` Dataverse schema or admin-profiles UX must be preceded by reading `specs/admin-managed-profiles/` and ADR 0008. The admin-managed profiles surface has a dedicated spec folder (purpose, design, pod briefs, handovers) and is tied to a named ADR that records the load-bearing architectural decision. Evolving the schema or UX without that context risks breaking invariants already encoded in the solution scaffold and adapter layer.

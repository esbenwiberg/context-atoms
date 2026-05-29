---
kind: rationale
claim: Profile configuration is stored in a Dataverse table (`pum_portfoliosimulationprofile`)
  rather than environment variables, browser localStorage, PCF control config, or
  an in-app JSON editor because those alternatives are either banned by prior ADRs
  (ADR 0001 bans PCF, ADR 0003 bans browser persistence) or too confusing for the
  admin audience.
anchors:
- src/adapters/profileConfig.ts
- src/adapters/dataverse/index.ts
- solution/src/Other/Customizations.xml
tags:
- profiles
- dataverse
- architecture
- adr
source: doc-import:docs/adr/0008-admin-managed-profiles.md
status: active
---
Profile configuration is stored in a Dataverse table (`pum_portfoliosimulationprofile`) rather than environment variables, browser localStorage, PCF control config, or an in-app JSON editor because those alternatives are either banned by prior ADRs (ADR 0001 bans PCF, ADR 0003 bans browser persistence) or too confusing for the admin audience.

The table has four columns: `pum_name` (display name), `pum_key` (stable key for Web Resource placement), `pum_isdefault` (bit flag), and `pum_configjson` (JSON payload).

The managed solution seeds a single default profile row (`pum_key = "default"`, `pum_isdefault = true`) so the app works out of the box without any post-install admin setup. Multiple placements can bind to different profiles via `pum_key`.

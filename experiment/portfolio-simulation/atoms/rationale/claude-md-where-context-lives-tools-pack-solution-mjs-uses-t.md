---
kind: rationale
claim: '`tools/pack-solution.mjs` uses the system `zip` command instead of the Dataverse
  `pac` CLI to build the managed and unmanaged solution ZIPs.'
anchors:
- tools/pack-solution.mjs
tags:
- build
- dataverse
- pac
- zip
- tooling
source: doc-import:CLAUDE.md#where-context-lives
status: active
---
`tools/pack-solution.mjs` uses the system `zip` command instead of the Dataverse `pac` CLI to build the managed and unmanaged solution ZIPs. The pac CLI is a heavyweight Dataverse-specific dependency that would require separate installation in CI and contributor environments. Using the ubiquitous system `zip` keeps the build self-contained with no extra toolchain. The solution scaffold lives in `solution/src/` and the packed ZIPs are what the release workflow publishes.

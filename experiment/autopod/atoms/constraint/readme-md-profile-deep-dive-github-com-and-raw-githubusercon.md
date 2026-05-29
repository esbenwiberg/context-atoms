---
kind: constraint
claim: github.com and raw.githubusercontent.com must NOT be included in the built-in
  default network allowlist; profiles that require direct GitHub egress must add them
  explicitly.
anchors:
- packages/daemon/src/pods/runtime-network-defaults.ts
tags:
- network-policy
- allowlist
- github
source: doc-import:README.md#profile-deep-dive
status: active
---
github.com and raw.githubusercontent.com must NOT be included in the built-in default network allowlist; profiles that require direct GitHub egress must add them explicitly. The default list includes api.anthropic.com, api.openai.com, registry.npmjs.org, pypi.org, NuGet hosts, Azure CDN hosts, pkgs.dev.azure.com, platform.claude.com, and GitHub Copilot endpoints. The omission of github.com is intentional: only profiles whose dependencies are fetched directly from GitHub should open that route, keeping the default surface minimal.

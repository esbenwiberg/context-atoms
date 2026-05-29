---
kind: rationale
claim: '"Allow public client flows" is enabled on the Entra ID app registration to
  support device code flow for headless/server machine authentication.'
anchors:
- packages/cli/src/auth/msal-client.ts
- packages/cli/src/commands/auth.ts
tags:
- auth
- azure
- device-code
- headless
source: doc-import:README.md#auth-setup
status: active
---
"Allow public client flows" is enabled on the Entra ID app registration to support device code flow for headless/server machine authentication. Without this setting, the device code grant is blocked by Entra ID regardless of the MSAL client configuration. This enables autopod to authenticate on machines that have no browser (CI runners, remote servers) by displaying a code the user enters on a separate device.

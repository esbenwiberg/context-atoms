---
kind: constraint
claim: AES-256 credential encryption uses a key file stored at ~/.autopod/secrets.key,
  outside the repo and database.
anchors:
- packages/daemon/src/crypto/credentials-cipher.ts
tags:
- security
- credentials
- encryption
- key-management
source: doc-import:CLAUDE.md#security-architecture
status: active
---
AES-256 credential encryption uses a key file stored at ~/.autopod/secrets.key, outside the repo and database. The key must never be committed, embedded in config, or stored in the daemon database. Any credential-handling code must read the key exclusively from this path.

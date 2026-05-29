---
kind: rationale
claim: HAProxy is used as an SNI proxy that validates the TLS ClientHello SNI against
  an allowlist and splices raw bytes through without MITM decryption, deliberately
  avoiding full TLS inspection.
anchors:
- packages/daemon/src/containers/haproxy-config.ts
- packages/daemon/src/containers/haproxy-deny-stream.ts
- packages/daemon/src/containers/haproxy-deny-parser.ts
tags:
- network-policy
- security
- tls
- haproxy
source: doc-import:ARCHITECTURE.md#container-security-model
status: active
---
HAProxy is used as an SNI proxy that validates the TLS ClientHello SNI against an allowlist and splices raw bytes through without MITM decryption, deliberately avoiding full TLS inspection. In restricted mode, container egress is routed via iptables NAT to HAProxy on loopback port 8443. HAProxy reads the SNI hostname from the TLS ClientHello, checks it against the allowlist, and either splices the raw TCP stream through or drops the connection — it never terminates TLS. This design was chosen over a full TLS-intercepting proxy because it avoids certificate trust issues inside containers, has no key material to leak, and is simpler to audit. Denials are logged as safety events.

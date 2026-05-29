---
kind: rationale
claim: Restricted network mode uses HAProxy as a pass-through SNI proxy rather than
  a TLS-terminating MITM so that HTTPS egress can be filtered at the hostname level
  without breaking TLS or substituting certificates.
anchors:
- packages/daemon/src/containers/haproxy-config.ts
- packages/daemon/src/containers/haproxy-deny-stream.ts
- packages/daemon/src/containers/haproxy-deny-parser.ts
tags:
- network-policy
- haproxy
- tls
- security
source: doc-import:README.md#profile-deep-dive
status: active
---
Restricted network mode uses HAProxy as a pass-through SNI proxy rather than a TLS-terminating MITM so that HTTPS egress can be filtered at the hostname level without breaking TLS or substituting certificates. iptables NAT redirects outbound port 443 to an HAProxy instance on loopback; HAProxy reads the TLS ClientHello SNI field, checks it against the allowlist, and splices raw TLS bytes through to the real host. Rejected connections are logged and counted as safety events. Port 80 follows the same pattern. DNS (UDP/TCP 53) is always permitted in all modes. Alternatives that terminate and re-encrypt TLS were ruled out because they require injecting a custom CA into containers, which breaks certificate pinning and adds operational complexity.

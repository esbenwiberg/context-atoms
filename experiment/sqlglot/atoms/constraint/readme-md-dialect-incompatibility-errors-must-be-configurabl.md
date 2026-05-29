---
kind: constraint
claim: Dialect incompatibility errors must be configurable to either warn or raise,
  not hard-fail unconditionally.
anchors:
- sqlglot/dialects/dialect.py
- sqlglot/errors.py
tags:
- errors
- dialects
- configuration
source: doc-import:README.md
status: active
---
Dialect incompatibility errors must be configurable to either warn or raise, not hard-fail unconditionally. The README documents this as an explicit feature: 'dialect incompatibilities can warn or raise depending on configurations'. This allows best-effort transpilation (warnings) for pipelines that need resilience, and strict validation (raise) for tooling that requires correctness. Any new dialect-specific error path must respect this configurable behaviour rather than unconditionally raising.

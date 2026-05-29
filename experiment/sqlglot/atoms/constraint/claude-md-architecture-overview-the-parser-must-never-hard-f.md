---
kind: constraint
claim: The parser must never hard-fail on unparseable SQL; instead it falls back to
  an `exp.Command` node that preserves the original SQL text verbatim.
anchors:
- sqlglot/parser.py
- sqlglot/parsers/base.py
- sqlglot/expressions/core.py
tags:
- parser
- error-handling
- exp.Command
- graceful-degradation
source: doc-import:CLAUDE.md#architecture-overview
status: active
---
The parser must never hard-fail on unparseable SQL; instead it falls back to an `exp.Command` node that preserves the original SQL text verbatim. This is a deliberate resilience invariant: callers that round-trip SQL through parse→generate rely on lossless preservation of statements the parser does not understand. Breaking this fallback — e.g. by raising instead of emitting `exp.Command` — would silently drop SQL clauses for any dialect or vendor extension not yet modelled in the AST.

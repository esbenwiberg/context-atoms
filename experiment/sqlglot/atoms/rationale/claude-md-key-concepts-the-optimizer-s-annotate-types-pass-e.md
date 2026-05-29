---
kind: rationale
claim: The optimizer's `annotate_types` pass exists because certain transpilations
  (e.g., whether `+` means numeric addition or string concatenation) cannot be resolved
  from syntax alone and require propagated type information.
anchors:
- sqlglot/optimizer/annotate_types.py
- sqlglot/schema.py
tags:
- types
- optimizer
- transpilation
- schema
source: doc-import:CLAUDE.md#key-concepts
status: active
---
The optimizer's `annotate_types` pass exists because certain transpilations (e.g., whether `+` means numeric addition or string concatenation) cannot be resolved from syntax alone and require propagated type information. The pass walks the AST and annotates each expression node with its inferred data type, drawing on schema information when available. Without schema information the pass operates on a best-effort basis. Downstream generator logic consults these annotations to emit the correct dialect-specific operator or function.

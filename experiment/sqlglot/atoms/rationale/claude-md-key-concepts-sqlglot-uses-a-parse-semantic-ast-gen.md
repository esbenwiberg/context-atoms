---
kind: rationale
claim: "SQLGlot uses a parse\u2192semantic-AST\u2192generate pipeline (rather than\
  \ text-to-text transformation) because preserving semantics\u2014not syntax\u2014\
  is what makes accurate cross-dialect transpilation possible."
anchors:
- sqlglot/parser.py
- sqlglot/generator.py
- sqlglot/expressions/core.py
- posts/ast_primer.md
tags:
- architecture
- ast
- transpilation
- design
source: doc-import:CLAUDE.md#key-concepts
status: active
---
SQLGlot uses a parse→semantic-AST→generate pipeline (rather than text-to-text transformation) because preserving semantics—not syntax—is what makes accurate cross-dialect transpilation possible. The AST is a dialect-neutral semantic representation; the generator then serialises it into whatever target dialect is requested. Comments are preserved on a best-effort basis only, since they are not semantic. This design means callers should never expect round-trip syntactic identity—only semantic equivalence.

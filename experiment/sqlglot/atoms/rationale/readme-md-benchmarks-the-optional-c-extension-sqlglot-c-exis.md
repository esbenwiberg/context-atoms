---
kind: rationale
claim: The optional C extension (`sqlglot[c]`) exists to close the ~4x performance
  gap between pure-Python sqlglot and Rust-based parsers, achieving near-Rust parse
  speeds while keeping a Python-native codebase.
anchors:
- sqlglot/tokenizer_core.py
- sqlglotc/pyproject.toml
- benchmarks/parse.py
tags:
- performance
- c-extension
- benchmarks
source: doc-import:README.md#benchmarks
status: active
---
The optional C extension (`sqlglot[c]`) exists to close the ~4x performance gap between pure-Python sqlglot and Rust-based parsers, achieving near-Rust parse speeds while keeping a Python-native codebase. Benchmark data shows pure-Python sqlglot takes ~4x longer than `sqlglot[c]` across all query shapes (e.g. tpch: 0.002709s vs 0.000740s). With the C extension, sqlglot reaches within ~1.1–1.5x of Rust-based competitors sqloxide and polyglot-sql (e.g. tpch: 0.000740 vs 0.000655/0.000698). The C extension was chosen over a full Rust rewrite to preserve the pure-Python fallback path and avoid mandatory native compilation for users who don't need peak throughput. Rust-based parsers were considered but rejected as the primary implementation because they would break pure-Python compatibility.

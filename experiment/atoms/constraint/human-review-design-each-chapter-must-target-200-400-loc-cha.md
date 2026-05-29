---
kind: constraint
claim: "Each chapter must target ~200\u2013400 LOC; chapters exceeding 500 LOC must\
  \ be split and chapters below 100 LOC must be merged with related neighbours."
anchors:
- src/pr_guardian/wizard/capability_clusterer.py
tags:
- human-review
- chapters
- loc-budget
source: doc-import:docs/human-review-design.md
status: active
---
Each chapter must target ~200–400 LOC; chapters exceeding 500 LOC must be split and chapters below 100 LOC must be merged with related neighbours. This range is the SmartBear/Cisco optimal for defect detection (70–90% detection rate across 2,500 reviews). Past 600 LOC, reviewer attention collapses to style/typo comments only. Chapter computation: (1) group files by longest common path prefix, (2) merge groups <100 LOC with related neighbours, (3) split any chapter >500 LOC. The target ceiling is 500 LOC to give headroom before the 600 LOC cognitive cliff.

---
kind: constraint
claim: "Chapters must be ordered by highest finding severity descending, then production\
  \ files before test/config \u2014 never alphabetically."
anchors:
- src/pr_guardian/wizard/capability_clusterer.py
- src/pr_guardian/dashboard/human_wizard.html
tags:
- human-review
- chapters
- ordering
source: doc-import:docs/human-review-design.md
status: active
---
Chapters must be ordered by highest finding severity descending, then production files before test/config — never alphabetically. ICSE 2026 ('Breaking the Alphabet') found only 10.2% of reviewers consider alphabetical ordering optimal; Microsoft research on 1.5M comments shows more files correlates with fewer useful comments, so attention must be front-loaded on high-risk material. Within a chapter, files are further ordered by dependency: files that others import come first (callee before caller) so the reviewer sees foundational code before code that depends on it.

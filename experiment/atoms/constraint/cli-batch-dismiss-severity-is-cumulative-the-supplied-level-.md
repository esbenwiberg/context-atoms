---
kind: constraint
claim: '`batch-dismiss --severity` is cumulative: the supplied level is a ceiling,
  dismissing all findings at that severity AND below.'
anchors:
- src/pr_guardian/cli.py
tags:
- batch-dismiss
- severity
- filter-semantics
source: doc-import:docs/cli.md
status: active
---
`batch-dismiss --severity` is cumulative: the supplied level is a ceiling, dismissing all findings at that severity AND below. Passing `--severity medium` dismisses both `medium` and `low` findings, not just `medium`. Passing `--severity low` dismisses only `low`. This mirrors a 'max severity to dismiss' contract rather than an exact-match filter. Any code implementing this filter must treat the argument as an upper bound on the severity enum, not an equality check.

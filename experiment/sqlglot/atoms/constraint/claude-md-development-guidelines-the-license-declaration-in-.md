---
kind: constraint
claim: The license declaration in setup.py must not be modified, even if it looks
  incorrect or inconsistent.
anchors:
- setup.py
- LICENSE
tags:
- legal
- license
- do-not-touch
source: doc-import:CLAUDE.md#development-guidelines
status: active
---
The license declaration in setup.py must not be modified, even if it looks incorrect or inconsistent. The CLAUDE.md explicitly states 'there's nothing wrong with it', anticipating that agents or reviewers may flag it as a false positive. Treat any automated suggestion to change setup.py's license field as a false positive and reject it.

---
kind: constraint
claim: "Language detection must use file-extension lookup only \u2014 no file content\
  \ parsing, no heuristics \u2014 and config/data formats (yaml, json, markdown) must\
  \ be excluded from the `cross_stack` flag, which counts only RUNTIME_LANGUAGES."
anchors:
- src/pr_guardian/languages/detector.py
- src/pr_guardian/languages/registry.py
- src/pr_guardian/models/languages.py
tags:
- language-detection
- cross-stack
- discovery
source: doc-import:docs/plan/01b-discovery.md
status: active
---
Language detection must use file-extension lookup only — no file content parsing, no heuristics — and config/data formats (yaml, json, markdown) must be excluded from the `cross_stack` flag, which counts only RUNTIME_LANGUAGES.

`cross_stack` is true only when more than one language from the RUNTIME_LANGUAGES set (`python`, `typescript`, `javascript`, `csharp`, `go`, `java`, `kotlin`, `rust`, `sql`, `shell`, `powershell`) appears in the diff. Files like `.yaml`, `.json`, and `.md` are detected and grouped but never count toward this flag. Primary language is whichever runtime language has the most changed files (by file count, not line count).

---
kind: rationale
claim: Deterministic validation phases (lint, SAST, build, test, health) run before
  AI-backed phases so the system does not spend reviewer LLM tokens on code that cannot
  build, test, or pass basic checks.
anchors:
- packages/daemon/src/interfaces/validation-engine.ts
- packages/daemon/src/pods/state-machine.ts
- packages/daemon/src/pods/validation-repository.ts
tags:
- validation
- pipeline
- ordering
- cost
source: doc-import:ARCHITECTURE.md#validation-pipeline
status: active
---
Deterministic validation phases (lint, SAST, build, test, health) run before AI-backed phases so the system does not spend reviewer LLM tokens on code that cannot build, test, or pass basic checks. The ten-phase pipeline gates AI review (phases 7–9) behind mechanical gates (phases 1–6). This ordering is intentional: running the AI reviewer on broken code wastes tokens and produces low-signal feedback. The deterministic phases are cheap to run and act as a filter so the expensive AI phases only see code that at minimum compiles and passes tests.

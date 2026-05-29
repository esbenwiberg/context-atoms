---
kind: constraint
claim: '`architecture_intent` must remain a resolvable agent identity for historical
  re-review; fresh triage must not select it, but it cannot be deleted until historical
  reviews age out or a migration is explicitly designed.'
anchors:
- src/pr_guardian/agents/architecture_intent.py
- src/pr_guardian/core/orchestrator.py
- src/pr_guardian/triage/work_item.py
tags:
- agents
- legacy
- re-review
- signatures
source: doc-import:docs/decisions/ADR-006-split-verifier-agent-identity.md
status: active
---
`architecture_intent` must remain a resolvable agent identity for historical re-review; fresh triage must not select it, but it cannot be deleted until historical reviews age out or a migration is explicitly designed. Finding signatures are defined as `file::category::agent` (ADR-004); removing `architecture_intent` would strand existing DB findings that reference it by name and break focused re-review on historical PRs. `weights.architecture_intent` must also be kept as a deprecated config alias: when only the legacy key is set, its value is copied to both `weights.intent` and `weights.architecture`; when a new key is present, it wins.

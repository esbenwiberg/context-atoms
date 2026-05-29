---
kind: constraint
claim: All agent-relevant knowledge must live inside the repository; information not
  present in the repo is invisible to agents.
anchors:
- CLAUDE.md
- AGENTS.md
- ARCHITECTURE.md
- PRACTICES.md
- e2e/AGENTS.md
- packages/cli/AGENTS.md
- packages/daemon/CLAUDE.md
tags:
- agents
- documentation
- discoverability
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#15-key-quotes-worth-remembering
status: active
---
All agent-relevant knowledge must live inside the repository; information not present in the repo is invisible to agents. CLAUDE.md, AGENTS.md, ARCHITECTURE.md, and PRACTICES.md are the canonical surfaces where working conventions, constraints, and architectural decisions must be recorded. Any rule, pattern, or decision that exists only in Slack, wikis, or human memory is effectively absent when an agent operates on the codebase. This applies to every package boundary — each package with agent interaction (e.g. packages/daemon, packages/cli, e2e) must maintain its own AGENTS.md or CLAUDE.md rather than relying on root-level docs alone.

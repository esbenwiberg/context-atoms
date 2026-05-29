---
kind: rationale
claim: A thin ~100-line LLM abstraction with three concrete implementations was chosen
  over LiteLLM because only three providers are needed and LiteLLM pulls in 50+ packages.
anchors:
- src/pr_guardian/llm/protocol.py
- src/pr_guardian/llm/anthropic.py
- src/pr_guardian/llm/azure_foundry.py
- src/pr_guardian/llm/openai_compat.py
- src/pr_guardian/llm/factory.py
tags:
- llm
- dependencies
- architecture
source: doc-import:docs/plan/07-architecture.md
status: active
---
A thin ~100-line LLM abstraction with three concrete implementations was chosen over LiteLLM because only three providers are needed and LiteLLM pulls in 50+ packages. The abstraction exposes a single `complete(system, user, response_format)` call. Rejected alternative: LiteLLM — too heavy for the narrow provider matrix (Anthropic, Azure OpenAI, OpenAI-compatible). Adding a new provider means adding one ~30-line file under `src/pr_guardian/llm/`, not upgrading a framework.

---
kind: rationale
claim: Keyword overlap scoring was chosen over embedding similarity for section relevance
  because it delivers approximately 80% of the value at medium implementation effort
  versus the higher effort required for embedding-based approaches.
anchors:
- packages/daemon/src/pods/system-instructions-generator.ts
tags:
- context-assembly
- relevance-scoring
- design-tradeoff
source: doc-import:docs/ai-coding-agent-proposals.md#proposal-3-context-relevance-scoring
status: active
---
Keyword overlap scoring was chosen over embedding similarity for section relevance because it delivers approximately 80% of the value at medium implementation effort versus the higher effort required for embedding-based approaches. The simple approach counts shared significant words between the task description and each section's heading and content. The advanced embedding approach requires a model to be available at injection time. The keyword approach was selected as the default recommendation; embedding similarity remains a valid upgrade path if precision requirements increase.

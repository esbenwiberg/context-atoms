---
kind: rationale
claim: The /prep and exec skills were chosen as the project's equivalent of OpenAI's
  ExecPlan pattern, covering spec decomposition, dependency DAGs, handover chains,
  and parallel dispatch, making a separate ExecPlan implementation redundant.
anchors:
- .agents/skills/prep/SKILL.md
- .agents/skills/plan-feature/SKILL.md
tags:
- prep
- exec
- execplan
- planning
- skills
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#14-prioritized-recommendations-for-autopod
status: active
---
The /prep and exec skills were chosen as the project's equivalent of OpenAI's ExecPlan pattern. /prep decomposes tasks into spec suites with briefs, contracts, ADRs, validation plans, and required facts. The exec skill orchestrates multi-brief execution with subagents, handover chains, dependency DAGs, parallel dispatch, and drift detection — functionally equivalent to ExecPlan. Three patterns from ExecPlan research are still candidates for enhancing these skills: (1) living document updates — timestamped Progress/Surprises/Decision Log sections updated as work progresses (currently the plan is static); (2) idempotence and recovery section — explicit rollback/retry documentation in brief templates; (3) context preamble per brief — key file paths and module explanations to improve subagent orientation.

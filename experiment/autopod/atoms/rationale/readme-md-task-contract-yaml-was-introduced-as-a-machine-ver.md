---
kind: rationale
claim: contract.yaml was introduced as a machine-verifiable executable proof layer
  so pods can automatically run integration tests that prove each scenario, replacing
  prose criteria that the harness could not execute.
anchors:
- packages/daemon/src/db/migrations/101_pod_contract.sql
- .agents/skills/prep/SKILL.md
- .claude/skills/prep/SKILL.md
tags:
- contract
- spec
- integration-test
- automation
source: doc-import:README.md#task
status: active
---
contract.yaml was introduced as a machine-verifiable executable proof layer so pods can automatically run integration tests that prove each scenario, replacing prose criteria that the harness could not execute.

Each required_fact names a scenario it proves, specifies kind (e.g. integration-test), points to an artifact (file path + change type), and provides a command the harness runs to verify the fact. This wires spec authorship directly to CI-style verification, so a pod cannot declare a scenario satisfied without a passing test command on record. The depends_on field additionally lets contracts express ordering constraints between specs.

# Ablation results  (48 runs)

## Success
- atoms : 100.0%  (n=24)
- none  : 100.0%  (n=24)
- delta : +0.0 pp

### Per stratum (pass rate atoms / none)
- simple : 100%/100%  (n=3/3)
- medium : 100%/100%  (n=15/15)
- novel  : 100%/100%  (n=6/6)

## Exploration
- file-reveal calls in first 5: atoms 2.96 / none 3.12  -> ratio 0.95
- total tool calls: atoms 13.0 / none 12.8

## Cost
- $ per run: atoms $0.144 / none $0.140  -> +2.2%
  (cost is the honest overhead measure; usage.input_tokens excludes cached prompt so it is NOT used for the verdict)
- mean atoms injected (atoms arm): 17.1

## Kill criteria (pre-registered)
| Metric | Value | Verdict |
|---|---|---|
| Success delta | +0.0 pp | UNINFORMATIVE |
| Exploration ratio | 0.95 | GREEN |
| Simple-task delta | +0.0 pp (n=3) | UNINFORMATIVE |
| Cost overhead | +2.2% | GREEN |

## Verdict
**SUCCESS METRIC CEILINGED (100%/100%).** Every task was solved by both arms, so the pre-registered PRIMARY metric (success delta) cannot discriminate. The bet is NEITHER proven NOR refuted by success.

The behavioural metric the bet hinged on — file-reveal calls in the first 5 tool calls — is FLAT (ratio 0.95). Anchor-matched injection did not measurably reduce early exploration on this benchmark.

=> DO NOT build the mechanism on this evidence. The benchmark lacks discriminating power (tasks too easy / budget too generous). Re-run with harder discrimination (lower turn budget, harder tasks, or weaker model) BEFORE any green light. Total-tool-calls did drop (13.0 vs 12.8) — a weak secondary signal worth chasing in the re-run, not acting on now.

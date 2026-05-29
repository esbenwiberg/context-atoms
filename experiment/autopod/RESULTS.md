# Ablation results  (18 runs)

## Success
- atoms : 100.0%  (n=9)
- none  : 100.0%  (n=9)
- delta : +0.0 pp

### Per stratum (pass rate atoms / none)
- simple : nan%/nan%  (n=0/0)
- medium : 100%/100%  (n=6/6)
- novel  : 100%/100%  (n=3/3)

## Exploration
- file-reveal calls in first 5: atoms 3.11 / none 2.89  -> ratio 1.08
- total tool calls: atoms 8.0 / none 7.4

## Cost
- $ per run: atoms $0.279 / none $0.243  -> +14.8%
  (cost is the honest overhead measure; usage.input_tokens excludes cached prompt so it is NOT used for the verdict)
- mean atoms injected (atoms arm): 29.7

## Kill criteria (pre-registered)
| Metric | Value | Verdict |
|---|---|---|
| Success delta | +0.0 pp | UNINFORMATIVE |
| Exploration ratio | 1.08 | GREEN |
| Simple-task delta | +0.0 pp (n=0) | UNINFORMATIVE |
| Cost overhead | +14.8% | GREEN |

## Verdict
**SUCCESS METRIC CEILINGED (100%/100%).** Every task was solved by both arms, so the pre-registered PRIMARY metric (success delta) cannot discriminate. The bet is NEITHER proven NOR refuted by success.

The behavioural metric the bet hinged on — file-reveal calls in the first 5 tool calls — is FLAT (ratio 1.08). Anchor-matched injection did not measurably reduce early exploration on this benchmark.

=> DO NOT build the mechanism on this evidence. The benchmark lacks discriminating power (tasks too easy / budget too generous). Re-run with harder discrimination (lower turn budget, harder tasks, or weaker model) BEFORE any green light. Total-tool-calls did drop (8.0 vs 7.4) — a weak secondary signal worth chasing in the re-run, not acting on now.

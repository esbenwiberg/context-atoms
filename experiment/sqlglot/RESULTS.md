# Ablation results  (96 runs)

## Success
- atoms : 68.8%  (n=48)
- none  : 68.8%  (n=48)
- delta : +0.0 pp

### Per stratum (pass rate atoms / none)
- simple : 95%/95%  (n=20/20)
- medium : 50%/50%  (n=20/20)
- novel  : 50%/50%  (n=8/8)

## Exploration
- file-reveal calls in first 5: atoms 2.58 / none 2.56  -> ratio 1.01
- total tool calls: atoms 32.1 / none 29.9

## Cost
- $ per run: atoms $0.659 / none $0.602  -> +9.4%
  (cost is the honest overhead measure; usage.input_tokens excludes cached prompt so it is NOT used for the verdict)
- mean atoms injected (atoms arm): 7.4

## Kill criteria (pre-registered)
| Metric | Value | Verdict |
|---|---|---|
| Success delta | +0.0 pp | YELLOW |
| Exploration ratio | 1.01 | GREEN |
| Simple-task delta | +0.0 pp (n=20) | GREEN |
| Cost overhead | +9.4% | GREEN |

## Verdict
MIXED -> narrow scope (e.g. inject only on the class that helped).

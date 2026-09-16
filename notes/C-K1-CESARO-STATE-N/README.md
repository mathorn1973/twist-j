# K1 Cesaro comparison state

NON-CANONICAL. Candidate mathematical results only. No GitHub modification,
no current H/O closure, no physical energy, no scalar denominator, no r_T.

Read PROOF.md for the complete proof, source scope, and exact limitations.
PREREG.md was frozen before the first candidate computation and is unchanged.

Python 3, standard library only:

```sh
python3 verify.py > actual.json
python3 break.py > actual-break.json
cmp actual.json EXPECTED.json
cmp actual-break.json BREAK-EXPECTED.json
```

The two scripts use different exact algebraic routes, but the same agent wrote
both. This is not blind independent confirmation or a two-architecture gate.
The actual source law is the optional nu in v82; time averaging is an explicit
additional mathematical readout convention, not a physical law selected by J.

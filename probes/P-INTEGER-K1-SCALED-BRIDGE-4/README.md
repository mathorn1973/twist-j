# P-INTEGER-K1-SCALED-BRIDGE-4

Status: `NON-CANONICAL` (`L1`, `RESULT=PASS`)
Public lock: `#1635`
Predecessor probe: `P-INTEGER-SOURCE-HOLONOMY-1` (`PR #1633`, issue `#1632`)
Abandoned predecessors: `P-INTEGER-K1-SCALED-BRIDGE-1` (`#1636`), `P-INTEGER-K1-SCALED-BRIDGE-2` (`#1637`), `P-INTEGER-K1-SCALED-BRIDGE-3` (`#1638`)

## Overview

Resolves the two `L1` constructive bridge obligations identified by
`P-INTEGER-SOURCE-HOLONOMY-1` (`PR #1633`):

1. **Scaled Integer K1 Carrier + Domain-and-Bank Reflection Bijection (`B1-B3`):**
   Embeds `DEF-K1-LINEAR-METRIC` into the integer carrier
   `X_K1 = Z^5 x Z^5 x Z_(>=1)` via `(U_k, W_k, k) = (2 * 324^k h_k, 2 * 324^(k-1) h_(k-1), k)`,
   proves that the Domain-and-Bank Reflection rule `F_K1` is a total bijection
   on `X_K1 x Z_(>=0) x {-1, +1}` with exact inverse `R_K1 o F_K1 o R_K1`,
   establishes lossless periodic bounce cycles of period `2N` at the sharp
   horizon bank `B_sharp^(w)(N) = E_K1(x_N^(w)) - E_K1(x_1^(w))`, and proves
   the unconditional 3-adic quadratic precision lower bound
   `sum_(r=0)^4 P_n(r)^2 + D_n^2 >= (6/5) * d_n^2 >= (6/5) * 3^(8(n-1))`.
2. **Additive Transverse Metric Readout + Coupled 7-Phase, 40-Integer Bridge (`B4-B5`):**
   Couples the 6-phase Hermitian source-holonomy loop over `O = Z[j]` with the
   scaled K1 step in a 7-phase, 40-integer bijection `F_bridge` with additive
   transverse metric readout `g_r(U, k) = diag(-1, 1 + h_k(r), 1 - h_k(r), 1)`.

## Files

- `PREREG.md` — Frozen preregistration, equations, falsifiers, and scope.
- `PROOF.md` — Proofs of Claims `B1` through `B5`.
- `SOURCE.md` — Source and predecessor pin manifest.
- `verify.py` — Primary verifier (4-coefficient polynomial `Z[j]` + `Fraction` K1).
- `breaker.py` — Independent implementation (5-cyclic `Z[j]` + pure integer K1).
- `FROZEN.sha256` — Pre-execution SHA-256 manifest of the 5 frozen files above.
- `EXPECTED.txt` — Exact stdout of `python3 probes/P-INTEGER-K1-SCALED-BRIDGE-4/verify.py`.
- `RUN.md` — Formal execution record and pin custody.
- `RESULT.md` — Final `L1` result summary and scope boundaries.

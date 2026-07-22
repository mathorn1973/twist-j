# P-C20-TEICHMULLER-SPLIT-1 result

status: theorem candidate at T, L1 scope, formal aarch64 leg 6/6 ALL PASS;
the two-architecture gate completes with the required GitHub x86_64 check at
pull-request time. No falsifier fired. No frozen file was amended after the
pin.

Earned content at the frozen scope, conditional on the GitHub leg:

```text
CYCLE       ord(J) = 20 in Z[zeta_5]/5, J^10 = -1.
WHEEL       J^5 = 2 exactly; the fifth powers walk 2, -1, 3 = phi_lambda; the
            Teichmueller component of the J-cycle is the registered time
            quantum scalar i_5.
SPLIT       J = J^5 * J^16 with u = J^16 = 3J unipotent of order 5 and
            nilpotency index exactly 4; <J> = C_4 x C_5 internally.
TWO-PART    the 2-part of <J> is <J^5> = C_4; exhaustively over all 625
            elements no order-8 element exists.
DEPTH       4 * 5^(m-1) has 2-valuation exactly 2 at every nilpotent depth:
            the eight-phase is forbidden in the ramified fiber by Lagrange
            and first lives one quadratic floor up.
MATRIX      the raw axiom step matrix independently reproduces the cycle,
            the wheel, the split, and the Jordan block J_4(2), in exact
            column agreement with the ring walk.
```

Proposed disposition (separate reviewed fold, not part of this probe): one
registry row C20-TEICHMULLER-SPLIT [T] in section 2, evidence this probe,
consistency anchors FIB-ROOT-TIES [T] and TIME-QUANTUM-TOWER [C]. This probe
reads no clock and identifies no tick.

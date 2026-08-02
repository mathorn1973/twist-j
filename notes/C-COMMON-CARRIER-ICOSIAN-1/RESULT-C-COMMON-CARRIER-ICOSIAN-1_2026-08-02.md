# RESULT C-COMMON-CARRIER-ICOSIAN-1, 2026-08-02

NON-CANONICAL. Recorded run of the incubation candidate. No authority,
no Canon change.

## Recorded leg

```text
leg 1  x86_64, Ubuntu 24.04.3 LTS (WSL2), Python 3.12.3
       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
verify_common_carrier_icosian.py   exit 0, empty stderr, 45 gates,
                                   45 PASS, 0 FAIL
  stdout common_carrier_icosian.stdout.txt
  sha256 e83e5c494038b53be5236327b1c10a01a91307754c2813391306b31cdd560d91
  7154 bytes
break_common_carrier_icosian.py    exit 0, empty stderr, 6 gates,
                                   6 PASS, 0 FAIL
  stdout common_carrier_icosian_break.stdout.txt
  sha256 956054a7e65ee8dcda7fbc74c054c592bb200be4aee0c997535f4ff069929a36
  1073 bytes
```

One architecture is recorded here. These are incubation pins, not a
public probe; the two-architecture computation gate of POLICY section 4
is NOT claimed. A second leg on a different architecture (or the GitHub
x86_64/aarch64 pair on a future probe head) is the named next step for
any promotion.

## Per-claim outcome

```text
I1-I4   candidate-T   2I closed, 120 units, order profiles, A5 quotient
Q1-Q5   candidate-T   internal CM: q, Z[q]=Z[zeta5], single class
J1-J3   candidate-T   J unit, nrd = 2-phi, J phi = q, J^-1 in Z[q]
O1,FB1  candidate-T   O rank 8; FREE Z[zeta5]-basis {1, omega}
E1-E2   candidate-T   the K e line meets 2I; gamma = -1
G1-G4   candidate-T   glue index 5 at p5; diagonal glue; h in p5^-1 O_K
B1,H1-3 candidate-T   coordinates; h Hermitian definite, Gram identity
A1-A3   candidate-T   right 2I h-unitary; left K similitude; commuting
T1-T2   candidate-T   J as K-scalar; ramified residues, res(J) = 2
T3      candidate-T   glue criterion res(D1) = res(D2), 400-pair sweep
T4-T5   candidate-T   twisted even tick, phase 1 - J; five/ten closure
T6-T7   candidate-T   half-step obstruction; K(sqrt J) = K(sqrt phi)
C1-C2   candidate-T   conjugation 3-space traces {1-phi, phi}
X1-X2   candidate-T   golden-twisted trace form is E8 (with [T, lit.])
L1-L2   candidate-T   registered lift reproduced; SL2(F5) bijection
L3-L4   candidate-T   rho integral, same class function, conjugate lift
L5      candidate-T   class of q = 5a; conjugation 3-space = canon 3a
L6      candidate-T   residue 5a/5b labels are basis gauge (res phi = 3)
BK1-BK6 candidate-T   all six break attempts refuted
```

## Falsification first

Any FAIL line fires F-ICO-1 (verifier) or F-ICO-2 (breaker); the [H]
carrier-completeness claim carries the separate falsifier F-ICO-3
(decoder shape, deferred to P-DECODER-SOS-FORM-1).

No falsifier fired. No threshold moved. PROMO deferred.

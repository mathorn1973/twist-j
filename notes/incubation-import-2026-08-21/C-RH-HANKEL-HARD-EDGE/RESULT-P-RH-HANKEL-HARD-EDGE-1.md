# RESULT P-RH-HANKEL-HARD-EDGE-1

```text
STATUS:      NON-CANONICAL INCUBATION RESULT, no authority
DATE:        2026-08-20 (UTC)
VERDICT:     STOP-GATE FIRED. At the frozen hard edge c_d = (33/4) d + 9/2
             and frozen range D = {2,4,8,16,24}, none of the three standard
             families (affine, Chebyshev T, Chebyshev U) passes the double
             gate. [F-bounded, STANDARD HARD-EDGE FAMILIES, candidate-C at
             the frozen scale and range]
FIREWALL:    no RH claim. J7 SOURCE [O]. RH [O]. Public Canon v55 untouched.
PARENT:      RH-T1-GLOBAL-TRANSFORM-ATTACK-2026-08-20.md, sha256 ca6cdfc4...
PIN:         commit b6e325c5d9308d7478074f4ded44a643048193cd, prereg and
             verifier committed before first execution, author A. M. Thorn
PREREG:      PREREG-P-RH-HANKEL-HARD-EDGE-1.md
             sha256 c615a52e1e14a2bc530fee27b0a60d6fcf10c31f5856bc971eaf77eaff5de309
VERIFIER:    verify_rh_hankel_hard_edge_1.py
             sha256 0b896a9fadad28cbc8c89e9dc5764ad705679ca8072bd95888b05849b77e33d0
STDOUT:      verify_rh_hankel_hard_edge_1.stdout.txt, 6190 bytes
             sha256 2458864c934c7d31291c25134712cc52b9721ac61301b34e7b67479e55a70207
             BYTE-IDENTICAL on macOS arm64 CPython 3.9.6 and
             Linux x86_64 CPython 3.11.15, env
             LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
             exit 0, foundations 4 of 4 PASS (CHECK 0, 1, 2, 5)
BREAKER:     breaker_rh_hankel_hard_edge_1.py with stdout committed beside
             this file; hashes in INDEX.md. No authority, floats allowed.
```

## 1. What was frozen and what fired

The prereg froze the double gate of the owner's step-1 plan on the Hankel
carrier `Q_c[P]` of the parent draft: Gate B, Fourier sign
`G(x) <= 0 for all x >= c_d log 2` decided exactly (Sturm chain, root
isolation, rational log 2 enclosure); Gate A, exact off-line detection
`V(alpha) = 2 Re[q(2-q)P(q)^2] < 0` in `Q(i)` at d = 24 for three pinned
quartets. Survival required both. The frozen stop-gate: if none of F1, F2,
F3 survives, the standard-family hard-edge route closes as
[F-bounded, STANDARD HARD-EDGE FAMILIES] and the lane re-targets the T2
Weyl/Nevanlinna construction.

The stop-gate fired. Survival table from the pinned run:

```text
F0 monomial      Gate B PASS at all d in D      Gate A blind (control PASS)
F1 affine        Gate B fails at every d in D   Gate A PASS (all 3 quartets)
F2 Chebyshev T   Gate B fails at every d in D   Gate A blind
F3 Chebyshev U   Gate B fails at every d in D   Gate A blind
```

The verifier labeled the Gate B failures AMBIGUOUS under its frozen
sampling rule (it evaluated x_lo and the gap points, not x_hi). The breaker
upgraded every one of the 30 verdicts by an exact sign evaluation at
`x_hi = c_d LOG2_HI`: `G(x_hi) > 0` in all 30 cases. The failures are real
sign failures at the threshold, not enclosure artifacts. The gray zone
played no role. AMBIGUOUS counted as FAIL for survival by the frozen rule,
so the verdict is unchanged; the labeling rule was merely weaker than the
achievable certificate. Recorded for the successor, no rerun needed.

## 2. Where exactly the Fourier gate fails (breaker B2, exact-sign bisection)

The last positive-to-negative crossing of G against the threshold
`x_lo = c_d log 2 = 5.7189 d + 3.119`:

```text
F0:  crossing = 4 sqrt(2) d + 3.06, deficit -0.20 .. -1.54 (passes, margin
     grows like (33/4 log2 - 4 sqrt2) d = 0.062 d). This reproduces the
     parent threshold (5.17) exactly at the numeric level: 2 sqrt(2) n +
     13 sqrt(2)/6 with n = 2d. [candidate-C confirmation of the parent row]
F1:  crossing = 4 sqrt(2) d + 14.2 within 0.1 across d and theta. Constant
     offset excess about +11.1 over the monomial, deficit 10.7 (d=2) down
     to 9.7 (d=24), shrinking only at the 0.062 d slack rate. At the frozen
     beta = 9/2 the gate would first clear near d of order 180.
F2:  crossings 18.9, 34.9, 66.8, 130.8 at d = 2, 4, 8, 16; increments
     8.0 per unit d. SLOPE excess, not offset excess: 8.0 > 5.719, the
     deficit grows without bound. At d = 24 the crossing left the 40-unit
     scan window entirely.
F3:  same behavior as F2 within 0.5.
```

Consequences, both first-class:

```text
[F-bounded, CHEBYSHEV HARD EDGE] The Chebyshev families fail structurally:
their crossing grows at slope about 8.0 d against the threshold slope
5.719 d, so no admissible beta and no linear hard edge with kappa near the
parent threshold repairs them. Raising kappa above 8/log 2 = 11.54 would be
a different, unpreregistered scale, and both families are detection-blind
anyway (section 3). This lane treats them as closed.

[candidate-C, AFFINE OFFSET DIAGNOSIS] The affine family fails only by a
measured constant offset near 11.1 in x units, equivalently a beta lift of
about 16. Breaker B5 (diagnostic, no authority): the minimal integer beta
with a clean Gate B pass for the matched theta member is 20 (d = 2), 20
(d = 8), 19 (d = 24). One frozen parameter short, not a structural wall.
```

## 3. Detection data (Gate A and breaker B3, B4)

Exact values at d = 24 (all signs reproduced independently by the breaker's
complex-float path):

```text
matched affine members: V(alpha1) = -1.893e-10, V(alpha2) = -6.471e-9,
  V(alpha3) = -1.023e-8, all exactly negative. Gate A PASS.
mismatched theta: positive throughout, e.g. theta=0 at alpha1 gives
  +1.866e-8. Matching theta = Re alpha^2 is what buys the negative sign.
margin scaling, alpha1: -1.52e-6 (d=2), -1.56e-7 (4), -1.27e-8 (8),
  -9.15e-10 (16), -1.89e-10 (24): the predicted c^-4 law of parent (5.21).
onset: alpha2 (T=14) first detected at d = 16; alpha3 (delta=1/4, T=6)
  at d = 4. Detection needs |alpha^2|/c^2 small, as expected.
controls: F0 blind (V = +1.99 at alpha1, limit value +2 of parent (5.20),
  CHECK 5 PASS). F2 and F3 blind at all three quartets with large positive
  values; the prereg prediction (bounded cosh-type limit) was correct for
  the sign but wrong about magnitudes, U_24 reaches +1.15e+3.
```

Breaker B4, roam over 200 random quartets (delta in (0.01, 0.49),
T in (0.5, 30)) with matched theta at d = 24: 27 of 200 matched detections
FAIL, first failure at delta = 0.135, T = 24.25 with V = +1.67e-8. The
c^-4 margin -2 (Im alpha^2)^2 / c^4 loses to the next-order correction
once T is large at fixed c. So each member has a height ceiling
T*(d), near T* = 24 at d = 24. For any FIXED quartet the parent asymptotic
(5.21) still gives detection at all large d; the ceiling moves up with d.
The family as a whole detects, no single member does. [candidate-C data]

## 4. Honest verdict for the route

```text
STOP-GATE               FIRED as frozen and archived. At the frozen scale
                        and range the standard-family hard-edge route is
                        [F-bounded, STANDARD HARD-EDGE FAMILIES].
Frozen next action      re-target the T2 Weyl/Nevanlinna construction
                        (owner's plan, frozen in the prereg).
What the data add       the affine failure is one measured constant
                        (beta near 20 instead of 9/2), not a wall; the
                        Chebyshev failure IS a wall (slope excess plus
                        detection blindness); the detection ceiling
                        T*(d) is the new quantitative object, and the
                        step-3 tail problem exists independently of any
                        beta repair, because every member is blind above
                        its ceiling and the infinite family plus a
                        summable tail majorant must carry the argument.
```

Owner fork, not decided here:

```text
A  Follow the frozen action: open the T2 Weyl/Nevanlinna lane now.
B  One narrow successor first, P-RH-HANKEL-HARD-EDGE-2: identical double
   gate, single change c_d = (33/4) d + 20 (fresh freeze, no threshold
   moved inside a sealed probe), affine family only, plus a T*(d) scaling
   measurement at d in {8, 16, 24, 32, 48}. Predicted from B5: Gate B
   PASS; then the route stands or falls on the step-3 tail majorant,
   which is the real mathematics either way.
```

Recommendation of this session: B, then A regardless of B's outcome. B is
one cheap freeze and settles whether the Euler route enters step 3 with a
live family; the tail majorant and the multi-quartet competition are the
actual wall and they are shared with every other zero-side route.

## 5. Pins of this result

```text
breaker_rh_hankel_hard_edge_1.py         sha256 in INDEX.md
breaker_rh_hankel_hard_edge_1.stdout.txt sha256 in INDEX.md
                                         single leg Linux x86_64 CPython
                                         3.11.15 (a breaker gates nothing)
project copies: claude/PREREG-P-RH-HANKEL-HARD-EDGE-1.md,
                claude/RESULT-P-RH-HANKEL-HARD-EDGE-1.md and the four
                machine files under the claude/ namespace
```

A fired stop-gate is progress: two of three standard families are closed
with measured mechanisms, the third is localized to one frozen constant,
and the decisive open object (the tail majorant over the detection
ceiling) is now explicit. Nothing here moves J7 SOURCE or RH; both stay
[O].

End of result.

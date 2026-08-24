# RESULT P-RH-HANKEL-HARD-EDGE-2

```text
STATUS:      NON-CANONICAL INCUBATION RESULT, no authority
DATE:        2026-08-20 (UTC)
VERDICT:     F1 SURVIVES. At the frozen hard edge c_d = (33/4) d + 21 the
             affine family passes the full double gate on D = {2,4,8,16,24}
             and detects all three pinned quartets at d = 24. The stop-gate
             did NOT fire. ROUTE ARMED. [candidate-C at the frozen scale
             and range]
NEW OBJECT:  measured detection-ceiling law T_ff^3 / (delta c^2) in
             [2.01, 2.16] across all ten table cells. [candidate-C]
FIREWALL:    no RH claim. J7 SOURCE [O]. RH [O]. Public Canon v55 untouched.
PARENT:      P-RH-HANKEL-HARD-EDGE-1, stop-gate fired, sealed.
PIN:         commit 48d2b4579cc6be2cf368e4b9b7db0cf1b24846f4, prereg and
             verifier committed before first execution, author A. M. Thorn
PREREG:      PREREG-P-RH-HANKEL-HARD-EDGE-2.md
             sha256 c6765178b24a8d58b75ec4140fb9ccd0f714ad135b0c8b6b0896de984cd647a0
VERIFIER:    verify_rh_hankel_hard_edge_2.py
             sha256 94c2dc679924e1916155afb0be1794289980ee76c07b9e1347285dcee8e4ee71
STDOUT:      verify_rh_hankel_hard_edge_2.stdout.txt, 4928 bytes
             sha256 fd01d872f91d31e72fa3d3daca51026e501c8031d97a3680cdf8df0bcac33a02
             BYTE-IDENTICAL on macOS arm64 CPython 3.9.6 and Linux x86_64
             CPython 3.11.15, env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC, exit 0, foundations 4 of 4 PASS
BREAKER:     breaker_rh_hankel_hard_edge_2.py
             sha256 e8c052713755e126bed8f1374f784d5ae7e577c89cd91d6ba19dd8fd03061092
             stdout ad4078db81df2112f2f8f5ac0f29f1a154f656c72f160a2e746372fba8de6c84
             single leg Linux x86_64, FINDINGS: 0
```

## 1. Gate B, Fourier sign at beta = 21

All twenty members (F0 control plus F1 at four thetas, five degrees) PASS
with zero roots beyond the threshold; every verdict now includes the exact
evaluation at x_hi. The breaker localized every crossing independently:

```text
margins x_lo - crossing, F1 members:
  d=2   0.72 .. 1.84       d=4   0.70 .. 1.31   (minimum 0.704 at theta=0)
  d=8   0.84 .. 1.09       d=16  1.26 .. 1.34   d=24  1.72 .. 1.76
```

The prereg design note predicted the minimum near d = 4; measured minimum
is 0.704 at (theta = 0, d = 4). At beta = 20 this member would have sat at
about 0.01; the one-unit lift was the difference between survival and a
spurious second stop-gate. The extended DATA-SCAN at d = 32, 48 (theta in
{0, -399/100}) shows sign(x_lo) = -1, no positive value on 120 half-unit
grid points, leading sign negative; grid evidence only, no certificate.

## 2. Gate A, detection at d = 24 (c = 219)

Matched members detect all three pinned quartets exactly:

```text
V(alpha1) = -1.385e-10,  V(alpha2) = -5.068e-9,  V(alpha3) = -7.526e-9,
mismatched thetas positive throughout; F0 control blind (+1.99), CHECK 5
PASS. Margins follow the c^-4 law along D. All signs independently
reproduced by the breaker's complex-float path.
```

## 3. The measured ceiling law

The frozen table (delta in {1/10, 1/4}, d in {8,16,24,32,48}, grid
T = k/2 up to 50) gives first-failure frontiers:

```text
delta=1/10: T_ff = 11.5, 17, 21.5, 25.5, 33
delta=1/4:  T_ff = 16, 23, 29, 34.5, 44.5
ratio T_ff^3/(delta c^2): 2.0093, 2.0988, 2.0722, 2.0414, 2.0667,
                          2.1646, 2.0790, 2.0341, 2.0222, 2.0271
```

All ten cells sit in [2.01, 2.16] with no trend larger than the grid
step. Read as data: the matched affine member at scale c detects an
isolated quartet (delta, T) iff roughly

```text
T^3 < 2 delta c^2,
```

consistent with the balance of the c^-4 margin -2 (Im alpha^2)^2/c^4 =
-8 delta^2 T^2/c^4 against a next-order correction of size about
4 delta T^5/c^6. The exponent pattern (T* proportional to delta^(1/3)
c^(2/3)) is measured, not derived; deriving it exactly is a successor
obligation. [candidate-C, CEILING LAW, frozen grid only]

Breaker FH5 cross-check: the full table recomputed on the independent
float path matches every T_ff and every n_fail, 10 of 10 rows. Breaker
roam (200 random quartets, d = 24): 24 failures, every one at
T >= 0.85 of the law ceiling; none below.

## 4. Honest scope, unchanged

Gate A is the isolated-quartet restricted model. Against the real zero
set, a single member's negative margin of order c^-4 competes with a
positive critical-line background of order c log c, so no single member
detects anything by itself; detection must come from the family (the fan
mechanism of the grandparent, section 6, or a background-immune Hankel
minor argument). That is exactly the step-3 obligation and it is
untouched by this probe. The probe's contribution is that the family now
EXISTS at an explicit scale: Fourier-favorable on all prime frequencies
(certified on D, grid-supported to d = 48) while remaining a complete
detector in the limit, with the detection range per member quantified by
the ceiling law.

## 5. Verdict and the frozen next action

```text
F1 SURVIVES              [candidate-C at the frozen scale and range]
STOP-GATE                not fired; archived as such.
ROUTE ARMED              the Euler-side hard-edge route enters step 3 with
                         a live family: c_d = (33/4) d + 21, members
                         q^d (q - 1 - theta/c_d^2).
STEP-3 OBLIGATIONS       (i) tail majorant and limit exchange over the
                         infinite zero sum, (ii) detection against the
                         positive critical background above the ceiling
                         frontier T* ~ (2 delta)^(1/3) c^(2/3) (fan over
                         theta and d, or Hankel-minor detection),
                         (iii) multi-quartet competition, (iv) derivation
                         of the ceiling law replacing the measurement.
NEXT LANE                T2 Weyl/Nevanlinna opens now, per the owner's
                         B-then-A order, regardless of this survival.
J7 SOURCE                [O]
RH                       [O]
```

End of result.

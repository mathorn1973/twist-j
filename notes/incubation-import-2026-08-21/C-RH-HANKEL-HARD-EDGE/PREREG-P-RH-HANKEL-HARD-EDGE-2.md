# PREREG P-RH-HANKEL-HARD-EDGE-2

```text
DATE:        2026-08-20 (UTC)
STATUS:      NON-CANONICAL INCUBATION PREREG, no authority
TARGET LINE: private handoff only (mathorn1973/twistj-handoff),
             stacked on agent/rh-hankel-hard-edge head
             593bf1a8f82968f0ebc577c4ddc1b0f29e3fe4d1
PARENT:      P-RH-HANKEL-HARD-EDGE-1 (stop-gate fired), pins:
             PREREG c615a52e1e14a2bc530fee27b0a60d6fcf10c31f5856bc971eaf77eaff5de309
             RESULT 2face7888acf05400d43a6b431e76faa4cb5cd42d3d696abf82472269103058c
             verifier stdout 2458864c934c7d31291c25134712cc52b9721ac61301b34e7b67479e55a70207
GRANDPARENT: RH-T1-GLOBAL-TRANSFORM-ATTACK-2026-08-20.md, sha256 ca6cdfc4...
OWNER CALL:  fork B approved by the owner ("Jo. Prvni jdi na B."):
             one narrow successor before the T2 Weyl/Nevanlinna lane.
PUBLIC GATE: Public Canon v55 ACTIVE, main 362e9c3a, verified this session
             before the HE-1 freeze; nothing public is touched here.
FIREWALL:    no RH claim, no evidence claim for RH, no Canon, Registry,
             Frontier or status movement. J7 SOURCE [O]. RH [O].
LAYER:       L1. No layer lift.
SESSION:     the same named session that owned HE-1 owns this successor.
```

This successor is the narrow probe recorded as fork B in
RESULT-P-RH-HANKEL-HARD-EDGE-1.md: identical double gate, a single scale
change, affine family only, plus the detection-ceiling measurement T*(d).
HE-1 fired its stop-gate at beta = 9/2; the breaker localized the affine
failure to a constant offset. This probe tests exactly that repair. A fresh
freeze is the honest instrument: no threshold inside sealed HE-1 moves.

## Design note, recorded before any computation

The fork-B sketch named beta = 20 from breaker B5, which tested d = 2, 8,
24 only. Extrapolating the HE-1 measured crossings (theta = 0 member:
offset 13.955, 14.099, 14.212, 14.287, 14.315 at d = 2, 4, 8, 16, 24,
against a threshold offset 20 log 2 + 0.0620 d) puts the d = 4 margin at
beta = 20 near +0.01 in x units, untested and within a hair of the
threshold. This freeze therefore takes

```text
beta = 21,
```

which the same extrapolation puts at margin >= +0.5 across all of D, with
the minimum at d = 4. This choice is made now, before any HE-2
computation, and does not move any HE-1 threshold; HE-1 remains sealed
with its fired stop-gate.

## Falsifiers first

```text
FH1  foundations: failure of any of CHECK 0 to CHECK 2. Fires the probe.
FH2  survival claim: if F1 is declared SURVIVES, a certified
     x >= c_d * LOG2_HI with G(x) > 0 for a member on D, or a pinned
     quartet with V >= 0 at the matched member and d = 24.
FH3  method: a demonstrated error in the Sturm/sampling verdicts.
FH4  control: V(alpha_1; F0, d = 24) <= 0.
FH5  ceiling table: any grid point whose exact detection sign disagrees
     with an independent recomputation. Kills the T*(d) table.
```

A fired falsifier or a fired stop-gate is archived, not deleted. No
threshold moves after this freeze.

## Field 1, equation

All objects are those of the HE-1 prereg (carrier k = q(2-q)P(q)^2,
Bessel polynomials R_m, gate polynomial G, exact detection value V), with
one change and two additions.

The change, frozen scale:

```text
c_d = (33/4) d + 21.
```

Families, frozen:

```text
F0  control monomial:  P(q) = q^d
F1  affine hard edge:  P(q) = q^d (q - 1 - theta/c_d^2),
                       theta in Theta = {0, -399/100, -19599/100, -575/16}
```

Chebyshev families are closed by HE-1 (slope excess plus detection
blindness) and do not reappear.

Gate B and Gate A are verbatim HE-1: Gate B is G(x) <= 0 for every
x >= c_d log 2, decided exactly through the enclosure
693147/10^6 < log 2 < 693148/10^6 with the HE-1 gray-zone rule sharpened
by one repair carried from the HE-1 record: the verifier now also
evaluates G exactly at x_hi = c_d LOG2_HI, so a positive value there is a
certified FAIL without breaker help. Gate A is V(alpha) < 0 exactly in
Q(i), asserted into survival at d = 24 for the unchanged quartet set

```text
alpha_1 = 1/10 + 2i,   alpha_2 = 1/10 + 14i,   alpha_3 = 1/4 + 6i,
```

with matched theta_i = Re alpha_i^2. Survival, frozen:

```text
F1 survives iff every member (Theta x D) passes Gate B, D = {2,4,8,16,24},
and the matched member detects all three pinned quartets at d = 24.
```

First addition, frozen: the extended-range Fourier record. At

```text
d in {32, 48}, theta in {0, -399/100},
```

the verifier records a DATA-SCAN of G: exact sign at x_lo, exact signs on
the grid x_lo + j/2 for j = 1..120, and the leading sign. This is labeled
DATA, not a certificate (no Sturm chain at degree near 100 inside the
runtime budget), and does not gate survival.

Second addition, frozen: the detection-ceiling table. For

```text
delta in {1/10, 1/4},   d in {8, 16, 24, 32, 48},
```

and the grid T = k/2, k = 1..100, the matched member
P = q^d (q - 1 - theta/c_d^2) with theta = delta^2 - T^2 is evaluated
exactly at alpha = delta + iT. Recorded per (delta, d): T_ff = the
smallest grid T with V >= 0 (or NONE), and n_fail = the number of grid
points with V >= 0. T*(d) is read as the first-failure frontier. This is
a candidate-C measurement; no functional form is asserted.

## Field 2, code

```text
verify_rh_hankel_hard_edge_2.py
  Python standard library only, exact int/Fraction in every assertion,
  floats nowhere in the file, deterministic output, target under 120 s
  per leg, env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
  TZ=UTC.
  CHECK 0  enclosures (log 2, sqrt 2) and the kappa witness
           33 log 2 > 16 sqrt 2.
  CHECK 1  R_m recurrence equals closed form, m <= 99.
  CHECK 2  spot identities R_0, R_1, R_m(0), m <= 99.
  CHECK 3  Gate B certificates for F0 and F1 x Theta on D, now with the
           exact x_hi evaluation folded into the verdict rule.
  CHECK 3X extended DATA-SCAN at d in {32,48} (reported, never gating).
  CHECK 4  Gate A values at d = 24, the F1 matched-margin table on D,
           and the ceiling table. Verdicts reported, not asserted,
           except the control.
  CHECK 5  control assertion: V(alpha_1; F0, d = 24) > 0.
  Exit 0 iff CHECK 0, 1, 2, 5 pass. Survival and stop-gate are printed
  verdict lines, first-class either way.

breaker_rh_hankel_hard_edge_2.py
  Independent numeric path, floats allowed, no authority. Attacks:
  quadrature check of the Fourier identity; independent crossing
  localization for every D member against the new threshold; independent
  complex-float recomputation of the full ceiling table (FH5 check) and
  of all pinned detection values; a 200-quartet roam at d = 24; a scan
  hunting any Gate B violation on the extended range the DATA-SCAN grid
  might straddle.
```

## Field 3, carrier and data

Purely synthetic restricted zero model, as HE-1: no zeta zero tables, no
external data, no downloads, no floats in assertions. Primes enter only
through the ray [log 2, infinity).

## Field 4, systematics

S1, S2, S3, S5 verbatim from HE-1 (enclosures, one-sided sign method,
finite-range candidate-C labels, determinism), with S2 sharpened: the
sample set now always includes x_hi, so FAIL is certified directly
whenever G(x_hi) > 0; AMBIGUOUS remains only for a feature strictly
inside the gray zone. S4: Gate A asserted into survival only at d = 24;
the ceiling table and margins elsewhere are data. S6, new: the DATA-SCAN
rows are grid evidence only; absence of a positive grid value is not a
certificate and is never cited as one.

## Field 5, failure threshold and stop-gate

```text
F1 fails iff any member has Gate B verdict FAIL or AMBIGUOUS on D, or a
pinned quartet has V >= 0 at the matched member at d = 24.

STOP-GATE, frozen action: if F1 fails, the affine hard-edge route closes
as [F-bounded, AFFINE HARD EDGE] with no further scale successors, and
the lane moves to T2 Weyl/Nevanlinna only. If F1 survives, the route is
ARMED at the measured scale and hands one object to step 3: the tail
majorant over the measured ceiling frontier T*(d); the T2 lane opens
next regardless, per the owner's B-then-A order.
```

Predictions, recorded before any computation, non-binding: F1 passes
Gate B on all of D with minimum margin near d = 4; the ceiling T_ff
increases with d for both deltas and is higher at delta = 1/4 than at
delta = 1/10 for equal d; F0 control stays blind. The functional form of
T*(d) is the measurement, not a prediction.

## Field 6, action layer

L1 throughout. Out of scope, unchanged from HE-1: the summable tail
majorant, limit exchange with the infinite zero sum, multi-quartet
competition, the archimedean term, the full prime sum, every Euler-side
positivity claim.

## Pin plan

Freeze this file and the verifier, record sha256 of both, commit to
branch agent/rh-hankel-hard-edge-2 from 593bf1a8, author
A. M. Thorn <thorn@twistj.com>, BEFORE the first execution. Two legs,
macOS arm64 CPython 3.9 and Linux x86_64 CPython 3.11+, byte-identical
stdout required. Breaker runs after and is committed with its stdout.

End of preregistration.

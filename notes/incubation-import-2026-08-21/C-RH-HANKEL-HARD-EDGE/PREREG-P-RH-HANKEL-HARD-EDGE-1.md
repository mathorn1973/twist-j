# PREREG P-RH-HANKEL-HARD-EDGE-1

```text
DATE:        2026-08-20 (UTC)
STATUS:      NON-CANONICAL INCUBATION PREREG, no authority
TARGET LINE: private handoff only (mathorn1973/twistj-handoff),
             stacked on agent/rh-t1-weight-theorem head
             f2331627b4999364b2689cee455e76b3ebc75f67
PARENT DOC:  RH-T1-GLOBAL-TRANSFORM-ATTACK-2026-08-20.md
             sha256 ca6cdfc4a9f754fc889f0bc141a23fa3434b8a8265a6f0ebfa5145d3507242f6
PARENT LOCK: mathorn1973/twist-j issue #374, C-RH-WEIL-NORM-JUNCTION-1-N
PUBLIC GATE: performed this session before this freeze: Public Canon v55
             ACTIVE, main 362e9c3a9afa9f63005eaf0a1c03baac66617012,
             tag canon-v55 and content commit 6236c10c ancestors of main,
             canon/SHA256SUMS 5 of 5 OK. This probe touches nothing public.
FIREWALL:    no RH claim, no evidence claim for RH, no Canon, Registry,
             Frontier or status movement. J7 SOURCE [O]. RH [O].
LAYER:       L1. No layer lift is requested or implied.
SESSION:     one named session owns this probe.
```

This probe arms the hard-edge construction left open by the parent draft,
section 5.5: the exact open problem is one `c_d`-dependent polynomial family
that simultaneously retains global off-line detection and places all prime
frequencies in a favorable Fourier region. The probe subjects the three
standard families named by the owner (affine, Chebyshev, Jacobi) plus the
monomial control to a frozen double gate at a frozen hard-edge scale.

## Falsifiers first

```text
FH1  foundations: failure of any of CHECK 0 to CHECK 2 (enclosure
     certificates, Bessel-polynomial identity, Fourier normalization
     spot values). Fires the whole probe; nothing downstream is usable.
FH2  survival claim: for a family declared SURVIVES, a certified
     x >= c_d * LOG2_HI with G(x) > 0 for one of its members, or a pinned
     quartet with V >= 0 at the asserted member and d = 24. Kills that
     family's survival verdict.
FH3  gate verdicts: a demonstrated error in the one-sided sign method
     (Sturm count or gap sampling) on any recorded member. Kills every
     Gate B verdict until repaired and rerun as a successor probe.
FH4  control: V(alpha_1; F0, d = 24) <= 0. Kills the blind-spot reading
     of parent (5.20) as implemented here; survival verdicts unusable
     until the mechanism is re-derived.
```

A fired falsifier or a fired stop-gate is archived, not deleted. No
threshold moves after this freeze.

## Field 1, equation

All notation is the parent's. For a zero parameter `alpha` and scale `c`:

```text
q_c(alpha) = c^2/(c^2 - alpha^2),
critical line:  q_c(t) = c^2/(c^2 + t^2), t real, q in (0,1],
carrier:        k_{P,c}(t) = q(2-q) P(q)^2, q = q_c(t).
```

Fourier normalization (parent section 5.4, `hat f(l) = integral f(t)
exp(-i l t) dt`):

```text
FT[q^m](l) = pi c exp(-c l) R_{m-1}(c l),   m >= 1, l > 0,
R_m(x) = theta_m(x) / (2^m m!),
theta_m = Bessel polynomial: theta_0 = 1, theta_1 = x + 1,
theta_m(x) = (2m-1) theta_{m-1}(x) + x^2 theta_{m-2}(x),
closed form R_{m,k} = (2m-k)! 2^k / (4^m m! k! (m-k)!) for the x^k
coefficient.
```

For `k_{P,c} = sum_{m>=1} b_m q^m` define the gate polynomial

```text
G(x) = sum_{m>=1} b_m R_{m-1}(x).
```

Hard-edge scale, frozen rational:

```text
c_d = (33/4) d + 9/2.
```

Rational witnesses, certified in CHECK 0: `33/4 > 4 sqrt(2)/log 2` and
`9/2 > 13 sqrt(2)/(6 log 2)`, via the enclosures
`693147/10^6 < log 2 < 693148/10^6` (LOG2_LO, LOG2_HI) and
`14142/10^4 < sqrt(2) < 14143/10^4`.

Degree set, frozen:

```text
D = {2, 4, 8, 16, 24}.
```

Families, frozen (P is a polynomial in q with rational coefficients):

```text
F0  control monomial:   P(q) = q^d
F1  affine hard edge:   P(q) = q^d (q - 1 - theta/c_d^2),
                        theta in Theta = {0, -399/100, -19599/100, -575/16}
F2  Chebyshev:          P(q) = T_d(2q - 1)
F3  Jacobi, second-kind normalization: P(q) = U_d(2q - 1)
```

`T_d`, `U_d` are Chebyshev polynomials of the first and second kind by the
standard recurrence with integer coefficients. `U_d(2q-1)` is the Jacobi
`(1/2,1/2)` member up to positive normalization; other Jacobi parameters
are successor work, not this probe.

Pinned off-critical quartets and matched affine parameters
(`theta_i = Re alpha_i^2 = delta^2 - T^2` exactly):

```text
alpha_1 = 1/10 + 2i,    theta_1 = -399/100
alpha_2 = 1/10 + 14i,   theta_2 = -19599/100
alpha_3 = 1/4 + 6i,     theta_3 = -575/16
```

GATE B (Fourier sign). A member passes at degree `d` iff

```text
G(x) <= 0 for every x >= c_d log 2,
```

decided exactly through the frozen enclosure with the gray-zone rule of
Field 4. Passing Gate B places every prime frequency `log p^k >= log 2`
in the favorable region for that member.

GATE A (detection). For a pinned quartet `alpha` and a member `P` at
scale `c_d`, with `q = q_{c_d}(alpha)` computed exactly in `Q(i)`:

```text
V(alpha; P, c_d) = 2 Re[ q (2-q) P(q)^2 ].
```

The member detects `alpha` iff `V < 0` exactly.

SURVIVAL, frozen definition. Family F survives iff

```text
(i)  every member of F passes Gate B at every d in D, and
(ii) at d = 24, V(alpha_i) < 0 for i = 1, 2, 3, where the tested member
     is: F1 the matched member theta = theta_i; F2, F3 the single member.
```

F0 is a control, not a survival candidate.

Heuristic recorded as [R], explicitly NOT asserted and not a gate: the
asymptotic transfer `G(x) ~ -R_n(x) * rho^(-n-1) * [q(q-2)P(q)^2]_{q=rho}`
with `rho = rho(x,n) ~ (n + sqrt(n^2+x^2))/(2n)` suggests the universal
threshold `rho = 2`, i.e. the same `4 sqrt(2)/log 2` slope for every
squared-polynomial family, with family-dependent finite-d corrections.
The probe measures those corrections; it does not assume them.

## Field 2, code

```text
verify_rh_hankel_hard_edge_1.py
  Python standard library only, runs from the probe directory, no
  arguments, no network, no data files. Every assertion uses int or
  Fraction; floats appear only in labeled witness printouts, never in
  an assertion. Target runtime under 120 seconds per leg. Environment
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
  Checks:
  CHECK 0  enclosure certificates for log 2 and sqrt 2, and the two
           hard-edge witness inequalities for 33/4 and 9/2.
  CHECK 1  R_m by recurrence equals R_m by closed form, all m <= 51.
  CHECK 2  Fourier spot identities: R_0 = 1, R_1 = (1+x)/2,
           R_m(0) = C(2m,m)/4^m for all m <= 51.
  CHECK 3  Gate B verdict PASS/FAIL/AMBIGUOUS for every member of
           F0..F3 at every d in D, by the one-sided sign method of
           Field 4. Verdicts are reported, not asserted.
  CHECK 4  Gate A exact values V(alpha_i) for all families at d = 24,
           and the F1 matched-margin table over all d in D (data).
           Verdicts reported, not asserted, except the control.
  CHECK 5  control assertion: V(alpha_1; F0, d = 24) > 0.
  Exit 0 iff CHECK 0, 1, 2, 5 all pass. Survival and stop-gate are
  printed verdict lines, first-class either way, never an exit failure.

breaker_rh_hankel_hard_edge_1.py
  Independent numeric path, floats allowed, no authority, no shared
  helper code with the verifier beyond the family definitions restated.
  Attacks: numeric quadrature of the Fourier transforms against the
  R-polynomial values; dense numeric scan for Gate B sign violations
  above threshold; independent complex-float recomputation of every
  V(alpha_i); a roam over random quartets delta in (0,1/2), T <= 30
  hunting a quartet whose matched F1 member fails detection at d = 24;
  a roam over extreme theta hunting a Gate B failure the pinned grid
  missed. Discrepancies are reported, they do not gate.
```

## Field 3, carrier and data

Purely synthetic restricted zero model. No zeta zero tables, no external
data, no downloads, no floats in assertions. Primes enter only through
the frequency ray `[log 2, infinity)`; no individual prime data is used.
Nothing in this probe opens the archimedean term.

## Field 4, systematics

```text
S1  Enclosures. LOG2_LO/HI certified in-run by exact Taylor bounds of
    exp with the geometric remainder x^(K+1)/((K+1)!(1-x)), K = 30;
    sqrt 2 by integer squaring. Gray zone: if the Gate B decision for a
    member depends on the subinterval [c_d LOG2_LO, c_d LOG2_HI), the
    verdict is AMBIGUOUS and counts as FAIL for survival.
S2  One-sided sign method. G is cleared to integer coefficients. The
    Sturm chain of (G, G') counts distinct real roots in (x_lo, +inf),
    x_lo = c_d LOG2_LO. Roots are bisection-isolated below the Cauchy
    bound; G itself is evaluated exactly at x_lo, at one rational point
    in each gap between consecutive isolating intervals, and at one
    point beyond the last root. PASS iff every evaluated value is <= 0
    and the sign at +inf is negative; FAIL iff some evaluated value is
    > 0 at a point >= c_d LOG2_HI; otherwise AMBIGUOUS.
S3  Finite range. Every Gate B and Gate A verdict is a computation at
    the frozen finite ranges D and quartet set; every outcome label is
    candidate-C at that range. No claim beyond the ranges is made.
S4  Detection regime. Gate A is asserted into survival only at d = 24,
    where |alpha_i^2|/c_24^2 <= 196/41006 is small; smaller d values
    are recorded as data on margin scaling, not gated.
S5  Determinism. Output contains only exact integers, exact fractions,
    fixed strings, and 6-significant-digit decimal witnesses computed
    by integer arithmetic; identical bytes are required on both legs.
```

## Field 5, failure threshold and stop-gate

```text
A family fails iff any of its members has Gate B verdict FAIL or
AMBIGUOUS at any d in D, or a pinned quartet has V >= 0 at d = 24 at
the member named in the survival definition.

STOP-GATE, frozen action: if none of F1, F2, F3 survives, the
standard-family hard-edge route is closed as
[F-bounded, STANDARD HARD-EDGE FAMILIES] and the lane re-targets the
T2 Weyl/Nevanlinna construction. The verdict is archived either way.
```

Predictions, recorded before any computation, non-binding and worthless
as evidence: F0 passes B and fails A (control). F1 passes both and is
the expected sole survivor; its small-d Gate B verdicts for the large
|theta| members are the least certain entries. F2 and F3 are expected
blind at alpha_1 and alpha_2 (limit value of P at the off-line point is
a bounded cosh/sinc-type expression whose squared real part is
generically positive), with alpha_3 near a narrow detection window;
expected verdict fail on Gate A.

## Field 6, action layer

L1 throughout. Explicitly out of scope, left to successor probes: the
summable tail majorant and the exchange of limit with the infinite zero
sum, competition among several off-critical quartets, the archimedean
term, the full prime sum, and every Euler-side positivity claim. This
probe outputs gate verdicts and margin scaling data only.

## Pin plan

Freeze this file and the verifier, record both sha256, commit to branch
`agent/rh-hankel-hard-edge` from f2331627 in the private handoff
repository, author `A. M. Thorn <thorn@twistj.com>`, before the first
execution of the verifier. Two legs: macOS arm64 CPython 3.9 and Linux
x86_64 CPython 3.11+, byte-identical stdout required; a single-leg or
non-identical result is at most a candidate-C single-platform record.
The breaker runs after the verifier and is committed with its stdout.

End of preregistration.

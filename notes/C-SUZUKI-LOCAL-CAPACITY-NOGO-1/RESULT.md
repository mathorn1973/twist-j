# C-SUZUKI-LOCAL-CAPACITY-NOGO-1: frozen run, all gates passed

```text
STATUS   incubation candidate, NO AUTHORITY; candidate labels only.
DATE     2026-08-13 (UTC)
SESSION  the 2026-08-13 prime-capacity session (single named session).
BASIS    Public Canon v46, twist-j main 6545c1d0, gate 5/5 OK at freeze.
PREREG   PREREG-C-SUZUKI-LOCAL-CAPACITY-NOGO-1.md
         sha256 37cc1a43238a4b076578a59b70009628d61b31f9da126b7e02662cdaad1d8218
         14340 B, frozen before the verifier was written.
VERIFIER verify_suzuki_local_capacity_nogo_1.py
         sha256 c68381aff92bd6b01d2170e40d1d82da909f7ec11c3f597516da8c1c1e128ddb
STDOUT   sha256 ad99e73f827fbc075342d93fbc8e840c05cba8764c99b5c26bedf37b46050a84
         1054 B, 12 of 12 gates PASS, exit 0, empty stderr, wall 0.67 s,
         Linux x86_64, Python 3, env LC_ALL=C LANG=C
         PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
         Second execution on the same platform: stdout byte-identical.
         SINGLE ARCHITECTURE ONLY: per house rules the computed legs stay
         at candidate-C evidence grade until a second-architecture leg runs
         (public probe material, not rerun here).
BREAKER  breaker_suzuki_local_capacity_nogo_1.py (independent mpmath path)
         sha256 f624e530b53c94c2f40d355dd26d0a038518e2d2162f81c6a9ac1abc77f65e55
         stdout sha256 9819e011f74b12b3f78ef88c96b77f14fd18a738cd0b0675ce5eb03943bb8a6e
         exit 0: zero breaks, all independent recomputations agree.
DEFECTS  three verifier defects found in static review BEFORE the formal
         run (S-series stop condition, one leftover expression, a
         hard-coded gate count) and fixed; no formal gate was executed
         before the fix. Recorded here per integrity discipline.
CONTEXT  Mittermeier v5 record verified this session from owner-supplied
         files (pdf sha256 37e8642b..., zip sha256 c86eb077..., internal
         SHA256SUMS 30 of 30 OK); consumed as attribution and cross-check
         values only, not as gate input.
```

## Result by claim

```text
N1  PRIME CURVE            candidate-T   proof + gate V1 PASS
    For any event family: ||Y_t||^2 = F(t), <Y_s,Y_t> = F(min),
    orthogonal increments, ||Y_t - Y_u||^2 = F(t) - F(u).
    Proof: componentwise, <Y_t, Y_u> = sum_q w_q^2 |[tau_q,t] cap
    [tau_q,u]| = sum_q w_q^2 (min(t,u) - tau_q)_+ = F(min); (iii) and
    (iv) follow by bilinearity from (ii). Exact surrogate check plus a
    firing negative control (1/16 != 0).
R2  CURVATURE + PLASTIC    candidate-T   reproduction of M-4; V2a, V2r,
    V2b PASS. A''(log 2) encloses 5 sqrt2/6, A''(log 3) encloses
    23 sqrt3/24 (M-5 eq. 12); h(13/10) = -103/1000 < 0 < 1/27 = h(4/3),
    so rho_plastic in (13/10, 4/3) and log rho < log 2;
    A''(1/4) <= -0.227215... < 0; A''(log 2) > 0.
N3  RAMP CLASS EMPTY       candidate-T; the class carries candidate-F.
    V3 PASS: (A(1/4)-A(1/20))(1/4) >= 0.002382 > -0.002214 >=
    (A(1/2)-A(1/4))(1/5): certified three-point convexity violation.
    Every member of {c0 + c1 t + integral (t-a)_+ dmu, mu >= 0} is
    convex; A is not convex on (0, 1/2); the class is EMPTY. Breaker:
    best nonnegative-ramp fit misses A by 2.5e-2 max residual
    (readout), and 55 of 137 grid triples show decreasing slopes: the
    violation is broad, not knife-edge.
N4  FILTRATION + DOMINATION KILLS   candidate-T   V4a, V4b PASS.
    A(1/4) >= 0.051233 > 0.040163 >= A(1/2): dA is not a nonnegative
    measure, no filtration model exists on (0, log 2). At the first
    event: certified dP >= 0.052371 > 0.031051 >= dA on [log 2, 4/5]
    (P is the single exact ramp (log2/sqrt2)(t - log2) there):
    increment domination dies at q = 2. Corollary: no nonnegative
    per-place budget decomposition of dA dominates the prime ramps.
N5  BOTH SCREW KERNELS INDEFINITE   candidate-T   V5 PASS.
    4A(3) - A(6) <= -35.854 < 0, 4P(3) - P(6) <= -35.964 < 0, both
    functions positive at 6; event-boundary guards e^3 in (20,23),
    e^6 in (401,409) certified. Neither the capacity nor the prime
    side alone is a screw geometry; only the difference can be.
R6  PRIME-FREE WINDOW      candidate-C   reproduction of a corner of
    M-5 Thm 1.1 by an independent code path. V6 PASS: A > 0 certified
    on [1/128, 45/64] by a 100-leaf adaptive cover, zero undecided.
    Breaker grid minimum 0.01348 at the left edge (readout).
R7  EVENT COUNT            candidate-C   V7 PASS: N(10^6) = 78734 by
    two independent counting paths, exact integer equality (method of
    M-5 claim C3 at small X).
N8  NORM ONE FORCED        candidate-T by proof; no machine gate.
    ||T|| <= 1 - delta forces Psi >= delta(2-delta) A ~ 4 delta e^(t/2),
    against Psi = o(e^(t/2)) from PNT (named import) via
    P(t) = integral_0^t sum_(n <= e^u) Lambda(n) n^(-1/2) du and
    partial summation. Hence norm exactly 1, asymptotically isometric.
X   MACHINERY CROSS-GATES  X1, X2 PASS: psi(3/4) - psi(1/4) encloses
    pi; psi'(1/4) + psi'(3/4) encloses 2 pi^2. Breaker cross-checks
    the verifier constants against M-5 printed values (42), (43) at
    1e-15 by a third route (mpmath): agreement.
```

## Consequence carried in scope (no new claim)

The local capacity factorization is impossible: the completion capacity is
not a positive superposition of prime-type ramp atoms (N3), admits no
filtration or per-place domination reading (N4), and is not itself a screw
geometry (N5); any Gram realization dominating the prime curve has norm
exactly one (N8) and must be nonlocal in t. Together with the recon 11.2
diagonal-model lemma (bare existence of a contraction pair is verbatim RH),
every remaining question in this complex lives in the frozen canonicity
class of the decoder frame. RH is untouched; nothing here moves it.

## Break attempts (recorded)

```text
B1  slope scan for vanishing convexity violation: violation broad
    (55/137 triples), max gap 0.2529 near t = 0.01. Not broken.
B2  nonnegative-ramp least squares on [1/50, 3/5], 30 knots, free
    affine part: max residual 2.54e-2, five orders above the 1e-6
    break threshold. Not broken.
B3  window positivity scan, 3000 points: min 0.01348 > 0. Not broken.
```

## Next steps (owner decisions)

```text
1  PROMO-C-SUZUKI-LOCAL-CAPACITY-NOGO-1: package for a public probe
   (adds the issue claim and the two-architecture byte-identity leg;
   the verifier is stdlib-only and runs in 0.67 s, well under the
   120 s budget). Proposed public claim name: SUZUKI-LOCAL-CAPACITY-NOGO.
2  Lane B (C-SUZUKI-COMPLETION-GRAM-N) stays blocked on the G0 domain
   freeze and a full read of arXiv 2606.09096 and 2607.24830.
3  The scalar tail stays with M-5 obligations 7.4 and 8.1; no census.
```

# PREREG P-RH-WEYL-CANONICAL-2

```text
STATUS:   NON-CANONICAL INCUBATION PREREGISTRATION, no authority
PROBE:    P-RH-WEYL-CANONICAL-2 (T2 lane, successor to obligation O5 of
          P-RH-WEYL-CANONICAL-1 as re-specified by
          CORRECTION-P-RH-WEYL-CANONICAL-1)
LANE:     T2 Weyl/Nevanlinna (consolidation #374), model side only
OWNER:    one named session; frozen BEFORE first execution of the
          frozen grid; pinned on branch agent/rh-weyl-canonical-2
          above the correction head a3509c9
FIREWALL: no RH claim, no zeta claim. Every statement is about the
          finite free Jacobi model. J7 SOURCE [O]. RH [O]. Public
          Canon v55 untouched.
```

Purpose. Replace the dropped finite-node detection claim of the lane
opener by the exact object: the rank-two threshold map. For four
frozen node designs and a frozen defect grid, compute exact block
quadratics and certified enclosures of the detection threshold
w*(x, delta; design, m), m to 24, and the detection depths N* at two
frozen weights. Detection semantics: strictly negative direction only;
a zero is the boundary. Results are restricted to the frozen grid; for
every finite design w* > 0, so no finite design detects arbitrarily
weak defects, and no uniform claim is in scope at any N.

## Prior knowledge, admitted before the freeze

This probe is partially confirmatory, not blind. Known before freeze:

```text
K1  Pinned WEYL-1 outcomes at 8 chain nodes: D1 undetected, D2
    detected at N* = 6, D3 undetected.
K2  Breaker 1b exact thresholds at N = 8 on the chain:
    w*(D1) = 1.709752e-1, w*(D2) = 1.800331e-2, w*(D3) = 2.141727e+1
    (6-digit roundings of exact bisection brackets).
K3  Owner-reported (owner computation, parametrization possibly
    differing from the designs frozen here): D1 reaches N* ~ 11 on the
    1 + 1/n chain; ~ 11 on a range-matched spread; 9 to 10 on
    lower-shifted node windows.
```

The ONLY gated prediction is the ND1 window in FW-C below (the chain
here extends the WEYL-1 chain exactly, so K3's chain number applies).
K3's spread and shifted numbers are context, NOT gated: the frozen ND2
and ND3 below need not match the owner's parametrizations. ND4 has no
prior and is a pure map.

## Falsifiers first

```text
FW-A  instruments: failure of CHECK 0 (foundations: distinct upper
      half-plane nodes, strictly positive background pivots for all
      four designs), CHECK 1 (rank-two determinant identity against
      direct exact determinants at the frozen sample cells), or
      CHECK 2 (D_m >= 0 for every block, every cell, every design).
      Frozen action: [F-bounded, T2 INSTRUMENTS], exit 1, redesign
      before any zeta-side work.
FW-B  consistency: failure of CHECK 3 (reproduction of the pinned
      WEYL-1/1b chain results at m <= 8: D1 sign +, D2 N* = 6, D3
      sign +, and the three w* brackets inside the frozen K2 anchor
      intervals). Frozen action: [F-bounded, T2 INSTRUMENTS], exit 1;
      both records archived, discrepancy is the finding.
FW-C  prediction: CHECK 4 fails, i.e. N*(D1, ND1, w = 1/10) is not in
      [9, 13]. Frozen action: the prediction row is recorded
      candidate-F, verdict line "PREDICTION F, MAP STANDS", exit 1;
      the map itself remains the record.
FW-D  depth: CHECK 5 fails, i.e. D1 (x = 1/3, delta = 1/10) is
      undetected at w = 1/10 at depth 24 on ALL FOUR designs. Frozen
      action: [F-bounded, DEPTH READING], exit 1: the narrowed E4
      reading of the correction fails at these depths and the wall is
      recorded as data.
```

Decision tree, frozen (per the E2 binding rule of the correction,
every firewall has an action and instrument branches are tested
first): if FW-A or FW-B fired then [F-bounded, T2 INSTRUMENTS];
else if FW-D fired then [F-bounded, DEPTH READING] (and if FW-C also
fired, both lines print); else if FW-C fired then "PREDICTION F, MAP
STANDS"; else "MAP RECORDED, all gates pass". Exit 0 iff no check
failed, else exit 1. A fired falsifier is archived, not deleted; no
threshold moves after this freeze.

## Field 1, equation (frozen instruments and designs)

Background model: free Jacobi J_R, a_k = 1/2, b_k = 0, R = 64
throughout; Q_R(z) = e1^T (J_R - z)^{-1} e1 by exact tridiagonal
elimination over Q(i).

Defect (conjugate pole pair, A4 orbit analogue): mu = x + i delta,
weight w > 0:

```text
Q_w(z) = Q(z) + w ( 1/(mu - z) + 1/(conj mu - z) )
```

Rank-two threshold theorem, adopted [candidate-T] in
CORRECTION-P-RH-WEYL-CANONICAL-1 E5. Pick designs (ND1, ND2, ND3),
nodes z_j = i a_j: P(w) = P0 + w(AB* + BA*) with A_j = 1/(mu - z_j),
B_j = 1/(conj mu - z_j); for each leading m-block

```text
det P(w)_m / det P0_m = 1 + 2 w Re(gamma_m) - w^2 D_m
alpha_m = A* P0m^-1 A,  beta_m = B* P0m^-1 B,  gamma_m = A* P0m^-1 B,
D_m = alpha_m beta_m - |gamma_m|^2 >= 0
```

computed via one exact LDL* of P0 at m = 24 and prefix sums of the
forward substitutions (the leading blocks of an LDL* are nested).

One-point design (ND4), symmetric variant, derived and frozen here:
moments q_s = e1^T (J_64 - c)^{-(s+1)} e1 at c = 5/4, s <= 47; Gram
H_{mn} = q_{m+n+1} (m, n = 0..23), PSD for any positive background
measure; defect vector a_m = A^{m+1} with A = 1/(mu - c); the defect
adds w (a a^T + conj a conj a^T), a REAL symmetric rank-two update,
and with s_m = a^T Hm^-1 a (complex), h_m = a^T Hm^-1 conj a (real,
equal to the Hermitian norm a* Hm^-1 a):

```text
det H(w)_m / det H_m = 1 + 2 w Re(s_m) - w^2 (h_m^2 - |s_m|^2)
h_m^2 - |s_m|^2 >= 0, equality iff a is proportional to conj a,
which for A not real (delta > 0) forces m = 1 only
```

so the same threshold machinery applies with Re(gamma_m) := Re(s_m),
D_m := h_m^2 - |s_m|^2.

Degenerate blocks: D_1 = 0 identically (a 1x1 block sees parallel
vectors); wherever D_m = 0 the law is linear, threshold
w*_m = -1/(2 Re gamma_m) if Re gamma_m < 0, else no finite threshold
(printed inf).

Detection semantics (correction E6, frozen): defect detected at depth
m iff 1 + 2 w Re(gamma_m) - w^2 D_m < 0 STRICTLY; exact zero is
boundary, reported, never counted as detection. N*(w) = least such m,
or none. w*_m enclosed by dyadic bisection, 40 iterations, from [0, 1]
with doubling.

Frozen node designs (descending distance from the real axis, matching
the WEYL-1 chain order; the block order is part of the design):

```text
ND1  chain:   a_n = 1 + 1/n,          n = 1..24   (first 8 = WEYL-1)
ND2  spread:  a_j = 1 + (25 - j)/24,  j = 1..24   (equispaced 2..25/24)
ND3  shifted: a_j = (30 - j)/24,      j = 1..24   (equispaced 29/24..1/4)
ND4  one-point Gram at c = 5/4 as above, blocks m = 1..24
```

Frozen defect grid: x in {1/10, 1/3, 3/5, 4/5, 9/10}, delta in
{1/10, 1/100} (10 cells; includes the WEYL-1 defects D1 = (1/3, 1/10),
D2 = (9/10, 1/10), D3 = (1/3, 1/100)). Frozen weights for N* rows:
w in {1/10, 1/100}. Reported threshold depths: m in {8, 12, 16, 20,
24} plus min over m <= 24 (elementwise-min enclosure).

## Field 2, code

```text
verify_rh_weyl_canonical_2.py
  Python standard library only, exact arithmetic (Fraction, Q(i)
  pairs), no float in any assertion; dec6 integer-computed witnesses;
  deterministic output; run from repo root with LC_ALL=C LANG=C
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC; target well under
  120 s (prototype of the machinery on variant data: ~3 s at full
  scale). Two legs, byte-identical stdout required (macOS arm64 and
  Linux x86_64).

  CHECK 0  foundations: 24 distinct nodes per Pick design, all in the
           upper half plane; background LDL pivots strictly positive
           to m = 24 for ND1, ND2, ND3; ND4 Gram pivots strictly
           positive to m = 24.
  CHECK 1  identity: for every design, cells (1/3, 1/10) and
           (4/5, 1/100), block m = 12, w in {1/10, 1/17}: direct exact
           determinant of the perturbed leading block equals
           det(P0_12) * (1 + 2 w Re gamma_12 - w^2 D_12) exactly
           (16 determinant comparisons).
  CHECK 2  Cauchy-Schwarz: D_m >= 0 for all m = 1..24, all 10 cells,
           all 4 designs.
  CHECK 3  WEYL-1/1b consistency on ND1 restricted to m <= 8:
           D1 not detected at w = 1/10 within 8; D2 N* = 6 at
           w = 1/10; D3 not detected at w = 1/100 within 8; and the
           three w*_8 brackets lie inside the frozen anchor intervals
           (the pinned 1b 6-digit values widened by 2 ulp on each side
           so a rounding-boundary epsilon cannot fire the gate; any
           real discrepancy misses by far more)
           D1 (1709750/10^7, 1709754/10^7),
           D2 (1800329/10^8, 1800333/10^8),
           D3 (2141725/10^5, 2141729/10^5).
  CHECK 4  prediction window: N*(D1, ND1, w = 1/10) in [9, 13].
  CHECK 5  depth stop-gate: D1 detected at w = 1/10 by m <= 24 on at
           least one of the four designs.

breaker_rh_weyl_canonical_2.py
  Independent attack, floats allowed, no authority. Planned paths:
  full float recomputation of the map (dense float LDL, no exact
  reuse); exact direct-determinant bisection of w* at pinned spot
  triples (no LDL, no prefix sums) compared against the verifier's
  brackets; an inertia attack hunting w with two or more negative
  eigenvalues (leading-minor sign count, exact at flagged points),
  which the theorem forbids; a roam over random rational defect cells
  hunting D_m < 0 or tiny D_m (ill-conditioning stress); independent
  numeric re-derivation of the ND4 symmetric law via the 2x2
  det(I + w C^T H^-1 C).
```

## Field 3, carrier and data

Purely synthetic finite model. No zeta zeros, no external data, no
downloads. Nothing here evaluates or approximates any arithmetic
object. All inputs are the frozen rationals above.

## Field 4, systematics

```text
S1s  Exactness. All gates exact rational or Q(i) pair arithmetic; the
     only nonrational reals entering any assertion are avoided
     entirely (no square roots are needed: detection is the sign of a
     rational quadratic; w* enclosures are dyadic brackets).
S2s  Enclosures. w* brackets by 40 dyadic bisection steps; stated
     width <= (initial hi) * 2^-40; anchors in CHECK 3 are open
     rational intervals from the pinned 1b roundings.
S3s  Finite range. All verdicts candidate-C at the frozen designs,
     grid, weights and m <= 24. No claim beyond the ranges; no
     uniform-in-defect claim at any m.
S4s  Order dependence. N* and the block map depend on the frozen node
     ORDER (leading blocks); this is part of the design, stated, not
     a defect.
S5s  Determinism. Output is fixed strings, integers, exact fractions
     and dec6 integer-computed witnesses; byte-identical on both legs.
S6s  Model scope. Every statement is about the finite free Jacobi
     model with an added non-Herglotz defect. The zeta side stays in
     obligations O1-O3 of the lane, untouched here.
```

## Field 5, failure threshold and stop-gate

The probe PASSES iff CHECK 0..5 all pass; then the verdict is "MAP
RECORDED, all gates pass" and the map rows are the record
[candidate-C]. Otherwise the frozen decision tree under "Falsifiers
first" applies verbatim. A fired FW-C or FW-D is a first-class
outcome: merged, archived, threshold unmoved. The w* map rows
themselves remain valid data under every branch except FW-A/FW-B
(instrument failure invalidates the map of the failing design).

## Field 6, action layer

L1 (state-level model computation). No layer lift. Any zeta-side use
of the map is successor work under its own gate.

## Execution plan, frozen

Pin this prereg and the verifier on branch agent/rh-weyl-canonical-2
(from the correction head a3509c9) BEFORE first execution. Two legs:
macOS arm64 CPython 3.9.6 and Linux x86_64 CPython 3.11.15,
byte-identical stdout. Then the breaker (single leg allowed), then
RESULT-P-RH-WEYL-CANONICAL-2.md, then a draft PR with base
agent/rh-weyl-canonical. Commit identity A. M. Thorn
<thorn@twistj.com>.

End of preregistration.

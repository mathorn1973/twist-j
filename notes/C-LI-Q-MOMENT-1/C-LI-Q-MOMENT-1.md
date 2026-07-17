# C-LI-Q-MOMENT-1. The pole-chart moment interface, the ladder junction, and the counting selection for a J-native q_n

```text
CANDIDATE ID:   C-LI-Q-MOMENT-1
DATE:           2026-07-17
TARGET ROWS:    J-LI-W-CHART-EQUIVALENCE
                J-LI-SIGMA-HANKEL-DICTIONARY
                J-LI-LADDER-JUNCTION
                J-LI-Q-CALIBRATION-LADDER
                J-LI-Q-COUNTING-GATE
                J-LI-Q-ANALYTIC-NUCLEAR-NOGO
                J-LI-Q-CARRIER-SMOOTHNESS-SELECTION
                J-LI-Q-MOMENT-REALIZATION
PARENTS:        C-LI-S2-RELATIVE-DETERMINANT-1 (frozen prereg predefinition
                P-J-LI-S2-RELATIVE-DETERMINANT-1); C-PENTAGON-WEIL-1;
                C-LI-COCYCLE-1 through amendment 4; notes/j-li-schoenberg-2
                (Fejer carrier draft and lane consolidation REV4)
LAYER:          L5 finite exact statements and exact dictionaries; the
                realization target is L6; no lift is claimed or created
AUTHORITY:      none. NON-CANONICAL candidate document under POLICY.md.
PUBLIC STATUS:  no registry row, no Canon promotion, no formal probe.
RH:             O.
```

## 0. Result and non-result

The parent candidate fixed the operator class of an all-n positive Li
realization and installed the Stieltjes-Hankel ladder on the chart
`x = t^2`.  Its closing line demands a J-derived positive moment
functional.  This candidate builds the exact interface that any such
proposal must hit, and it selects the chart on which the reference side
is already computable with the machinery this program has pinned:

```text
1. The pole chart w = s(1-s).  The Xi zeros collapse pairwise to
   y_rho = rho(1-rho); RH is equivalent to double shifted-Hankel
   positivity of the pole-chart moments qw_n (section 3), by the same
   proof spine as the parent's section 9.
2. The sigma dictionary.  qw_(m-1) is an exact integer-triangular
   combination of the pole power sums sigma_j = sum_rho rho^(-j)
   (section 4).  The reference ladder therefore needs NO new analytic
   machinery through the current sigma depth.
3. The ladder junction.  Exactly and with no analysis:
       qw_0 = sigma_1 = lambda_1,
       qw_1 = 2 sigma_1 + sigma_2 = M_1,
   where M_1 is the pinned T_1 Toeplitz gate margin of the cocycle lane.
   The first two Hankel gates of the moment lane are ALREADY CLOSED at
   candidate grade by the existing lambda_1 and M_1 interval pins.  The
   two falsification ladders meet at their first rungs (section 4).
4. The next razor.  The first genuinely new finite gate is the 2x2
   determinant SH-1 with the exact expression
       det H_1^(0) = qw_0 qw_2 - qw_1^2,
       qw_2 = sigma_3 + 3 sigma_2 + 6 sigma_1,
   evaluable from the already-derived sigma_3 once a gamma_2 bracket of
   width about 1e-9 is pinned; expected magnitude about 2e-9 (section 5).
5. Exact chart transforms.  The Catalan reversion tying the owner's
   xi(1+t) germ machinery to the w-chart, the g-to-q recursion, and the
   eigenvalue-level Moebius map to the parent's frozen x-chart operator
   (section 6).
6. The counting gate and two no-gos.  The forced two-term counting law
   for the moment measure, the Schatten boundary in the w-chart, a
   theorem-grade exclusion of analytic-nuclear (exponential singular
   value) carriers, and the finite-smoothness selection principle that
   survives it (section 7).
7. The pentagon stream at the q-interface.  The exact coefficient-level
   content of Z_J = P_0/f_5 for the log-derivative stream that generates
   every q ladder, machine-pinned through n = 125 (section 8).
8. A route map for the J-native construction with a frozen kill order
   (section 9), and an exact stdlib verifier for every finite dictionary
   above (section 10).
```

It does **not** construct `A_J`, `B_J`, or any J-native moment
functional.  It does not prove RH.  It narrows and instruments the
target; it does not enter it.  All target rows remain unregistered; the
realization row and RH remain O.

## 1. Falsifiers first

A proposed J-native moment functional q (equivalently a positive
operator, equivalently a Stieltjes measure) fails on the first
occurrence of any of the following.

1. Any exactly derived shifted Hankel matrix of the proposal has a
   negative direction (either family, any order).
2. The proposal's `qw_0` interval misses the pinned `lambda_1` interval,
   or its `qw_1` interval misses the pinned `M_1` interval.  These are
   the junction kill tests; they cost nothing new.
3. The proposal carries a continuous scale, gauge, or normalization
   parameter tuned after seeing reference data.  The chart variable
   `w = s(1-s)` and the normalization `G(0) = 1` leave no scale freedom;
   a fitted scale is COCYCLE-BY-FINITE-FIT in moment language.
4. The counting function of the proposed spectrum violates the forced
   two-term law of section 7 (leading term or second term).
5. The proposed operator lies in the exponential singular-value class
   (analytic-nuclear, order zero); excluded by section 7 regardless of
   construction provenance.
6. The trivial C4 sector uses raw `P_0` rather than `Z_J = P_0/f_5`, or
   the ramified tower at 5 fails the exact coefficient accounting of
   section 8.
7. Zeta, Xi, a zero list, a prime table, Li coefficients, sigma_k
   values, or the standard Weil form enters the construction as an
   undeclared input (G7 of the frozen prereg).  Reference data live only
   in the comparator.
8. The proposal asserts the unsquared real determinant without the
   polarization of the parent candidate, or changes the frozen chart
   conventions of section 3 after seeing outputs.

Failure of a proposal before the terminal identity kills that proposal,
not RH.  The negative-vector discipline of the pentagon ledger applies
unchanged.

## 2. Imported classical inputs

The analytic statements below import, and do not reprove:

- Li's criterion and the Lagarias asymptotic for lambda_n (as already
  imported by the parents);
- the Hadamard product of xi over paired zeros, xi(0) = 1/2, and the
  reality/functional-equation pairing of the zeros;
- the Stieltjes moment theorem (double shifted-Hankel positivity
  characterizes Stieltjes moment sequences) and determinacy for
  compactly supported moment problems;
- the Vivanti-Pringsheim positivity argument and analytic continuation
  on the slit plane, as organized in the parent's section 9;
- the Riemann-von Mangoldt counting law with its error term;
- the classical closed forms of sigma_1, sigma_2, sigma_3 in gamma,
  gamma_1, gamma_2, zeta(3), pi as already derived and pinned in
  C-LI-COCYCLE-1 amendment 3;
- the exponential singular-value decay of nuclear-order-zero transfer
  operators with holomorphic contracting kernels (Grothendieck; Ruelle;
  Mayer; Bandtlow-Jenkinson) for section 7 only.

The included verifier checks only finite exact dictionaries; it promotes
no imported theorem into a TWIST-J result.

## 3. The pole chart

### 3.1 Definitions, frozen

Write the paired Hadamard product with the standard pairing and
`xi(0) = 1/2`.  Freeze the chart

```text
w := s(1-s),        y_rho := rho(1-rho),
```

and the upper-zero multiset `{ y_rho : Im rho > 0 }`, each zero with its
multiplicity.  This multiset is conjugation-closed, and exactly

```text
1 - w/y_rho = (1 - s/rho)(1 - s/(1-rho)),
```

because `y_rho - w = (rho - s)((1-rho) - s)`.  Therefore, defining

```text
Gw(w) := xi(s)/xi(0)  read as a function of w,
```

Gw is entire of order 1/2 in w, `Gw(0) = 1`, and

```text
Gw(w) = prod_(Im rho > 0) (1 - w/y_rho)
```

converges absolutely (genus zero; sum of |y_rho|^-1 converges by the
zero count).  Freeze the moment stream

```text
-Gw'(w)/Gw(w) = sum_(n>=0) qw_n w^n     near w = 0,
qw_n = sum_(Im rho > 0) y_rho^(-(n+1)),
```

absolutely convergent for n >= 0, real by conjugation closure.

### 3.2 Equivalence

```text
RH  <=>  (qw_(i+j))_(i,j=0..N) >= 0  and  (qw_(i+j+1))_(i,j=0..N) >= 0
         for every N.
```

Proof is the parent's section 9 argument verbatim on the w-chart.
Forward: under RH, y_rho = 1/4 + gamma^2 in (1/4, infinity), so qw_n are
the moments (shifted by one power) of the finite positive measure
sum m_gamma delta at 1/y_rho with support in (0, 4); both quadratic
forms are traces of positive operators against |p|^2.  Converse: the two
Hankel families give a Stieltjes measure; the germ radius is positive
because the smallest |y_rho| is positive; compact support, determinacy,
and continuation on the slit plane force every zero of Gw onto the
positive real w-axis.  A real zero w0 > 0 of Gw means s(1-s) = w0 with
xi(s) = 0; reality of w0 forces Re s = 1/2 (the only way rho(1-rho) is
real for a nontrivial zero), which is RH.  No new mathematics beyond the
parent's imports is used.

### 3.3 Operator form and the parent chart

Under RH the minimal positive realization on the w-chart is

```text
B e_(rho,r) = y_rho^(-1) e_(rho,r),      B >= 0,  B in S1,
det_1(I - w B) = Gw(w) = xi(s)/xi(0),
qw_n = Tr(B^(n+1)).
```

The parent's frozen x-chart operator `A` (eigenvalues gamma^(-2), chart
`x = t^2`, determinant `det_1(I - t^2 A) = Xi(t)/Xi(0)`) is the exact
operator Moebius transform

```text
B = A (I + A/4)^(-1),        A = B (I - B/4)^(-1),
```

read eigenvalue-wise as `b = a/(1 + a/4)`, `a = b/(1 - b/4)`, that is,
`y = x + 1/4`.  Both directions preserve positivity, S1, infinite rank,
and the Schatten boundary (b and a are comparable near 0).  If H is any
self-adjoint realization with spectrum {gamma}, then

```text
B = (1/4 + H^2)^(-1):
```

the pole-chart operator is the resolvent of the Hilbert-Polya square at
-1/4.  The x-chart stays the frozen construction target of the parent
prereg; the w-chart is the calibration chart.  The two are exactly
interchangeable at the operator level, and deliberately NOT
interchangeable at the reference level: their reference ladders rest on
different constant families (w-chart: the s = 1 pole germ, i.e. the
sigma machinery; x-chart: the s = 1/2 central germ, i.e. Phi-moment
constants that this program has not yet bracketed).  This asymmetry is
the reason the w-chart goes first.

## 4. The sigma dictionary and the ladder junction

### 4.1 Partial-fraction dictionary

For m >= 1, exactly as rational functions,

```text
1/(x^m (1-x)^m)
  = sum_(j=1..m) binom(2m-1-j, m-j) * ( x^(-j) + (1-x)^(-j) ).
```

(Machine-pinned as Q1 for m = 1..6 by clearing denominators.)  Apply at
x = rho, sum over ALL zeros with the standard pairing (the j = 1 term
uses the paired conditionally convergent sigma_1; all j >= 2 terms are
absolute), use the invariance of the zero multiset under rho -> 1-rho,
and halve to pass to the upper multiset:

```text
qw_(m-1) = sum_(j=1..m) binom(2m-1-j, m-j) sigma_j,
sigma_j := sum_rho rho^(-j)   (paired at j = 1).
```

The matrix is integer, triangular, with unit diagonal, hence invertible
over Z: the pole power sums and the pole-chart Hankel stream are the
SAME data.  First rows:

```text
qw_0 = sigma_1
qw_1 = 2 sigma_1 +   sigma_2
qw_2 = 6 sigma_1 + 3 sigma_2 +   sigma_3
qw_3 = 20 sigma_1 + 10 sigma_2 + 4 sigma_3 + sigma_4
```

### 4.2 The junction theorem

The cocycle lane froze `lambda_1 = sigma_1` and the T_1 Toeplitz gate
margin `M_1 = 4 lambda_1 - lambda_2 = 2 sigma_1 + sigma_2` (C-LI-COCYCLE-1,
CO1, exact vector algebra).  Comparing with 4.1:

```text
qw_0 = lambda_1,
qw_1 = M_1.
```

Exactly, with no analysis: the mass of the pole-chart moment measure is
the first Li coefficient, and the first shifted moment is the T_1
Toeplitz margin.  Consequences:

1. The 1x1 Hankel gates of the moment lane,
   `H_0^(0) = (qw_0) >= 0` and `H_0^(1) = (qw_1) >= 0`, are ALREADY
   closed at candidate grade by the pinned intervals
   `lambda_1 in [23095708964233559, 23095708972138893] * 10^-18` and
   `M_1 in [37100438723459, 37100843555683] * 10^-18`, both strictly
   positive, two independent methods each.
2. The angular (Toeplitz/Herglotz) ladder and the radial
   (Hankel/Stieltjes) ladder are not merely analogous: they are two
   positivity structures carried by one coefficient stream (the s = 1
   germ of log xi), and they agree at their first rungs.  A proposed
   J-native q_n inherits every consequence of the M_1 pin for free.
3. The junction is also a falsifier amplifier: any proposal whose qw_1
   misses the M_1 interval is dead even if its own 1x1 Hankel data look
   positive.

Grade: T (exact rearrangement of absolutely convergent sums plus the
paired sigma_1 convention already frozen in the lane; the algebra is
machine-pinned as Q2).

## 5. The calibration ladder and the next razor

### 5.1 SH-1, frozen expression

The first finite gate not already closed by existing pins is the 2x2
determinant of the unshifted family,

```text
SH-1:   det H_1^(0) = qw_0 qw_2 - qw_1^2
      = sigma_1 (6 sigma_1 + 3 sigma_2 + sigma_3) - (2 sigma_1 + sigma_2)^2  >= 0,
```

with sigma_3 = 1 + gamma^3 + 3 gamma gamma_1 + (3/2) gamma_2
- (7/8) zeta(3) as derived and pinned in amendment 3 of the cocycle
lane.  Under RH this is strictly positive (Cauchy-Schwarz for the
measure with infinite support), so it is a genuine kill test with a
one-sided margin.

### 5.2 Cancellation depth, stated in advance

The combination `qw_2 = 6 sigma_1 + 3 sigma_2 + sigma_3` cancels to
about `1.5e-7` from terms of size about `1.4e-1`: six digits of exact
cancellation.  Float readings (engineering witnesses only, never
assertions): qw_0 ~ 2.31e-2, qw_1 = M_1 ~ 3.71e-5, qw_2 ~ 1.5e-7,
det H_1^(0) ~ 2e-9.  Therefore the SH-1 gate needs interval brackets of
width about 1e-10 on the sigma side, which in turn needs a gamma_2
bracket of width about 1e-9.  The cocycle lane's EM-2 machinery on
f(x) = ln^2(x)/x is the declared route (already listed there as the
ready extension for the T_2 gate); the same bracket serves both lanes,
another junction dividend.

The escalating-razor law continues on the Hankel side exactly as on the
Toeplitz side: the moment measure accumulates at 0 (as the Toeplitz
measure accumulates at 1), the top atom `1/y_1 ~ 1/200.03` dominates,
and each further minor is thinner by roughly the ratio `y_1/y_2`.
Every new antidiagonal needs one new sigma_(k), i.e. one new gamma_(k-1)
bracket; the derivation-then-freeze rhythm of sigma_3 extends verbatim
to sigma_4 (needs gamma_3 and the gamma gamma_2, gamma_1^2, zeta(3)
gamma terms of the classical expansion).

### 5.3 Named next gates

```text
N1  gamma_2 EM-2 bracket (width <= 1e-9), then exact interval evaluation
    of SH-1.  One new verifier, one run, pinned before execution.
N2  sigma_4 derivation and freeze by the same xi(1+t) route as
    amendment 3 (route-validated on sigma_1..sigma_3), then SH-1' =
    qw_1 qw_3 - qw_2^2 and the 3x3 families.
N3  Two-architecture re-run of N1/N2 at public validation time, per the
    lane's standing rule.
```

## 6. Exact chart transforms

### 6.1 Catalan reversion (owner germ to w-germ)

The lane's sigma machinery expands at s = 1 + t.  With w = s(1-s) one
has w = -t - t^2, whose compositional inverse is

```text
t(w) = -sum_(k>=1) C_(k-1) w^k = -w - w^2 - 2 w^3 - 5 w^4 - 14 w^5 - ...
```

with Catalan numbers C_k.  Any s = 1 germ stream transports to the
w-chart by this exact integer substitution (machine-pinned as Q3
through order 10).  This is the precise sense in which the w-chart is
"the pole chart": it is the s = 1 expansion in a coordinate that also
sees s = 0 and squares away nothing.

### 6.2 g-to-q recursion and scale rigidity

With Gw(w) = 1 + sum_(k>=1) g_k w^k, the moment stream obeys the
parent's recursion

```text
qw_n = -(n+1) g_(n+1) - sum_(k=1..n) g_k qw_(n-k),
```

pinned exactly on synthetic spectra (Q4).  Covariance trap: rescaling
the chart w -> c w rescales qw_n -> c^(n+1) qw_n and det H_N^(0) ->
c^((N+1)^2) det H_N^(0).  Positivity is scale-blind, but the junction
values qw_0 = lambda_1 and qw_1 = M_1 are NOT: the chart is pinned by
w = s(1-s) with no free constant.  A proposal that only matches the
ladder up to an overall scale has not matched it at all; this is
falsifier 3 of section 1 in exact form.

### 6.3 To and from the parent x-chart

Eigenvalue-wise b = a/(1+a/4) and back (Q4 pins both directions on
synthetic rational spectra).  Note the transforms are exact and finite
at the OPERATOR and SPECTRUM level, while the two moment ladders are
not finitely inter-derivable (moments of a shifted measure are not a
finite transform of moments of the reciprocal-shifted one); the two
ladders are therefore independent finite falsifier families for one and
the same realization, and section 4 says they share their first rungs
through the sigma stream.

## 7. Counting gate, Schatten boundary, and two selection theorems

### 7.1 The exact counting dictionary

With one boundary convention fixed as in the parent's section 5, the
eigenvalue counting of B and the zero counting function N(T) satisfy,
exactly,

```text
N_B(eps) := #{ j : b_j >= eps } = N( sqrt(1/eps - 1/4) )    (0 < eps < 4),
```

and with the imported Riemann-von Mangoldt law,

```text
N_B(eps) = (1/(2 pi)) eps^(-1/2) ( log(1/eps)/2 - log(2 pi e) )
           + O(log(1/eps)).
```

Both displayed terms are forced.  A proposed J-native spectrum must
reproduce the leading term AND the second term; the second term is the
cheap killer of dimensional-analysis fits, exactly as the constant
B_J = gamma - 1 - log(2 pi) is on the Fejer side.

### 7.2 Schatten boundary in the w-chart

```text
b_j ~ ( log j / (2 pi j) )^2:    B in S_p <=> p > 1/2;
sqrt(B) in S_p <=> p > 1;  hence  B in S1,  sqrt(B) not in S1,
```

matching the parent's frozen G2 boundary verbatim under the Moebius
dictionary (a and b comparable at 0).  Any proposal with sqrt(B_J)
trace class claims the wrong boundary and dies at G2.

### 7.3 Analytic-nuclear no-go (theorem grade, operator-class scope)

Import: a transfer/composition operator with holomorphic contracting
kernel on a disk-type space (nuclear of order zero in Grothendieck's
sense; the Mayer operator of the Gauss or golden continued-fraction map
is the standard example) has singular values s_k = O(r^k) for some
r < 1.  Then

```text
N(eps) = O( log(1/eps) ),
```

against the forced eps^(-1/2) log(1/eps) of 7.1.  Hence NO realization
of the pole-chart (equivalently x-chart) Fredholm target lies in the
exponential singular-value class.  Because the parent's spectral
rigidity fixes the nonidentity spectrum of every exact witness, this is
an exclusion by operator class, independent of construction provenance:
it kills every direct "analytic transfer operator" route, including the
phi-continued-fraction route R3 in its holomorphic form, in one stroke.
Scope discipline: it does NOT kill transfer-operator ideas as such; it
forces them off analytic function spaces.

### 7.4 Finite-smoothness selection (H)

For transfer operators on finite-smoothness spaces (C^alpha, Sobolev,
Besov) over a d-dimensional carrier, singular values decay polynomially,
s_k ~ k^(-alpha/d) up to slowly varying factors.  Matching 7.1-7.2
forces

```text
alpha/d = 2   at the level of exponents,  with the log^2 correction
              carried by a slowly varying factor,
```

for the operator B itself (b_j ~ j^(-2) log^2 j), equivalently
smoothness exactly ONE derivative in one dimension for a square-root
carrier realizing sqrt(B) (s_j(sqrt B) ~ j^(-1) log j).  The selection
principle: the Li Schatten boundary is an exact smoothness dial, and it
points at the C^1/H^1 boundary of a one-dimensional J-carrier, not at
analyticity and not at mere measurability.  This is a heuristic
selection (H): the exponent arithmetic is exact, the identification of
the carrier class is not a theorem.

### 7.5 Pair-count heuristic (H, clearly labeled)

The two-term law of 7.1 is, up to its second constant, a hyperbola
lattice-point count.  The J-native candidates for such counting are
pair structures (wedge/commutator sectors of the kernel, ideal pairs of
Z[zeta_5] under the norm form), not single streams.  This is recorded
as a route-selection heuristic only; the second-term comparison of 7.1
is the corresponding kill test.

## 8. The pentagon stream at the q-interface

Every q ladder is generated from a logarithmic derivative.  On the
arithmetic side the pentagon package fixes, exactly,

```text
-P_0'/P_0 (s) = sum_n Lambda(n) n^(-s) - sum_(m>=1) (log 5) 5^m (5^m)^(-s),
```

i.e. the raw pentagon carrier equals the von Mangoldt stream plus the
counterfeit ramified tower at 5, and the filter division by f_5 removes
exactly that tower (C-PENTAGON-WEIL-1, section 4b).  This candidate
machine-pins the identity at the COEFFICIENT level: computing the
Dirichlet coefficients of -P_0'/P_0 by exact formal inversion from
c(n) = 5*[5|n] - 1 alone, in the free Q-module with basis
{1} union {log p}, and comparing against Lambda(n) - (log 5) n [n = 5^m]
for every n <= 125 (Q6).  This is the exact G4-side accounting that a
relative-determinant proposal must reproduce on its named test domain:
the declared blocks for any proposal on the w-chart are frozen as

```text
(i)   the pole block: s(s-1) = -w contributes d/dw log(s(s-1)) = 1/w,
      a pure pole, no series;
(ii)  the archimedean block: (1/2) psi(s/2) - (log pi)/2, transported by
      the Catalan reversion of 6.1;
(iii) the pentagon arithmetic block: -P_0'/P_0;
(iv)  the filter tower block: +f_5'/f_5, cancelling the counterfeit
      tower of (iii) exactly.
```

A proposal that reproduces (iii) without (iv), or (iv) with any
coefficient other than the exact tower weights, fails falsifier 6.

## 9. Route map with frozen kill order

Universal kill order for EVERY proposed J-native moment functional,
cheapest first; the first miss kills the proposal, not RH:

```text
K0  scale rigidity: no free constant (section 6.2);
K1  qw_0 interval must hit the pinned lambda_1 interval;
K2  qw_1 interval must hit the pinned M_1 interval (junction);
K3  top-of-spectrum gate: 1/b_max must hit the y_1 = 1/4 + gamma_1^2
    reference interval (the reference bracket is comparator data, like
    lambda_1);
K4  counting: both terms of 7.1; Schatten boundary of 7.2;
K5  SH-1 and the growing Hankel/Toeplitz minor ladders (both lanes);
K6  the G4 coefficient accounting of section 8 on the named domain;
K7  the frozen prereg gates G0-G7, then the proof-only G8 wall.
```

Routes, each H, each with its first expected failure point named:

```text
RA  RELATIVE/PARENT-PAIR (the parent's intended architecture): a
    J-native parent pair with trace-class difference whose relative
    determinant carries blocks (i)-(iv) of section 8.  The pentagon
    package supplies the arithmetic and tower blocks exactly; the open
    engineering is the archimedean block and positivity.  First kill
    tests: K0, then section 8 accounting, then K1.
RB  IDEAL/FOCK RELATIVE: the direct occupation Cayley died (parent
    section 10.2, no finite Schatten class).  A surviving RB must be a
    RATIO of two ideal-lattice objects whose difference of counting
    laws is RvM-shaped; K4 first, and 7.5's second-term test is the
    cheap killer.
RC  STREAM/CENSUS Cesaro functionals over the F_5^6 kernel: finite
    carriers are excluded unconditionally by the cocycle lane's carrier
    no-go; any RC must produce an infinite J-object first, then faces
    K0-K2 immediately.
```

Removed from the board by section 7.3: every direct analytic-nuclear
transfer realization (holomorphic R3).  R3 survives only in finite
smoothness (7.4).

## 10. Exact machine audit

`verify_q_moment_interface.py` is a stdlib-only exact dictionary audit;
Fraction/integer arithmetic in every assertion; no floats anywhere, no
files, no network, no subprocesses.  It checks:

```text
Q1  the partial-fraction sigma dictionary, m = 1..6, as polynomial
    identities over Q;
Q2  the junction algebra: qw_0 = sigma_1 = lambda_1 and
    qw_1 = 2 sigma_1 + sigma_2 = M_1 = 4 lambda_1 - lambda_2, as exact
    vector identities in the frozen constant module, plus the qw_2 and
    qw_3 rows of the dictionary;
Q3  the Catalan reversion of w = -t - t^2 through order 10, by exact
    formal composition both ways;
Q4  the g-to-q recursion against power sums on two synthetic rational
    spectra; the eigenvalue Moebius maps b = a/(1+a/4), a = b/(1-b/4)
    as exact involutive dictionaries; scaling covariance
    qw_n(c dot spectrum inverse) = c^(n+1) qw_n;
Q5  double-Hankel discipline: a positive instance with all leading
    minors positive; the Hamburger separator (moments of delta_(+1) +
    delta_(-1)) passing every H^(0) minor while H^(1) fires at once
    (the shifted family is not redundant); a signed instance firing
    H^(0) itself;
Q6  the pentagon log-derivative coefficient identity of section 8 for
    all n <= 125, exact in the free Q-module over {log p};
Q7  the counting dichotomy skeleton on exact integers: a geometric
    spectrum yields N(4^-M) = M while the log-polynomial reference
    shape yields eventual dominance of any linear-in-M bound within the
    tested window (restricted scope: finite skeleton only, in the sense
    of the parent's S8).
```

```text
verifier sha256  ca8fdc902ea6410c4e4c89885da10dbc44cc4965f5427897461a6791f4f938d9
verifier bytes   13301
stdout sha256    a5fc3a479c6094b46513c7a06f10aa3b7a44fb36436d2a56d76208255c6d9b34
stdout bytes     1636
result           7 PASS, 0 FAIL, exit 0, empty stderr
environment      LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                 PYTHONHASHSEED=0 TZ=UTC; Linux x86_64; Python 3.11.15
scope            non-formal one-environment dictionary audit; not a
                 public reproduction, not a probe execution
```

## 11. Proposed non-public ledger

| Candidate row | Mathematical classification | Public state |
|---|---:|---:|
| `J-LI-W-CHART-EQUIVALENCE` | T as equivalence (parent spine) | unregistered |
| `J-LI-SIGMA-HANKEL-DICTIONARY` | T | unregistered |
| `J-LI-LADDER-JUNCTION` | T | unregistered |
| `J-LI-Q-CALIBRATION-LADDER` | frozen interface; SH-1 pending N1 | unregistered |
| `J-LI-Q-COUNTING-GATE` | T (dictionary) + imported RvM | unregistered |
| `J-LI-Q-ANALYTIC-NUCLEAR-NOGO` | T, operator-class scope | unregistered |
| `J-LI-Q-CARRIER-SMOOTHNESS-SELECTION` | H | unregistered |
| `J-LI-Q-MOMENT-REALIZATION` | O | unregistered |
| RH | O | unregistered |

## 12. Non-claims

No J-native `A_J`, `B_J`, or moment functional is constructed.  The
junction theorem transfers existing pins; it creates no new positivity.
SH-1 is frozen but not evaluated: its interval evaluation is gate N1
and happens in a fresh pinned run, never retroactively.  The
smoothness selection and the pair-count reading are H and are not
inputs to any gate.  Nothing here changes the frozen parent prereg;
the x-chart remains the construction target and the w-chart is
calibration.  G8 remains proof-only.  J-LI-Q-MOMENT-REALIZATION stays
O.  RH stays O.  No public registration, no push, no normative change
is made by this candidate.

## 13. Promotion posture

```text
current   notes-only candidate; exact dictionaries machine-pinned in one
          environment
next      N1 (gamma_2 bracket + SH-1 interval), N2 (sigma_4 freeze,
          SH-1'), owner review of the junction theorem and the no-go
then      fold of the junction and dictionary rows into the lane map;
          any public probe needs a NEW PREREG and NEW pins per the
          standing rule; the moment-realization probe additionally
          waits for a concrete G0-G3 construction per the frozen
          S2 prereg
never     retroactive promotion of this notes run; no finite prefix,
          junction included, is evidence for RH
```

# PREREG P-RH-WEYL-CANONICAL-1

```text
DATE:        2026-08-20 (UTC)
STATUS:      NON-CANONICAL INCUBATION PREREG, no authority
TARGET LINE: private handoff only (mathorn1973/twistj-handoff),
             new lane branch agent/rh-weyl-canonical, stacked on
             agent/rh-hankel-hard-edge-2 head
             5ab83b032cc897fa12886f8c927589928dad3ccc
LANE:        T2 of the #374 consolidation: canonical finite Weyl
             construction with gates S1-S5 and scalar node convergence
             Q_R(i a_n) -> Q_xi(i a_n), equivalently convergence of finite
             resolvent moments at one point (then A10+A11 finish).
             This probe is the lane OPENER: it validates the entire gate
             machinery exactly on a finite canonical model. It makes no
             statement about zeta.
PARENTS:     claude/CONSOL-RAY-PICK-KERNEL-374_2026-08-20.md (gates S1-S5
             adopted there as C14; C10 float warning; A9/A10/A11),
             claude/ADDENDUM-RAY-PICK-KERNEL-374_2026-08-19.md (A9
             narrowed limit gate; PSD passes to entrywise limits).
OWNER CALL:  B-then-A order; A = this T2 lane, opened on "pust".
PUBLIC GATE: Public Canon v55 ACTIVE, main 362e9c3a, verified this session
             (this calendar day) before the HE-1 freeze; this probe touches
             nothing public. Any future formal step re-gates first.
FIREWALL:    no RH claim, no evidence claim for RH, no Canon, Registry,
             Frontier or status movement. Model statements are never
             statements about zeta. J7 SOURCE [O]. RH [O].
LAYER:       L1. No layer lift.
SESSION:     one named session owns this probe (same session as HE-1/HE-2).
```

## The five gates, fixed for this lane

As adopted in the consolidation (C14), named and frozen here for every
future T2 document:

```text
S1  canonical choice: the Weyl function is determined by the canonical
    data alone, with an explicit dictionary from characteristic functions
    to Q-functions.
S2  positive residues: Q is Herglotz with nonnegative spectral weights;
    operationally, Pick matrices at upper half-plane nodes are PSD.
S3  stable affine normalization: the normalization of Q is fixed and
    stable (model form: Q(z) = -1/z - b_1/z^2 + O(z^-3) for a unit
    cyclic vector).
S4  definedness at the nodes: Q is defined at every node i a_n,
    a_n = 1 + 1/n (no real spectrum at the nodes; exact solvability).
S5  the limit is the true Q: finite Weyl functions converge at the nodes
    to the Weyl function of the limit object, not merely to a function
    with the same poles.
```

Per C10, no instrument in this lane ever rests on float sign readings of
the ill-conditioned 1+1/n chain; every gate below is exact rational or
carries certified rational enclosures.

## Falsifiers first

```text
FW1  foundations: failure of CHECK 0 (enclosure certificates) or of the
     Laurent normalization CHECK 2. Fires the probe.
FW2  gate machinery: failure of CHECK 3 (exact Herglotz/Pick PSD in the
     unperturbed model) or CHECK 4 (certified node convergence to the
     known limit). Kills the instrument set of the lane.
FW3  detection: no nonpositive Pick pivot up to N = 8 nodes for the
     frozen defect D1 (conjugate pole pair mu = 1/3 + i/10, weight 1/10)
     on top of Q_64. Kills the finite-node detection mechanism claim in
     the model.
FW4  dictionary: failure of CHECK 1 (chi_1/chi equals the resolvent Q
     exactly). Kills the S1 dictionary instrument.
FW5  moment table: any exact Taylor-coefficient value at c = 2 whose
     certified enclosure disagrees with the independent breaker path.
```

A fired falsifier or stop-gate is archived, not deleted. No threshold
moves after this freeze.

## Field 1, equation (the frozen model and gates)

Model class: real symmetric Jacobi matrices J_R of size R with unit
off-diagonals a_k = 1/2 and zero diagonal b_k = 0 (free Jacobi matrix,
spectral measure of e_1 the semicircle on [-1,1]), cyclic vector e_1.
Exact rational data throughout.

```text
Weyl function:      Q_R(z) = e_1^T (J_R - z)^{-1} e_1, exact in Q(i) or
                    Q at the frozen evaluation points.
Dictionary (S1):    Q_R(z) = chi^(1)(z) / chi(z), where chi = det(J_R - z)
                    and chi^(1) = det of the minor with row and column 1
                    removed, both by the exact three-term recurrence.
Limit object (S5):  Q_inf(z) = 2(-z + sqrt(z^2 - 1)), the Herglotz branch;
                    at the nodes Q_inf(i a) = 2 i (sqrt(a^2 + 1) - a),
                    at the real point c = 2 the Taylor coefficients lie
                    in Q(sqrt 3) and are computed exactly by truncated
                    power-series square root over Q(sqrt 3).
Nodes:              z_n = i a_n, a_n = 1 + 1/n, n = 1..8.
Pick matrix:        P[j,k] = (Q(z_j) - conj Q(z_k)) / (z_j - conj z_k),
                    Hermitian over Q(i); PSD decided by exact LDL* with
                    real rational pivots.
Detection model:    the A4 orbit mechanism analogue: a conjugate pair of
                    complex poles with positive weight added to the
                    canonical function,
                    Q'(z) = Q_64(z) + w (1/(mu - z) + 1/(conj mu - z)).
                    Frozen defects:
                    D1  mu = 1/3 + i/10,  w = 1/10   (asserted detection)
                    D2  mu = 9/10 + i/10, w = 1/10   (data)
                    D3  mu = 1/3 + i/100, w = 1/100  (data)
                    N*(D) = minimal N <= 8 with a nonpositive exact Pick
                    pivot at nodes z_1..z_N. A rank-one non-self-adjoint
                    matrix perturbation is NOT used: it gives the Moebius
                    map Q/(1 + i eps Q), which need not break Pick
                    positivity on a compact node set; the pole-pair defect
                    is the faithful analogue of an off-critical quartet.
Truncation sizes:   R in {4, 8, 16, 32, 64}.
Moment point:       c = 2, orders k = 0..6,
                    Q_R^(k)(c)/k! = e_1^T (J_R - c)^{-(k+1)} e_1 exactly.
```

## Field 2, code

```text
verify_rh_weyl_canonical_1.py
  Python standard library only; every assertion uses int or Fraction;
  floats appear nowhere in the file; sqrt(a^2+1) and sqrt(3) enter only
  through certified rational enclosures (integer square-root bracketing
  at width 10^-40). Deterministic output; target under 120 s per leg;
  env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
  CHECK 0  enclosure certificates: sqrt(a_n^2+1) for n = 1..8 and sqrt 3,
           each bracketed by squaring.
  CHECK 1  S1 dictionary: exact equality Q_R(z) = chi^(1)(z)/chi(z) for
           R in {4, 8, 16}, z in {z_1, z_4, 2}, both sides exact.
  CHECK 2  S3 normalization: e_1^T J^0 e_1 = 1 and e_1^T J e_1 = 0
           exactly (Laurent leading data -1/z + 0/z^2 + ...).
  CHECK 3  S2 and S4: at every node and every R the exact solve succeeds
           (S4) and Im Q_R(z_n) > 0 exactly (S2 pointwise); at R = 64
           the full 8x8 Pick matrix passes exact LDL* with every pivot
           real and positive (S2 matrix form). Assertions.
  CHECK 4  S5 node convergence: certified upper bounds on
           |Q_R(z_n) - Q_inf(z_n)|^2 for all R and n; assert the bound
           decreases along R at each node and is below 10^-40 at R = 64.
           The decay table is printed as data.
  CHECK 5  moment convergence at c = 2: exact Q_R coefficients k <= 6
           against exact Q(sqrt 3) limit coefficients via enclosure;
           table printed as data; assert distance below 10^-30 at R = 64
           for every k <= 6.
  CHECK 6  detection: assert N*(D1) exists and is <= 8; record N*(D2)
           and N*(D3) as data (no assertion).
  Exit 0 iff CHECK 0, 1, 2, 3, 4, 5, 6 all pass. The lane verdict line
  (OPEN or INSTRUMENTS-FAILED) is printed either way.

breaker_rh_weyl_canonical_1.py
  Independent numeric path, floats allowed, no authority. Attacks:
  dense float inverse (Gaussian elimination, no libraries) against the
  exact Q values; float LDL sign pattern against the exact pivots;
  independent recomputation of the moment table by float resolvent
  powers (FW5 check); a 50-model roam over random rational Jacobi
  matrices (seed 0, R = 12, N = 6) hunting a Herglotz model with a
  negative exact-path pivot; a defect scan N*(delta, w) over pole
  offsets delta in {1e-1, 1e-2, 1e-3} and weights w in {1e-1, 1e-3}
  (detection-cost analogue of the consolidation's R2 reading);
  convergence-rate fit of the CHECK 4 table against the
  continued-fraction prediction (q(a)^2/4 per step).
```

## Field 3, carrier and data

Purely synthetic finite model. No zeta zeros, no xi values, no external
data, no downloads, no floats in assertions. Nothing here evaluates or
approximates any arithmetic object.

## Field 4, systematics

```text
S1s  Enclosures. All square roots enter through integer-sqrt brackets of
     width 10^-40; distance bounds use worst-case endpoints; an assertion
     never depends on which endpoint is the truth.
S2s  Exactness. Solves, characteristic recurrences, Pick matrices, LDL*
     pivots, and Taylor coefficients are exact rational or Q(i)/Q(sqrt 3)
     pair arithmetic. C10 discipline: no float ever gates.
S3s  Finite range. All verdicts are candidate-C at the frozen R, node,
     epsilon and k ranges. No claim beyond the ranges.
S4s  Model scope. Every statement is about the finite Jacobi model. The
     zeta-side construction is an enumerated obligation, not a claim.
S5s  Determinism. Output is integers, fractions, fixed strings, and
     6-digit integer-computed decimal witnesses; byte-identical output
     required on both legs.
```

## Field 5, failure threshold and stop-gate

```text
The probe PASSES iff CHECK 0..6 all pass. Then the lane verdict is:
T2 LANE OPEN: the S1-S5 gate machinery, the node-convergence gate, the
one-point moment gate, and the finite-node detection mechanism are all
exact-verified on the canonical model, and the lane's remaining content
is exactly the zeta-side obligations O1-O4 below.

STOP-GATE, frozen action: if FW2 or FW4 fires, the verdict is
[F-bounded, T2 INSTRUMENTS] and the instrument set must be redesigned
before any zeta-side work; if only FW3 fires, the lane still opens but
the detection claim is dropped and re-derived as a successor obligation.
Either way the record is archived and no threshold moves.
```

Zeta-side obligations of the lane (enumerated, NOT claimed, out of scope
for this probe):

```text
O1  canonical-system construction of finite Q_R^(xi) from the screw
    function route of arXiv:2606.09096 v1, satisfying S1-S4.
O2  the dictionary from the paper's normalized characteristic functions
    e^phi(R,z) W(R,theta;z) (conjectural limit
    z^2 xi(1/2-iz)/xi'(1/2-iz)) to Q-functions; part of gate S1 on the
    zeta side.
O3  gate S5 for zeta: scalar node convergence Q_R(i a_n) -> Q_xi(i a_n),
    or equivalently convergence of the finite resolvent moments at one
    real point c > 1/2; with A9 (PSD passes to entrywise limits) and
    A10+A11 (one-point criterion and recursion) this closes RH, which is
    precisely why O3 carries the full difficulty.
O4  certified instruments only, per C10: exact or interval LDL, never
    float signs on the 1+1/n chain.
```

Predictions, recorded before any computation, non-binding: all seven
checks pass; N*(D1) is small (2 to 4: the deep Pick pivots at the
clustered nodes are exponentially small and the pole-pair defect is an
order-0.1 indefinite direction); N*(D3) larger or undetected at 8
nodes; the CHECK 4 decay rate per unit R is close to q(a)^2/4 with
q(a) = 2(sqrt(a^2+1) - a); the random-model roam finds no Herglotz
counterexample.

## Field 6, action layer

L1 throughout.

## Pin plan

Freeze this file and the verifier, record sha256 of both, commit to
branch agent/rh-weyl-canonical from 5ab83b03, author
A. M. Thorn <thorn@twistj.com>, BEFORE the first execution. Two legs,
macOS arm64 CPython 3.9 and Linux x86_64 CPython 3.11+, byte-identical
stdout required. Breaker runs after and is committed with its stdout.

End of preregistration.

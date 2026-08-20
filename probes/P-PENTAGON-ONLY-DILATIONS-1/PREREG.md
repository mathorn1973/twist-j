# P-PENTAGON-ONLY-DILATIONS-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / PROOF-FIRST`

One elementary unconditional theorem and the route kill it forces. The
theorem is carried by the written proof below; the verifier is a finite
exact audit (independent integration of the Gram, exact linear algebra for
the collapse), not a discovery engine. The result is exposed before
execution: every gate passes and the route is dead.

## Public identity, authority, and action layer

```text
probe:           P-PENTAGON-ONLY-DILATIONS-1
public claim:    issue #445
probe owner:     A. M. Thorn / delegated session cleanup-batch-2026-08-20
branch:          probe/P-PENTAGON-ONLY-DILATIONS-1
basis:           Public Canon v54, main 70e1c480, tag canon-v54,
                 SHA256SUMS 5 of 5 OK
action layer:    L2 (function-space geometry; enrichment lane). No layer
                 lift, no physical claim, no canon edit by this probe.
lineage:         carries in the incubation promotion
                 PROMO-C-PENTAGON-ONLY-DILATIONS-1 (2026-07-17); the lane
                 verifier pins are recorded there; this probe re-derives
                 everything fresh with new files.
```

## Falsifier, first

For the T row: an exact computation exhibiting, for some q coprime to 5
and some M, a 5-power combination with squared distance to g_q below
(1/12)(1 - 1/q^2), or an exact Gram value differing from
gcd(m,n)^2/(12mn). For the F row: the same exhibition would return the
route to life. The written proof below excludes both; a pinned-gate FAIL
on rerun is the operational falsifier.

## The six fields

```text
EQUATION     in H = L^2(0,1) with g_n(x) = frac(nx) - 1/2:
             <g_m, g_n> = gcd(m,n)^2 / (12 m n); for every q coprime to 5
             and every M >= 0,
             dist(g_q, span{g_(5^m): 0 <= m <= M})^2 = (1/12)(1 - 1/q^2),
             constant in M, best approximant exactly (1/q) g_(5^0).
CODE         probes/P-PENTAGON-ONLY-DILATIONS-1/verify.py, stdlib only,
             Fraction arithmetic, no float anywhere, deterministic, well
             under 120 s, run from repository root, environment
             LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC.
CARRIER      none external. Pure exact mathematics; the verifier's own
             piecewise integration is the independent second path for the
             Gram.
SYSTEMATICS  breakpoint handling in the exact integration (midpoint floor
             evaluation, degenerate intervals skipped); solver is plain
             Gaussian elimination over Q. The audited instances are
             finite (q in {2,3,6,7,12}, M <= 8, Gram pairs to (q,125));
             the universal statements are carried by the proof, not the
             sweep.
THRESHOLD    any gate FAIL kills the probe. No numerical tolerance exists
             anywhere; every comparison is exact equality in Q.
LAYER        L2. The two proposed rows are mathematics of the enrichment
             lane; RH stays O and no live row moves.
```

## The written proof

Gram. g_n(x) = frac(nx) - 1/2 has the Fourier expansion
g_n = -sum_(k>=1) sin(2 pi k n x)/(pi k). Parseval gives
<g_m, g_n> = (1/(2 pi^2)) sum over k m = l n of 1/(k l); writing
m = g m', n = g n' with g = gcd(m,n) and coprime m', n', the solutions
are k = j n', l = j m', so the sum is (1/(m' n')) zeta(2)/(2 pi^2)
= g^2/(12 m n). The verifier independently re-derives every audited value
by exact piecewise polynomial integration (PD1), so the closed form is
checked, not assumed.

Tower and collapse. On the tower indices m = 5^a the Gram is the
Kac-Murdock-Szego matrix G_(ab) = 5^(-|a-b|)/12 (PD2). For q coprime to 5,
gcd(q, 5^a) = 1, so the cross vector is c_a = 1/(12 q 5^a). Then
G e_0 (1/q) = c exactly, entry by entry: G_(a0)/q = 5^(-a)/(12 q) = c_a
(PD0). Since G is positive definite, the normal equations have the unique
solution x = (1/q) e_0 for every M: the best approximant is (1/q) g_1 and
adding any number of higher tower rungs changes nothing (PD3, PD5, PD6).
The squared deficiency is
||g_q||^2 - c . x = 1/12 - 1/(12 q^2) = (1/12)(1 - 1/q^2),
a positive rational constant in M, with witnesses 1/16 (q = 2) and 2/27
(q = 3) (PD4).

Consequence, the F. The Nyman-Beurling / Baez-Duarte criterion (cited as
motivation, not reproved) requires the closure of the dilation family to
reach a target carrying every prime direction. Dilations restricted to the
pentagon tower 5^m leave every direction coprime to 5 at a fixed positive
distance, so the pentagon-only route can never satisfy the criterion. The
route PENTAGON-ONLY-DILATIONS is falsified as a route; the deficiency
theorem is the exact witness.

## Proposed fold edits (a later sealed fold, not this probe)

Registry, two rows (tab-separated; canon section 16, p = 5 and the wall):

```text
J-LI-PENTAGON-DILATION-DEFICIENCY	T	in L^2(0,1) the clock functions g_n = frac(nx) - 1/2 have exact Gram gcd(m,n)^2/(12mn); the pentagon tower {g_(5^m)} has KMS Gram 5^(-|a-b|)/12, and for every q coprime to 5 the squared distance of g_q to the span of any number of tower rungs is exactly (1/12)(1 - 1/q^2), constant in the tower height, with best approximant (1/q) g_1; witnesses 1/16 at q = 2 and 2/27 at q = 3	16. p = 5 and the wall	probes/P-PENTAGON-ONLY-DILATIONS-1	an exact 5-power combination reaching a smaller squared distance for some q coprime to 5, or an exact Gram value off the closed form
PENTAGON-ONLY-DILATIONS	F	the Nyman-Beurling / Baez-Duarte closure route restricted to pentagon-tower dilations 5^m is falsified: the entire non-5 spectrum is unreachable, deficiency bounded below by the exact positive rational (1/12)(1 - 1/q^2) per direction q coprime to 5	16. p = 5 and the wall	probes/P-PENTAGON-ONLY-DILATIONS-1	fired: the exact deficiency theorem above; the route returns only if the deficiency computation is exactly refuted
```

Frontier: no change (a T no-go and an F; no live row moves). Ledger
delta: claims +2, T +1, F +1.

## Non-claims

Nothing about RH, zero locations, Nyman-Beurling completeness for other
dilation families, the operator content of the LAMBDA rows, or any
physical reading. The theorem narrows the realization space by killing
one route permanently; it does not enter the space.

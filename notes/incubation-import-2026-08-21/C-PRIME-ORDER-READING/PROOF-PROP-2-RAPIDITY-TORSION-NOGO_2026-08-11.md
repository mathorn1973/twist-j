# PROOF: PROP-2, rapidity torsion no-go and isogeny-stable separation

Status: candidate-T support document inside C-PRIME-ORDER-READING-1 stage A.
NON-CANONICAL, no authority, no computation. 2026-08-11, night.
SOURCE: statement and proof skeleton proposed by the external PUBLIC review
of claude/MEDITACE-DIMENZE-RH_2026-08-11.md under the name
C-RAPIDITY-TORSION-NOGO-1 (recorded here as a content alias per the naming
drift rule); verified, completed with the equal-absolute-value lemma, and
extended by PROP-2b in this session. PROP-2 strictly generalizes the
fixed-point clause of PROP-1 (fixed points are exactly the 2-torsion).

Setting as in claude/PROOF-PROP-1-C-PRIME-ORDER-READING-1_2026-08-11.md.
LEMMA E (from there, restated): u in F with |u|_1 = |u|_2 and N(u) = +1
is +-1; if moreover the place-1 image is positive, u = +1.

PROP-2 (torsion no-go). For every prime ideal P above a split rational
prime, the oriented class r(P) in R/(log phi)Z has infinite order.

Proof. Let P = (pi) and suppose m r(P) = 0 for some m >= 1, i.e.
m t = n log phi for some integer n, where |pi|_1 = sqrt(p) e^t. Put
u = (pi / sigma(pi))^m phi^(-2n). Then |u|_1 = e^(2mt) phi^(-2n) = 1,
N(u) = (N(pi)/N(sigma pi))^m N(phi)^(-2n) = 1, hence |u|_2 = 1 as well,
and by Lemma E u = +-1. Passing to fractional ideals,
(P sigma(P)^(-1))^m = (1), so P^m = sigma(P)^m, and unique factorization
of ideals gives P = sigma(P), contradicting that p splits. qed

PROP-2b (isogeny-stable separation). For every m >= 1 and distinct split
rational primes p != q, with any orientations:
(i)  m r(P) != 0  (PROP-2);
(ii) m r(P) != m r(Q) for P above p, Q above q, same orientation;
(iii) m r(P) != -m r(Q), opposite orientation.
Hence the m-fold scaling map of the circle keeps all split classes
pairwise distinct and nonzero: separation survives every finite isogeny
of the rapidity circle.

Proof. (ii): the hypothesis gives m(t_p - t_q) = n log phi; put
u = (pi_p / sigma(pi_p))^m (sigma(pi_q) / pi_q)^m phi^(-2n). As above
|u|_1 = |u|_2 = 1, N(u) = 1, so u = +-1, and the ideal identity reads
P^m sigma(Q)^m = sigma(P)^m Q^m. Unique factorization forces the multiset
equality {P, sigma(Q)} = {sigma(P), Q}; P = sigma(P) contradicts split,
and P = Q contradicts distinct residue characteristics. (iii): the same
with u = (pi_p/sigma(pi_p))^m (pi_q/sigma(pi_q))^m phi^(-2n), giving
{P, Q} = {sigma(P), sigma(Q)}, killed the same way. qed

COROLLARIES.

```
C1  For every k != 0 and every split P, chi_k(P) is not a root of unity
    (a finite order M would give M k r(P) = 0 against PROP-2).
C2  No fixed finite cyclic phase model preserves the stage A separation:
    split primes are infinite in number (Dirichlet) and their classes are
    pairwise distinct (PROP-1), so any map to a finite phase set
    identifies infinitely many distinct classes. By PROP-2b the collision
    is always an artifact of rounding, never of the arithmetic: even the
    m-scaled classes never collide.
C3  Seam accounting, correcting the meditation's poetry: the zero class
    is occupied by ALL inert rational primes and by the ramified place;
    the five is exceptional there by ramification, not by exclusivity.
    The split stream avoids not only the two involution fixed points
    (PROP-1) but the entire torsion subgroup of the circle (PROP-2).
```

CONSEQUENCES FOR THE PROGRAM (analysis, no claims).

```
1  The review's correction of the meditation is adopted in full: there is
   no exact finite integer phase lattice; the honest carriers are
   symbolic phases, certified intervals, declared-loss finite quotients,
   or a trace formulation that eliminates individual phases. PROP-2b
   supports the interval route: certified intervals can always be
   refined to re-separate, because the underlying classes never merge
   at any isogeny level.
2  The corrected working object stands as the review put it: a Weil
   Hermitian form with integer combinatorics, archimedean rapidity
   coefficients, and certified inertia; compression to the trivial
   channel must yield zeta only after the Galois character projector
   (zeta_F = zeta times L(chi_5): the circle alone does not isolate
   zeta, matching the 4x4 scalar-corner finding).
3  The DH guard redesign is accepted: F'/F of a linear combination is
   not the linear combination of F'/F, so the naive odd 2x2 block is
   not type-closed; the guard must be a local Euler gate or a Weil form
   built from the true DH logarithmic derivative.
4  Nothing here opens the Gram test. That step waits for the owner:
   carrier, cutoffs, projector, sign rule and the four pre-frozen
   endings (STOP on noncanonical section; F on zeta-by-subtraction;
   F on DH positive; F on normalization-dependent sign) go into a
   prereg only after an explicit ANO.
```

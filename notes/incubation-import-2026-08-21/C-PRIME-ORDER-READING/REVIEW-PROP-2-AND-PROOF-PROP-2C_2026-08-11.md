# REVIEW of PROP-2 / PROP-2b, and PROOF of the proposed PROP-2C

Status: independent review record plus one new candidate-T support statement.
NON-CANONICAL, no authority, no promotion. 2026-08-11, night.
Target on promotion: internal line first, public line only through a fold.

SCOPE. This session did not write and does not touch
`claude/PROOF-PROP-2-RAPIDITY-TORSION-NOGO_2026-08-11.md` or
`claude/PROOF-PROP-1-C-PRIME-ORDER-READING-1_2026-08-11.md`. It is the
independent second reading those documents name as their open item, run by a
second author with a second code path. Corrections below are recommendations
to the owner of those docs, not edits.

Setting as in PROOF-PROP-1. F = Q(sqrt5), O = Z[phi], sigma the nontrivial
automorphism, O^x = {+-phi^m}, N(phi) = -1, class number one. For a prime P
with generator w, the rapidity t is fixed by |w|_1 = N(P)^(1/2) e^t, and
r(P) = t mod (log phi)Z.

## 1. Verdict on PROP-2

PROP-2 SURVIVES the reading. The chain is complete and every step is forced:
m t = n log phi gives |u|_1 = e^(2mt) phi^(-2n) = 1 for
u = (pi/sigma pi)^m phi^(-2n); u = +-1; (phi) = (1) so the ideal identity is
P^m = sigma(P)^m; unique factorization gives P = sigma(P); split forbids it.
No gap found. The even exponent -2n is load bearing and is correctly placed:
it is forced by the doubling in e^(2mt), not by the norm sign, and the proof
does not silently need N(phi^(-n)) = +1.

Claim to the fixed-point clause of PROP-1 is upheld: m = 2 recovers it, and
the odd-half-period sub-case of PROP-1 A1(iii) needs no separate sign
argument here.

## 2. Verdict on PROP-2b

PROP-2b SURVIVES the reading, with one boundary that the statement should
name explicitly.

(ii) and (iii) are correct as proved. Both multiset arguments are valid and
both exclusions are used: `P = sigma(P)` dies on split, the cross identity
dies on distinct residue characteristic.

BOUNDARY (recommend a wording fix, not a defect of the proof). The header
reads "with any orientations". Read together with (iii) that phrasing invites
the case Q = sigma(P) above the SAME p, where (iii) is FALSE by identity:
r(sigma P) = -r(P), so m r(P) = -m r(sigma P) for every m and every split p.
The proof is safe because it uses p != q. The statement is safe only if the
conclusion is carried on the unordered class R(p) = {t, -t} that PROP-1
defines. Recommended conclusion line:

```
For every m >= 1 the map p -> m R(p) = {m t, -m t} is injective on split
rational primes and never equals the zero class.
```

The breaker below turns this boundary into a positive control: the pair test
with q = p and opposite orientation collides for every m tested, exactly as
the identity demands.

## 3. Two corrections to the support text

C3-NORM (real, one line). C3 says the zero class is occupied by ALL inert
rational primes and by the ramified place. That is TRUE under the norm
normalization |w|_1 = N(P)^(1/2) e^t, and FALSE under the literal
`|pi|_1 = sqrt(p) e^t` written in the setting line, which is the split
specialization N(P) = p. Under sqrt(p) an inert prime would sit at
(1/2) log p mod log phi, which is not the zero class. Fix the setting line to
N(P)^(1/2), then C3 stands: inert P = (p) has |p|_1 = p = N(P)^(1/2), and the
ramified P = (sqrt5) has |sqrt5|_1 = sqrt5 = N(P)^(1/2). Both give t = 0
exactly. Verified exactly in the breaker.

LEMMA-E-WEIGHT (simplification, not an error). Lemma E is stated with
hypotheses it does not need. F is totally real, so place 1 is an injective
field embedding into R: |u|_1 = 1 alone forces u = +-1, and place-1
positivity then forces u = +1. The hypotheses `|u|_1 = |u|_2` and `N(u) = +1`
only serve to derive |u|_1 = 1 when the product is what is known. PROP-2 and
PROP-2b compute |u|_1 = 1 directly, so both proofs can cite the one-place
form. The same shortcut removes the ab = 0 branch analysis from PROP-1 A1
(Lemma 1 is still required by A2 and stays).

## 4. PROP-2C, the statement that subsumes both

PROP-2C (rapidity independence). Let p_1, ..., p_k be pairwise distinct split
rational primes and P_i a prime above p_i. Then the real numbers
t_1, ..., t_k, log phi are linearly independent over Q. Equivalently: if
m_1 t_1 + ... + m_k t_k = n log phi with m_i, n integers, then every m_i = 0
and n = 0.

Proof. Put u = prod_i (pi_i / sigma(pi_i))^(m_i) . phi^(-2n). At place 1,
log|pi_i|_1 - log|sigma(pi_i)|_1 = 2 t_i, the norm halves cancelling between
conjugates, so log|u|_1 = 2(sum_i m_i t_i - n log phi) = 0. Hence |u|_1 = 1
and u = +-1. Passing to fractional ideals, prod_i P_i^(m_i) sigma(P_i)^(-m_i)
= (1). The 2k prime ideals P_1, sigma(P_1), ..., P_k, sigma(P_k) are pairwise
distinct: P_i != sigma(P_i) because p_i splits, and no prime above p_i equals
a prime above p_j for i != j. Unique factorization therefore forces every
exponent to vanish, m_i = 0 for all i, and the relation collapses to
0 = n log phi, so n = 0. qed

A Q-relation clears denominators to a Z-relation, so the Q-statement and the
Z-statement are the same statement.

k = 1 is PROP-2. k = 2 with coefficients (m, -m) is PROP-2b(ii) and with
(m, m) is PROP-2b(iii). One proof, one page, strictly stronger conclusion.

HONESTY ON NOVELTY. This is not new mathematics in the wider literature. It
is the injectivity of the logarithmic embedding on the group generated by the
split primes and the fundamental unit, which is classical. What is new is
that the chain is explicit, elementary, and pinned inside this program, with
no analytic input and no float.

## 5. Consequences that PROP-2C buys and PROP-2b does not

```
C4  EQUIDISTRIBUTION, not merely non-collision. Fix split p_1..p_k and set
    alpha_i = t_i / log phi. PROP-2C says <h, alpha> is irrational for every
    nonzero integer vector h, so by Weyl's criterion the sequence
    m -> (m t_1, ..., m t_k) mod log phi is equidistributed in the k-torus,
    and in particular dense (Kronecker). The isogeny orbit of any finite set
    of split classes does not merely avoid collision, it fills the torus with
    the uniform measure. Status: candidate-T conditional on PROP-2C, standard
    theorem applied.
C5  FREE RANK. The split classes generate a free abelian subgroup of
    R/(log phi)Z of infinite rank (Dirichlet supplies infinitely many split
    p, PROP-2C supplies independence). No finite-rank or finite-quotient
    carrier can hold them, which is the group-theoretic form of C2.
C6  INTERVAL ROUTE STRENGTHENED. Consequence 1 of the reviewed doc says
    certified intervals can always be refined to re-separate. PROP-2C gives
    that for every finite linear test, not only for pairwise ones: no finite
    set of split classes admits ANY integer linear coincidence, so no
    refinement schedule can be defeated by a conspiracy among several primes
    at once.
```

C1 stands, with a bookkeeping note: the order M and the character index k
combine as m = M |k| >= 1, which is what PROP-2 consumes.
C2 stands. Its two halves are different in kind and the doc keeps them
apart correctly: quotients by a finite subgroup of the circle are exactly the
m-scalings and are excluded by PROP-2b, while an arbitrary rounding map to a
finite set collides by pigeonhole and is declared loss.
Consequence 2 of the reviewed doc is arithmetically correct as written:
zeta_F = zeta . L(chi_5) for F = Q(sqrt5), so the circle alone does not
isolate zeta.

## 6. Breaker

An independent code path was written and run against PROP-2, PROP-2b and
PROP-2C. It shares no code with the accepted verifier of C-PRIME-ORDER-
READING-1 and it never uses Lemma E: it compares place-1 absolute values by
exact sign determination in Z[phi] and only afterwards asks whether the two
elements agree up to sign, so a false Lemma E would show up as a disagreement
between the two answers rather than being assumed away.

```
file        breaker_prop2_torsion_nogo.py
sha256      853d6a38f79c18ec5656a965b9b533ef6ea7d82ea24cb1c9011cfbc1b8c84550
bytes       12199
stdout      sha256 097b7f963c0d324e61bd610feff5c58646c8c6f3341516eb5dde24f31cd965e4
            (of the report text above the hash line)
env         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
            Python 3.11.15, Ubuntu 24.04, x86_64, single platform
method      exact integers only, no float in any assertion AND none in the
            search steering: the candidate exponent n is bracketed by
            doubling and bisection on exact sign comparisons, so a reported
            miss is certified, not sampled
```

Result: 5 of 5 positive controls FOUND, 52878 certified tests, 0
counterexamples, 0 Lemma E disagreements, 0 gauge-dependent verdicts.

```
controls   synthetic phi^6 and -phi^(-4) ratios located at n = 3 and n = -2;
           inert primes 2, 3, 7, 13, 17 at the zero class; ramified sqrt5 at
           the zero class; P against sigma(P) above the same p colliding for
           every m from 1 to 12 (the boundary of section 2)
T2         28 split primes below 300, m from 1 to 64, 1792 tests, 0 hits
T2b        378 unordered pairs, both orientations, m from 1 to 16, 12096
           tests, 0 collisions
T2C        three coefficient boxes, {11,19,29,31,41,59} with coefficients in
           [-2,2], {11,19,29,31} in [-4,4], {61,71,79,89,101} in [-3,3],
           38990 tests, 0 relations
gauge      verdict invariant under w -> phi w, phi^3 w, -w, sigma(w),
           -phi sigma(w) on the first 8 split primes
```

Status of this run: candidate-C at audited range, single platform. It is an
attack survival and a check on the SETTING (normalization, gauge invariance,
class number one witnessed for every split p below 300). It is not the
evidence for PROP-2, PROP-2b or PROP-2C. The proofs are.

## 7. What is still open

```
1  This review is a second reading by a second author, which is what PROP-1
   asked for. It is not a fold. Nothing here promotes anything.
2  PROP-2C is written but has had exactly one honest attempt to break it, in
   this session. It should get a third reading before it is packaged.
3  The C3-NORM correction is owner work: it touches the setting line of a doc
   this session did not write.
4  Consequence 4 of the reviewed doc stands unchanged: nothing here opens the
   Gram test, and no prereg is written without an explicit ANO.
```

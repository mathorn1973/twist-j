# ATTACK-M37-STRENGTH: strength reading of the reduced target (M37)

```text
STATUS     NON-CANONICAL incubation note. Lane C of the 2026-09-15 RH attack session.
           No status motion. Gates nothing.
DATE       2026-09-15
BASIS      Public Canon v86 (STATUS.md ACTIVE, tag canon-v86), unchanged by this note
RH         unchanged. Open program-level obligation per ZETA-RH-STATUS-2026-09-08.md
           section 1 and RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md.
TARGET     (M37) of README.md in the signed-moment note (draft PR #856), identical to
           (A71) of ANALYTIC.md. Read with ARITHMETIC.md and PRIME-CANCELLATION.md.
VERIFIER   verify_m37_strength.py, stdout verify_m37_strength.stdout.txt; SHA-256 of both
           in the Pins section. CHECKS: 17 of 17 PASS, exit 0, empty stderr, byte-identical
           on rerun, env -i LC_ALL=C PYTHONHASHSEED=0, CPython 3.11, standard library,
           exact int/Fraction in every gated assertion.
REVISION   Repaired after two adversarial referee reports (same date); every accepted
           correction and every rejected objection is listed in the Review record
           section. Statuses below are the post-repair statuses.
COUNTING   RH-ONE-WALL-CROSSREF_2026-08-17.md applies. Section 3.6 and item (ii) of
           section 4 are a reading of the known Gram/detection wall, not a new theorem.
LABELS     candidate-T, F-route, R, O, HEURISTIC as defined by the session discipline.
```

## 0. Summary

The task asked for a "strength reading" of (M37) through a pole mechanism and
expected the conclusion that (M37) with kappa near 1 is of quasi-GRH strength for
zeta_F, F = Q(sqrt 5). The mechanism was carried out exactly and the expected
conclusion does not survive. Five lines:

1. Series structure (Theorem 1, candidate-T, corrected after review): F^{(k)}(s) =
   G_k(s) / (zeta(s) L(s,chi_5)) with G_k an Euler product, absolutely convergent,
   holomorphic and zero-free on Re s > 1/2. Poles of F^{(k)} on Re s > 1/2 are exactly
   the zeros of zeta_F there, with equal order, independently of k; the residue carries
   the finite factor G_k(rho) = G_1(rho) prod_{p | k} (1 - 2 p^{-rho})^{-1} (CHECK 16;
   the pre-review display carried a spurious factor prod_{p|k}(1 - p^{-rho})^2, see the
   Review record). This is the O_5 divisor dictionary of
   C-GRH-QSQRT5-SPLIT-ORIENTATION-1.md section 5 transported to the support series of
   the note (local factor 1 - 2x instead of (1-x)^2/(1+x^2)); one dictionary, not a
   second theorem.
2. Ceiling (Theorem 4, candidate-T, conditional with the hypothesis displayed; it is
   the record's own (A62)-(A64) argument with the pointwise exponent nu_sigma of (A41)
   replaced by epsilon, as (A73) already anticipates, not a new ceiling): the Lindelof
   hypothesis for the single function L(s, chi_5), LH(chi_5), implies (M37) uniformly
   in every k <= T, hence the note's analytic target (A54). The Fejer form (A58) would
   follow by the same route only through a partial-sum bound under LH that is not
   written here; that part is O (Corollary 4.2). RH for zeta(s) never enters. So (M37)
   is at most LH(chi_5)-strength.
3. Floor (Theorem 3, F-route; no zero hypothesis; residue hypothesis
   |R_rho| <= T^{delta/2} displayed): under that residue bound the single-pole Perron
   mechanism cannot extract a zero-free strip Re s > beta_1, beta_1 < 1 - nu_sigma/(2-kappa),
   for zeta_F from (M37); for larger beta the route is unsupported unconditionally
   (not ruled out) and excluded under LH(chi_5). Without any residue bound the route is
   not closed but undefined (lemma (i) of section 4). The task's threshold
   beta*(kappa) = (3 - 2 kappa)/(4 - 2 kappa) is the w = 1/2 member of the family
   beta_pole(kappa, w) = 1 - w/(2 - kappa); it presupposes weight mass T^{2w} = T in a
   unit window at the ordinate of the zero, which the note's own pointwise bound (A41)
   excludes (2 nu_sigma < 1). Under the natural weight lower bound (W) the mechanism
   is vacuous (beta_pole = 1). The algebra is verified exactly (CHECK 09-13).
4. Multi-pole reading (HEURISTIC): at best zero-density strength for zeta_F, never
   zero-free-strip strength; its domination lemma is the large-values problem for
   Dirichlet polynomials, read here as the least eigenvalue of a Cauchy/Pick Gram
   matrix of Lorentzians: the same wall as the T2 Weyl detection threshold.
5. Bookkeeping (Proposition 6, R): the normalized mean-value bound already sits at
   the (M37) scale, unconditionally, with no zero hypothesis. The "factor T" of the
   task is the normalization T^{-1} of ||.||_{2,T}. The (M32)-(M33) gap 2 nu_sigma is
   a different quantity (the pointwise weight loss). Exact fractions in CHECK 11-12.

Placement: (M37)'s inputs are classical L(s, chi_5) information outside the fence of
TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]; the guard makes the difficulty explicit
(subconvexity-versus-Lindelof for L(s, chi_5) at two off-line abscissae, or a joint
cancellation replacing pointwise control) rather than moving it; the bridge row stays
O/STOP; RH stays open.

## Falsifiers first

| Claim | What kills it |
|---|---|
| C1 Theorem 1 (series structure) | Any r <= 2000 and k in {1, 11, 209, 6061} where the Euler-product coefficient differs from f(r) 1_{(r,k)=1} (CHECK 05-06); any n <= 2000 where (f^{(k)} * (1*chi))(n) differs from the local table g_k(n) (CHECK 07); any split prime p and s with Re s > 1 at which G_{k,p}/G_{1,p} differs from 1/(1 - 2p^{-s}), or any n <= 2000 at which (G_k/G_1)(n) differs from 2^{Omega(n)} 1_{supp(n) subset {p | k}} (CHECK 16); a split prime p and s with Re s >= 1/2 and p^{-s} = 1/2 (impossible: the smallest split prime is 11 and 2^2 < 11, CHECK 04); an error in the majorant sum_p p^{-1-2 delta} used for absolute convergence. For T1': a split prime and s on Re s >= 1/2 with 2p^{-3s}/(1-p^{-s})^2 = 1 (excluded by CHECK 17). |
| C2 Theorem 4 (LH(chi_5) implies (M37) and (A54)) | A misquotation of (A45) or (A60) of ANALYTIC.md, which are the only inputs besides the hypothesis; or a proof that the supremum of the weight on [T,2T] is not bounded by the two L-values plus O(1). The hypothesis LH(chi_5) is displayed; the theorem is falsified, not weakened, if either input is wrong. The (A58) part (Corollary 4.2) is O and has no claim to kill. |
| C3 Theorem 3 / Theorem 5 (single-pole budget, F-route) | An error in the ratio exponent 2w - 2(2-kappa)(1-beta) (CHECK 13); an unconditional weight concentration W_gamma >> T^{2 nu_sigma + epsilon} (would contradict (A41)); a residue R_rho of size exceeding the displayed bound |R_rho| <= T^{delta/2} (then the zero is outside the scope of Theorem 3, which is conditional on that bound and says nothing about such a zero; the F-route is closed only under the residue hypothesis). |
| C4 Proposition 6 (bookkeeping) | A rational-arithmetic error (CHECK 11-12) or a misquotation of the normalization ||Q||_{2,T}^2 = T^{-1} int_T^{2T} |Q|^2 from README.md section 2 and ANALYTIC.md section 1. |
| C5 Threshold algebra | Failure of the polynomial identity (2-k)(3-2k) = (2-k)(4-2k) - (4-2k)/2 (CHECK 09) or of the table beta*(0) = 3/4, beta*(0.98) = 26/51, beta*(0.99) = 51/101, beta*(0.999) = 501/1001 (CHECK 10). |
| C6 Multi-pole reading | Not a claim (HEURISTIC). It is superseded, not killed, by a proof of the domination lemma (ii) of section 4. |
| C7 Placement | The bridge-row text used here was compared byte for byte with canon/REGISTRY.tsv at canon-v86 during this session; a later change of that row invalidates the quotation, not the mathematics. |

## Verdict table

| ID | Statement | Status | Where |
|---|---|---|---|
| T1 | F^{(k)} = G_k / (zeta L); G_k absolutely convergent, holomorphic, zero-free on Re s > 1/2; poles = zeros of zeta_F with equal order, k-independent; residue R_rho = G_k(rho)/(zeta L)'(rho) with k-factor G_k(rho) = G_1(rho) prod_{p|k}(1 - 2p^{-rho})^{-1} | candidate-T (corrected after review: k-factor replaced, now CHECK 16 certified; duplicate of the record's O_5 divisor dictionary with a second local factor) | section 2; CHECK 01-08, 16 |
| T1' | Relation to the Canon channel: F^{(1)} = O_5 prod_{split}(1 - 2p^{-3s}/(1-p^{-s})^2), the product absolutely convergent for Re s > 1/3 and zero-free on Re s >= 1/2; same divisor dictionary, one wall reading | candidate-T (duplicate of record, second local factor) | section 2.4; CHECK 03, 17 |
| P2 | Exact size of one pole term: unweighted, weighted upper (two ways), weighted lower under a window bound | candidate-T (proof-based; CHECK 14 certifies only its finite pieces: the modulus expansion, the b-range endpoints and the window inequality; the all-t bounds rest on the written proof and on (A25), (A41)) | section 3.3; CHECK 14 |
| A3 | beta_pole(kappa, w) = 1 - w/(2-kappa) when both the unit-window mass W_gamma and sup_{[T,2T]}|A_M B_M|^2 are T^{2w}; beta*(kappa) = beta_pole(kappa, 1/2) = (3-2kappa)/(4-2kappa); table; equivalently beta*(kappa) is where sup_t|Pi_rho| = T_0 | candidate-T (finite algebra) | section 3.4; CHECK 09-10, 13 |
| T3 | Single-pole F-route, no zero hypothesis, residue hypothesis displayed: under |R_rho| <= T^{delta/2}, no zero-free strip Re s > beta_1, beta_1 < 1 - nu_sigma/(2-kappa) - delta, follows from (M37) by one pole term; for larger beta the term reaches the scale only with |R_rho|^2 W_{gamma,j} >= min(b^2,j^2) T^{2(2-kappa)(1-beta)}, which no known result supplies (route unsupported, not ruled out) and which LH(chi_5) excludes for every beta < 1 given |R_rho| <= T^{o(1)} | F-route (conditional on the displayed residue bound) | section 3.5 |
| H4 | Multi-pole reading: zero-density strength at best; domination lemma = large values = Gram least eigenvalue | HEURISTIC / O | section 3.6 |
| T4 | LH(chi_5) implies (M37) uniformly in k <= T, hence (A54) | candidate-T (conditional, hypothesis displayed; the record's (A62)-(A64)/(A73) method with nu_sigma -> epsilon, not a new ceiling) | section 4.2 |
| T4-Fejer | LH(chi_5) implies (A58) = (M18) | O (needs a partial-sum-under-LH lemma uniform in M and t, not written; withdrawn from candidate-T after review) | Corollary 4.2 |
| T5 | The pole guard made rigorous: (M37) + (D) + (W_w) + (Res) implies beta_0 <= 1 - w/(2-kappa) + o(1); vacuous at w = 0, empty hypothesis set at w > nu_sigma | candidate-T (conditional, vacuous under (W); A3 restated with explicit constants, one reading) | section 4.3 |
| P6 | Normalized mean value = (M37) scale unconditionally; the task's "factor T" is normalization; (M32) gap is 2 nu_sigma from the weight | R (exact bookkeeping; the mean value is literally (A60) = (A11)+(A21) of the record) | section 5; CHECK 11-12, 15 |
| PL | Placement: inputs classical, outside the bridge fence; difficulty explicit, not moved; bridge row O/STOP; RH unchanged | R | section 6 |

## 1. Notation and the record used

chi = chi_5 with values (0, 1, -1, -1, 1) on residues (0, 1, 2, 3, 4) mod 5. A prime is
split if chi(p) = 1 (p = 1, 4 mod 5; smallest 11), inert if chi(p) = -1, ramified if
p = 5. R is the set of squarefree integers supported on split primes, including 1,
and f(r) = (-2)^{omega(r)} on R, f = 0 off R (README.md (M1), ANALYTIC.md (A1)).
For k in R,

    F^{(k)}(s) = sum_{r in R, (r,k)=1} f(r) r^{-s},
    F^{(k)}_U(s) = sum_{r <= U, r in R, (r,k)=1} f(r) r^{-s}          (A60), (M35).

Parameters as in the note: 1/4 < sigma < 0.26 fixed, s = sigma + it, T >= 2,
Y = T^2, M = ceil(40T), 1/(4 sigma) < kappa < 1, A_M and B_M as in (M14)/(A30),
||Q||_{2,T}^2 = T^{-1} int_T^{2T} |Q(t)|^2 dt. The target:

    (M37)  ||A_M B_M F^{(k)}_{Y/k}||_{2,T}  <<_{sigma,kappa,epsilon}  (Y/k)^{1-sigma} T^{-1/2+epsilon},
           k in R, k <= T^kappa, constant independent of k.

Write U = Y/k, so U >= T^{2-kappa} > T, and T_0 := U^{1-sigma} T^{-1/2} for the
target scale. Statements of the note used as proved inputs (not re-proved here):
(A11) positive support sums; (A21) elementary mean value for Dirichlet polynomials;
(A25) fourth moments of A_M, B_M uniformly in M; (A41) pointwise
|A_M(t) B_M(t)| << (1+|t|)^{nu_sigma + epsilon}, nu_sigma = a_sigma + b_sigma of (A40),
0 < nu_sigma < sigma, 2 nu_sigma < 1; (A45) the approximate functional equation
||A - A_M||_{infty,T} << T^{-(1-sigma)}, ||B - B_M||_{infty,T} << T^{-2 sigma} with
A(t) = L(1-sigma-it, chi), B(t) = L(2 sigma + 2it, chi); (A60) the mean value for
F^{(k)}_U uniform in k; section 9 of ANALYTIC.md, the sufficiency (A71) => (A54).
Classical facts are marked [T-lit] and named where used, in the convention of
C-GRH-QSQRT5-SPLIT-ORIENTATION-1.md.

## 2. The full series (task 1)

### 2.1 Theorem 1 (candidate-T)

Let x = p^{-s}. Define the local factors

    G_{k,p}(x) = (1 - 2x)/(1 - x)^2 = 1 - x^2/(1-x)^2 = 1 - sum_{j>=2} (j-1) x^j   (split p, p not | k),
    G_{k,p}(x) = 1/(1 - x)^2                                                       (split p, p | k),
    G_{k,p}(x) = 1/(1 - x^2) = 1 + x^2/(1 - x^2)                                   (inert p),
    G_{k,5}(x) = 1/(1 - x)                                                         (p = 5),

and G_k(s) = prod_p G_{k,p}(p^{-s}). Then:

(a) For Re s > 1, F^{(k)}(s) = prod_{p split, p not | k} (1 - 2 p^{-s}), absolutely convergent.

(b) zeta(s) L(s,chi) = zeta_F(s) has local factors (1-x)^{-2} (split), (1-x^2)^{-1} (inert),
    (1-x)^{-1} (p = 5).

(c) The product defining G_k converges absolutely and uniformly on every closed
    half-plane Re s >= 1/2 + delta, delta > 0. G_k is holomorphic and zero-free on
    Re s > 1/2, and F^{(k)}(s) zeta(s) L(s,chi) = G_k(s) for Re s > 1.

(d) Hence F^{(k)} continues meromorphically to Re s > 1/2 as G_k/(zeta L). On this
    half-plane its poles are exactly the zeros of zeta(s) L(s,chi) there, with the same
    order, and this set and these orders do not depend on k; its only zero there is
    s = 1 (simple). At a zero rho of order m, the principal part of F^{(k)} at rho has
    leading coefficient m! G_k(rho) / (zeta L)^{(m)}(rho), which is nonzero; for a
    simple zero the residue is

        R_rho^{(k)} = G_k(rho) / (zeta L)'(rho),
        G_k(rho) = G_1(rho) prod_{p | k} (1 - 2 p^{-rho})^{-1}.

    (Corrected after review; the pre-review display prod_{p|k}(1-p^{-rho})^2/(1-2p^{-rho})
    was wrong. CHECK 16.)

### 2.2 Proof

(a) sum_{p split} 2 p^{-Re s} < infinity for Re s > 1, so the product converges
absolutely; expanding it, the coefficient of r^{-s} is prod_{p | r}(-2) when r is
squarefree, split-supported and coprime to k, and 0 otherwise, which is
f(r) 1_{(r,k)=1}. The verifier confirms this for all r <= 2000 and k in
{1, 11, 209, 6061} (CHECK 05-06); at this scope only primes <= 2000 enter, so the
finite check is exact for the finite prefix.

(b) zeta has local factor (1-x)^{-1}, L(s,chi) has (1 - chi(p) x)^{-1}; the product is
(1-x)^{-2}, (1-x^2)^{-1}, (1-x)^{-1} in the three cases (CHECK 02). In-repo the
factorization zeta_F = zeta L(., chi_5) is recorded as a literature import in
C-GRH-QSQRT5-SPLIT-ORIENTATION-1.md section 2 and in the PREREG of
P-O5-DEDEKIND-GRH-READ-1, item A1; the coefficient sequence of zeta_F is 1 * chi,
the ideal count of J-IDEAL-COUNT-QUADRATIC-CHARACTER [T].

(c) The local identity (1-2x)(1-x)^{-2} = 1 - x^2/(1-x)^2 = 1 - sum_{j>=2}(j-1)x^j is
CHECK 01 (formal power series over Q to order x^12; the identity is a rational
function identity, (1-x)^2 - x^2 = 1 - 2x, so the order-12 check is a check of the
implementation, the identity itself is one line). Absolute convergence: fix
delta > 0 and Re s >= 1/2 + delta. For split p >= 11, |x| <= 11^{-1/2} < 1/2 because
2^2 < 11 (CHECK 04), so |1-x| >= 1/2 and |x^2/(1-x)^2| <= 4 p^{-1-2 delta}. For inert
p >= 2, |x^2/(1-x^2)| <= p^{-1-2delta}/(1 - p^{-1}) <= 2 p^{-1-2delta}. The finitely
many factors at p | k and p = 5 are holomorphic and nonzero for Re s > 0. Hence
sum_p |G_{k,p}(p^{-s}) - 1| <= 4 sum_p p^{-1-2delta} + O_k(1) < infinity uniformly on
the closed half-plane, so the product converges absolutely and uniformly there, its
limit is holomorphic, and it vanishes only where a factor vanishes. No factor
vanishes: 1 - 2x != 0 since |x| < 1/2 at split primes, and 1 - x, 1 - x^2 != 0 since
|x| < 1. For Re s > 1 all three Euler products F^{(k)}, zeta, L converge absolutely
and the factorwise identity (a), (b) gives F^{(k)} zeta L = G_k. CHECK 07 verifies
this identity at coefficient level, (f^{(k)} * (1*chi))(n) = g_k(n) for n <= 2000 and
k in {1, 11, 209}, where g_k is the multiplicative sequence read off the local table
(g_k(p) = 0 at split p not dividing k, g_k(p^j) = -(j-1) for j >= 2 there,
g_k(p^j) = j+1 at split p | k, 1 or 0 at inert p by parity of j, 1 at powers of 5);
CHECK 08 verifies g_1(n) = 0 for every squarefree n > 1 prime to 5, the global
expression of "each infinite factor is 1 + O(p^{-2s})".

(d) G_k/(zeta L) is meromorphic on Re s > 1/2 (zeta has one pole, at s = 1; L is
entire [T-lit]) and agrees with the Dirichlet series on Re s > 1, so it is the
meromorphic continuation. Since G_k is zero-free and holomorphic there, the divisor
of F^{(k)} on Re s > 1/2 is minus the divisor of zeta L: poles at the zeros of zeta L
with equal order, one zero at s = 1 (L(1,chi) != 0 [T-lit]). The divisor of zeta L
does not involve k; only G_k does, through the finite product over p | k: the factor
at p | k is (1-x)^{-2} instead of (1-2x)(1-x)^{-2}, and the quotient is
(1-x)^{-2} / [(1-2x)(1-x)^{-2}] = 1/(1-2x). Equivalently F^{(k)} = F^{(1)} prod_{p|k}(1-2p^{-s})^{-1}
on Re s > 1 (the product over p not dividing k is the product over all split p with
the factors at p | k removed), so G_k = G_1 prod_{p|k}(1-2p^{-s})^{-1} on Re s > 1 and,
by uniqueness of continuation, on Re s > 1/2. CHECK 16 verifies the local quotient as a
formal series (coefficients 2^j), at p = 11, s = 2 (121/119), and at coefficient level:
(G_k/G_1)(n) = 2^{Omega(n)} for n supported on the primes dividing k and 0 otherwise,
n <= 2000, k in {11, 209}. The leading coefficient of the principal part is
m! G_k(rho)/(zeta L)^{(m)}(rho) by the standard expansion of 1/(zeta L) at a zero of
order m. QED.

### 2.3 Remarks on the residue

The residue is not controlled unconditionally: |G_k(rho)| is bounded above and
below by constants depending on delta = Re rho - 1/2 times the finite k-factor
prod_{p | k} |1 - 2p^{-rho}|^{-1}, whose modulus lies between
prod_{p | k} (1 + 2p^{-1/2})^{-1} and prod_{p | k} (1 - 2p^{-1/2})^{-1} (since |1 - 2x| lies in
[1 - 2|x|, 1 + 2|x|] and |x| <= p^{-1/2} < 1/2 at split p >= 11; bounds corrected after
review together with the k-factor); but 1/|(zeta L)'(rho)| has no known upper bound at a
hypothetical off-line zero. Theorem 3 below is therefore stated
with an explicit residue condition. Nothing in this section locates a zero or asserts
one.

### 2.4 One wall reading (T1')

C-GRH-QSQRT5-SPLIT-ORIENTATION-1.md sections 5-6 and the PREREG of
P-O5-DEDEKIND-GRH-READ-1 record the same divisor statement for the Canon channel
O_5(s) = prod_{split} (1-x)^2/(1+x^2): its continuation is G/zeta_F with G a unit on
Re s > 1/2. Since (1 - 2x)(1 + x^2) = (1 - x)^2 - 2x^3 (CHECK 03),

    F^{(1)}(s) = O_5(s) prod_{p split} ( 1 - 2 p^{-3s}/(1 - p^{-s})^2 ),

and the last product converges absolutely for Re s > 1/3 (|x| <= 11^{-1/3} < 1/2 so
|1 - x| >= 1/2 and the terms are at most 8 p^{-3 Re s}). It is also zero-free on
Re s >= 1/2, which the "same divisor" statement needs and the pre-review text left
implicit: at a split prime with y = |x| <= 11^{-1/2}, |2x^3/(1-x)^2| <= 2y^3/(1-y)^2 < 1/8,
since 2y^3/(1-y)^2 is increasing on (0,1) and at y = 11^{-1/2} the inequality
16y^3 < (1-y)^2 reduces, with y^2 = 1/11, to y < 6/19, i.e. 1/11 < 36/361 (CHECK 17, exact,
with the rational witness 0.302 > 11^{-1/2}). Hence F^{(1)} and O_5 have the same divisor
on Re s > 1/2. Theorem 1 is that dictionary transported to the support series of the signed-moment note; under the
counting rule it is one dictionary with a second local factor, not a second theorem.
Not claimed: the closed-line floor sigma_c(F^{(k)}) >= 1/2 (the analogue of
QS5-SUMMATORY-FLOOR), which would need G_k on Re s = 1/2, where the product is not
absolutely convergent; it is not needed here.

## 3. The pole mechanism (task 2)

### 3.1 Perron representation (exact, [T-lit])

Fix s = sigma + it and c = 1 - sigma + eta with eta > 0, so that Re(s + w) = 1 + eta
on the line Re w = c, where the series of F^{(k)}(s+w) converges absolutely. Perron's
formula (Montgomery-Vaughan, Multiplicative Number Theory I, Theorem 5.1; Titchmarsh,
Lemma 3.12) gives, for U > 1 not an integer (with the half-term convention at
integers),

    F^{(k)}_U(s) = (1/2 pi i) int_{c - i infinity}^{c + i infinity} F^{(k)}(s + w) U^w dw/w,

the integral understood as a symmetric limit. Truncating at |Im w| <= V costs the
standard error, of the kind bounded in the note's (A26)-(A27); its size is not needed
below. This representation is exact and is labelled candidate-T by citation.

### 3.2 Shape of one pole term (exact)

Let rho = beta + i gamma be a simple zero of zeta L with beta > 1/2. Since
Re s = sigma < 1/2 < beta, the point w = rho - s has Re w = beta - sigma > 0. Any
contour shift that stays inside Re(s + w) > 1/2, i.e. to a line Re w = c' with
c' = 1/2 + delta - sigma > 0, remains to the right of w = 0: no residue at w = 0 is
ever collected, and the only poles between Re w = c and Re w = c' are the points
w = rho - s with Re rho > 1/2 + delta. Formally,

    (1/2 pi i) int_{(c)} = (1/2 pi i) int_{(c')} + sum_{rho: Re rho > 1/2 + delta} Pi_rho(t),
    Pi_rho(t) := R_rho^{(k)} U^{rho - s} / (rho - s),

with the sign fixed by the counterclockwise rectangle; the modulus is convention-free.
The word "formally" is the whole content of lemma (i) in section 4: the horizontal
segments at height +-V require a bound for |G_k/(zeta L)| on the strip, which is not
available. The shape of Pi_rho is exact:

    |Pi_rho(t)|^2 = |R_rho|^2 U^{2(beta - sigma)} / ( (beta - sigma)^2 + (t - gamma)^2 ),

a Lorentzian in t centred at gamma with half-width b := beta - sigma, and
b in (1/2 - 0.26, 1 - 1/4) = (6/25, 3/4) for the parameter ranges (CHECK 14). At a
zero of order m the term is U^{beta - sigma} times a polynomial of degree m - 1 in
log U over (rho - s)^m; this changes no exponent and is not treated separately.

### 3.3 Proposition 2 (sizes of one pole term; candidate-T)

Let gamma in [T + 1, 2T - 1], b = beta - sigma, and
W_gamma := int_{gamma - 1}^{gamma + 1} |A_M(t) B_M(t)|^2 dt.

(a) Unweighted:
    2 |R_rho|^2 U^{2b} (1 + b^2)^{-1} T^{-1}  <=  ||Pi_rho||_{2,T}^2  <=  pi |R_rho|^2 U^{2b} b^{-1} T^{-1}.
    Proof: the full-line integral of the Lorentzian is pi/b; on |t - gamma| <= 1 the
    Lorentzian is at least 1/(b^2 + 1) (CHECK 14).

(b) Weighted, two upper bounds:
    ||A_M B_M Pi_rho||_{2,T}^2 <= |R_rho|^2 U^{2b} b^{-2} T^{-1} int_T^{2T} |A_M B_M|^2 dt
                                <<_{sigma,epsilon} |R_rho|^2 U^{2b} T^{epsilon},
    by the note's fourth-moment consequence int_{-X}^{X} |A_M B_M|^2 << X^{1+epsilon}
    (ANALYTIC.md section 4, the line after (A30), from (A25) and Cauchy-Schwarz); and
    ||A_M B_M Pi_rho||_{2,T}^2 <= pi |R_rho|^2 U^{2b} b^{-1} T^{-1} sup_{[T,2T]} |A_M B_M|^2
                                <<_{sigma,epsilon} |R_rho|^2 U^{2b} T^{2 nu_sigma - 1 + epsilon}
    by (A41).

(c) Weighted, lower bound through the window:
    ||A_M B_M Pi_rho||_{2,T}^2 >= |R_rho|^2 U^{2b} (1 + b^2)^{-1} T^{-1} W_gamma.

Dividing by T_0^2 = U^{2 - 2 sigma} T^{-1}: the weighted single-pole contribution
relative to the squared target scale is

    ratio(rho) = ||A_M B_M Pi_rho||_{2,T}^2 / T_0^2,
    |R_rho|^2 U^{2 beta - 2} (1+b^2)^{-1} W_gamma  <=  ratio(rho)  <=  pi b^{-1} |R_rho|^2 U^{2 beta - 2} sup_{[T,2T]} |A_M B_M|^2.

### 3.4 The threshold algebra (task 2, exact; CHECK 09, 10, 13)

Suppose W_gamma and sup_{[T,2T]}|A_M B_M|^2 are both of size T^{2w} for some
0 <= w <= 1/2 (w = 1/2 is the extreme case in which the whole L^2 mass T^{1+epsilon} of
the weight sits in the unit window), |R_rho| is of size T^{o(1)}, and U = T^{2-kappa}.
Then ratio(rho) = T^{2w - 2(2-kappa)(1-beta) + o(1)}, which stays bounded by T^{o(1)}
exactly when

    beta <= beta_pole(kappa, w) := 1 - w/(2 - kappa).

At w = 1/2 this is beta_pole(kappa, 1/2) = 1 - 1/(2(2-kappa)) = (3 - 2 kappa)/(4 - 2 kappa)
= beta*(kappa), the task's formula. The verifier checks the identity
(2 - kappa)(3 - 2 kappa) = (2 - kappa)(4 - 2 kappa) - (4 - 2 kappa)/2 as an identity of
polynomials in kappa (both sides 6 - 7 kappa + 2 kappa^2), the sigma-independence of
the exponent equation U^{beta - sigma} = U^{1 - sigma} T^{-1/2} at U = T^{2-kappa}, and
the table

    beta*(0) = 3/4 (k = 1 alone, U = T^2),  beta*(0.98) = 26/51,  beta*(0.99) = 51/101,
    beta*(0.999) = 501/1001,  beta*(1) = 1/2.

Reading of this formula. The equation U^{beta - sigma} = U^{1-sigma} T^{-1/2} compares
the peak of the unweighted pole term (equivalently, the unnormalized integral
int_T^{2T} |Pi_rho|^2 of size U^{2b}) with the normalized target. In other words
(a reading added at review, R): beta*(kappa) is exactly the beta at which
sup_t |Pi_rho(t)| = |R_rho| U^{b}/b equals T_0 = U^{1-sigma} T^{-1/2} up to |R_rho|/b, i.e.
U^{beta-1} = T^{-1/2} at U = T^{2-kappa}; the task compares a supremum with an L^2 mean
over an interval of length T. Under the note's
normalization the two objects differ by the factor T, and the comparison is
legitimate only if the weight contributes a factor T in the window, i.e. w = 1/2.
That is excluded: by (A41), W_gamma <= 2 sup |A_M B_M|^2 << T^{2 nu_sigma + epsilon}
with 2 nu_sigma < 1 (CHECK 11; at sigma = 51/200, 2 nu_sigma = 7069361/16895592
= 0.4184...). So the mechanism can never reach beta*(kappa). Its best conceivable
threshold is w = nu_sigma:

    beta_pole(kappa, nu_sigma) = 1 - nu_sigma/(2 - kappa),
    e.g. 676493371/853227396 = 0.79286... at kappa = 99/100, sigma = 51/200,
    and 1 - nu_sigma/2 = 60513007/67582368 = 0.89540... at kappa = 0,

which is strictly larger than beta*(kappa) for every kappa (CHECK 13). Under the
natural hypothesis (W) of the task, W_gamma >> T^{-epsilon}, w = 0 and
beta_pole = 1: no constraint at all.

### 3.5 Theorem 3 (single-pole F-route; no zero hypothesis; residue hypothesis displayed)

Fix sigma in (1/4, 0.26), kappa in (1/(4 sigma), 1), epsilon > 0, delta > 0. Let
rho = beta + i gamma be a simple zero of zeta(s) L(s, chi_5) with 1/2 < beta < 1 and
gamma in [T+1, 2T-1], b = beta - sigma, and let U >= T^{2-kappa}. Write

    J_gamma   := T^{-1} int_{|t - gamma| <= 1} |A_M(t) B_M(t) Pi_rho(t)|^2 dt,
    J_{gamma,j} := T^{-1} int_{j < |t - gamma| <= j+1} |A_M(t) B_M(t) Pi_rho(t)|^2 dt   (j >= 1),

the contributions of the central window and of the j-th shell to the squared (M37)
norm of the pole term, and W_gamma, W_{gamma,j} for the corresponding masses of the
weight |A_M B_M|^2.

(a) [whole interval] If beta < 1 - nu_sigma/(2 - kappa) - delta and |R_rho| <= T^{delta/2},
    then ||A_M B_M Pi_rho||_{2,T} <<_{sigma, epsilon} T^{-delta/2 + epsilon} T_0: the weighted
    single-pole term is below the (M37) scale by a fixed power.

(b) [window and shells, any beta < 1]
    J_gamma <= |R_rho|^2 b^{-2} T^{-(2-kappa)(2-2beta)} W_gamma . T_0^2,
    J_{gamma,j} <= |R_rho|^2 j^{-2} T^{-(2-kappa)(2-2beta)} W_{gamma,j} . T_0^2.
    Consequently the pole term reaches the (M37) scale on the central window or on
    some shell only if |R_rho|^2 W_{gamma,j} >= min(b^2, j^2) T^{2(2-kappa)(1-beta)} for
    some j >= 0 (j = 0 the central window): a weight concentration of exponent
    2(2-kappa)(1-beta) > 0 in a unit window near the ordinate of a hypothetical zero
    of zeta_F, weighted by the squared residue. No unconditional result supplies such
    a concentration. The residue enters and is not controlled (section 2.3): with the
    residue hypothesis |R_rho| <= T^{o(1)}, (A41) caps every |R_rho|^2 W_{gamma,j} at
    T^{2 nu_sigma + epsilon}, which contradicts the condition as soon as
    2(2-kappa)(1-beta) > 2 nu_sigma, i.e. for beta < 1 - nu_sigma/(2-kappa), which is (a)
    again; and LH(chi_5) caps it at T^epsilon, so under LH(chi_5) and the same residue
    hypothesis no single pole term reaches the scale for any beta < 1. Without a residue
    bound neither exclusion holds. (Wording corrected after review: the pre-review text
    dropped the factor |R_rho|^2 in this sentence.)

Proof. (a) By Proposition 2(b), second bound, and (A41),
ratio(rho) << |R_rho|^2 U^{2 beta - 2} T^{2 nu_sigma + epsilon} <= |R_rho|^2 T^{2 nu_sigma - 2(2-kappa)(1-beta) + epsilon},
using U >= T^{2-kappa} and 2 beta - 2 < 0. With beta < 1 - nu_sigma/(2-kappa) - delta the
exponent is at most 2 nu_sigma - 2(2-kappa)(nu_sigma/(2-kappa) + delta) + epsilon
= -2(2-kappa) delta + epsilon <= -2 delta + epsilon, and |R_rho|^2 <= T^delta. Take
square roots. (b) On |t - gamma| <= 1 the Lorentzian factor of |Pi_rho|^2 is at most
b^{-2}, on the j-th shell at most j^{-2}; multiply by |R_rho|^2 U^{2b} T^{-1}, integrate
the weight over the window or shell, divide by T_0^2 = U^{2-2sigma} T^{-1}, and use
U^{2 beta - 2} <= T^{-(2-kappa)(2-2beta)}. The consequences are read off. QED.

Scope. Theorem 3 rules out one route exactly and conditionally: "derive a zero-free
strip Re s > beta_1 for zeta_F, beta_1 < 1 - nu_sigma/(2-kappa), from (M37) through the
single Perron pole term, at zeros whose residue satisfies |R_rho| <= T^{delta/2}". For
beta in [1 - nu_sigma/(2-kappa), 1) the route is unsupported (no unconditional weight
concentration is known), not ruled out; it is excluded under LH(chi_5) with the residue
hypothesis. Without any residue bound the route is not closed but undefined, since
lemma (i) of section 4 is then missing as well. Theorem 3 does not say (M37) has no zero
content of any kind; it says the single-pole term is inside the budget, so that any such
content must come from lemma (ii) of section 4, which is the wall.

### 3.6 Multi-pole reading (HEURISTIC)

Suppose J zeros rho_j = beta + i gamma_j of zeta L have ordinates in [T+1, 2T-1]
pairwise at distance >= 2, each with W_{gamma_j} >> T^{-epsilon} and
|R_{rho_j}| >> T^{-epsilon}, and suppose (D): the pole sum dominates F_U^{(k)} on each
unit window. Then (M37) would give J U^{2 beta - 2 sigma} T^{-1-epsilon} << U^{2-2sigma} T^{-1+epsilon},
i.e. J << U^{2-2beta} T^{2 epsilon} = T^{(2-kappa)(2-2beta) + 2 epsilon}; at kappa -> 1 this
is the density-hypothesis exponent N(beta, T) << T^{2(1-beta)+epsilon} for zeta_F.
HEURISTIC in every step after the first. Two remarks that are not heuristic:

- Even at face value the reading is of zero-density strength, never of
  zero-free-strip strength: one zero contributes nothing (Theorem 3).
- The same heuristic applied to the unweighted F_U, for which the (M37)-scale bound
  is an unconditional theorem (Proposition 6), would "prove" the density hypothesis
  for zeta_F unconditionally. It is not a theorem; the rigorous versions of this
  heuristic are the zero-density theorems (Ingham, Huxley, [T-lit]) with exponents
  A(beta) > 2, and the density hypothesis A = 2 is exactly the heuristic optimum.
  So (D), together with (Res) and the separation hypothesis, cannot be a currently
  provable theorem in general: with Proposition 6 it would prove the density
  hypothesis for zeta_F. Whether (D) is false in general is not shown (wording
  corrected after review; the pre-review text said "fails in general"). In the
  language of the T2 Weyl lane (RESULT-P-RH-WEYL-CANONICAL-2.md, sections 2 and 2b),
  (D) asks for a lower bound on the least eigenvalue of the Cauchy/Pick Gram matrix
  of the pole nodes restricted to a window; clustered nodes drive it to zero (that
  record's R4 "weak-defect wall", w*_24 in [0.10, 1.07] at delta = 1/100; its CHECK 0 /
  ND1 background pivot ladder descends to 6.8e-88; citation split after review). One
  wall, one more reading.

## 4. What is missing for a rigorous guard (task 3)

A "guard" here means a theorem of the form "(M37) implies Re rho <= beta_1 + epsilon
for zeros rho of zeta_F with ordinate in [T,2T]". The pole mechanism needs three
unconditional lemmas, none available:

(i) Growth of 1/(zeta L) to the right of the hypothetical zero. To shift the
    Perron contour to Re w = c' and truncate at height V one needs
    |1/(zeta(z) L(z,chi))| << V^{A} on Re z >= beta_0 + delta', |Im z| <= 3V, with A
    small. Unconditionally such bounds exist only in the classical zero-free region
    Re z > 1 - c/log V (de la Vallee Poussin, for zeta and for L(s, chi_5) [T-lit]);
    no polynomial bound for 1/zeta is known in any fixed strip inside 1/2 < Re z < 1.
    Zero-density estimates do not give it (they count zeros, they do not bound
    1/(zeta L) on a segment through the cluster); mean-value theorems do not give it
    (they bound averages of zeta L, not of its reciprocal). A polynomial bound with
    a small exponent on Re z >= beta_0 + delta' at heights near T follows from a
    zero-free region Re z > beta_0 at heights [T/2, 4T] by the Borel-Caratheodory
    mechanism of Titchmarsh section 14.2 [T-lit]; so (i) is of the same kind as the
    conclusion of the guard, not an input to it. Under GRH(zeta_F), (i) holds with
    A = epsilon [T-lit, the import already named in QS5-SUMMATORY-BRIDGE-DOWN].

(ii) Domination of the single pole term over the other zeros' terms and the shifted
    integral, in L^2 on the window. The Gram matrix of the functions Pi_{rho_j} on
    [gamma_0 - 1, gamma_0 + 1] is a Cauchy/Pick-type matrix; its least eigenvalue
    tends to zero as nodes cluster, and the number of zeros of zeta L in a unit
    window at height T is only known to be O(log T) (Riemann-von Mangoldt for zeta
    and L(s,chi_5) [T-lit]). An isolation hypothesis (I) of the form "no other zero
    of zeta L within distance eta of rho_0 in Re s >= beta_0 - eta'" is not available
    unconditionally, and zero-density estimates bound N(beta_0, T), not the local
    clustering around a given zero. The Weyl-lane analogy is in section 3.6.

(iii) Local lower bound for the weight,
    (W): W_{gamma_0} = int_{|t - gamma_0| <= 1} |A_M B_M|^2 dt >> T^{-epsilon}.
    By (A45), A_M = L(1 - sigma - it, chi) + O(T^{-(1-sigma)}) and
    B_M = L(2 sigma + 2it, chi) + O(T^{-2 sigma}) on [T, 2T], so W_{gamma_0} is, up to
    these errors, the window integral of |L(1-sigma-it,chi) L(2sigma+2it,chi)|^2. A
    zero of L(z, chi) at 1 - sigma + i gamma' with |gamma' - gamma_0| <= 1, or at
    2 sigma + 2 i gamma'' with |gamma'' - gamma_0| <= 1/2, makes a factor small on
    part of the window; several such zeros can make the window integral small, and
    zeros of L(s, chi_5) with real part in (1/2, 1) near a prescribed ordinate cannot
    be excluded unconditionally. The mean value int_T^{2T} |L(u+it,chi)|^2 ~ c T
    (u > 1/2, [T-lit]) gives lower bounds on average over ordinates, not at the
    ordinate of a hypothetical zero of zeta, which is unrelated to L(., chi_5).
    Under GRH(L(., chi_5)), 1/L(z, chi) << |z|^epsilon for Re z >= 1/2 + delta
    [T-lit] and (W) holds; but then Theorem 4 makes (M37) itself a theorem, so a
    guard conditional on (iii) through GRH(chi_5) has nothing left to guard.

### 4.2 Theorem 4 (LH(chi_5) implies (M37); candidate-T, conditional, hypothesis displayed; the record's (A62)-(A64) method with one hypothesis substituted)

Framing (added after review; duplicate-of-record attribution). ANALYTIC.md proves
(A62)-(A64) as [pointwise weight bound (A41)] x [mean value (A59)/(A60)], and (A73)
records that the entire loss above the (M37)/(A54) scale in the separate-moment family
is nu_sigma, attained at the pointwise input p_A = p_B = infinity. Theorem 4 is the
observation that under LH(chi_5) that pointwise input is T^epsilon on [T,2T]; it is the
record's own method with the hypothesis substituted, not a new ceiling, and it is
recorded here because the strength reading of (M37) needs it stated.

Hypothesis LH(chi_5): for every fixed u in [1/2, 1] and every epsilon > 0,
|L(u + it, chi_5)| <<_{u, epsilon} (1 + |t|)^epsilon. (By convexity of the Lindelof
mu-function this is equivalent to the statement on the line u = 1/2 [T-lit].)

Conclusion: for fixed 1/4 < sigma < 1/2, T >= 2, M = ceil(40 T), every k in R and every
U >= 1,

    ||A_M B_M F^{(k)}_U||_{2,T} <<_{sigma, epsilon} T^epsilon (1 + log U)^{1/2} ( U^{1/2 - sigma} + U^{1 - sigma} T^{-1/2} ).

In particular, with Y = T^2 and U = Y/k >= T (all k in R with k <= T, a fortiori
k <= T^kappa), (M37) = (A71) holds with a constant independent of k:

    ||A_M B_M F^{(k)}_{Y/k}||_{2,T} <<_{sigma, epsilon} (Y/k)^{1 - sigma} T^{-1/2 + epsilon}.

Proof. Pointwise for t in [T, 2T]: by (A45), |A_M(t)| <= |L(1 - sigma - it, chi)| + C_sigma T^{-(1-sigma)},
and |L(1 - sigma - it, chi)| = |L(1 - sigma + it, chi)| because chi is real; LH(chi_5)
at u = 1 - sigma in (1/2, 3/4) gives |A_M(t)| << T^epsilon. Likewise
|B_M(t)| <= |L(2 sigma + 2it, chi)| + C_sigma T^{-2 sigma} << T^epsilon by LH(chi_5) at
u = 2 sigma in (1/2, 1) and ordinate 2t in [2T, 4T]. Hence
sup_{[T,2T]} |A_M B_M| << T^{2 epsilon}. Then
||A_M B_M F^{(k)}_U||_{2,T} <= sup_{[T,2T]} |A_M B_M| . ||F^{(k)}_U||_{2,T}, and (A60), which
is (A11) and (A21) with the coprimality restriction only removing positive terms,
gives ||F^{(k)}_U||_{2,T} <<_sigma (1 + log U)^{1/2} (U^{1/2 - sigma} + U^{1 - sigma} T^{-1/2})
uniformly in k. For U >= T the second term dominates (CHECK 12: the exponent
(2 - kappa)(1 - 2 sigma) is at most (2 - kappa)(2 - 2 sigma) - 1 exactly when
kappa <= 1). Relabel epsilon. QED.

Corollary 4.1 ([T-lit] chain). GRH for L(s, chi_5) implies LH(chi_5) (the classical
mechanism of Titchmarsh, Theorem 14.2, for a Dirichlet L-function; Montgomery-
Vaughan chapter 13), hence (M37) by Theorem 4, hence by ANALYTIC.md section 9,
(A67)-(A71), the analytic target r_Y(sqrt Y) << Y^{1 - 3 sigma/2 + epsilon} of (A54).

Corollary 4.2 (Fejer form; O, not claimed; withdrawn from candidate-T after review).
The statement one would like is: under LH(chi_5), F_T(P) <<_{sigma, epsilon} N^2 T^epsilon
uniformly in finite M, K, i.e. (M18) = (A58), and then the relative errors in (M33)-(M34)
would become T^{-2 sigma + epsilon} log^2 Y. The intended route is the note's proof of
(A62)-(A64) with (A41) replaced by an LH-type bound. The gap: (A62)-(A63) integrate over
all real t ((A63): "this proof controls all real times") and use (A41) for every finite
M and every real t, whereas the proof of Theorem 4 bounds A_M B_M only on [T,2T] at
M = ceil(40T) through (A45), whose (A29) hypothesis x = M/5 > C_0 |Im z|/(2 pi) fails once
|t| is a fixed multiple of T. LH(chi_5) is a statement about L, not about its partial sums
of arbitrary length at arbitrary height; the missing step is a partial-sum bound under
LH, uniform in M and t (a Perron truncation as in (A26)-(A28) with LH on the shifted
line). It is not written here and not in the record, so the (A58) part is O. The
pre-review text claimed it; the claim is withdrawn (Review record).

What Theorem 4 says about strength. RH for zeta(s) is absent from the hypothesis.
Any zero-location consequence of (M37) is therefore also a consequence of the
growth hypothesis LH(chi_5) alone; no implication from LH(chi_5) to a statement about
zeros of zeta(s) is known. So no RH-strength content of (M37) is known, the phrase
"quasi-GRH strength for zeta_F" is not supported, and the note's own wording in
README.md section 7 (no RH-strength transfer, no zero-free statement for L(s, chi_5))
is the consistent one. Unconditionally, the gap between (M32) and (M37) is exactly
the gap between the exponent-pair bound (A38)-(A41) and Lindelof at the two abscissae
u = 1 - sigma (exponent a_sigma = 5603/95780 = 0.0585... at sigma = 51/200) and
u = 2 sigma (exponent b_sigma = 5317/35280 = 0.1507...), or a joint cancellation that
replaces pointwise control, which is what README.md section 6 says in other words.

### 4.3 Theorem 5 (the pole guard made rigorous; candidate-T, conditional; vacuous under (W); A3 restated with explicit constants)

Fix sigma, kappa, epsilon as above, T large, k in R with T^kappa/2 < k <= T^kappa (such
a split prime exists once T^kappa/2 >= 8 . 10^9, i.e. T^kappa >= 1.6 . 10^10, by the
explicit bound (P7) of PRIME-CANCELLATION.md [T-lit] applied at both endpoints
x = T^kappa and x = T^kappa/2 exactly as in the derivation of (P8) there; (P8) itself is
printed in the standing range Y >= 10^12. Threshold corrected after review: the
pre-review text wrote 8 . 10^9), U = Y/k, so T^{2-kappa} <= U < 2 T^{2-kappa}. Let
rho_0 = beta_0 + i gamma_0 be a simple zero of zeta L with gamma_0 in [T+1, 2T-1],
b = beta_0 - sigma. Assume:

    (M37)  at this T and this k, with exponent epsilon';
    (D)    |F^{(k)}_U(sigma + it)| >= (1/2) |Pi_{rho_0}(t)| for all |t - gamma_0| <= 1;
    (W_w)  W_{gamma_0} >= T^{2w} for some 0 <= w <= 1/2;
    (Res)  |R_{rho_0}| >= T^{-epsilon}.

Then

    beta_0 <= 1 - w/(2 - kappa) + (epsilon + epsilon')/(2 - kappa) + log(16 C (1 + b^2)) / (2 (2 - kappa) log T),

where C is the constant in (M37) at this sigma, kappa, epsilon' (kept explicit after
review; the pre-review display absorbed it, an O(1/log T) discrepancy).

Proof. (M37) gives ||A_M B_M F_U||_{2,T}^2 <= C U^{2-2sigma} T^{-1+2epsilon'}. Restricting the
integral to the window and using (D), Proposition 2(c), (W_w) and (Res):
||A_M B_M F_U||_{2,T}^2 >= (1/4) T^{-1} |R_{rho_0}|^2 U^{2b} (1+b^2)^{-1} W_{gamma_0}
>= (1/4)(1+b^2)^{-1} T^{-1 - 2 epsilon + 2w} U^{2b}. Hence U^{2 beta_0 - 2} <= 4 C (1+b^2) T^{2 epsilon + 2 epsilon' - 2w}.
Since 2 beta_0 - 2 < 0 and U < 2 T^{2-kappa}, U^{2 beta_0 - 2} > (2 T^{2-kappa})^{2 beta_0 - 2} >= (1/4) T^{-(2-kappa)(2 - 2 beta_0)}.
Taking logarithms, (2-kappa)(2 - 2 beta_0) >= 2w - 2 epsilon - 2 epsilon' - log(16 C (1+b^2))/log T,
which rearranges to the display. QED. Counting: this is the algebra of section 3.4 (A3)
restated as a conditional theorem with explicit constants and hypotheses; one reading,
not a second result.

Reading. At w = 0, the natural (W), the conclusion is beta_0 <= 1 + o(1): vacuous. At
w = 1/2 the conclusion is beta_0 <= beta*(kappa) + o(1), the task's threshold, but the
hypothesis (W_{1/2}) is empty for large T because W_gamma << T^{2 nu_sigma + epsilon}
with 2 nu_sigma < 1. At the largest admissible w = nu_sigma the conclusion is
beta_0 <= 1 - nu_sigma/(2-kappa) + o(1), about 0.79 at kappa near 1, and it needs (D),
which is the wall of section 4(ii), together with a weight concentration of exponent
2 nu_sigma at the ordinate of a hypothetical zero of zeta_F, which nothing supplies.
No version of this theorem with a nonvacuous conclusion was found under the
available hypotheses (a judgement, not a theorem); the mechanism is recorded as
HEURISTIC beyond Theorem 5, and Theorem 5 is recorded to make the vacuity exact rather
than argued.

## 5. Mean value versus target (task 4)

### 5.1 Proposition 6 (unconditional; no zero hypothesis; R with candidate-T citation)

For every k in R, U >= 1, V >= 2 and fixed sigma in (1/4, 1/2),

    int_V^{2V} |F^{(k)}_U(sigma + it)|^2 dt <<_sigma (V + U) U^{1 - 2 sigma} (1 + log U),

equivalently ||F^{(k)}_U||_{2,V}^2 <<_sigma (1 + U/V) U^{1 - 2 sigma} (1 + log U). This is
(A21) applied with b_r = f(r) 1_{(r,k)=1} r^{-sigma} together with (A11), which is
sum_{r <= U} f(r)^2 r^{-2 sigma} << U^{1-2sigma}(1 + log U) from f(r)^2 = (a_chi * a_chi)(r)
on R (CHECK 15 verifies |f| = a_chi and f^2 = a_chi * a_chi on R for r <= 2000). The
note proves (A21) from the Fejer identity (A17) without importing the
Montgomery-Vaughan mean value theorem; the latter [T-lit] gives the sharper
(V + O(U)) sum |b_r|^2 with an explicit constant and is not needed. No hypothesis on
zeros of zeta or L is used; the "under RH" premise of the task is dropped as
unnecessary.

### 5.2 Exponent bookkeeping (exact Fractions, CHECK 11-12)

With U = T^{2-kappa} and exponents of T for squared norms:

| quantity | exponent | at sigma = 51/200, kappa = 0 (U = Y = T^2) |
|---|---|---|
| normalized mean value, first term (U^{1/2-sigma})^2 | (2-kappa)(1-2sigma) | 49/25 ... dominated |
| normalized mean value, second term U^{1-2sigma} U/T | (2-kappa)(2-2sigma) - 1 | 99/50 |
| (M37) target squared, T_0^2 = U^{2-2sigma}/T | (2-kappa)(2-2sigma) - 1 | 99/50 |
| unnormalized int_T^{2T} |F_U|^2 | (2-kappa)(2-2sigma) | 149/50 |
| unnormalized minus target | 1 | 1 |
| (M32) gap, F_T(P)/N^2 | 2 nu_sigma | 7069361/16895592 = 0.4184... |
| (M32) gap in the tail, Y^{nu_sigma/2} | nu_sigma/2 (in Y) | 7069361/67582368 = 0.1046... |

(At kappa = 0 the first row reads (2)(1 - 51/100) = 49/25 < 99/50.) Conclusions:

- The normalized mean-value bound sits exactly at the (M37) target exponent for
  every kappa in [0, 1]; the unweighted version of (M37) is a theorem up to
  (1 + log U)^{1/2}, unconditionally. The task's premise "misses the target by exactly
  a factor T = Y^{1/2}" is the normalization T^{-1} of ||.||_{2,T} (README.md section 2,
  ANALYTIC.md section 1): the unnormalized integral exceeds the normalized target
  by T, as the table shows, and by nothing else.
- The (M32)-(M33) gap is not that factor. It is 2 nu_sigma in T for the squared Fejer
  moment (0.4184... at sigma = 51/200, exact fraction above; nu_sigma/2 = 0.1046... in
  Y for the tail, the note's Y^{0.1046}), and it comes entirely from the pointwise
  weight bound (A41), since (A62)-(A64) is [pointwise weight] x [mean value]. CHECK 12
  records that 2 nu_sigma is neither 0 nor 1.
- Therefore (M37) is exactly the statement that the weight |A_M B_M|^2 (mean T^epsilon
  by (A32), supremum T^{2 nu_sigma + epsilon} by (A41)) does not correlate with
  |F^{(k)}_U|^2 beyond T^epsilon. Under LH(chi_5) the supremum is T^epsilon and no
  correlation question remains (Theorem 4). This is what "the note needs cancellation
  beyond mean-value technology" means precisely: beyond the mean value, it needs
  either Lindelof-type pointwise control of L(s, chi_5) at u = 1 - sigma and u = 2 sigma,
  or a joint estimate that avoids it.

## 6. Placement (task 5)

- Inputs. A_M and B_M are literal partial sums of L(1 - sigma - it, chi_5) and
  L(2 sigma + 2it, chi_5); F^{(k)} is the split-support series whose analytic structure
  is G_k/zeta_F (Theorem 1). All of it is classical L(s, chi_5) and zeta_F information;
  ZETA-RH-STATUS-2026-09-08.md section 3 already records that the inputs of #856 are
  outside the fence of TRIVIAL-RAPIDITY-EVALUATION-BRIDGE. A Lindelof-type growth
  hypothesis for L(s, chi_5) (Theorem 4) is not a zeta-zero statement, but it is
  classical information not derived from the refined shell, so nothing in this note
  can feed the row; the row's own wording forbids assuming "an equivalent Mertens
  estimate, a zeta-zero statement or the target bound".
- The guard makes the difficulty explicit rather than moving it. The target is
  sandwiched, in a loose strength ordering: (M32), proved with Bourgain's exponent pair
  (loss T^{nu_sigma} in norm; a theorem, hence trivially at the bottom) <= (M37) <=
  LH(chi_5) (loss T^0, Theorem 4). Its residual difficulty is subconvexity
  versus Lindelof for one L-function at two off-line abscissae, or a joint
  cancellation replacing pointwise control. No zero-location content of (M37) is
  known; the single-pole route to such content is closed under the displayed residue
  bound (Theorem 3); the multi-pole route runs into the Gram/detection wall
  (section 3.6, section 4(ii)).
- Bridge row. TRIVIAL-RAPIDITY-EVALUATION-BRIDGE stays O/STOP. Its decision condition
  (REGISTRY-RH-ROWS.tsv, identical to canon/REGISTRY.tsv at canon-v86): "STOP until a
  non-circular transfer mechanism, its complete domain, approximation or kernel,
  uniform norm and reconstruction errors are frozen; closes positively at RH strength
  only by deriving the displayed all-epsilon estimate from the refined shell". Nothing
  here touches the transfer class; (M37) neither derives the M(N) estimate nor closes
  anything negatively. RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md section 7 forbids
  attaching #856 material to the dependency row; respected.
- Counting. The reading of lemma (ii) as a Gram least-eigenvalue problem is a reading
  of the wall of ZETA-RH-STATUS-2026-09-08.md section 4 (capacity/Gram realization
  nonlocal in t; Hankel detection ceiling; the T2 Weyl detection threshold), per
  RH-ONE-WALL-CROSSREF_2026-08-17.md. No new theorem is booked for it.
- Correction of the task's premise, for the record. The expected conclusion
  "(M37) with kappa near 1 forces zeta_F to have no zeros with Re s > beta*(kappa)"
  rests on comparing an unnormalized pole integral with the normalized target; under
  the note's normalization it is not supported, and the theorem that is supported
  points the other way (LH(chi_5) implies (M37)). The 2026-09-08 page's step 2 ("record
  its M37 as the exact target") can carry the annotation: implied by LH(chi_5); no
  known zero-location consequence; the unweighted version is an unconditional theorem.

## 7. Verifier (task 6)

verify_m37_strength.py, Python 3 standard library, int and fractions.Fraction only in
gated code, deterministic, about 0.1 s, exit 0 iff all pass. Stdout saved as
verify_m37_strength.stdout.txt (byte-identical on rerun from a clean shell, empty
stderr; hashes in the Pins section). Checks (labels as revised after review):

```text
01  (1-2x)/(1-x)^2 = 1 - x^2/(1-x)^2 = 1 - sum_{j>=2}(j-1)x^j, formal series over Q to x^12
02  zeta L local factors (split, inert, p=5) and the G_k local table; the infinite factors are 1+O(x^2); inert factor = 1/(1-x^2) = 1 + x^2/(1-x^2) (non-tautological form after review)
03  (1-2x)(1+x^2) = (1-x)^2 - 2x^3, i.e. F^{(1)}/O_5 local factor = 1 - 2x^3/(1-x)^2, as formal series only (label narrowed after review)
04  chi_5 table, 146 split and 156 inert primes <= 2000, smallest split prime 11, 2^2 < 11
05  Euler-product coefficients of prod_{split}(1-2p^{-s}) = f(r) on R, 0 off R, all r <= 2000 (180 nonzero)
06  coprime-to-k version for k in {11, 209, 6061}
07  (f^{(k)} * (1*chi))(n) = g_k(n), n <= 2000, k in {1, 11, 209}: the identity F^{(k)} zeta L = G_k at coefficient level
08  g_1(n) = 0 for every squarefree n > 1 prime to 5, n <= 2000
09  (2-k)(3-2k) = (2-k)(4-2k) - (4-2k)/2 as polynomials in kappa (both 6 - 7k + 2k^2)
10  beta*(kappa) = beta_pole(kappa, 1/2); table 3/4, 26/51, 51/101, 501/1001, 1/2; sigma cancels
11  nu(51/200) = 7069361/33791184; 0 < nu < sigma and 2nu < 1 at the strip endpoints; 1 - 3sigma/2 = 247/400
12  normalized mean value = target exponent for all kappa; the unnormalized exponent (T+U)U^{1-2sigma}, formed independently from Proposition 6, = target + 1; 2nu is neither 0 nor 1
13  single-pole ratio exponent 2w - 2(2-kappa)(1-beta): sign table (sampled) plus the affine identity; beta_pole(kappa, nu) > beta*(kappa); decimal by exact integer division
14  |rho - s|^2 = (beta-sigma)^2 + (gamma-t)^2 (samples); b-range endpoints 6/25, 3/4 exact; window inequality at both endpoints
15  |f(r)| = a_chi(r), f(r)^2 = (a_chi*a_chi)(r) on R, r <= 2000 (input of (A60))
16  residue k-factor: G_{k,p}/G_{1,p} = 1/(1-2x), not (1-x)^2/(1-2x); p = 11, s = 2 gives 121/119; (G_k/G_1)(n) = 2^Omega(n) on n supported on p | k, n <= 2000, k in {11, 209} (added after review)
17  F^{(1)}/O_5 correction factor zero-free on Re s >= 1/2: 1/11 < (6/19)^2 and the rational witness 0.302 (added after review)
DIAGNOSTIC (floats, asserts nothing): decimals of nu, beta*, beta_pole, Lorentzian window mass fractions
```

## Pins

```text
verify_m37_strength.py          sha256 219c5885ccf63f4ed009c9a79024b74dd35268ea80b1f35516dcded72954e593  (22170 bytes)
verify_m37_strength.stdout.txt  sha256 e55369bfcff6f4462c785897ebddb1d96381fdae65efac9e3aaa36ffd8ec4b18  (4526 bytes)
run: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_m37_strength.py
result: CHECKS: 17 of 17 PASS, exit 0, empty stderr, stdout byte-identical to the committed file
pre-review pins (superseded): verifier 02ae33675807bfad3ddb87398e070bf3e67756d9d8d01274a812020106b39264,
                              stdout   f0c7c7510f56452315daae272a347ad1564fd04dd77c246a703ad4be52a2b282
```

## Review record

Two adversarial referee reports (mathematics lens; evidence-and-code lens) were applied
on 2026-09-15. Accepted corrections (each changes the text above; none adds a claim):

1. T1 residue k-factor (both referees, REFUTED as stated). The display
   G_k(rho) = G_1(rho) prod_{p|k}(1-p^{-rho})^2/(1-2p^{-rho}) was false; the local
   quotient (1-x)^{-2}/[(1-2x)(1-x)^{-2}] is 1/(1-2x), so
   G_k = G_1 prod_{p|k}(1-2p^{-s})^{-1}. Corrected in the summary, Theorem 1(d), the
   proof of (d), section 2.3 (two-sided k-factor bounds redone) and the verdict table;
   CHECK 16 added (formal series, p = 11 at s = 2: 121/119 versus the old 14400/14399,
   and the coefficient-level quotient for k = 11, 209 to n <= 2000). T1 stays
   candidate-T with the corrected statement, which is the referees' own "corrected
   statement to adopt"; the rest of Theorem 1 was confirmed by both.
2. T1' zero-freeness of the correction product on Re s >= 1/2 (referee 1, F6) made
   explicit in section 2.4; CHECK 17 added (exact: 1/11 < (6/19)^2; rational witness
   0.302).
3. T3 (both referees, WEAKENED). The sentence "(A41) caps every W_{gamma,j} ... which
   makes it impossible" dropped the uncontrolled factor |R_rho|^2; the label
   "unconditional" overstated. Relabelled "F-route; no zero hypothesis; residue
   hypothesis displayed"; part (b) and the Scope paragraph rewritten with the residue
   hypothesis in every exclusion; the claim-list overreach "for any beta < 1 ... hence no
   zero-free strip" (referee 2) replaced by the two-regime statement (closed below
   1 - nu_sigma/(2-kappa) under the residue bound; unsupported, not ruled out, above it;
   excluded under LH(chi_5) with the residue bound). Summary line 3 and section 6
   adjusted accordingly (and kill K1 of the lane's structured result).
4. T4 (both referees, WEAKENED). Corollary 4.2 ((A58) under LH) needs a pointwise bound
   for the partial sums A_M B_M at all real t and all finite M, which LH(chi_5) does not
   supply without a Perron argument that is not written; demoted to O and the claim
   withdrawn. Theorem 4 is now framed up front as the record's (A62)-(A64)/(A73) method
   with nu_sigma -> epsilon (duplicate-of-record attribution), not a new ceiling.
5. T5 (referee 1, F4; referee 2 cosmetic). Prime-existence threshold corrected from
   T^kappa >= 8 . 10^9 to T^kappa >= 1.6 . 10^10 via (P7) at both endpoints ((P8) as
   printed is for Y >= 10^12); the (M37) constant C kept explicit in the display; the
   judgements "the only rigorous pole guard" and "no nonvacuous version exists"
   reworded as judgements; duplicate-of-record attribution added (A3 restated with
   constants; one reading).
6. A3 wording (referee 1, F5): the verdict table now says that both the unit-window
   mass and sup_{[T,2T]}|A_M B_M|^2 must be T^{2w}; the sup-versus-L2 reading of
   beta*(kappa) (referee 1, F7) added to section 3.4 as an R remark.
7. H4 (referee 2): "the domination step (D) fails in general" replaced by the valid
   inference (with (Res) and separation it cannot be a currently provable theorem,
   else the density hypothesis for zeta_F would follow); the citation "R4 ... pivots at
   10^{-88}" split into R4 (w*_24 wall) and CHECK 0 / ND1 (6.8e-88 pivot floor) of
   RESULT-P-RH-WEYL-CANONICAL-2.md.
8. PL (both referees): the sandwich "(M32) <= (M37) <= LH(chi_5)" marked as a loose
   strength ordering.
9. Verifier (referee 2): CHECK 02 inert test rewritten in non-tautological form
   (1/(1-x^2) and 1 + x^2/(1-x^2)); CHECK 03 label narrowed to what is tested; CHECK 12
   unnormalized exponent now formed independently from Proposition 6 instead of as
   norm + 1; CHECK 13 decimal computed by exact integer division instead of a string
   literal, and the affine identity behind the sign table added; CHECK 14 extended to
   the exact endpoints of the b-range and the window inequality there; runtime in
   section 7 corrected to about 0.1 s; hashes refreshed (Pins).
10. Duplicate-of-record attributions added in the verdict table for T1, T1', T4, T5,
    P6 (both referees' lists); H4 was already booked as a reading.

Referee objections considered and rejected, or accepted only in part:

- Referee 2, P2 WEAKENED "because CHECK 14 certifies almost nothing of it": accepted in
  part. CHECK 14 was extended to certify the finite pieces exactly (b-range endpoints,
  window inequality at the endpoints); the label is kept at candidate-T with the
  annotation "proof-based", because both referees confirm the written proof and the
  remaining content of Proposition 2 (the full-line Lorentzian integral, the (A25) and
  (A41) inputs) has no finite piece that a rational check could certify; the
  discipline's "every finite piece exactly verified" is met after the extension.
- Referee 1's characterization of the unweighted sanity argument in H4 as "a valid
  proof that (D) is not a theorem" and referee 2's "not proved" are both accommodated
  by the new wording ("cannot be a currently provable theorem"); no rejection.
- No other objection was rejected.

Position of this section: placed immediately before the closing "What this does not
do" section, which the session format keeps final.

## What this does not do

- It does not prove, disprove, evidence or approach RH, GRH(zeta_F), GRH(L(., chi_5)),
  LH(chi_5), or any zero-location or zero-density statement. RH stays open;
  RH-PROGRAM-DEPENDENCE is untouched; LAMBDA-COCYCLE-ANGLES [H] is untouched.
- It does not prove (M37), (M18), (M15) or the analytic target: Theorem 4 is
  conditional on LH(chi_5), whose status is open; it does not prove (M18) = (A58) even
  under LH(chi_5) (Corollary 4.2 is O); Corollary 4.1 adds a [T-lit] chain that must be
  audited against the named sources before being called more than candidate-T-lit.
- It does not prove that (M37) has no zero content: Theorem 3 closes one route (the
  single Perron pole term) only under the displayed residue hypothesis, and Theorem 5
  shows the conditional guard is vacuous under the available weight bound; the
  multi-pole reading is HEURISTIC and open.
- It does not supply lemma (i), (ii) or (iii) of section 4, does not improve
  nu_sigma, and does not touch the exponent-pair inputs of the note.
- It does not move TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O], does not propose a registry
  row, does not edit the Canon, and is not a probe, preregistration or run.
- It does not claim the closed-line floor sigma_c(F^{(k)}) >= 1/2 or any statement of
  the split-orientation note beyond the divisor dictionary quoted in section 2.4.
- It does not identify the residue R_rho at a hypothetical zero, does not bound
  1/(zeta L)' there, and makes no assertion about the ordinates of zeros of L(s, chi_5)
  relative to those of zeta(s).
- The finite checks verify finite algebra and finite coefficient identities only; the
  theorems are the written proofs, and no finite run certifies an all-T estimate.

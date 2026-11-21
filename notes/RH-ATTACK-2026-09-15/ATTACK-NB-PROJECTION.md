# ATTACK-NB-PROJECTION: exact projection census for the binary-routing route and the mean-channel debt of the Mobius note

```text
STATUS      NON-CANONICAL incubation material. No status motion, no registry
            row, no probe, no Canon change. Nothing here is a proof of RH,
            evidence for RH, or a falsification of RH.
DATE        2026-09-15
BASIS       Public Canon v86 (STATUS.md ACTIVE, tag canon-v86,
            content commit 56068ba4423a2ca38ce5760f1e34e82e2597f99f)
RH          unchanged: open program-level obligation
            (ZETA-RH-STATUS-2026-09-08.md, RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md)
LANE        A (attack session 2026-09-15)
BUILDS ON   NOTE-SOURCE-CZ.md (sec. 1, 3, 6, 7), REVIEW-CZ.md (sec. 0-4,
            Lemma 3.2, 3.5, Theorem 3.6, sec. 7),
            C-RH-MOBIUS-MEAN-CHANNEL-N.md (sec. 0-2, 4, 6, 8, 13, 14),
            RH-ONE-WALL-CROSSREF_2026-08-17.md (counting rule)
VERIFIER    verify_nb_projection.py (Python 3 standard library, int and
            fractions.Fraction only; every PASS/FAIL predicate is exact;
            float renderings occur only in lines and blocks carrying the
            word DIAGNOSTIC and assert nothing); stdout in
            verify_nb_projection.stdout.txt; K_max = 72; 20 of 20 checks
            PASS; about 143 s wall on one x86_64 lane; run from a clean shell
            with LC_ALL=C PYTHONHASHSEED=0 (SHA-256 pins in sec. 12).
COUNTING    By the rule of RH-ONE-WALL-CROSSREF_2026-08-17.md this note is a
            further reading of the one wall at the Nyman-Beurling level
            (REVIEW-CZ sec. 5), not a new theorem about RH.
REVISION    Repaired 2026-09-15 after two adversarial referee reports
            (mathematics lens; evidence-and-code lens). Every accepted
            correction and every rejected objection is listed in sec. 11
            (Review record). No claim was added.
```

## 0. Summary

1. The exact binary inner product of integer-periodic sequences was
   re-implemented from the record's closed form (NOTE-SOURCE-CZ sec. 6 boxed
   formula, cycle parameters `h = v_2(L)`, `t = ord_{L/2^h}(2)` of REVIEW-CZ
   sec. 2; Lemma B below is that theorem re-derived, a duplicate of record,
   not a lane result) and checked against two independent brute-force
   enclosures on 240 random periodic sequences, then calibrated
   byte-for-byte against the record: `||1||_B^2 = 2`,
   `||a_j||_B^2 = 3/(2*4^j)`, the Gram entries of NOTE-SOURCE-CZ sec. 7,
   `c_2 = 160/251`, `c_3 = 105/251`, `d_3^2 = 52/251`, `d_4^2 = 95/766`, and
   the review's exact `d_K(1)^2` for `K <= 12` (checks C01-C05, C08, C09).
2. The Gram matrix `G_K = [<r_k, r_l>_B]` and the squared distances
   `d_K(x)^2 = ||x||_B^2 - b^T G_K^{-1} b` were computed exactly for every
   `2 <= K <= 72` and for the four targets `x = 1, A_2, A_4, A_8`, by one
   exact `LDL^T` factorisation of the `71 x 71` Gram matrix (candidate-C;
   sec. 8). The review's observation `d_K(1)^2 log K ~ 0.10` (REVIEW-CZ
   sec. 2, `K <= 40`) extends to `K = 72` (`0.0969 ... 0.1004` for
   `32 <= K <= 72`, minimum at `K = 42`, DIAGNOSTIC); the three layer
   targets are new finite scope.
3. The Mobius note's approximants `p_h`, the averages `avg_J`, the channels
   `Y_{Q,J}` and `D_{Q,J}` were computed exactly for all cuts `K_h <= 72`
   (`Q = 2`: `h <= 3`; `Q = 4`: `h <= 2`; `Q = 8`: `h <= 1`); the note's
   identity (1) holds exactly on all nine `(Q, J)` pairs with the three norms
   taken from three independent Gram tables (C17), and by direct evaluation
   over the full period for three of them (C18). Identities (12), (13), (14)
   hold exactly; the bound (3) holds for all `K <= 4096` (C13-C16).
4. The Delta convention of the Mobius note (R, a reading): the note contains
   no explicit definition line for `Delta`, but its identities (4) (source
   pairs `a = mQu`, `b = min(m(Qu+1), K)`) and (23)
   (`A_Q(s) = sum_{u odd} [(Qu)^{-s} - (Qu+1)^{-s}]`) encode the backward
   difference `Delta x(n) = x(n) - x(n-1)`, `x(0) = 0`, as in REVIEW-CZ.
   Lemma C (candidate-T) under that convention gives `t_Q(1) = 0` and
   `p_h = A_Q` below the cut, hence identity (1). Exact computations at
   finite scope (candidate-C, C12) record what the forward difference would
   do instead: `t_2(1) = 1`, `S_{2,J}(1) = -J`, (1) fails for `Q = 2` by
   exactly `1` (computed over the period 840), `p_h(n) = A_Q(n+1)` below the
   cut for every `Q`, and (3) fails for `Q = 2` at `K = 2, 3` (sec. 3).
5. Lemma D (candidate-T, elementary): `avg_J` lies in
   `span{r_k : 2 <= k <= K_{J-1}}`, hence
   `||A_Q - avg_J||_B^2 >= d_{K_{J-1}}(A_Q)^2` and
   `||Y_{Q,J}||_B^2 >= 2 J^2 d_{K_{J-1}}(A_Q)^2 - ||D_{Q,J}||_B^2 / 4`.
   The chain holds exactly on all computed values (C19), and every
   efficiency ratio is `>= 1` (C20, a corollary of C19). Proposition E
   (candidate-T, conditional algebra on (1) and Lemma D): a `CJ` bound with
   bounded difference channel forces `d_K(A_Q)^2 = O(1/log K)` along the
   dyadic grid, and a lower bound `d_K(A_Q)^2 >= c/log K` on the grid forces
   `||Y_{Q,J}||_B^2 >= (2c/log 2) J - O(1)`. Reading (R, sec. 9.3): the
   note's "closure-strength `CJ` mean-channel bound" is therefore a rate
   statement for the twisted Nyman-Beurling distance, not a bare membership
   statement, and an `o(J)` bound would force `d_K(A_Q)^2 = o(1/log K)`.
   HEURISTIC (sec. 9.3): the comparison with the
   Baez-Duarte-Balazard-Landreau-Saias conjecture is an analogy across a
   different norm, target and setting; the transfer of Burnol's continuous
   lower bound to this setting is NOT claimed.
6. Logical status of the mean-channel debt (sec. 9.4, references only):
   mean-channel closure for one `Q = 2^j` implies `a_j in V`; `a_j in V` for
   infinitely many `j` implies RH (REVIEW-CZ Theorem 3.6); for one `j` it
   yields the Hurwitz shadow condition. The debt is the twisted
   Nyman-Beurling problem of REVIEW-CZ sec. 4 (with a rate, by item 5); the
   converse direction for the note's specific family is open (O). It is not
   a numerical seam.
7. Two diagnostic findings about the Mobius family itself (sec. 9.2, R):
   the sharp single-cut errors `||A_2 - p_h||_B^2` do not decrease over the
   computed cuts (`0.0678, 0.0686, 0.0865, 0.0806`) while `d_{K_h}(A_2)^2`
   halves, so the efficiency ratio of the sharp cut grows (`1.49, 1.93,
   3.10, 3.59`); the Cesaro average repairs this (`1.49, 1.32, 1.23, 1.21`).
   The averaging in the note is therefore essential, not cosmetic. Also
   `d_K(A_2)^2` is nearly as large as `d_K(1)^2` (`0.0221` versus `0.0235`
   at `K = 72`) although `||A_2||_B^2 = 3/8` against `||1||_B^2 = 2`.

## 1. Falsifiers first

| Claim | What kills it |
|---|---|
| L-A (split identity) and identity (1) | one sequence `x` with `||x||_B^2 != x(1)^2 + ||Lx||_B^2/2 + ||Hx||_B^2/8`, or one `(Q, J)` with `S_{Q,J}(1) != 0` under the backward convention; the verifier would print FAIL at C06 or C17 |
| L-B (exact periodic closed form) | one periodic sequence whose closed-form value falls outside either brute-force enclosure (C01, C02), or a value that changes under period doubling (C03) |
| L-C (approximant equals target below the cut; `t_Q(1) = 0`) | one `n < K_h` with `p_h(n) != A_Q(n)`, or `t_Q(1) != 0` for some `Q >= 2` under the backward convention (C12) |
| Convention reading (V4b) | a reading of the Mobius note's (4) (source pairs `mQu`, `min(m(Qu+1), K)`) or (23) (`sum_{u odd}[(Qu)^{-s} - (Qu+1)^{-s}]`) compatible with the forward difference; there is none, since the Dirichlet series of `Delta^+ A_Q` is `sum_{u odd}[(Qu-1)^{-s} - (Qu)^{-s}]` |
| Forward-convention record (V4c) | a FAIL at C12: a `Q` with `p^fwd_h(n) != A_Q(n+1)` below the cut, or a computed gap in (1) for `Q = 2` different from `1` |
| Duplicate-of-record filing (V1) | a step in Lemma B absent from NOTE-SOURCE-CZ sec. 6 plus REVIEW-CZ sec. 2; none is claimed |
| Identities (12), (13), (14) | one exact pointwise failure in the tested range (C13, C15, C16); the proofs in sec. 5-6 would then contain an error |
| Bound (3) at finite scope | one `K <= 4096` with `abs(gamma_{Q,K}) >= 5/(4 Q^2)` (C14); nothing is claimed beyond `K <= 4096` |
| Census `d_K(x)^2`, `K <= 72` | a second-architecture run printing a different fraction or fingerprint at any `K`, or a pivot `<= 0` (C07-C11); a disagreement with the review's `K <= 12` values (C08) |
| L-D (span lemma, inequality chain) | one computed `(Q, J)` with `||A_Q - avg_J||_B^2 < d_{K_{J-1}}(A_Q)^2`, or `||Y||^2 < 2 J^2 d^2 - ||D||^2/4` (C19); a coefficient of `p_h` on `r_k` with `k > K_h` or `k = 1` (C19) |
| Efficiency ratios `>= 1` | any ratio `< 1` (C20); that would mean the Gram census and the approximant norms disagree |
| Proposition E (rate reading), exact part | an algebraic error in sec. 7; it is two lines of algebra on (1) and L-D |
| Proposition E, HEURISTIC part | a proof that `d_K(A_Q)^2 = o(1/log K)` is possible for some `Q` (then an `o(J)` mean-channel bound would not be excluded), or a proof that Burnol's lower bound does not transfer to the target `A_Q` in the `B`-norm |
| Reading 9.4 (the debt is `a_j in V`, not numerical) | a finite computation deciding `a_j in V`; excluded by REVIEW-CZ sec. 4 and the owner verdict cited there ("no finite prefix is progress"), so only an error in that record could revive it |

## 2. Verdict table

| id | statement | status | verifier checks |
|---|---|---|---|
| V1 | exact binary inner product of integer-periodic sequences, closed form with pre-period `v_2(L)` and cycle `ord_{L/2^{v_2(L)}}(2)` (Lemma B). This is the record's theorem: NOTE-SOURCE-CZ sec. 6 boxed formula, cycle parameters in REVIEW-CZ sec. 2, enclosure test already in the review verifier (group F). Re-derived and re-implemented here | duplicate of record (record theorem re-verified; lane contribution R, finite enclosure checks candidate-C); no lane candidate-T | C01, C02, C03 |
| V2 | calibration against the record: `||1||_B^2 = 2`, `||a_j||_B^2 = 3/(2*4^j)`, `G_22, G_23, G_33, b_2, b_3`, `c_2 = 160/251`, `c_3 = 105/251`, `d_K(1)^2` for `K <= 12` (deliberate duplication of NOTE-SOURCE-CZ sec. 7 and verify_rh_binary_review.stdout.txt) | candidate-C | C04, C05, C08, C09 |
| V3 | split identity `||x||_B^2 = x(1)^2 + ||Lx||_B^2/2 + ||Hx||_B^2/8` (Lemma A) and identity (1) of the Mobius note (the note's own boxed identity; the proof is supplied here, sec. 4) | candidate-T | C06, C17, C18 |
| V4a | Lemma C: under the backward convention `t_Q(1) = 0`, `p_h(1) = 0`, `p_h = A_Q` on `1 <= n < K_h` | candidate-T | C12 (C15, C16 as consistency under the same convention) |
| V4b | the Mobius note's `Delta` is the backward difference with `x(0) = 0`: not defined explicitly there, but encoded in its identities (4) and (23) (sec. 3) | R (reading of the note) | none (textual) |
| V4c | forward-convention record: `t_2(1) = 1`, `S^fwd_{2,1}(1) = -1`, identity (1) fails for `Q = 2` by exactly `1`, `p_h(n) = A_Q(n+1)` below the cut for `Q in {2, 4, 8}`, `abs(gamma^fwd_{2,K}) >= 5/16` at `K = 2, 3` | candidate-C (exact, finite scope) | C12 |
| V5 | identities (12), (13), (14) of the Mobius note (stated there without proofs; proofs supplied here, sec. 5-6) | candidate-T | C13, C15, C16 |
| V6 | bound (3) `abs(gamma_{Q,K}) < 5/(4Q^2)` for `Q in {2,4,8}`, `2 <= K <= 4096`; maxima `1/6, 1/20, 1/72` attained at `K in {3,4}, {5..8}, {9..16}` | candidate-C (finite scope only) | C14 |
| V7 | Gram matrix `G_72` positive definite; exact `d_K(x)^2` for `2 <= K <= 72` and `x in {1, A_2, A_4, A_8}`; positivity and monotonicity (`d_K(1)^2` for `K <= 40` is in REVIEW-CZ sec. 2; `K <= 72` and the three layer targets are new finite scope) | candidate-C | C07, C09, C10, C11 |
| V8 | Lemma D: `avg_J in span{r_k : 2 <= k <= K_{J-1}}`, `||A_Q - avg_J||^2 >= d_{K_{J-1}}(A_Q)^2`, `||Y||^2 >= 2J^2 d^2 - ||D||^2/4` | candidate-T | C19 |
| V9 | efficiency ratios `||A_Q - p_h||^2 / d_{K_h}(A_Q)^2` and `||A_Q - avg_J||^2 / d_{K_{J-1}}(A_Q)^2` are `>= 1` on all computed cuts (a corollary of Lemma D); exact values printed as fractions in the stdout, decimals in sec. 8 DIAGNOSTIC | candidate-C | C20 (corollary of C19, not independent) |
| V10 | Proposition E, exact part: a `CJ` mean-channel bound with bounded difference channel gives `d_K(A_Q)^2 <= C/(2J) + C_D/(8J^2)` at `K = 2^{J+j+1}`; a lower bound `d_K(A_Q)^2 >= c/log K` gives `||Y||^2 >= (2c/log 2) J - O(1)` | candidate-T (conditional algebra on (1) and Lemma D; its all-`J` hypotheses have no finite instance, so no check tests E1/E2) | none (C19 tests Lemma D(3) instances only) |
| V10r | reading of Proposition E: the note's `CJ` target implies an `O(1/log K)` rate for `d_K(A_Q)^2` on the dyadic grid and is at least as strong as that rate (the converse, rate to `CJ`, is the open item of sec. 9.4 item 2); an `o(J)` bound would force `o(1/log K)`. The comparison with the BBLS conjecture is an analogy across norm, target and setting | R; the BBLS comparison HEURISTIC | none |
| V11 | Proposition E, HEURISTIC part: `O(J)` is the exact order of the mean channel | HEURISTIC, O | none |
| V12 | logical status of the mean-channel debt (sec. 9.4); duplicate of REVIEW-CZ sec. 4, Lemma 3.5 item 6, Theorem 3.6 | R (references only) | none |
| V13 | sharp cuts do not converge in the computed range; averaging is essential; `d_K(A_2)^2 ~ d_K(1)^2` | R (diagnostic; exact fractions in the stdout, decimals DIAGNOSTIC) | C17, C19 (values) |

No claim above is a status motion for any registry row. No `F` is recorded:
no proof route was killed here that the record had not already scoped.

## 3. Setting, and the Delta convention of the Mobius note

Notation follows NOTE-SOURCE-CZ sec. 1, 3 and the Mobius note sec. 1:
`r_k(n) = n mod k` for `n >= 1`, `k >= 2`; `A_Q(n) = 1` iff
`n = Q (mod 2Q)`, `Q = 2^j`, so that `A_Q = a_j` is the `j`-th layer
(`a_j = 1_{v_2(n) = j}`, NOTE-SOURCE-CZ sec. 3); `w_B(n) = 4^{-(bitlen(n)-1)}`;
`||x||_B^2 = sum w_B(n) x(n)^2`; `V` the closure of `E = span{r_k : k >= 2}`;
`V_K = span{r_2, ..., r_K}`; `d_K(x)^2 = dist_B(x, V_K)^2 = ||x||_B^2 -
b^T G_K^{-1} b` with `G_K = [<r_k, r_l>_B]_{2 <= k,l <= K}`,
`b_k = <x, r_k>_B`; `t_Q = mu * Delta A_Q`; `T_{Q,N} = sum_{k <= N} t_Q(k)/k`;
`s_Q(u) = sum_{k <= u} t_Q(k)`; `K_h = 4 Q 2^h`;
`p_h = -sum_{k < K_h} (t_Q(k)/k) r_k + T_{Q,K_h - 1} r_{K_h}`;
`e_h = A_Q - p_h`; `S_{Q,J} = sum_{h < J} e_h`; `avg_J = (1/J) sum_{h<J} p_h`,
so that `A_Q - avg_J = S_{Q,J}/J`; `(Hx)(n) = x(2n+1) - x(2n)`,
`(Lx)(n) = (x(2n) + x(2n+1))/2` for `n >= 1`; `D_{Q,J} = H S_{Q,J}`,
`Y_{Q,J} = L S_{Q,J}`; `gamma_{Q,K} = T_{Q,K-1} - (1/K) sum_{k<K} t_Q(k)`.

**Convention (R, a reading of the note).** `Delta x(n) = x(n) - x(n-1)`
with `x(0) = 0` (backward difference, as in REVIEW-CZ). The Mobius note has
no explicit definition line for `Delta`, but two of its displayed identities
fix the convention: (4), whose source pairs are `a = mQu`,
`b = min(m(Qu+1), K)`, and (23), whose paired source Dirichlet function is
`A_Q(s) = sum_{u odd} [(Qu)^{-s} - (Qu+1)^{-s}]`. Under the backward
difference `Delta A_Q(n) = 1_{n = Q (mod 2Q)} - 1_{n-1 = Q (mod 2Q)}` has
support `{Qu : u odd}` with sign `+` and `{Qu+1 : u odd}` with sign `-`,
which is exactly (4) after Mobius convolution and exactly (23) as a
Dirichlet series; the forward difference `Delta^+ x(n) = x(n+1) - x(n)`
would give `sum_{u odd} [(Qu-1)^{-s} - (Qu)^{-s}]` instead. The convention
is therefore the note's own, not a determination made here; this section
records its consequences (Lemma C, candidate-T) and, as exact computations
at finite scope (candidate-C, check C12), what the forward difference would
do instead:

1. Backward: `t_Q(1) = A_Q(1) - A_Q(0) = 0` for every `Q >= 2` (since
   `1 != Q (mod 2Q)`), hence `p_h(1) = 0 = A_Q(1)`, hence `S_{Q,J}(1) = 0`,
   which by Lemma A is exactly the condition for identity (1) (sec. 4).
   Forward: `t_2(1) = A_2(2) - A_2(1) = 1`, and `p_h(1) = t(1)` for any `t`
   (because `r_k(1) = 1` for `k >= 2`), so `S_{2,J}(1) = -J` and by Lemma A
   (1) fails for `Q = 2` by exactly `S(1)^2/J^2 = 1`. C12 computes this gap
   directly for `Q = 2`, `J = 1` over the period 840 (`S^fwd(1) = -1`, gap
   `= 1`), independently of Lemma A.
2. Backward: `p_h(n) = A_Q(n)` for all `1 <= n < K_h` (Lemma C). Forward,
   every `Q`: `p^fwd_h(n) = sum_{m <= n} Delta^+ A_Q(m) = A_Q(n+1) - A_Q(1)
   = A_Q(n+1)` for `1 <= n < K_h`, a shifted target (C12 for `Q = 2, 4, 8`
   at `h = 0`; the `Q = 2` case `p^fwd_h(1) = 1` is the `n = 1` instance).
3. Backward: identity (13) holds pointwise on all cuts `K_h <= 72`,
   `n <= 2000` (C15), and (14) on `n <= 400` (C16). These are consistency
   checks under the backward convention; they were not run under the
   forward one and do not by themselves discriminate.
4. Identity (12) is a pure summation by parts and holds under any
   convention; it does not discriminate (C13).
5. Bound (3): under the backward convention it holds for all `K <= 4096`
   with maxima `1/6, 1/20, 1/72` for `Q = 2, 4, 8` against `5/16, 5/64,
   5/256`, attained at `K in {3, 4}`, `{5..8}`, `{9..16}` (C14). Under the
   forward convention it fails for `Q = 2` at `K = 2, 3` (`gamma^+ = 1/2,
   1/3 >= 5/16`) and holds again from `K = 4` on in the tested range.

Item 1 shows that the note's identity (1), stated there as exact, is
consistent with the backward convention and not with the forward one; items
2 and 3 show the same for the note's construction (approximant equal to the
target below the cut, cell identities beyond it). None of this is a theorem
about the note; it is a reading confirmed by exact finite computation.

## 4. Lemma A (split identity) and identity (1)

**Lemma A (candidate-T).** For every real sequence `x` on `n >= 1` with
`||x||_B < infinity`,

```text
||x||_B^2 = x(1)^2 + ||Lx||_B^2 / 2 + ||Hx||_B^2 / 8,
```

and, polarised, `<x, y>_B = x(1) y(1) + <Lx, Ly>_B / 2 + <Hx, Hy>_B / 8`.

*Proof.* The index set `{n >= 1}` is the disjoint union of `{1}` and the
pairs `{2m, 2m+1}`, `m >= 1`. For `m >= 1`, `bitlen(2m) = bitlen(2m+1) =
bitlen(m) + 1`, so `w_B(2m) = w_B(2m+1) = w_B(m)/4`. For real `a, b` put
`l = (a+b)/2`, `h = b - a`; then `a^2 + b^2 = 2 l^2 + h^2/2` (expand
`2 l^2 + h^2/2 = (a+b)^2/2 + (b-a)^2/2 = a^2 + b^2`). With `a = x(2m)`,
`b = x(2m+1)` this gives `w_B(2m) x(2m)^2 + w_B(2m+1) x(2m+1)^2 =
(w_B(m)/4)(2 (Lx)(m)^2 + (Hx)(m)^2/2) = w_B(m) (Lx)(m)^2 / 2 +
w_B(m) (Hx)(m)^2 / 8`. Summing over `m >= 1` and adding `w_B(1) x(1)^2 =
x(1)^2` proves the identity; all terms are nonnegative, so the
rearrangement is legitimate, and polarisation is immediate. QED

**Identity (1) of the Mobius note (candidate-T).** Under the backward
convention, for every `Q = 2^j`, `j >= 1`, and `J >= 1`,

```text
||A_Q - avg_J||_B^2 = ||Y_{Q,J}||_B^2 / (2 J^2) + ||D_{Q,J}||_B^2 / (8 J^2).
```

*Proof.* `A_Q - avg_J = S_{Q,J}/J`, `L(S/J) = Y/J`, `H(S/J) = D/J`. By
Lemma A, `||S/J||_B^2 = S(1)^2/J^2 + ||Y||^2/(2J^2) + ||D||^2/(8J^2)`.
By Lemma C below, `p_h(1) = A_Q(1) = 0` for every `h`, so `S(1) = 0`. QED

Verifier: C06 checks the polarised identity on all three Gram tables
(`G[k][l] = 1 + GL[k][l]/8 + GH[k][l]/8` for all `2 <= k <= l <= 72`, where
`GL` and `GH` are the Gram tables of `2 L r_k` and `H r_k`), on the target
vectors, and on 60 random finitely supported rational sequences with the
weights computed directly; C17 checks (1) exactly on all nine `(Q, J)` pairs
with `K_{J-1} <= 72`; C18 recomputes `||S||^2`, `||D||^2`, `||Y||^2` and
`S(1)` by direct evaluation over the full periods 840 and 720720 for
`(Q, J) = (2,1), (4,1), (2,2)`.

## 5. Lemma B (exact periodic binary sum) and identity (12)

**Lemma B (record theorem, duplicate of record: the boxed closed form of
NOTE-SOURCE-CZ sec. 6 with the cycle parameters `h = v_2(L)`,
`t = ord_{L/2^h}(2)` of REVIEW-CZ sec. 2, whose review verifier already
encloses it in group F; re-derived and re-implemented here, no lane
candidate-T).** Let `q` be `L`-periodic with rational values
`q[0..L-1]` (`q_n = q[n mod L]`). Let `P(r) = sum_{a<r} q[a]`, `S = P(L)`,
`eta(r) = P(r) - r S/L`, `b_j = 2^j mod L`, `d_j = eta(b_{j+1}) - eta(b_j)`,
`h = v_2(L)`, `t = ord_{L/2^h}(2)` (with `ord_1(2) = 1`). Then

```text
sum_{j>=0} 4^{-j} sum_{n=2^j}^{2^{j+1}-1} q_n
  = 2S/L + sum_{j<h} 4^{-j} d_j + 4^{-h} (1 - 4^{-t})^{-1} sum_{a<t} 4^{-a} d_{h+a}.
```

*Proof.* For `M >= 0`, `sum_{n<M} q_n = floor(M/L) S + P(M mod L) =
M S/L + eta(M mod L)`, because `M - (M mod L) = L floor(M/L)`. Hence the
block sum over `2^j <= n < 2^{j+1}` equals `2^j S/L + eta(b_{j+1}) -
eta(b_j)`. The series `sum 4^{-j} 2^j S/L = 2S/L`. The residues
`b_j = 2^j mod L` satisfy `b_{j+1} = 2 b_j mod L`; by the Chinese remainder
theorem modulo `2^h` and `L' = L/2^h`, `2^j = 0 (mod 2^h)` for `j >= h`
while `2^j mod L'` is purely periodic with period `ord_{L'}(2)`; so
`b_{j+t} = b_j` for all `j >= h`, and `d_{j+t} = d_j` for `j >= h`. The
tail `sum_{j>=h} 4^{-j} d_j = sum_{c>=0} sum_{a<t} 4^{-(h+ct+a)} d_{h+a} =
4^{-h} (1-4^{-t})^{-1} sum_{a<t} 4^{-a} d_{h+a}`, absolutely convergent
since `|d_j| <= 2 max_r |eta(r)|`. QED

The proof adds nothing to the record; it is written out so that the
implementation below can be audited against it. Weakest step (for the
audit): `d_{j+t} = d_j` for `j >= h` needs `b_{j+1+t} = b_{j+1}` as well,
which holds because `j + 1 >= h`; the degenerate cases `L = 1` (`h = 0`,
`t = 1`, all `d_j = 0`, value `2S`) and `L = 2^h` (`t = 1`, tail zero) are
covered by `ord_1(2) = 1`.

Implementation: `bsum` in the verifier keeps `L*eta(r) = L P(r) - r S`
integral, asserts `b_{h+t} = b_h`, and divides once at the end. C01-C03
certify only that the closed form lies inside two independent enclosures
and is invariant under period multiples; exact equality rests on the
record's proof, on the calibrations C04, C05, C08 and on the direct
full-period cross-checks C10, C18. For the
inner products `<r_k, r_l>_B` the period is `lcm(k, l)`; the three tables
`G`, `GL`, `GH` are built in one pass per pair. C01 encloses the value by
the brute-force partial sum over `J_0 >= 12` blocks plus the crude tail box
`[2^{1-J_0} min q, 2^{1-J_0} max q]`; C02 by a tighter, still independent
window box (each block is `floor(2^j/L)` full periods plus a window of fewer
than `L` consecutive terms, whose sums are bounded by the extremal window
sums); C03 checks invariance under period doubling and tripling and
linearity. 240 random cases each, periods `1 <= L <= 128`, integer and
rational values.

**Identity (12) (candidate-T).** `gamma_{Q,K} = sum_{u=1}^{K-1}
s_Q(u) / (u(u+1))`.

*Proof.* `T_{Q,K-1} = sum_{k<K} (s(k) - s(k-1))/k = sum_{u<K} s(u) (1/u -
1/(u+1)) + s(K-1)/K` (Abel summation with `s(0) = 0`), and `1/u - 1/(u+1)
= 1/(u(u+1))`; subtract `s(K-1)/K`. QED. This holds for any sequence `t`
and any convention (C13).

## 6. Lemma C (below the cut) and identities (13), (14)

**Lemma C (candidate-T).** Backward convention, `Q >= 2`. Then
`t_Q(1) = 0`; `p_h(0) = 0`; and `p_h(n) = A_Q(n)` for `0 <= n < K_h`. In
particular `p_h(1) = 0` and `e_h` is supported on `n >= K_h`.

*Proof.* `t_Q(1) = mu(1) Delta A_Q(1) = A_Q(1) - A_Q(0) = 0 - 0`. All
`r_k(0) = 0`, so `p_h(0) = 0 = A_Q(0)`. For `n >= 1`, `Delta r_k(n) = 1 - k
1_{k | n}` (REVIEW-CZ Lemma 3.2 proof; note `r_1 = 0` and `1 - 1 = 0`
agree). Hence with `K = K_h`

```text
Delta p_h(n) = -sum_{k<K} (t(k)/k)(1 - k 1_{k|n}) + T_{K-1}(1 - K 1_{K|n})
             = sum_{k<K, k|n} t(k) - K T_{K-1} 1_{K|n}.
```

For `1 <= n < K` the second term vanishes and the first is
`sum_{k|n} t(k) = (1 * mu * Delta A_Q)(n) = Delta A_Q(n)` (Mobius inversion).
So `Delta p_h = Delta A_Q` on `1 <= n < K` and both vanish at `0`; summing
gives `p_h = A_Q` on `0 <= n < K`. QED (C12 checks this pointwise for all
cuts `K_h <= 72`.)

**Identity (13) (candidate-T).** With `e_K := A_Q - p` for the cut `K`,
`e_K(n) = sum_{l=1}^{floor(n/K)} s_Q(floor(n/l)) + K floor(n/K) gamma_{Q,K}`.

*Proof.* Summing the displayed `Delta` formula from `1` to `n` and using
`Delta A_Q(m) = sum_{k|m} t(k)`,
`e_K(n) = sum_{m<=n} sum_{k|m, k>=K} t(k) + K T_{K-1} floor(n/K) =
sum_{k>=K} t(k) floor(n/k) + K T_{K-1} floor(n/K)`. Write
`floor(n/k) = #{l >= 1 : kl <= n}` and exchange: `sum_{k>=K} t(k) floor(n/k)
= sum_{l <= n/K} sum_{K <= k <= n/l} t(k) = sum_{l <= n/K} (s(floor(n/l)) -
s(K-1))`. The subtracted term is `floor(n/K) s(K-1)`, and `K T_{K-1}
floor(n/K) - floor(n/K) s(K-1) = K floor(n/K) gamma_{Q,K}` by the
definition of `gamma`. QED (C15: all cuts `K_h <= 72`, `n <= 2000`.)

**Identity (14) (candidate-T).** `e_K(n) = sum_{u=K}^{n} T_Q(u)
[r_{u+1}(n) - r_u(n)]`.

*Proof.* Start from `e_K(n) = sum_{k=K}^{n} t(k) floor(n/k) + K T_{K-1}
floor(n/K)` (terms `k > n` have `floor(n/k) = 0`). With `t(k) = k (T(k) -
T(k-1))`, Abel summation gives `sum_{k=K}^{n} k floor(n/k) (T(k) - T(k-1))
= sum_{u=K}^{n} T(u) [u floor(n/u) - (u+1) floor(n/(u+1))] +
(n+1) floor(n/(n+1)) T(n) - K floor(n/K) T(K-1)`. The middle term is `0`,
the last cancels `K T_{K-1} floor(n/K)`, and `u floor(n/u) = n - r_u(n)`,
so `u floor(n/u) - (u+1) floor(n/(u+1)) = r_{u+1}(n) - r_u(n)`. QED
(C16: all cuts `K_h <= 72`, `n <= 400`.)

Bound (3), `abs(gamma_{Q,K}) < 5/(4Q^2)`, is only verified at finite scope
(`K <= 4096`, C14). Its proof for all `K` is the Mobius note's own
candidate-T and is not re-proved here; the computed maxima `1/6`, `1/20`,
`1/72` sit at `53 %`, `64 %`, `71 %` of the bound and are attained at
`K in {3, 4}`, `{5, ..., 8}`, `{9, ..., 16}`, i.e. before the second source
pair enters. The finite check therefore says nothing about the growth
regime of `gamma` and nothing is claimed beyond `K <= 4096`.

## 7. Lemma D (span lemma) and Proposition E (rate reading)

**Lemma D (candidate-T).** Fix `Q = 2^j`, `j >= 1`, backward convention.
For every `J >= 1`:

1. `avg_J = (1/J) sum_{h<J} p_h` lies in `V_{K_{J-1}} = span{r_k : 2 <= k
   <= K_{J-1}}`.
2. `||A_Q - avg_J||_B^2 >= d_{K_{J-1}}(A_Q)^2`.
3. `||Y_{Q,J}||_B^2 >= 2 J^2 d_{K_{J-1}}(A_Q)^2 - ||D_{Q,J}||_B^2 / 4`.
4. Likewise `||A_Q - p_h||_B^2 >= d_{K_h}(A_Q)^2` for every `h`.

*Proof.* (1) `p_h = -sum_{k<K_h} (t_Q(k)/k) r_k + T_{Q,K_h-1} r_{K_h}`. The
index `k = 1` occurs in the first sum with coefficient `-t_Q(1) = 0` by
Lemma C, and in any case `r_1 = 0`; so `p_h in span{r_k : 2 <= k <= K_h}`.
Since `K_h = 4Q 2^h <= K_{J-1}` for `h < J`, every `p_h` with `h < J` lies
in `V_{K_{J-1}}`, and so does the average. (2) `d_K(x)` is by definition the
infimum of `||x - v||_B` over `v in V_K`; `avg_J` is one such `v`. (3)
Insert (2) into identity (1): `||Y||^2/(2J^2) + ||D||^2/(8J^2) >= d^2`, and
multiply by `2J^2`. (4) `p_h in V_{K_h}`. QED

C19 checks `t_Q(1) = 0` (the only substantive part of the support
statement; the key range `2..K_h` of the coefficient dictionary holds by
construction) and the inequalities (2), (3) exactly on all nine computed
`(Q, J)`; C20 records that every efficiency ratio is `>= 1`, which is a
corollary of (2) and (4) and not an independent test.

**Proposition E (exact part candidate-T; conditional algebra).** Fix
`Q = 2^j`. Write `K(J) = K_{J-1} = 2^{J+j+1}`, so `log K(J) = (J+j+1) log 2`.

(E1) If `||Y_{Q,J}||_B^2 <= C J` and `||D_{Q,J}||_B^2 <= C_D` for all
`J >= 1`, then for all `J`,

```text
d_{K(J)}(A_Q)^2 <= C/(2J) + C_D/(8J^2),
```

i.e. `d_K(A_Q)^2 <= (C log 2 / 2) / (log K - (j+1) log 2) + O(1/log^2 K)`
along the grid `K = K(J)`.

(E2) If `d_K(A_Q)^2 >= c / log K` for all grid points `K = K(J)`, then for
all `J`,

```text
||Y_{Q,J}||_B^2 >= (2c/log 2) J^2/(J+j+1) - ||D_{Q,J}||_B^2/4
                >= (2c/log 2)(J - j - 1) - ||D_{Q,J}||_B^2/4,
```

and if moreover `||D_{Q,J}||_B^2 <= C_D`, then `||Y_{Q,J}||_B^2 >=
(2c/log 2) J - (2c/log 2)(j+1) - C_D/4 = (2c/log 2) J - O(1)`.

*Proof.* (E1): Lemma D(2) and identity (1) give `d_{K(J)}^2 <=
||Y||^2/(2J^2) + ||D||^2/(8J^2) <= C/(2J) + C_D/(8J^2)`; substitute
`J = log K/log 2 - j - 1`. (E2): Lemma D(3) with `d^2 >= c/((J+j+1) log 2)`
gives the first line; `J^2/(J+j+1) = J - (j+1) + (j+1)^2/(J+j+1) >=
J - (j+1)` gives the second. QED

Scope of the label: (E1) and (E2) are conditional on all-`J` hypotheses
that have no finite instance, so no verifier check tests them; the
candidate-T label covers the algebra only. Illustration (not a test): at
`Q = 2`, `J = 4` (`K = 64`) the exact lower bound of Lemma D(3) is `0.3605`
against the exact `||Y_{2,4}||^2 = 0.5096`, and the (E2) first line with
`c = 0.09`, `j = 1` would read `0.334 <= 0.5096` (DIAGNOSTIC decimals of
exact fractions; sec. 8.3). What (E1), (E2) mean for the note's closure
target, and where the analogy with the continuous setting stops, is in
sec. 9.3 (R and HEURISTIC, respectively).

## 8. Census tables (exact; decimals are DIAGNOSTIC)

All values are exact rationals in the verifier; the stdout prints every
approximant error, distance at the cuts, mean-channel norm, lower bound and
efficiency ratio exactly: as a fraction when it has at most 8000 digits
(this covers all approximant errors and channel norms, up to about 6700
digits, and everything at `K_h <= 32`), and otherwise (the `K_h = 64`
distances, lower bounds and ratios, 44,000 to 51,000 digits each) as the
digit count plus the SHA-256 of the canonical string `num/den`, which a
replay compares exactly. Float renderings appear separately under a
DIAGNOSTIC label. Decimals below are float renderings of those fractions
and assert nothing.

### 8.1 Squared distances `d_K(x)^2`, exact for `K <= 10`

| K | `d_K(1)^2` | `d_K(A_2)^2` | `d_K(A_4)^2` | `d_K(A_8)^2` |
|---|---|---|---|---|
| 2 | 1/2 | 3/8 | 3/32 | 3/128 |
| 3 | 52/251 | 1425/8032 | 11541/128512 | 46605/2056192 |
| 4 | 95/766 | 3507/49024 | 69987/784384 | 283035/12550144 |
| 5 | 987196/11709287 | 26146687/374697184 | 306759529/5995154944 | 2016558867/95922479104 |
| 6 | 168677/2018075 | 34425611/581205600 | 426635279/9299289600 | 3123911471/148788633600 |
| 7 | 427057462138410/8196142861502003 | 224999221125595187/4720978288225153728 | 1561213928561656111/37767826305801229824 | 25373343670983234059/1208570441785639354368 |
| 8 | 99798522848850307/1929506790431462857 | 25299136948869186175/555697955644261302816 | 302510924803233786109/8891167290308180845056 | 2963083005104248396747/142258676644930893520896 |
| 9 | 60622737896864509142/1176007057940578080117 | 28802276502543186874637/677380065373772974147392 | 176600555493776489267383/5419040522990183793179136 | 141369923244168800103901/10200546866805051845984256 |
| 10 | 705092006280271911060007117/13738605773891725756927498559 | 1131797849883947519775219203/26916452128440932095204895136 | 599194277821964678570570392759/21102498468697690762640637786624 | 30746212518814182629171837801/2296870581626959538790817718272 |

`K = 11, 12` are printed exactly in the stdout (about 70 digits each).
The column `d_K(1)^2` reproduces the review's table (C08). Note
`d_2(A_Q)^2 = ||A_Q||^2 = 3/(2*4^j)` exactly: `<A_Q, r_2>_B = 0` for
`Q >= 2` (`A_Q` is supported on even `n`, `r_2` on odd `n`), so `r_2`
contributes nothing; `d_3(A_Q)^2 < d_2(A_Q)^2` is the first genuine
projection.

### 8.2 DIAGNOSTIC decimals along the dyadic grid and at `K_max`

| K | `d_K(1)^2` | `*log K` | `d_K(A_2)^2` | `*log K` | `d_K(A_4)^2` | `*log K` | `d_K(A_8)^2` | `*log K` |
|---|---|---|---|---|---|---|---|---|
| 8 | 0.051722 | 0.1076 | 0.045527 | 0.0947 | 0.034024 | 0.0708 | 0.020829 | 0.0433 |
| 16 | 0.037426 | 0.1038 | 0.035611 | 0.0987 | 0.024098 | 0.0668 | 0.011161 | 0.0309 |
| 32 | 0.028568 | 0.0990 | 0.027933 | 0.0968 | 0.018042 | 0.0625 | 0.008375 | 0.0290 |
| 40 | 0.027127 | 0.1001 | 0.027178 | 0.1003 | 0.017381 | 0.0641 | 0.008202 | 0.0303 |
| 48 | 0.025395 | 0.0983 | 0.024533 | 0.0950 | 0.016540 | 0.0640 | 0.007879 | 0.0305 |
| 64 | 0.023795 | 0.0990 | 0.022482 | 0.0935 | 0.014652 | 0.0609 | 0.006818 | 0.0284 |
| 72 | 0.023488 | 0.1004 | 0.022096 | 0.0945 | 0.014304 | 0.0612 | 0.006778 | 0.0290 |

The full table `K = 2..72` is in the stdout. `d_K(1)^2 log K` stays in
`[0.0969, 0.1004]` for `32 <= K <= 72`, extending REVIEW-CZ sec. 2 (sec. 7
item) from `K = 40` to `K = 72`. `d_K(A_2)^2 log K` stays in `[0.0935,
0.1004]` on the same range; `d_K(A_4)^2 log K` in `[0.0608, 0.0649]`;
`d_K(A_8)^2 log K` in `[0.0283, 0.0305]`. These are finite observations,
not asymptotics.

### 8.3 Approximants, averages and channels (exact fractions in the stdout; short ones repeated here)

Sharp cuts, `||A_Q - p_h||_B^2` and efficiency `||A_Q - p_h||^2 /
d_{K_h}(A_Q)^2` (every entry of both tables below is printed as an exact
fraction in the stdout; the decimals here are DIAGNOSTIC renderings):

| Q | h | K_h | `||A_Q - p_h||^2` (exact where short; decimal DIAGNOSTIC) | `d_{K_h}(A_Q)^2` | ratio |
|---|---|---|---|---|---|
| 2 | 0 | 8 | 217759/3210480 = 0.067828 | 0.045527 | 1.4898 |
| 2 | 1 | 16 | 16888898572930617627517/246084177629303845731900 = 0.068631 | 0.035611 | 1.9272 |
| 2 | 2 | 32 | 0.086469 | 0.027933 | 3.0956 |
| 2 | 3 | 64 | 0.080608 | 0.022482 | 3.5854 |
| 4 | 0 | 16 | 245736174487/4536558936000 = 0.054168 | 0.024098 | 2.2478 |
| 4 | 1 | 32 | 0.041500 | 0.018042 | 2.3003 |
| 4 | 2 | 64 | 0.036253 | 0.014652 | 2.4742 |
| 8 | 0 | 32 | 0.023593 | 0.008375 | 2.8171 |
| 8 | 1 | 64 | 0.020852 | 0.006818 | 3.0582 |

Averages and channels (identity (1) holds exactly on every row, C17):

| Q | J | K_{J-1} | `||A_Q - avg_J||^2` | `||Y||^2` | `||D||^2` | `2J^2 d^2 - ||D||^2/4` | eff. | `||Y||^2/J` | `||D||^2/(8J^2)` |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 8 | 0.067828 | 0.059190 | 0.305861 | 0.014588 | 1.4898 | 0.05919 | 0.03823 |
| 2 | 2 | 16 | 0.047072 | 0.165155 | 0.845694 | 0.073468 | 1.3218 | 0.08258 | 0.02643 |
| 2 | 3 | 32 | 0.034354 | 0.319818 | 1.194191 | 0.204239 | 1.2299 | 0.10661 | 0.01659 |
| 2 | 4 | 64 | 0.027143 | 0.509619 | 1.435825 | 0.360483 | 1.2073 | 0.12740 | 0.01122 |
| 4 | 1 | 16 | 0.054168 | 0.083940 | 0.097584 | 0.023801 | 2.2478 | 0.08394 | 0.01220 |
| 4 | 2 | 32 | 0.029480 | 0.171313 | 0.258093 | 0.079810 | 1.6340 | 0.08566 | 0.00807 |
| 4 | 3 | 64 | 0.021751 | 0.294070 | 0.389760 | 0.166300 | 1.4845 | 0.09802 | 0.00541 |
| 8 | 1 | 32 | 0.023593 | 0.039644 | 0.030166 | 0.009208 | 2.8171 | 0.03964 | 0.00377 |
| 8 | 2 | 64 | 0.014628 | 0.098247 | 0.075122 | 0.035766 | 2.1455 | 0.04912 | 0.00235 |

Exact values at the smallest cut: `||A_2 - p_0||^2 = 217759/3210480`,
`||Y_{2,1}||^2 = 47507/802620`, `||D_{2,1}||^2 = 167/546` (check:
`47507/(2*802620) + 167/(8*546) = 217759/3210480`); `||A_4 - p_0||^2 =
245736174487/4536558936000`, `||Y_{4,1}||^2 = 47599861003/567069867000`,
`||D_{4,1}||^2 = 4365817/44739240`; the `Q = 8` fractions have about 110
digits, and the fractions of every row with `J >= 2` or `K_h >= 32` are
longer; all of them are in the stdout (in full, or as digit count plus
SHA-256 fingerprint above 8000 digits, sec. 8 preamble).

`gamma_{Q,K}` at the cuts (exact): `Q = 2`: `11/168, 89/2772,
6461513/450627408, 921199518865/94031632629396` at `K = 8, 16, 32, 64`;
`Q = 4`: `23/1560, 19043/2111200, 16110959369/6250460416200` at `K = 16,
32, 64`; `Q = 8`: `43/10800, 95647/58892400` at `K = 32, 64`.

## 9. Readings

### 9.1 Calibration and scope of the exact machinery

The closed form of Lemma B, the three Gram tables and the `LDL^T`
factorisation reproduce every number of the record that they touch (C04,
C05, C08, C09) and agree with two brute-force enclosures (C01, C02), with a
direct normal-equation solve for `K <= 16` (C09), with pointwise normal
equations over the period 840 (C10), and with direct full-period evaluation
of the channel norms over periods up to 720720 (C18). The cost driver is
not the Gram table (5 s at `K = 72`) but the exact `LDL^T` over rationals
(70 s at `K = 72`, 330 s at `K = 80` in a trial run), whose pivots reach
about `10^5` bits; `K_max = 72` is the budget cut, not a mathematical one.

### 9.2 The Mobius family against the optimal projection (R, diagnostic)

The sharp single-cut approximant `p_h` is not close to the orthogonal
projection of `A_Q` onto `V_{K_h}`, and it gets relatively worse with `h`
in the computed range: efficiency `1.49, 1.93, 3.10, 3.59` for `Q = 2`,
while its absolute error does not decrease (`0.0678, 0.0686, 0.0865,
0.0806`). The Cesaro average does decrease (`0.0678, 0.0471, 0.0344,
0.0271`) with efficiency falling towards `1.2`. So in the computed range the
averaging is the whole mechanism by which the note's family tracks the
distance `d_K(A_Q)`; the sharp family alone shows no convergence at
`K_h <= 64`. This is a finite observation at four cuts and is compatible
with every hypothesis about the limit.

Second observation: `d_K(A_2)^2` is nearly equal to `d_K(1)^2` for `K >= 32`
(ratio `0.94` at `K = 72`) although `||A_2||^2 = 3/8` is `3/16` of
`||1||^2 = 2`. Projection onto `V_K` removes almost all of `1` that it can
remove (the odd part `r_2 = a_0` is in `E`, and `1 = sum a_j`), and what
remains is dominated by the first missing layer `a_1 = A_2`, consistent
with REVIEW-CZ sec. 4 ("the smallest missing sequence is `a_1`"). The
higher layers contribute `d_K(A_4)^2 ~ 0.61 d_K(1)^2`, `d_K(A_8)^2 ~ 0.29
d_K(1)^2` at `K = 72`; the distances of the layers do not add (they are
not orthogonal after projection), so no decomposition of `d_K(1)^2` is
claimed.

### 9.3 What the "closure-strength CJ mean-channel bound" would be

The Mobius note (sec. 6, after (19), and sec. 14) names as its closure
target a bound `||Y_{Q,J}||_B^2 <= C J`, with the difference channel
already controlled (`||D_{Q,J}||_B^2 = O(1)` in `J`, its candidate-T after
(1)). Proposition E makes the exact content of that target explicit.

- (R) By (E1), a `CJ` bound with bounded difference channel gives
  `d_K(A_Q)^2 <= (C log 2/2 + o(1))/log K` along `K = 2^{J+j+1}`. That is a
  *rate* statement for the twisted Nyman-Beurling distance in the `B`-norm.
  Membership `a_j in V` by itself is only `d_K(A_Q) -> 0` with no rate.
  HEURISTIC (analogy only): the shape `const/log K` is the shape of the
  Baez-Duarte-Balazard-Landreau-Saias conjecture
  `d_N^2 ~ (2 + gamma - log 4 pi)/log N` in the continuous setting (cited
  in REVIEW-CZ sec. 4 and 7, not verified there or here); that conjecture
  concerns the `H`-norm distance of the target `1` in the continuous
  Nyman-Beurling space, while here the norm is `B`, the target is `A_Q` and
  the space is Bagchi's sequence space. No relation between the two
  distances, with or without constants, is claimed.
- (R) By (E2), if `d_K(A_Q)^2 >= c/log K` on the grid, then `||Y||^2 >=
  (2c/log 2) J - O(1)`: a bound `O(J)` would then be the exact order and no
  `o(J)` bound is possible. HEURISTIC: in the continuous setting, Burnol's
  unconditional lower bound `liminf d_N^2 log N >= sum_{rho on the line}
  m_rho^2/|rho|^2 > 0` excludes `o(1/log N)` for the target `1`; whether an
  analogous bound holds for the target `A_Q` in the `B`-norm is not proved
  here and its transfer is NOT claimed. The computed values are consistent
  with `c ~ 0.09` for `Q = 2` (sec. 8.2), which would make the forced slope
  `2c/log 2 ~ 0.26`; the observed `||Y||^2/J` is `0.059, 0.083, 0.107,
  0.127` for `J = 1..4`, still rising (DIAGNOSTIC; far from asymptotic).

Reading (R): the note's `CJ` target is not a bare membership statement but
a rate statement. This is consistent with, though not a consequence of, the
note's own guard (sec. 8 there: all-large-`J` convergence of the sharp
family for unbounded `Q` forces RH and simple zeros; no-go ledger item 7),
which concerns a different family and a different range of `Q`. Any
argument for `CJ` must therefore carry rate information about the
Nyman-Beurling distance of the layer `a_j`, and no finite table can supply
it. Conversely an `o(J)` bound should be treated as suspect on sight unless
it comes with a proof that `d_K(A_Q)^2 = o(1/log K)`.

### 9.4 Logical status of the mean-channel debt (R; references only)

Let `Q = 2^j`, `j >= 1`, and call "mean-channel closure for `Q`" the
statement `||A_Q - avg_J||_B -> 0` as `J -> infinity` (equivalently, by
identity (1) with bounded `||D||`, `||Y_{Q,J}||_B^2 = o(J^2)`).

1. Mean-channel closure for `Q` implies `a_j in V`: every `avg_J` is a
   finite rational combination of remainders (Lemma D(1)), so `A_Q = a_j`
   is a norm limit of elements of `E`, and `V` is closed. Equivalently, it
   implies `d_K(a_j) -> 0` along the dyadic grid, hence along all `K`
   (monotone).
2. The converse, `a_j in V` implies mean-channel closure for the note's
   specific family at that `Q`, is NOT established here (O): `a_j in V`
   says that *some* sequence in `E` converges to `a_j` (the orthogonal
   projections do, by definition), not that the Mobius averages do. The
   efficiency ratios of sec. 8.3 (`1.2` to `3.6`) leave this open
   numerically. The note's sec. 8 guard concerns the *sharp* family for
   *unbounded* `Q` and all large `J` and does not decide this single-`Q`
   question either way. By item 1, "mean-channel closure for `Q`" is *at
   least* `a_j in V`.
3. `a_j in V` is a consequence of RH (hard direction: RH implies `V = H` by
   Bagchi's theorem, imported in NOTE-SOURCE-CZ sec. 1 and REVIEW-CZ sec. 2)
   and, in the elementary direction, `a_j in V` together with a zero `rho`
   of `zeta` with `Re rho > 1/2` forces the Hurwitz shadow condition
   `zeta(rho, 1/2 + 2^{-j-1}) = 0` (REVIEW-CZ Theorem 3.6, corollary). For
   `j = 1` this is `beta(rho) = 0` (NOTE-SOURCE-CZ sec. 5).
4. `a_j in V` for infinitely many `j` implies RH (REVIEW-CZ Theorem 3.6,
   analyticity of the Hurwitz zeta in its parameter), and `a_j in V` for all
   `j` is equivalent to RH (NOTE-SOURCE-CZ sec. 4; REVIEW-CZ Lemma 3.5 item
   6). Hence mean-channel closure for infinitely many `Q = 2^j` implies RH,
   and mean-channel closure for one `Q` implies the shadow condition for
   that `j`.
5. Honest reading: the debt of the Mobius note, for one `Q`, is the twisted
   Nyman-Beurling problem of REVIEW-CZ sec. 4 (approximate the Mellin image
   of `a_j`, which carries the Hurwitz zeta `zeta(s, 1/2 + 2^{-j-1})`, by
   `zeta(s) P(s)/s` with Dirichlet polynomials `P`, `P(1) = 0`, in
   `H^2(Re s > 1/2)`), and with the note's specific family it is that
   problem with a rate (sec. 9.3). It is one obligation in a different
   dress (REVIEW-CZ Lemma 3.5, "each item is another dress of the same
   obligation"). It is not a numerical seam: no finite `J` decides it, the
   exact census here included; the finite table is consistent with every
   hypothesis about the limit, as the owner verdict cited in REVIEW-CZ
   sec. 4 states for finite prefixes.

### 9.5 Counting

Per RH-ONE-WALL-CROSSREF_2026-08-17.md this note adds an exact census and
one elementary lemma at the Nyman-Beurling level of the one wall. It does
not add a level, a carrier or a positive construction. It must not be
booked as a theorem about RH, and its rate reading (sec. 9.3) is a reading
of the known obstruction ("no finite prefix", "no rate from membership"),
not a new obstruction.

## 10. What this does not do

- It does not prove, disprove, assume, or provide evidence for RH. RH stays
  an open program-level obligation; no registry row moves.
- It does not prove `a_j in V` for any `j`, nor `d_K(x) -> 0` for any
  target, nor any lower bound `d_K(x)^2 >= c/log K`. All distance values are
  finite exact rationals at `K <= 72`.
- It does not prove the Mobius note's bound (3) for all `K` (finite scope
  `K <= 4096` only), nor its candidate-T bound on the difference channel
  (`||D_{Q,J}||^2 = O(1)`; the computed values `0.31, 0.85, 1.19, 1.44` for
  `Q = 2` are consistent with boundedness and with slow growth alike), nor
  any of its bounds (2), (7)-(11), (17)-(19), (38).
- It does not transfer Burnol's lower bound or the
  Baez-Duarte-Balazard-Landreau-Saias conjecture from the continuous
  Nyman-Beurling setting to the `B`-norm or to the twisted target `A_Q`;
  every use of them above is marked HEURISTIC.
- It does not establish the converse in sec. 9.4 item 2 (membership
  implies convergence of the Mobius averages); that direction is open (O).
- It does not repeat any route in the Mobius note's no-go ledger (sec. 13
  there) and kills none; no `F` is recorded.
- It does not verify the external references of either note (Bagchi,
  Baez-Duarte, Burnol, Lee-Leong); it uses them only as the record cites
  them.
- The verifier runs on one architecture; no second-architecture replay is
  claimed (the referee's modular `LDL^T` re-computation is an independent
  implementation on the same architecture, not a replay). Its checks are
  exact but finite; every floating-point rendering it prints is under a
  DIAGNOSTIC label and asserts nothing.
- It does not determine the Mobius note's `Delta` convention as a theorem;
  the convention is the note's own (identities (4) and (23)), and sec. 3 is
  a reading of it.

## 11. Review record (repair of 2026-09-15)

Two adversarial referee reports were applied: report 1 (mathematics lens:
independent re-derivation of every lemma and identity, independent exact
re-computation of every finite table, modular `LDL^T` cross-check of the
full census; 24 of 24 own checks PASS) and report 2 (evidence-and-code
lens: clean-shell replay, source audit, markdown hygiene, independent
spot-checks). Neither refuted any mathematical statement; both weakened
labels and framing. No claim was added in the repair.

### 11.1 Accepted corrections

| # | Source | Correction applied |
|---|---|---|
| A1 | R1 V1, R2 V1 | Lemma B / V1 relabelled "duplicate of record" (NOTE-SOURCE-CZ sec. 6 boxed formula; REVIEW-CZ sec. 2 cycle parameters; review verifier group F). No lane candidate-T. Lemma B header, summary item 1, verdict row V1, falsifier row rewritten; note added that C01-C03 certify enclosure, not the closed form. |
| A2 | R1 V7, R2 V7 | Summary item 2: range of `d_K(1)^2 log K` on `32 <= K <= 72` corrected from `0.0990 ... 0.1004` to `0.0969 ... 0.1004` (minimum at `K = 42`), matching sec. 8.2 and the stdout. |
| A3 | R1 V4, R2 V4 | The "determination of the convention" downgraded to a reading (R). Sec. 3 now cites the Mobius note's identities (4) and (23) as the source of the backward convention. V4 split into V4a (Lemma C, candidate-T), V4b (convention reading, R) and V4c (forward-convention record, candidate-C). Summary item 4 rewritten. |
| A4 | R1 V4, R2 V4 | Forward-convention shift `p^fwd_h(n) = A_Q(n+1)` stated and tested for every `Q in {2, 4, 8}`, not only `Q = 4, 8`; the `Q = 2` case `p^fwd(1) = 1` identified as its `n = 1` instance (C12). |
| A5 | R2 V4 | "(1) fails for `Q = 2` by exactly 1" is now computed in C12 by direct evaluation over the period 840 (`S^fwd(1) = -1`, gap `= 1`), not inferred from Lemma A; the PASS line no longer says "kills (1)". |
| A6 | R2 findings | Check-to-claim mapping repaired: C13 (convention-free) removed from V4; C09 added to V7; the C06 count is `2832 of 2832` (the earlier structured result's `2842` was a transcription error). |
| A7 | R1 V10, R2 V10 | The sentence "a rate statement of BBLS-conjecture type" removed from the candidate-T label. V10 now covers (E1), (E2) only, with the note that no check tests them (C19 tests Lemma D(3) instances); the reading is V10r (R) and the BBLS comparison is HEURISTIC in sec. 9.3 and summary item 5. |
| A8 | R1 V12, R2 V12 | Sec. 9.4 item 2: "not elementary (the note's sec. 8 guard)" replaced; the guard concerns the sharp family for unbounded `Q` and does not decide the single-`Q` converse, which is O. Summary item 6 and the "Reading" paragraph of sec. 9.3 adjusted accordingly. |
| A9 | R1 sec. 6, R2 findings | Verifier hygiene: the stdout now prints every approximant error, distance at the cuts, mean-channel norm, lower bound and efficiency ratio exactly (as a fraction up to 8000 digits, which covers all approximant errors and channel norms; the `K_h = 64` distances, lower bounds and ratios of 44,000 to 51,000 digits as digit count plus SHA-256 of `num/den`); float renderings appear only under DIAGNOSTIC labels (including the C14 PASS line and the gamma table). The header's "one DIAGNOSTIC float block" replaced by an accurate statement. V9 and V13 evidence fields now true. |
| A10 | R2 V8 | C19's support sub-check was tautological on the construction of `p_coeffs`; C19 now tests `t_Q(1) = 0` explicitly and its PASS line says what is tested. |
| A11 | R1 V9, R2 V9 | C20 annotated (in the verifier and in sec. 7) as a corollary of C19, not an independent test. |
| A12 | R1 V6 | Where the maxima of `abs(gamma_{Q,K})` are attained (`K in {3,4}`, `{5..8}`, `{9..16}`) added to C14, sec. 3 item 5, sec. 6 and V6, with the remark that the `K <= 4096` check is uninformative about the growth regime. |
| A13 | R1 V11, R2 V11 | Forced slope `2c/log 2` with `c ~ 0.09` corrected from `~0.27` to `~0.26`. |
| A14 | R1 sec. 4 | Weakest-step and degenerate-case notes for Lemma B (`d_{j+t} = d_j` needs `j + 1 >= h`; `L = 1`, `L = 2^h`) recorded next to the proof, attributed to the referee. |
| A15 | R2 hygiene | Sec. 10 updated: floats only under DIAGNOSTIC; the convention is the note's own; the referee's modular re-computation is not a second-architecture replay. Sec. 12 (Pins) added. |

### 11.2 Referee objections considered and rejected or qualified

- R1 V4 / R2 V4, premise "the Mobius note does not state its convention is
  false": objection considered and partially rejected because the note
  contains no explicit definition line for `Delta` (its sec. 1 writes
  `t_Q = mu * Delta A_Q` without defining `Delta`), so the literal sentence
  was true in the narrow sense; it is accepted in substance because the
  note's (4) and (23) fix the convention unambiguously, and the repaired
  sec. 3 says exactly that. The label change (candidate-T to R) is
  accepted in full.
- R2 finding "lane directory contamination" (sibling referee files in the
  lane directory): not an objection to the lane's content; those files were
  placed there by the session, are not lane deliverables and were left
  untouched.
- No other referee objection was rejected.

## 12. Pins

Fresh run from a clean shell after the repair
(`env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_nb_projection.py`):
exit 0, `CHECKS: 20 of 20 PASS`, stdout byte-identical to the committed
verify_nb_projection.stdout.txt.

```text
SHA-256  verify_nb_projection.py          25be0e1ec3b123de4234862f7581194647597a46716478135fdf9cc4f4f1045b
SHA-256  verify_nb_projection.stdout.txt  ee66bd9527a7d6b4136993051fced0632e25aea3a0c7bff228c84e9b6a487b4e
runtime  143 s wall (two consecutive runs, both exit 0, byte-identical stdout) on one x86_64 lane (Python 3.11)
```

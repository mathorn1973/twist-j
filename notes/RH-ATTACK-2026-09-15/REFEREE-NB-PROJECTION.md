# REFEREE-NB-PROJECTION: adversarial mathematics review of ATTACK-NB-PROJECTION (lane A)

```text
STATUS      NON-CANONICAL incubation material (referee report). No status
            motion, no registry row, no probe, no Canon change. Nothing here
            is a proof of RH, evidence for RH, or a falsification of RH.
DATE        2026-09-15
BASIS       Public Canon v86 (STATUS.md ACTIVE, tag canon-v86, content commit
            56068ba4423a2ca38ce5760f1e34e82e2597f99f; checked against
            STATUS.md and the tag on the local checkout)
RH          unchanged: open program-level obligation
            (ZETA-RH-STATUS-2026-09-08.md, RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md)
LENS        MATHEMATICS (re-derivation, weakest step, degenerate cases,
            status labels, RH-progress language, counting rule, duplication)
REVIEWED    ATTACK-NB-PROJECTION.md, verify_nb_projection.py (sha256
            fc1201242157ad1e6aa2a75ae450b2c081866d7c30b7924068566cda0cc4c20d,
            matches the declared hash), verify_nb_projection.stdout.txt
VERIFIER    referee_nb_projection.py (Python 3 standard library, int and
            fractions.Fraction; DIAGNOSTIC float lines assert nothing). It
            executes the lane's verifier in-process and compares its exact
            tables against an independent implementation: brute-force cycle
            detection for the periodic binary sum, divisor-sum Mobius
            convolution, Fraction Gaussian elimination for K <= 16, modular
            LDL^T modulo three 60-bit primes for the whole K <= 72 census,
            direct evaluation of the channel norms over the periods 840 and
            720720. 24 of 24 PASS, exit 0, about 250 s (146 s of which is the
            lane's own verifier); stdout in referee_nb_projection.stdout.txt.
            Run: LC_ALL=C PYTHONHASHSEED=0 python3 referee_nb_projection.py
            from its own directory, next to verify_nb_projection.py.
REPLAY      The lane's verifier was re-run unmodified from a clean shell:
            exit 0, 147 s wall, stdout byte-identical to
            verify_nb_projection.stdout.txt.
COUNTING    The lane books itself as a further reading of the one wall at the
            Nyman-Beurling level (REVIEW-CZ sec. 5). This referee agrees and
            adds nothing to the count.
```

## 0. Verdict in one paragraph

Every mathematical statement in the lane that I could re-derive or recompute
is correct: Lemma A (split identity), Lemma B (periodic closed form), Lemma C
(below the cut), identities (1), (12), (13), (14), Lemma D, Proposition E's
algebra, the finite bound (3) up to `K = 4096`, and the full exact census
`d_K(x)^2`, `2 <= K <= 72`, for the four targets (agreement modulo three
independent primes, exact agreement for `K <= 16`, exact agreement with all 44
printed fractions). No REFUTED verdict is warranted on mathematics. Four
verdicts are WEAKENED for the following reasons: (V1) the closed form is the
record's theorem (NOTE-SOURCE-CZ sec. 6 with REVIEW-CZ sec. 2) and must be
filed as a duplicate re-verification, not as a lane candidate-T; (V4) the
"determination of the Delta convention" is a reading, not a theorem, and the
premise "the Mobius note does not state its convention" is false: the note's
equations (4) and (23) fix the backward convention explicitly (sec. 3 below);
(V10) the exact algebra is correct and trivial, but the sentence "hence ... a
rate statement of BBLS-conjecture type" is an analogy across a different norm,
target and setting and cannot sit inside a candidate-T label; (V12) the
parenthetical "not elementary (the note's sec. 8 guard)" misattributes: the
guard concerns the sharp family for unbounded `Q` and does not bear on the
single-`Q` converse. One textual error was found in the summary (item 2: the
range `0.0990 ... 0.1004` should read `0.0969 ... 0.1004`, minimum at
`K = 42`), one omission (the forward-convention shift `p_h(n) = A_Q(n+1)`
holds for `Q = 2` too, not only for `Q = 4, 8`), and two verifier hygiene
points (float renderings inside non-DIAGNOSTIC PASS lines and under an
"exact" heading). No claim states or implies progress on RH, evidence for RH,
or any status change.

## 1. Falsifiers first

| Referee verdict | What kills it |
|---|---|
| "All exact values of the lane are reproduced independently" (R04-R09, R12-R23) | one FAIL line in referee_nb_projection.py on a clean re-run, or a demonstration that my modular LDL shares a bug with the lane's Fraction LDL (they share only the Gram entries, which are themselves recomputed with different cycle bookkeeping) |
| "The Mobius note fixes the backward convention through (4) and (23)" (sec. 3) | a reading of (4) with source pairs `(mQu, m(Qu+1))` or of (23) with `sum_{u odd}[(Qu)^{-s} - (Qu+1)^{-s}]` that is compatible with `Delta^+ A_Q(n) = A_Q(n+1) - A_Q(n)`; there is none, since the Dirichlet series of `Delta^+ A_Q` is `sum_{u odd}[(Qu-1)^{-s} - (Qu)^{-s}]` (sec. 3) |
| "V1 duplicates the record" | a step in the lane's Lemma B that is absent from NOTE-SOURCE-CZ sec. 6 plus REVIEW-CZ sec. 2 (item "sec. 6, implementation": `h = v_2(L)`, `t = ord_{L/2^h}(2)`); I found none |
| "V10's BBLS sentence is an analogy, not a theorem" | a proof relating `d_K(A_Q)^2` in the `B`-norm to the continuous NB distance `d_N^2` of the BBLS conjecture with explicit constants; none is offered and the lane itself marks the transfer HEURISTIC |
| "Summary item 2 misstates the range" | the lane's own table (stdout, `K = 42`: `0.0969`) and my recomputation agree; only a different definition of the range would rescue the sentence |
| "No RH-progress language" | any sentence in the lane presenting a finite value as evidence about the limit; I found none, every finite observation is fenced |

## 2. Verdict table

| id | verdict | reason (short) | corrected statement the lane should adopt |
|---|---|---|---|
| V1 | WEAKENED | mathematically confirmed (own proof re-derivation; R01-R04), but it is the record's theorem: NOTE-SOURCE-CZ sec. 6 boxed formula, cycle parameters `h = v_2(L)`, `t = ord_{L/2^h}(2)` in REVIEW-CZ sec. 2, independent enclosure check already in the review verifier (group F, 650 checks) | "Lemma B is the closed form of NOTE-SOURCE-CZ sec. 6 as sharpened in REVIEW-CZ sec. 2; re-implemented and re-checked here (C01-C03). Record theorem, duplicate; no lane candidate-T." |
| V2 | CONFIRMED | all hardcoded values are byte-identical to verify_rh_binary_review.stdout.txt (diff) and NOTE-SOURCE-CZ sec. 7; my own Gram and elimination reproduce them (R03, R05, R06) | none |
| V3 | CONFIRMED | Lemma A re-derived (pair `{2m, 2m+1}`, `w_B(2m) = w_B(2m+1) = w_B(m)/4`, `a^2 + b^2 = 2l^2 + h^2/2`); identity (1) follows from `S(1) = 0`, which follows from Lemma C; exact on 40 own random sequences (R24) and by direct period evaluation (R19-R21) | none; note that identity (1) is the Mobius note's own (1), the lane supplies the proof |
| V4 | WEAKENED | Lemma C is correct (own proof, R15); the forward-convention failures are correct exact computations (R18); but "the note does not state its convention" is false: the note's (4) (source pairs `a = mQu`, `b = min(m(Qu+1), K)`) and (23) (`A_Q(s) = sum_{u odd}[(Qu)^{-s} - (Qu+1)^{-s}]`) encode `Delta A_Q(n) = A_Q(n) - A_Q(n-1)` (sec. 3; R11); a convention "determination" is a reading, not a theorem; also `p_h(n) = A_Q(n+1)` under the forward convention holds for `Q = 2` as well | "Lemma C (candidate-T) under the backward convention, which is the convention written into the Mobius note's (4) and (23). Under the forward convention (candidate-C computations): `t_2(1) = 1`, `S_{2,J}(1) = -J`, (1) fails for `Q = 2` by exactly 1, `p_h(n) = A_Q(n+1)` below the cut for every `Q`, and (3) fails for `Q = 2` at `K = 2, 3`. (12) is convention-free." Status of the convention statement: R. |
| V5 | CONFIRMED | (12): Abel summation with `s(0) = 0`; (13): Mobius inversion plus hyperbola exchange `floor(n/k) = #{l : kl <= n}`; (14): Abel summation with `a_k = k floor(n/k)`, `a_{n+1} = 0`; all re-derived and checked pointwise `n <= 600` on all cuts (R13, R16, R17) | none; these are the Mobius note's stated identities, the lane supplies proofs |
| V6 | CONFIRMED | own Mobius data (divisor sums, no sieve), `|gamma_{Q,K}| < 5/(4Q^2)` for all `2 <= K <= 4096`, maxima `1/6, 1/20, 1/72` (R12); the maxima are attained at `K in {3,4}`, `{5..8}`, `{9..16}`, i.e. before the second source pair enters, so the finite check says nothing about the growth regime of (3); the lane claims nothing beyond `K <= 4096` | none (optionally add where the maxima sit) |
| V7 | CONFIRMED | 2556 Gram entries equal mine (R04); `d_K(x)^2` for all `K <= 72` and four targets agree with my modular LDL modulo `2^61 - 1`, `10^18 + 3`, `10^18 + 9` (R08), exactly for `K <= 16` (R05); positivity, monotonicity (R09); DIAGNOSTIC ranges of sec. 8.2 reproduced; but summary item 2 of the markdown states `0.0990 ... 0.1004` for `d_K(1)^2 log K` on `32 <= K <= 72`, the true range is `[0.0969, 0.1004]` (minimum at `K = 42`) as sec. 8.2 and the claim list correctly say | fix summary item 2 to `0.0969 ... 0.1004`; the claim as listed in the claim list is correct |
| V8 | CONFIRMED | Lemma D is a one-line consequence of `p_h in V_{K_h}` (coefficient support `{2..K_h}`, `t_Q(1) = 0`, `r_1 = 0`) and the definition of `d_K`; chain holds on all nine `(Q, J)` (R23) | none; it is elementary and the lane says so |
| V9 | CONFIRMED | exact ratios recomputed from the lane's tables and from direct period evaluation (R19-R23); note that `>= 1` is a corollary of Lemma D, so C20 is not an independent test of anything C19 does not already test | none |
| V10 | WEAKENED | (E1), (E2) are two correct lines of algebra on (1) and Lemma D (re-derived; `J^2/(J+j+1) >= J - (j+1)`); but the claim text continues "hence the note's closure-strength CJ bound is a rate statement of BBLS-conjecture type": the BBLS conjecture concerns the `H`-norm distance of the target `1` in the continuous NB setting, here the norm is `B`, the target is `A_Q` and the setting is Bagchi's sequence space; "of the same shape" is an analogy, HEURISTIC by the lane's own sec. 9.3, and cannot sit inside a candidate-T label | "Proposition E (candidate-T, conditional algebra): (E1) and (E2) as stated. Reading (R): a CJ bound with bounded difference channel is equivalent, up to constants, to an `O(1/log K)` rate for `d_K(A_Q)^2` along the dyadic grid; an `o(J)` bound would force `d_K(A_Q)^2 = o(1/log K)`. The comparison with the BBLS conjecture is an analogy across norm, target and setting (HEURISTIC)." |
| V11 | CONFIRMED | correctly labelled HEURISTIC / O; the numbers (`||Y||^2/J = 0.059, 0.083, 0.107, 0.127`, `c ~ 0.09`, forced slope `2c/log 2 ~ 0.26`) are reproduced; the E2 instance at `J = 4` gives `0.334 <= 0.5096`, consistent | none |
| V12 | WEAKENED | items 1, 3, 4 are correct references (REVIEW-CZ Lemma 3.5, Theorem 3.6, sec. 4); item 2's "is not elementary (the note's sec. 8 guard)" misattributes: the guard concerns the *sharp* family for *unbounded* `Q` and all large `J` and says nothing about whether `a_j in V` implies convergence of the Cesaro averages for one fixed `Q`; "not elementary" is an opinion, not a record statement; the "So" in item 2 follows from item 1, not from the guard | "The converse (`a_j in V` implies mean-channel closure for the note's family at that `Q`) is not established here (O). The note's sec. 8 guard concerns the sharp family for unbounded `Q` and does not decide this single-`Q` question." Status R, duplicate of REVIEW-CZ sec. 4 (acknowledged by the lane). |
| V13 | CONFIRMED | all quoted values recomputed (R19-R23 and the lane's tables): sharp errors `0.0678, 0.0686, 0.0865, 0.0806`; averages `0.0678, 0.0471, 0.0344, 0.0271`; `||D_{2,J}||^2 = 0.31, 0.85, 1.19, 1.44` with increments `0.54, 0.35, 0.24`; `d_72(A_2)^2 / d_72(1)^2 = 0.9407`; correctly fenced as finite observations | none |

No verdict above is a status motion for any registry row. No `F` is
recorded by this referee.

## 3. The one derivation this referee adds: the convention is written in the Mobius note

The lane (sec. 3) says "The Mobius note does not state its convention" and
then "determines" it from the behaviour of (1), (3), (13). The premise is
false; the determination is unnecessary. Two displayed equations of
C-RH-MOBIUS-MEAN-CHANNEL-N.md fix the convention directly.

**Claim (candidate-T, elementary).** With `t_Q = mu * Delta A_Q`, the
following are equivalent for `Q = 2^j`, `j >= 1`: (i) `Delta` is the backward
difference `Delta x(n) = x(n) - x(n-1)`, `x(0) = 0`; (ii) for every `k >= 1`,
`t_Q(k) = sum_{m | k, k/m = Qu, u odd} mu(m) - sum_{m | k, k/m = Qu + 1, u odd} mu(m)`
(the source-pair form behind the note's identity (4), whose pairs are
`a = mQu`, `b = m(Qu+1)`); (iii) for `Re s > 1`,
`sum_{n >= 1} Delta A_Q(n) n^{-s} = sum_{u odd} [(Qu)^{-s} - (Qu+1)^{-s}] = A_Q(s)`,
the paired source Dirichlet function of the note's (23).

*Proof.* Under (i), `Delta A_Q(n) = 1_{n = Q (mod 2Q)} - 1_{n-1 = Q (mod 2Q)}`
for `n >= 1` (the second indicator uses `A_Q(0) = 0`, and `0 != Q (mod 2Q)`,
so the convention `x(0) = 0` is consistent with the periodic extension). The
support of the first indicator is `{Qu : u odd}` and of the second
`{Qu + 1 : u odd}`; Dirichlet convolution with `mu` gives (ii), and the
Dirichlet series gives (iii). Conversely, (ii) or (iii) determines
`Delta A_Q` (Mobius inversion, or uniqueness of Dirichlet coefficients), and
the only difference operator of the form `x(n) - x(n - c)` or `x(n + c) - x(n)`
with that value is the backward one: the forward difference has
`Delta^+ A_Q(n) = 1_{n+1 = Q (mod 2Q)} - 1_{n = Q (mod 2Q)}`, support
`{Qu - 1 : u odd}` with sign `+` and `{Qu : u odd}` with sign `-`, whose
Dirichlet series is `sum_{u odd} [(Qu-1)^{-s} - (Qu)^{-s}] != A_Q(s)`. QED

Verifier: R11 checks (ii) against the divisor-sum Mobius convolution for
`k <= 2000`, `Q in {2, 4, 8}`. Consequence for the lane: V4 should cite (4)
and (23) of the Mobius note as the source of the convention and demote the
"determination" to R; the exact content of Lemma C and of the
forward-convention computations is unaffected.

The lane's (23)-consistency also settles a degenerate case the lane did not
mention: for the forward convention the shift `p_h(n) = A_Q(n+1)` on
`1 <= n < K_h` holds for `Q = 2` as well (R18): `p^+_h(n) = sum_{m <= n}
Delta^+ A_Q(m) = A_Q(n+1) - A_Q(1) = A_Q(n+1)`; the lane's separate report
`p_h(1) = t^+(1) = 1` for `Q = 2` is the case `n = 1` of the same formula.

## 4. Re-derivation notes and weakest steps (lens: mathematics)

- **Lemma A.** Weakest step: the rearrangement of the double sum. It is a sum
  of nonnegative terms under the hypothesis `||x||_B < infinity`, so
  unconditional. Degenerate case `x = delta_1`: `1 = 1 + 0 + 0`. Degenerate
  case `x = delta_2`: `w_B(2) = 1/4`; `Lx(1) = 1/2`, `Hx(1) = -1`, giving
  `1/4 = 0 + (1/4)/2 + 1/8 = 1/4`. Correct.
- **Lemma B.** Weakest step: `d_{j+t} = d_j` for `j >= h`, which needs
  `b_{j+1+t} = b_{j+1}` as well; true because `j + 1 >= h`. Degenerate cases
  `L = 1` (`h = 0`, `t = 1`, all `d_j = 0`, value `2S`) and `L = 2^h`
  (`t = 1`, `b_j = 0` for `j >= h`, tail zero) are handled by the formula
  and by the code (`ord_1(2) = 1`). Correct, and identical to the record.
- **Lemma C.** Weakest step: the `k = 1` term. `Delta r_1 = 0` and
  `t_Q(1) = 0`, so the term vanishes either way; Mobius inversion
  `1 * t = Delta A_Q` closes it. The lemma is the discrete Baez-Duarte
  construction and is what makes `p_h` an approximant at all. Correct.
- **Identity (13).** Weakest step: the exchange
  `sum_{k >= K} t(k) floor(n/k) = sum_{l <= n/K} (s(floor(n/l)) - s(K-1))`;
  the count of `l` is `floor(n/K)`, so the subtracted term is
  `floor(n/K) s(K-1)`. Correct.
- **Identity (14).** Weakest step: the boundary term `a_{n+1} T(n)` with
  `a_{n+1} = (n+1) floor(n/(n+1)) = 0`. Correct. For `n < K` both sides are
  `0` (empty sum, `e_K(n) = 0` by Lemma C).
- **Lemma D and Proposition E.** No weak step; four lines of algebra. E1's
  substitution `J = log K/log 2 - j - 1` is exact along the grid; E2's
  `J^2/(J+j+1) >= J - (j+1)` is `(j+1)^2/(J+j+1) >= 0`.
- **Census.** The lane's cost driver (exact `LDL^T`, 70 s) is confirmed;
  the modular route used here is a cheap second architecture for the same
  numbers and could serve as the two-architecture gate if the census is ever
  filed as `C`.

## 5. Status labels, RH language, counting, duplication

- **Labels.** candidate-T is acceptable for Lemmas A, C, D, identities (1),
  (12)-(14), Proposition E's algebra (complete proofs, exact finite checks).
  It is not acceptable for V4's convention "determination" (a reading; and
  the note fixes the convention itself) nor for the BBLS sentence of V10 (an
  analogy). candidate-C for V2, V6, V7, V9 is correct at the stated scopes.
  HEURISTIC / O for V11 and R for V12, V13 are correct.
- **RH language.** No sentence presents a finite value as evidence for or
  against RH; every DIAGNOSTIC number is fenced ("finite observations, not
  asymptotics"); sec. 10 lists the non-claims explicitly. Clean.
- **Counting rule.** The header and sec. 9.5 book the note as a further
  reading of the one wall at the NB level, consistent with REVIEW-CZ sec. 5
  and ZETA-RH-STATUS-2026-09-08.md sec. 4 ("a finite prefix ... is passed by
  some off-critical configuration"; "no finite prefix is progress"). Lemma D
  and Proposition E add no level, carrier or positive construction. Agreed.
- **Duplication.** V1 duplicates NOTE-SOURCE-CZ sec. 6 and REVIEW-CZ sec. 2
  (acknowledged but labelled as a lane candidate-T; should be filed as a
  record theorem re-verified). V2 is deliberate calibration. V3's identity
  (1) and V5's (12)-(14) are the Mobius note's own identities; the lane adds
  proofs and exact checks, which is legitimate verification of a candidate-T
  note. V7's `d_K(1)^2` for `K <= 40` is already in REVIEW-CZ sec. 2 and the
  review's JSON (`K <= 24` exactly); the lane extends to `K = 72` and adds
  three targets. V12 duplicates REVIEW-CZ sec. 4 and the Mobius note's
  sec. 8 (acknowledged as "references only").

## 6. Verifier hygiene (not affecting any PASS)

- C14's PASS line prints float renderings of exact maxima; the "exact
  approximant errors" block prints `float(PH)` for `K_h > 16` under a heading
  that says "exact". Neither asserts anything, but the discipline places
  floats only in blocks labelled DIAGNOSTIC; move the renderings under such a
  label or print the fractions.
- C20 is implied by C19 (Lemma D) and is not an independent check.
- The C06 count in the stdout file is `2832 of 2832` (`2556` Gram pairs +
  `3 x 72` target checks + `60` random sequences); a transcription elsewhere
  reading `2842` is not the lane's file.
- Determinism, exact arithmetic, runtime (147 s), exit code and the
  `CHECKS: 20 of 20 PASS` line are all as declared.

## 7. What this does not do

- It does not prove, disprove, assume, or provide evidence for RH; it moves no
  registry row and records no `F`.
- It does not extend any lane result: no new `K`, no new `Q`, no new bound.
  My verifier re-derives the lane's finite objects by other means and adds
  one elementary observation (sec. 3) about where the Mobius note fixes its
  convention.
- It does not verify the Mobius note's candidate-T bounds (2), (3) for all
  `K`, (7)-(11), (17)-(19), (38), nor its `||D_{Q,J}||^2 = O(1)`; the lane
  does not claim them either.
- It does not verify the external references (Bagchi, Baez-Duarte, Burnol,
  Lee-Leong, BBLS) or their transfer to the `B`-norm; the lane's HEURISTIC
  fences are accepted as fences, not as results.
- It does not decide the converse of sec. 9.4 item 2 of the lane
  (`a_j in V` implies mean-channel closure of the note's family); that
  remains O in both documents.
- It ran on one architecture; the modular route in referee_nb_projection.py
  is an independent implementation, not a second-architecture replay.

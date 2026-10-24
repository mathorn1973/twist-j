# REFEREE-C-M37-STRENGTH: adversarial referee report on ATTACK-M37-STRENGTH.md

```text
STATUS     NON-CANONICAL referee report (lens: mathematics). Lane C-m37-strength,
           2026-09-15 RH attack session. No status motion. Gates nothing.
DATE       2026-09-15
BASIS      Public Canon v86 (STATUS.md ACTIVE, tag canon-v86), unchanged by this report
RH         unchanged. Open program-level obligation per ZETA-RH-STATUS-2026-09-08.md
           section 1 and RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md.
OBJECT     ATTACK-M37-STRENGTH.md, verify_m37_strength.py
           (sha256 02ae33675807bfad3ddb87398e070bf3e67756d9d8d01274a812020106b39264),
           verify_m37_strength.stdout.txt
           (sha256 f0c7c7510f56452315daae272a347ad1564fd04dd77c246a703ad4be52a2b282).
           Rerun by the referee: exit 0, 15 of 15 PASS, stdout byte-identical, stderr empty.
VERIFIER   referee_m37_strength.py (this report's own finite checks; exact int/Fraction;
           run LC_ALL=C PYTHONHASHSEED=0 python3 referee_m37_strength.py; stdout
           referee_m37_strength.stdout.txt).
RECORD     Read in full: README.md, ANALYTIC.md, ARITHMETIC.md (header), PRIME-CANCELLATION.md
           (sections 1-2), ZETA-RH-STATUS-2026-09-08.md, RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md,
           RH-ONE-WALL-CROSSREF_2026-08-17.md, RESULT-P-RH-WEYL-CANONICAL-2.md,
           REGISTRY-RH-ROWS.tsv, C-GRH-QSQRT5-SPLIT-ORIENTATION-1.md sections 2, 5, 6,
           P-O5-DEDEKIND-GRH-READ-1 PREREG sections 4-7, canon/REGISTRY.tsv bridge row.
```

## 0. Summary of the refereeing

The lane's mathematics is largely sound and its RH hygiene is correct: nothing in
the note states or implies progress on RH, evidence for RH, or a status change,
and the counting rule is invoked where it applies. Two claims do not survive as
written:

1. Theorem 1 (T1) displays a false residue k-factor. The true relation is
   G_k(s) = G_1(s) prod_{p | k} (1 - 2 p^{-s})^{-1}; the lane's
   prod_{p | k} (1 - p^{-rho})^2 / (1 - 2 p^{-rho}) carries a spurious factor
   (1 - p^{-rho})^2. The error propagates to the two-sided bounds of section 2.3.
   No CHECK tests the ratio (CHECK 07 tests the local table, which is right).
   The divisor statement, the k-independence of poles and orders, and the
   nonvanishing of the residue are all correct.
2. Theorem 3 (T3) is labelled "unconditional" and says that (A41) alone makes the
   required concentration impossible. The concentration condition is on
   |R_rho|^2 W_{gamma,j}, not on W_{gamma,j}; the residue at a hypothetical zero is
   uncontrolled (the lane's own section 2.3 says so). The F-route holds only under
   the displayed residue bound, and the sentence "(A41) caps ... which makes it
   impossible" is false without it.

Two further claims are weakened by a missing step or a numerical scope slip
(T4 Corollary 4.2; T5 prime threshold). The remaining claims are confirmed at
the labels the lane gives them, with duplication of the record noted where the
lane already notes it.

## Falsifiers first

| Referee claim | What kills it |
|---|---|
| RC1 The residue k-factor in T1 is wrong; the correct one is prod_{p | k}(1 - 2p^{-s})^{-1} | Any split prime p and any s with Re s > 1 at which (1-x)^{-2} / [(1-2x)(1-x)^{-2}] differs from 1/(1-2x), x = p^{-s}; REF-CHECK 01-02 exhibit the identity as formal series and at p = 11, s = 2 (121/119 versus the lane's 14400/14399). |
| RC2 T3's (b) needs the residue bound; (A41) alone does not exclude the concentration | A proof that 1/|(zeta L)'(rho)| <= T^{o(1)} at every zero rho of zeta_F with Re rho > 1/2, |Im rho| <= 2T, without a zero hypothesis. None is in the record. |
| RC3 T4 Corollary 4.2 has an unwritten step | A written proof, from LH(chi_5) alone, that sup over all real t and all finite M of |A_M(t)B_M(t)| (1+|t|)^{-epsilon} is bounded; the lane cites (A45), which covers only t in [T,2T] at M = ceil(40T). |
| RC4 T5's prime-existence threshold is misquoted | (P7) is stated for x >= 8 . 10^9; a split prime in (x/2, x] by (P7) at both endpoints needs x >= 1.6 . 10^10; (P8) as written needs Y >= 10^12. REF-CHECK 05. |
| RC5 The threshold beta*(kappa) is the sup-versus-L2 reading | Failure of the identity "sup_t |Pi_rho(t)| = T_0 iff beta = beta*(kappa)" at U = T^{2-kappa}; REF-CHECK 04 verifies it at kappa in {0, 1/2, 49/50, 99/100, 1}. |

## Verdict table

| ID | Lane label | Referee verdict | Reason (short) |
|---|---|---|---|
| T1 | candidate-T | REFUTED as stated | Residue k-factor formula false (RC1); rest of the theorem confirmed. Corrected statement in section 2. |
| T1p | candidate-T | CONFIRMED | (1-2x)(1+x^2) = (1-x)^2 - 2x^3 and zero-freeness of the correction product on Re s > 1/2 (2 . 11^{-3/2}/(1 - 11^{-1/2})^2 < 1) both verified; a second local factor of the record's dictionary, as the lane says. |
| P2 | candidate-T | CONFIRMED | All four bounds re-derived; window [gamma-1, gamma+1] inside [T,2T] by the hypothesis gamma in [T+1, 2T-1]; fourth-moment and (A41) inputs quoted correctly. |
| A3 | candidate-T (finite algebra) | CONFIRMED | Exponent, threshold identity, table and beta_pole(kappa, nu) re-computed exactly; one nit: "bounded iff" needs both the window mass and the supremum to be T^{2w}, as the markdown (not the claim list) states. |
| T3 | F-route (unconditional) | WEAKENED | Valid only under the residue bound; the claim that (A41) forbids the concentration for beta above the strip is false without it (RC2). Label must read "F-route conditional on |R_rho| <= T^{delta/2}; no zero hypothesis". |
| H4 | HEURISTIC / O | CONFIRMED | Algebra of the density-exponent reading correct; the unweighted sanity argument (Prop 6 + (D) would give the density hypothesis) is a valid proof that (D) is not a theorem; the Gram/least-eigenvalue identification is an analogy, booked by the lane as a reading, not a theorem. |
| T4 | candidate-T (conditional on LH) | WEAKENED | Main theorem and the (A54) corollary confirmed (and they are a direct corollary of the record's (A62)-(A64) with (A41) replaced, which the lane should say up front). Corollary 4.2 (the Fejer target (A58)) uses a pointwise bound for A_M B_M at all heights and all M that LH(chi_5) does not supply without a Perron argument the lane does not write (RC3). |
| T5 | candidate-T (conditional, vacuous) | CONFIRMED with a scope correction | Inequality re-derived line by line; prime-existence threshold should be T^kappa >= 1.6 . 10^10 via (P7), or T^kappa >= 10^12 via (P8) as printed (RC4). The theorem is the A3 algebra restated; one reading, not a second result. |
| P6 | R | CONFIRMED | Literally (A60) = (A11)+(A21) of the record, as the lane says; exponent table exact; the "factor T" diagnosis correct, and equivalently beta*(kappa) is where sup|Pi_rho| = T_0 (RC5). |
| PL | R | CONFIRMED | Bridge row byte-identical between REGISTRY-RH-ROWS.tsv and canon/REGISTRY.tsv at canon-v86 (diff empty, checked by the referee); dependence patch section 7 respected; README section 7 wording consistent. |

## 1. What was verified and how

- The lane's verifier reruns to the declared hashes from a clean shell; every
  finite check does what its label says (read line by line). CHECK 07 tests the
  multiplicative table g_k, including g_k(p^j) = j+1 at split p | k; it does not
  test the displayed ratio G_k/G_1, which is where the error sits.
- referee_m37_strength.py (5 checks, exact): the local ratio identity; its
  evaluation at p = 11, s = 2; the nu_sigma, a_sigma, b_sigma fractions against
  (A39)-(A40); the sup-versus-L2 reading of beta*(kappa); the (P7) threshold.

## 2. T1: the residue k-factor (REFUTED as stated; corrected statement)

Lane's proof text, section 2.2(d), correctly says "the factor at p | k is
(1-x)^{-2} instead of (1-2x)(1-x)^{-2}". The quotient of these two is

    (1-x)^{-2} / [(1-2x)(1-x)^{-2}] = 1/(1-2x),

not (1-x)^2/(1-2x). Equivalently, F^{(k)} = F^{(1)} / prod_{p | k}(1 - 2p^{-s})
on Re s > 1 (drop the factors of the product), so G_k = F^{(k)} zeta L
= G_1 prod_{p | k}(1 - 2p^{-s})^{-1} on Re s > 1, and by uniqueness of
continuation on Re s > 1/2. Corrected statement to adopt:

    R_rho^{(k)} = G_k(rho) / (zeta L)'(rho),
    G_k(rho) = G_1(rho) prod_{p | k} (1 - 2 p^{-rho})^{-1},

and in section 2.3 the finite k-factor is at most prod_{p | k}(1 - 2p^{-1/2})^{-1}
and at least prod_{p | k}(1 + 2p^{-1/2})^{-1} in modulus (|1 - 2x| in
[1 - 2|x|, 1 + 2|x|], |x| <= p^{-1/2} < 1/2 at split p >= 11). All other parts of
Theorem 1 (a)-(d) are confirmed: absolute and uniform convergence on
Re s >= 1/2 + delta with the majorant 4 sum_p p^{-1-2 delta}, zero-freeness of G_k
(|1 - 2x| >= 1 - 2 . 11^{-1/2} > 0), the divisor statement, the order-m leading
coefficient m! G_k(rho)/(zeta L)^{(m)}(rho). REF-CHECK 01-02.

Counting: Theorem 1 is the record's dictionary (C-GRH-QSQRT5-SPLIT-ORIENTATION-1.md
section 5; P-O5-DEDEKIND-GRH-READ-1 PREREG sections 6-7) with the local factor
1 - 2x in place of (1-x)^2/(1+x^2); the lane says so in section 2.4. Not a new
theorem.

## 3. T3: the residue enters (WEAKENED)

Theorem 3(b) proves J_{gamma,j} <= |R_rho|^2 min(b,j)^{-2} T^{-(2-kappa)(2-2beta)}
W_{gamma,j} T_0^2 correctly. The consequence "the pole term reaches the scale only
if |R_rho|^2 W_{gamma,j} >= min(b^2,j^2) T^{2(2-kappa)(1-beta)}" is correct. The next
sentence, "(A41) caps every W_{gamma,j} at T^{2 nu_sigma + epsilon}, which makes it
impossible as soon as 2(2-kappa)(1-beta) > 2 nu_sigma", drops |R_rho|^2. Since
1/|(zeta L)'(rho)| has no unconditional upper bound at a hypothetical off-line
zero (lane section 2.3, correct), (A41) does not by itself exclude the
concentration; (a) is conditional on |R_rho| <= T^{delta/2}, and (b)'s
"impossible" is conditional on |R_rho| <= T^{o(1)}. The same omission is in the
claim-list wording "that (A41) forbids beyond exponent 2 nu_sigma, and that
LH(chi_5) forbids for every beta < 1".

Corrected statement to adopt: "Single-pole F-route, no zero hypothesis, residue
hypothesis displayed: if |R_rho| <= T^{delta/2} and beta < 1 - nu_sigma/(2-kappa) - delta,
the weighted single-pole term is below the (M37) scale by T^{-delta/2+epsilon}
(unconditional inputs (A25), (A41)). For any beta < 1 the term reaches the scale on
a unit window or shell only if |R_rho|^2 W_{gamma,j} >= min(b^2,j^2) T^{2(2-kappa)(1-beta)};
with |R_rho| <= T^{o(1)} this contradicts (A41) for beta < 1 - nu_sigma/(2-kappa) and
contradicts LH(chi_5) for every beta < 1. Without a residue bound the route is
not closed; it is undefined (lemma (i) of section 4)."

## 4. T4: the theorem holds, Corollary 4.2 has a gap (WEAKENED)

Theorem 4 re-derived: (A45) gives |A_M(t)| <= |L(1-sigma-it,chi)| + C T^{-(1-sigma)} on
[T,2T] at M = ceil(40T); chi real so |L(1-sigma-it,chi)| = |L(1-sigma+it,chi)|; LH at
u = 1-sigma and u = 2sigma gives sup_{[T,2T]}|A_M B_M| << T^{2 epsilon}; (A60) is
uniform in k; U^{1/2-sigma} <= U^{1-sigma}T^{-1/2} iff U >= T. Then ANALYTIC.md
section 9 ((A67)-(A71), all unconditional inputs) gives (A54). Confirmed.

Corollary 4.2 replaces (A41) inside the proof of (A62)-(A64). That proof needs
|A_M(t) B_M(t)| << (1+|t|)^{nu + epsilon} for every real t and every finite M
((A41) is stated with exactly that uniformity, and (A62) integrates over every
dyadic |t| ~ V, including V >> T where (A29)/(A45) no longer apply at M = 40T).
LH(chi_5) is a statement about L, not about its partial sums; the transfer to
partial sums of arbitrary length at arbitrary height (under LH, L_D(u+it,chi) <<
(1+|t|)^epsilon for fixed u > 1/2 uniformly in D, by a Perron shift to Re w = 1/2 - u + eta
with the LH bound on the shifted line) is standard but is not written in the lane
and is not in the record. Until it is written, Corollary 4.2 is candidate-T-lit at
best, and the (A58) part of the T4 claim is not certified. The (M37) and (A54)
parts stand.

Duplication: the record's (A73) already states that the entire loss above the
(M37)/(A54) scale in the separate-moment family is nu_sigma, attained at the
pointwise input. T4 is the observation that under LH that input is T^epsilon.
The lane should state T4 as a corollary of (A62)-(A64), not as a new ceiling.

## 5. T5, A3, P2, P6, PL, H4, T1p: confirmations with nits

- T5: the inequality chain (M37) + (D) + (W_w) + (Res) => the displayed bound is
  re-derived line by line (the step (2 T^{2-kappa})^{2 beta_0 - 2} >= (1/4) T^{-(2-kappa)(2-2beta_0)}
  uses 2 beta_0 - 2 >= -1). Prime existence: (P7) applied at x = T^kappa and at
  x/2 requires x/2 >= 8 . 10^9; the lane's "T^kappa >= 8 . 10^9" is off by a factor
  two, and (P8) as printed is for Y >= 10^12. Harmless for a "T large" theorem;
  the number should be corrected. The theorem is A3 restated with constants; the
  lane correctly records it as vacuous under (W).
- A3: all fractions exact (REF-CHECK 03). The claim-list wording "when the weight
  mass at the ordinate is T^{2w}" should read "when both the unit-window mass and
  the supremum of |A_M B_M|^2 on [T,2T] are T^{2w}", as section 3.4 does say.
- P2: confirmed; note the Lorentzian half-width b in (6/25, 3/4) uses
  beta in (1/2, 1) and sigma in (1/4, 13/50), consistent with the note's strip.
- P6: confirmed. A second, equivalent diagnosis of the task's threshold: with
  sup_t |Pi_rho(t)| = |R| U^b / b and T_0 = U^{1-sigma} T^{-1/2}, the two coincide
  (up to |R|/b) iff U^{beta-1} = T^{-1/2} iff beta = beta*(kappa) at U = T^{2-kappa}
  (REF-CHECK 04). The task's premise compares a supremum with an L^2 mean over an
  interval of length T; that is the lane's "weight mass T in a unit window" in
  other words.
- PL: bridge row diff empty against canon/REGISTRY.tsv at canon-v86
  (HEAD d008270c9c979f457f73087e17672b1db85ee6ad, tag canon-v86). The sandwich
  "(M32) <= (M37) <= LH(chi_5)" is a loose strength ordering ((M32) is a theorem,
  so trivially implied); acceptable in an R item.
- H4: the density-exponent algebra J << U^{2-2beta} T^{2 epsilon} is right, both
  weighted and unweighted; the unweighted sanity argument is a correct proof that
  (D) cannot be a theorem in general. The identification with the Gram/detection
  wall (ZETA-RH-STATUS-2026-09-08.md section 4; RESULT-P-RH-WEYL-CANONICAL-2.md R4)
  is an analogy at the level of "least eigenvalue of a Pick-type Gram matrix of
  clustered nodes"; the lane books no theorem for it, which is the correct
  application of RH-ONE-WALL-CROSSREF_2026-08-17.md.
- T1p: (1-2x)(1+x^2) = (1-x)^2 - 2x^3 verified; the lane does not state that the
  correction product is zero-free on Re s > 1/2 (needed for "same divisor"); it
  is, since |2x^3/(1-x)^2| <= 2 . 11^{-3/2} / (1 - 11^{-1/2})^2 < 1/8 at split primes.

## 6. Discipline audit

- RH hygiene: header block, "What this does not do" and section 6 are correct; no
  sentence states or implies progress on RH, GRH, LH, or a status change. T4's
  "(M37) is at most LH(chi_5)-strength" is a ceiling on the target, not a zero
  statement.
- Labels: T1 candidate-T fails on a finite formula that no CHECK certifies
  (violates "every finite piece exactly verified"); T3 "unconditional" overstates;
  T4 candidate-T covers a corollary with an unwritten step. Other labels are
  consistent with the discipline; HEURISTIC steps are confined to H4 and marked.
- Counting rule: invoked for section 3.6 and 4(ii) and for T1 versus the O5
  dictionary; the referee adds that T5 is A3 restated and T4 is (A62)-(A64) with a
  hypothesis substituted, i.e. the note contains two theorems' worth of new
  content (T1 corrected, T3 corrected) and several readings.
- Verifier: stdlib, int/Fraction in gated code, floats only in the DIAGNOSTIC
  block, deterministic, exit 0, one line per check, final CHECKS line; reruns
  byte-identically. No absolute paths, hostnames or secrets in the markdown.

## What this does not do

- It does not prove, disprove, evidence or approach RH, GRH(zeta_F),
  GRH(L(., chi_5)) or LH(chi_5); it does not prove (M37), (M18) or (A54); RH stays
  open; RH-PROGRAM-DEPENDENCE and LAMBDA-COCYCLE-ANGLES [H] are untouched.
- It does not supply the missing partial-sum-under-LH lemma for Corollary 4.2, a
  residue bound at a hypothetical zero, or any of lemmas (i)-(iii) of the lane's
  section 4.
- It does not move TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O], proposes no registry
  row, edits no Canon file, and is not a probe or preregistration.
- Its five finite checks certify finite identities and rational values only; the
  verdicts on all-T statements rest on the written re-derivations above.

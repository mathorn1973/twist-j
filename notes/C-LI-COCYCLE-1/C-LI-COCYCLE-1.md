# C-LI-COCYCLE-1. Continuation on the J-native uniform cocycle

```
CANDIDATE ID:   C-LI-COCYCLE-1
DATE:           2026-07-16
SESSION:        pentagon-weil-anchor-1 (directed by the owner:
                "zkus pokracovat na J nativni uniform cocycle")
TARGET ROW:     J-LI-COCYCLE-REALIZATION [O] (owner ledger name; = J-LI-ALL-N)
PARENTS:        C-WEIL-REALIZATION-1 rev3+; the owner-side J-LI-SCHOENBERG-2
                lane (Library folder, branch agent/j-li-schoenberg-2-incubation,
                unpushed); the frozen pentagon ledger and its gates
LAYER:          L5 finite exact statements plus exact real-interval gates on
                the sealed normalization; the target O is L6; no lift claimed
AUTHORITY:      none. Candidate document per the project contract.
```

## 0. What this candidate delivers

```
1. The exact finite normal form of the cocycle lane, with a hand proof:
   K = L T L^T (telescoping), t_m = psi(m+1) + psi(m-1) - 2 psi(m),
   K_jk = psi(j) + psi(k) - psi(|j-k|). Positivity transfers both ways
   (L unimodular). The owner's 1/2 normalization is an equivalent scaling.
2. The T_1 (= K_2) gate closed at candidate grade by a SECOND method and
   second code path, independent of the parallel J-LI-SCHOENBERG-2 run:
   the gate margin has the closed form
      M_1 = 4 lambda_1 - lambda_2 = 2 sigma_1 + sigma_2
          = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log(4 pi)
   and the exact interval
      M_1 in [37100438723459, 37100843555683] * 10^-18  (about 3.710e-5),
   strictly positive; det T_1 = M_1 * lambda_2 > 0.
3. A rigorous gamma_1 upgrade: second-order Euler-Maclaurin bracket,
   gamma_1 in [-72815845578467363, -72815845393082604] * 10^-18
   (width 1.9e-10), strictly negative. The amendment-1 elementary bracket
   (width 1.15e-4) could NOT have decided this gate; the margin is 3.7e-5
   and the gamma_1 coefficient in M_1 is 2. The method upgrade was
   necessary, not cosmetic.
4. The J-native finite exemplar, tied exactly to the plenum: the unitary
   U with spectrum the primitive 10th roots of unity IS the mixed 2-form
   sector of the step operator (-zeta_5^k = zeta_10^e, e in {1,3,7,9},
   machine-pinned), the cocycle b(n) = (U^n - I)(1,1,1,1) has ladder
   psi(n) = 8 - 2 c_10(n) = (0,6,10,6,10,16,...), period 10, rank 4,
   K = L T L^T exactly, all PSD minors nonnegative with 5x5 dets exactly 0.
5. The uniqueness consequence sharpening G6 (section 4), the erratum pins
   for the additive-branch wording (owner audit 3), and one first-class
   FIRED assertion with its archive and amendment (section 1).
```

## 1. Preregistration, pins, and the first-class fire

```
PREREG          PREREG_C-LI-COCYCLE-1.md
                sha256 38d42d852876ab51e24e0eb77a163e33746e731b20128ffd6f9bafe082804457
                frozen before the single run of the frozen verifier
FROZEN RUN      C-LI-COCYCLE-1_verifier.py
                sha256 db56b0b10b8f53e926facd2f9cfe95445ef1d64d2a42db6edf5ecf15c4f59850
                (12057 bytes); stdout sha256
                eeb424205400af53fe62de5187ca4eebafa56367f23689d2f9cb300295fd5b71
                (1759 bytes); 0.7 s, exit 0.
                RESULT: CO1, CO2, CO3, CO4, CO5 PASS; CO6 FAIL.
AMENDMENT 1     C-LI-COCYCLE-1_verifier_amend1.py
                sha256 8b0de9b8b2c145932ddf0c54de6b53e55eb89ca72ffe09624e2e191c38fc60b6
                (5497 bytes); stdout sha256
                43ab5fbff93786506e87adefd4bacf27440f2b8bb3d59530a353adf605693d9a
                (661 bytes); 1.5 s; CO6a, CO6b, CO3a all PASS.
ENVIRONMENT     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC; Linux x86_64, Python 3.11.15; single platform;
                two-architecture identity deferred to public validation.
```

The fire, recorded as required. Frozen CO6 asserted "lambda_1 recomputed
lies INSIDE the rev1 pinned interval". The recomputation used a single-N
gamma bracket, which produces a WIDER interval that CONTAINS the rev1
interval: recomputed [23095708961524905, 23095708987369468] against pin
[23095708964233559, 23095708972138893]. No numerical inconsistency exists;
the frozen assertion tested subset in the wrong direction. Per the
discipline the fired run is archived unmodified (pins above), the
threshold is not moved, and the amendment carries the correct invariant:
both intervals must intersect, since both contain lambda_1. With the same
two-N gamma intersection as the rev1 verifier, the recomputed interval is
in fact byte-identical to the rev1 pin (CO6b witness), and the T_1 gate
re-establishes with the tightened gamma (CO3a). The fire is a prereg
drafting error caught by the machinery, exactly what the discipline is
for; it is recorded, not hidden.

## 2. Hand proofs behind the frozen statements

Telescoping normal form. With psi even, psi(0) = 0, t_m = psi(m+1) +
psi(m-1) - 2 psi(m) = (Delta psi)(m) - (Delta psi)(m-1):

```
sum_{b=1..k} t_{a-b}  telescopes to  (Delta psi)(a-1) - (Delta psi)(a-k-1),
sum_{a=1..j} of that  telescopes to  psi(j) - psi(0) - psi(j-k) + psi(-k)
                                   = psi(j) + psi(k) - psi(j-k) = K_jk.
```

So K = L T L^T exactly, with L the lower-triangular ones, det L = 1;
K PSD iff T PSD (Sylvester). Cross-witness: the leading principal minors
of K and T coincide, as unimodular lower-triangular congruence forces.

EM-2 bracket for gamma_1. With f(x) = ln x / x, A_N = sum_{k<=N} f(k)
- ln^2(N)/2 and the harmonic-case shape check (f = 1/x reproduces the
classical gamma bracket):

```
gamma_1 = A_N - f(N)/2 - f'(N)/12 + R,   |R| <= (1/12) int_N^inf |f''|
        = (ln N - 1)/(12 N^2)   (f'' one-signed for x >= 5),
so gamma_1 in [A_N - f(N)/2, A_N - f(N)/2 + 2B], B = (ln N - 1)/(12 N^2).
```

Margin closed form. t_0 = 2 lambda_1, t_1 = lambda_2 - 2 lambda_1 =
-sigma_2; T_1 PSD iff t_0 >= |t_1| iff M_1 = t_0 - t_1 >= 0 and
t_0 + t_1 = lambda_2 >= 0; M_1 = 2 sigma_1 + sigma_2 gives the boxed
constant combination (CO1, exact vector algebra).

Exemplar correspondence. -zeta_5^k = zeta_10^(2k+5 mod 10); the exponents
{7, 9, 1, 3} are exactly the primitive residues mod 10, so the mixed
2-form eigenvalues of M_J (pinned in the rev1 verifier, A4/A5) are the
exemplar's unitary spectrum. The ladder is psi(n) = sum over primitive
10th roots of |z^n - 1|^2 = 8 - 2 c_10(n), a Ramanujan-sum ladder.

## 3. Results (witnesses from the pinned stdouts)

```
gamma_1   in [-0.072815845578467363, -0.072815845393082604]   width 1.9e-10
M_1       in [ 0.000037100438723459,  0.000037100843555683]   > 0
lambda_2  in [ 0.092345735029189221,  0.092345735434021445]   width 4.0e-10
det T_1   in [ 0.000003426066204530,  0.000003426110745058]   > 0
exemplar  psi = (0,6,10,6,10,16,10,6,10,6,0), period 10;
          t = (12,-2,-8,8,2); minors of K and of T both (12,140,800,2000,0)
erratum   b(1)=4 vs a_K(1)=1; b(5)=0 vs 1; b(6)=4 vs 0; within the ordered
          unramified prime-power list the first distinguishing witness is
          exactly 16, agreement at 11
```

The T_1 gate margin is a razor: pi^2/8 = 1.2337005... misses
3 + gamma + gamma^2 + 2 gamma_1 - log(4 pi) by 3.71e-5. An absolute error
of 1.9e-5 in gamma_1 would erase the gate; the EM-2 bracket is five
orders inside. This margin value is, to this session's knowledge, the
first exact interval pin of the quantity 2 sigma_1 + sigma_2 in the
program.

## 4. The uniqueness consequence, sharpening G6

Under RH the ladder has the pure Levy form lambda_n = int (2 - 2 cos n
theta) d mu(theta) with mu the angular zero measure (theta_rho = arg(1 -
1/rho)), and the Levy-Khintchine triple of a conditionally negative
definite sequence is UNIQUE (imported T). Consequence, stated plainly:

```
Any J-native cocycle whose ladder equals lambda_n for all n necessarily
constructs the angular measure of the zeta zeros. There is no way to
"fit around" the zeros; the realization target IS a J-native construction
of that measure. Admissible routes are therefore only those where a trace
formula FORCES the spectral measure (G3/G4 exactness), never parameter
fitting.
F-guard COCYCLE-BY-FINITE-FIT: a construction tuned to match finitely
many lambda_n is definitionally not a realization (already frozen: no
finite prefix is progress); by uniqueness it also cannot be "almost
right", since the full ladder pins the measure exactly.
```

The exemplar shows both sides: it is a genuine J-native cocycle (the
plenum's own 2-form torsion sector), its ladder is exactly Schoenberg,
and it is periodic (psi(10) = 0), so it can never host lambda (label D:
the finite model of the wall, per the owner's J-PHI10-SCHOENBERG-EXEMPLAR
grading). The uniform target needs an infinite J-object. Route map with
first falsifiers, carried from the recon and now quantitative:

```
R1  the time-driven stream Prod M_{t_n} (Thue-Morse):    first gate: its
    ladder must hit lambda_1's interval, then M_1's.        [H]
R2  the lambda-adic boundary at p = 5 plus archimedean:  same gates. [H]
R3  transfer operators of the phi-continued-fraction map: same gates. [H]
```

## 5. Next named gates

```
J-LI-LAMBDA-3 / T_2:  needs sigma_3. The sigma_3 formula in terms of
    gamma, gamma_1, gamma_2, zeta(3) must be DERIVED and frozen first;
    this session refuses to freeze a recalled formula unverified. The
    machinery extensions are ready: gamma_2 by the same EM-2 bracket on
    f(x) = ln^2 x / x; zeta(3) by elementary integral brackets.
T_N ladder:  each further N adds one named finite gate on the xi side and
    one falsifier for any proposed realization.
```

## 6. Break attempts

```
BR1  method-necessity: the elementary gamma_1 bracket (width 1.15e-4)
     cannot decide the 3.7e-5 margin; only the EM-2 upgrade can. Checked
     by comparing widths; guards against false confidence from the weaker
     method.
BR2  overreading CO4: K = L T L^T is an identity for ANY ladder
     (telescoping), so it is a structure check only; positivity lives in
     the minors. Stated to prevent the normal form itself being sold as
     evidence.
BR3  congruence witness: minors of K and T coincide exactly, as they
     must; a mismatch would have exposed an arithmetic slip.
BR4  the CO6 fire: the frozen run itself caught a wrongly oriented
     assertion; archived, amended, threshold unmoved. Process control
     demonstrated live.
BR5  razor sensitivity: shifting gamma_1 down by 2e-5 flips the M_1 gate
     sign (arithmetic on the closed form); the pinned bracket sits five
     orders inside. The gate is genuinely sharp, not slack.
```

## 7. Live falsifiers

```
F-a  any exact assertion of the amended chain failing on re-run
F-b  a correct evaluation placing M_1 outside [3.7100e-5, 3.7101e-5]
     (fires on the machinery or the imported sigma_2 identity first,
     per the negative-vector discipline)
F-c  for any proposed realization (R1-R3): its ladder missing lambda_1's
     interval, then M_1's; first miss kills the construction, not RH
F-d  the exemplar falsifiers: any n with psi(n) != 8 - 2 c_10(n), any
     negative minor, rank != 4
```

## 8. Non-claims

The T_1 gate PASS is a necessary-condition calibration on the xi side,
G3/G4 grade, exactly like lambda_n >= 0 prefixes: zero evidence for RH by
itself. The exemplar is a model, not the wall. The uniqueness consequence
is imported classical mathematics applied to the program's target; it
narrows the admissible routes, it does not walk them. J-LI-COCYCLE-
REALIZATION stays [O]. RH stays [O].

## 9. Promotion posture

The T_1 gate is now closed by two independent methods and code paths
(the owner-side J-LI-SCHOENBERG-2 run and this candidate). When the owner
pushes agent/j-li-schoenberg-2-incubation, the two verifiers should be
cross-run (each environment runs both) and the public probe assembled
with a NEW PREREG and NEW pins before the first public run, per the
owner's rule: no retroactive formalization of historical runs. This
candidate's contribution to that fold: the closed-form margin
M_1 = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log(4 pi), the EM-2
gamma_1 bracket, the exemplar's exact plenum tie, and the uniqueness
framing of G6. Nothing public was changed by this session.

## 10. Amendment 2: the carrier no-go, cross-lane (2026-07-16)

The owner's staging branch (a62b040) delivered J-LI-CYCLIC-CARRIER-
DIMENSION: for every finite-spectral pair (U, v), the cycle cocycle obeys
||sum_{k<n} U^k v||^2 = a_* n^2 + O(1); a Li realization implies RH, then
Lagarias's asymptotic makes lambda_n unbounded and o(n^2); finite carriers
are excluded and the realization measure must have infinite support,
1 in supp(mu_v), mu_v({1}) = 0. This lane re-derived the theorem
independently (Dirichlet-kernel split; the contradiction kills the
assumption on every branch, so the exclusion is unconditional) and pinned
it machine-exactly on two instances, plus the atom-test dictionary:
mu_v({1}) = lim 2 (lambda_{N+1} - lambda_N)/(2N+1) (telescoping exact,
Wiener imported), so the no-atom condition is equivalent to ladder
increments o(N). The owner verdict is archived (sha256 37864aae...f21f,
project copy claude/OWNER_VERDICT_4_C-LI-COCYCLE-1_2026-07-16.md); the
full lane state lives in
claude/LI-COCYCLE-LANE_CONSOLIDATION_2026-07-16.md.

```
verifier        C-LI-COCYCLE-1_verifier_amend2.py
file sha256     070e9f3d981fe37cbce8f683ea7a4d5c3f1988db9a88e32918d8b2a401304def
                (6603 bytes, pinned before its single run; 5/5 PASS first run)
stdout sha256   42be432bdf279fe990220e28d56dbf70b0db468f34c683c21d62942bb3772bb9
CC1  exemplar cycle ladder (0,4,10,14,20,24,20,14,10,4,0), period 10,
     zeros at 10m, max 24, a_* = 0: the finite J-native carrier is bounded
CC2  C_4 atom instance: g(n) = n^2 + (0,3,4,3), g(4m) = 16 m^2, a_* = 1
CC3  telescoping dictionary on two ladders, exact; the Wiener atom test
CC4  1_G vs chi_0^(5) (owner audit 1678d7b) pinned coefficientwise
CC5  the dichotomy summary: bounded against n^2 + O(1)
```

Consequences folded into this candidate: F-guard COCYCLE-BY-FINITE-FIT is
upgraded to a theorem-backed row; routes R1-R3 gain the cheap increment
kill test (a proposed realization must show increments growing like
(1/2) log N; bounded or quadratic ladders die immediately); the exemplar's
role as model-not-target is now a theorem, not a caution.

## 11. Amendment 3: sigma_3 derived, lambda_3 / T_2 witnesses (2026-07-16)

Recorded here for completeness; the pins were previously documented only in
the root consolidation map (REV2 addendum). The sigma_3 formula is DERIVED
by the xi(1+t) expansion (exact vector algebra; the t^1 and t^2 rows
reproduce the imported sigma_1 and sigma_2 identities, validating the
route), confirming the owner's frozen formula independently:

```
sigma_3 = 1 + gamma^3 + 3 gamma gamma_1 + (3/2) gamma_2 - (7/8) zeta(3)

verifier        C-LI-COCYCLE-1_verifier_amend3.py
file sha256     5d6ab0d0a7442e47fb742b1a3dfddcf4cfc9bbdc0827d4b36543f65dea7ae725
                (8963 bytes, pinned before its single run; 5/5 PASS first run)
stdout sha256   dc5eb44a463c3546e52ecc8bfccb049d87c1ec236e5b0ba9229cac03acf945d0
                (1321 bytes)
S1a-S1c  sigma_1, sigma_2 reproduced; sigma_3 derived, exact
S2       lambda_3 = 3 sigma_1 - 3 sigma_2 + sigma_3, exact binomial
S3       instance normalization: t_m = 2 * cosine moments of mu_v on both
         finite instances (see amendment 4 for the corrected general form)
S4       float witnesses: lambda_3 inside the owner's pinned interval;
         det T_2 printed against the owner's det K_3 interval -- MIS-SCALED,
         see the erratum in amendment 4
```

## 12. Amendment 4: det-scale erratum and measure symmetrization (2026-07-16)

Two errata against amendment 3, both machine-pinned; the amend3 artifacts
stay archived unmodified per the discipline.

ERR-A (scale). The amend3 S4 witness compared det T_2 itself against the
owner's interval for det K_3 and printed `contains float: False`. The
owner's K carries the 1/2 normalization, K_3 = T_2 / 2 entrywise, so
det K_3 = det T_2 / 8 (in general det K_N = 2^-N det T_{N-1}). With the
corrected scale the witness reads `contains float: True`:
det K_3 = 7.1975411709e-14 inside [6.9813247888e-14, 7.3758515923e-14].
The lambda_3 / T_2 gate status is unchanged (owner-side one-architecture
candidate-C); only the printed witness line was mis-scaled by 2^3.

ERR-B (symmetrization). Amend3 S3 concluded "hence sigma = 2 mu_v". The
correct general normalization, aligned with the corrected spine
(notes/j-li-schoenberg-2 consolidation, section 4):

```
sigma = mu_v + iota_* mu_v,  iota(z) = conj(z);
mu_v(T) = lambda_1,  sigma(T) = 2 lambda_1,  sigma_hat(m) = t_m;
mu_v({1}) = lim (lambda_{N+1} - lambda_N)/(2N+1),  sigma({1}) = 2 mu_v({1}).
```

sigma = 2 mu_v holds exactly iff mu_v is conjugation-invariant, which is
true on both real finite instances of S3 (machine-pinned as A3) but is not
forced in general: the cosine data t_m determines sigma only, never the
non-symmetric mu_v (A2 pins the separating instance mu_v = delta_i, exact
in Z[i]). The same erratum scopes the amendment-2 wording "mu_v({1}) =
lim 2 (lambda_{N+1} - lambda_N)/(2N+1)": the factor-2 limit is the SIGMA
atom; the mu_v atom carries no factor 2 (A4 pins both on the C_4 instance).

```
verifier        C-LI-COCYCLE-1_verifier_amend4.py
file sha256     351f3dae41df9dabf2230466b792d27e9045e81dfef4dbab37326cfda954e8e4
                (10910 bytes, pinned before its single run; 4/4 PASS first run)
stdout sha256   37c01ea5f79a52f7b5dcfcec2c7bd99b3a61d418af31b76f73b478b83259b876
                (1483 bytes); exit 0, empty stderr
A1  det K_3 = det T_2 / 8 exactly on both amend3 instances (400 -> 50,
    512 -> 64): the S4 comparison was mis-scaled by exactly 2^3
A2  the separating instance mu_v = delta_i: same cosine data, different
    measures; sigma = mu_v + iota_* mu_v pinned, sigma != 2 mu_v there
A3  both amend3 instances conjugation-invariant (moments exactly real):
    the instance-level S3 statement stays true; only its generality fell
A4  atom normalization on C_4: Delta g/(2N+1) -> 1 = mu_v({1}); factor 2
    belongs to sigma({1})
A5  float witnesses re-printed at the corrected scale: lambda_3 True,
    det K_3 True
ENVIRONMENT     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC; Linux x86_64, Python 3.11.15; single platform
```

Public-topology note (supersedes the provenance lines above where they
conflict): `agent/j-li-cross-branch-staging` is public at fc4d6016
("Publish J-LI cross-branch consolidation") and this candidate's content is
public on `c-li-cocycle-1-incubation` (content consolidation ac62cac; the
local commit aee7a376 and its parentage were not preserved, by design).
Cross-running of the two lanes' verifiers, anticipated in section 9, is
therefore unblocked.

## Appendix A. Frozen run stdout (pin eeb424205400af53fe62de5187ca4eebafa56367f23689d2f9cb300295fd5b71)

```
PASS CO1 dictionary algebra: t0 = 2 lambda_1, t1 = -sigma_2, t0+t1 = lambda_2, M1 = t0-t1 = 2 sigma_1 + sigma_2 = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log(4pi), exact
PASS CO2 gamma_1 by EM-2 bracket at N = 10^5: strictly negative, width < 1e-9, inside the amendment-1 elementary bracket (two independent bracket methods agree)
CO2 witness gamma_1 in [-72815845578467363, -72815845393082604] * 10^-18 (reference -0.0728158454836767)
PASS CO3 T_1 gate: M1 > 0 (and < 1e-4), lambda_2 > 0 (width < 1e-8), det T_1 = M1 * lambda_2 > 0, all exact intervals
CO3 witness M1       in [37100427052239, 37100909182139] * 10^-18 (about 3.7e-5)
CO3 witness lambda_2 in [92345734988606606, 92345735470736506] * 10^-18 (reference 0.09234573522804...)
CO3 witness det T_1  in [3426066204530, 3426110745058] * 10^-18
PASS CO4 J-native exemplar: -zeta_5^k are exactly the primitive 10th roots (exponents 1,3,7,9); cocycle ladder psi(n) = 8 - 2 c_10(n) = (0,6,10,6,10,16,...), period 10; t = (12,-2,-8,8,2); K = L T L^T exactly; K and T PSD with rank exactly 4 (dets 5x5 = 0)
CO4 witness minors K: [12, 140, 800, 2000, 0] ; minors T: [12, 140, 800, 2000, 0]
PASS CO5 erratum pinned: additive branch b(n) = 4*[n=1 mod 5] diverges from a_K already at n = 1 (4 vs 1), at n = 5 (0 vs 1), at n = 6 (4 vs 0); within the ordered unramified prime-power list the first distinguishing witness is exactly 16, with agreement at 11
FAIL CO6 chain regression: lambda_1 recomputed lies inside the rev1 pinned interval [23095708964233559, 23095708972138893] * 10^-18
CO6 witness lambda_1 in [23095708961524905, 23095708987369468] * 10^-18
FAILED: CO6 chain regression: lambda_1 recomputed lies inside the rev1 pinned interval [23095708964233559, 23095708972138893] * 10^-18
VERDICT: FAIL
```

## Appendix B. Amendment 1 stdout (pin 43ab5fbff93786506e87adefd4bacf27440f2b8bb3d59530a353adf605693d9a)

```
PASS CO6a gamma brackets at N = 1e5 and 2e5 overlap; intersection taken (same construction as the rev1 pinned verifier)
PASS CO6b corrected invariant: the recomputed lambda_1 interval and the rev1 pinned interval have nonempty intersection (both contain lambda_1)
CO6b witness lambda_1 recomputed in [23095708964233559, 23095708972138893]; rev1 pin [23095708964233559, 23095708972138893] * 10^-18
PASS CO3a T_1 gate re-established with the tightened gamma: M1 > 0, lambda_2 > 0, det T_1 > 0
CO3a witness M1 in [37100438723459, 37100843555683]; lambda_2 in [92345735029189221, 92345735434021445] * 10^-18
FAILED: none
VERDICT: PASS amendment 1 of C-LI-COCYCLE-1
```

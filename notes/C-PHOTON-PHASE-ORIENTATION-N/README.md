# Sector-filtered finite-volume contrast at the fixed weight t = 1

- **Working item:** C-PHOTON-PHASE-ORIENTATION-N, with follow-up
  C-PHOTON-CONTRAST-DRIFT-N.
- **Related:** P1 of the limit handoff (#1141, #1142), #1108, #1112, #1122,
  #1116, #1125, C-PHOTON-BCHI-DIRECT-BOUND-N (#1143), #757.
- **Author:** A. M. Thorn, drafted with an AI agent session.
- **Publication owner:** Codex-review-publication-pr2-20260923, issue #1146.
- **Date of supplied results:** 22 September 2026.
- **Status:** PUBLIC, NON-CANONICAL; no authority; candidate-C engineering
  orientation. Floating-point categorical draws, local heat-bath, finite L,
  sector conditioning. No exact-arithmetic or phase claim.
  PHOTON-MASSLESS-PHASE stays O.

Basis: Public Canon v91, `main = canon-v91 = 11b66d4`, `canon/SHA256SUMS`
5 of 5 OK at the publication review.

## Current interpretation after review

This corrected README governs the interpretation of this note. Archived
preregistrations, results, code and numerical transcripts retain their
original bytes. Their labels `b_L` and `25 chi_L` denote the diagnostics
below, not established coefficients of the unconditioned P1 measure. Their
mass language is conditional on a finite-volume fitting ansatz. The earlier
hypothesis proposal is not adopted. No P1, P2, S7 or Canon obligation closes.

**Drift reproduction: REPRODUCTION_BITWISE, checked 23 September 2026.**
The completed replacement x86_64 run was recovered from persistent storage.
All 20 raw-log hashes and END states match the published aarch64 records;
the unchanged analysis was rerun and reproduced all 1056 output bytes with
exit 0 and empty stderr. See the dated
[reproduction record](drift/REPRODUCTION-X86_64-20260923.md) for source
identity, custody checks and limits. This is recovery and reanalysis of a
known-result run, not a new simulation or blind confirmation. The historical
PENDING result is preserved. A successful repository check alone does not
reproduce these note-only simulations.

The supplied custody account says each preregistration was hashed before its
first execution in a non-public incubation record. Their bytes and hashes
are preserved below. None is a public probe or public pin. The quantity
reserved by #1116 has been seen: any prospective public #1116 run must carry
known-result disclosure.

## 1. Results and their scope

```text
v1   controls Z_30, ratio rule          ENGINE_CALIBRATION FAIL  (falsifier fired)
v2   absolute fit, sector conditioning  ENGINE_CALIBRATION FAIL  (falsifier fired)
v3   odd-N controls Z_13                ENGINE_CALIBRATION PASS
B3   fixed weight, L = 8 to 24          COULOMB_ORIENTATION
DR   drift follow-up, L = 24 and 32     NO_DRIFT; REPRODUCTION_BITWISE
```

B3's supplied record reports byte-identical logs on two architectures; its
full raw-data comparison was not replayed in this review. The recovered
x86_64 drift logs now match the published aarch64 manifest and END list,
and their analysis was replayed successfully. The terminals retain their
frozen engineering meaning; they are not mathematical Coulomb-phase or
zero-drift conclusions.

At `t = 1`, the supplied sector-filtered samples give contrasts of about
0.60 over the measured sizes `L = 8` to `L = 32`. Their by-products
`b_diag` and `c_diag` are about 0.600 and between about -0.002 and 0.02.
These are diagnostics, not bounds for P1. The archived scale near 0.04
lattice units belongs to an assumed fit model, not to a proved spectral
photon-mass bound. All decimals below are reported computed witnesses.

## 2. Observables, sampling law and the contact identity

Intended equilibrium link measure: `K_L = (Z/LZ)^4`,
`A in C^1(K_L; Z5)`, `f = dA mod 5`,
`mu_L ~ prod_p W(f_p)`, `W = (4, phi^2, phi^-2, phi^-2, phi^2)`.
This is the weight `W(f) = 2 + zeta_5^f + zeta_5^-f` of #1112 in its link
form. Score `X(f) = tan(pi f/5)`. For
`q = (2 pi m/L) e_mu`, `m in {1, 2}`, the measured Fourier quadratic
observables are

$$
A_L(m)=\frac{1}{12}\sum_{\mu}\sum_{I\ni\mu}\frac{1}{L^4}
\Big|\sum_x X_I(x)e^{-iq\cdot x}\Big|^2,\qquad
B_L(m)=\frac{1}{12}\sum_{\mu}\sum_{I\not\ni\mu}\frac{1}{L^4}
\Big|\sum_x X_I(x)e^{-iq\cdot x}\Big|^2,
$$

with contrast `A_L(m)-B_L(m)` and `s = 4 sin^2(pi m/L)`.

For the unconditioned equilibrium link and surface laws to which the
cited contact identity applies, `C_X + C_n = d I` identifies the relevant
surface coefficients with `d-B` and `d-A`. The data here instead come from
finite, sector-filtered local heat-bath trajectories, with observed sector
trapping. No quantitative theorem identifies their sampling law with the
prescribed unconditioned finite-volume law or controls the conditioning
correction in the ordered limit.

Write `A_est` and `B_est` for the sample estimates. Define diagnostics

$$
d_{\rm diag}=\frac{1+\widehat{X^2}}2,\qquad
b_{\rm diag}=d_{\rm diag}-B_{\rm est},\qquad
c_{\rm diag}=d_{\rm diag}-A_{\rm est},\qquad
\Delta_{\rm est}=b_{\rm diag}-c_{\rm diag}.
$$

The last equality is algebraic. Archived transcript labels `b_L` and
`25 chi_L` refer to these diagnostics, reported without decision weight.
They are not independently established estimates or bounds for the
unconditioned P1 coefficients. This note supplies neither a lower bound for
`b_*` nor an upper bound for `chi_*`.

For each of six plane orientations, `Fbar_a` averages integer flux over the
`L^2` parallel coordinate planes. A measurement is TRIVIAL iff
`max_a |Fbar_a| < 3/4`. Only TRIVIAL measurements enter, and a chain qualifies
iff at least 1/4 of its measurements are TRIVIAL. Complete sample survival
under this filter does not establish its equilibrium probability. Nor would
a small excluded probability alone control the limit without a uniform
bound for the volume-dependent Fourier quadratic observables.

## 3. Frozen fitting rule and calibration

The rule frozen in v2 and unchanged in v3 uses the explicitly assumed
finite-volume ansatz `Delta = Z s/(s + M)` on eight points:
`L in {8,12,16,24}`, `m in {1,2}`, with `thr = sin^2(pi/24)`.

- (a) MASSIVE if `|Delta_L(1)| <= 3 SE` at `L = 16` and `L = 24`.
- (b) COULOMB if `Z - 3 SE(Z) > 0` and `M + 2 SE(M) < thr`.
- (c) MASSIVE if `M - 2 SE(M) > thr`.
- (d) UNRESOLVED otherwise.

Gates require complete logs, stationarity of halves, at least one qualifying
cold chain at every L, and hot/cold agreement where a hot chain qualifies.
The reported `M` and its resolution are parameters of this ansatz, not a
spectral photon-mass bound. A smaller unresolved scale is not excluded.
Neither this fit nor the `q_min` sequence replaces the ordered limit or S7.

The failed calibrations remain visible because they delimit the rule:

- v1 used `Z_30` controls. The ratio rule was undefined for contrast already
  compatible with zero, and hot starts froze in flux sectors. Part B was VOID.
- v2 used the absolute fit and sector conditioning with `Z_12` controls.
  The principal lift maps `f=N/2` to `+N/2`, so the even-N confined control
  acquired a nonzero mean flux and never reached the classifier. Part B did
  not run.
- v3 changed the controls to odd `Z_13`, whose lift is symmetric. Its engine,
  rule and fixed-weight job list matched v2. The supplied calibration passed:
  C1 and C4 COULOMB, C2 MASSIVE; the allowed C3 STOP and C5 UNRESOLVED remain
  in [v3/RESULT-A3.md](v3/RESULT-A3.md).

## 4. Fixed weight B3 and the drift follow-up

B3 used two cold and two hot chains per size, with `2000 L^2/64`
thermalization sweeps and 4000 measurements separated by two sweeps.
The following table retains the reported values but uses diagnostic names:

```text
L    Delta_est(1)      Delta_est(2)      b_diag   c_diag
8    0.5998 +- 0.0027  0.6026 +- 0.0021  0.6006   0.0008 +- 0.0027
12   0.6024 +- 0.0056  0.6042 +- 0.0036  0.6005  -0.0018 +- 0.0056
16   0.5898 +- 0.0065  0.6031 +- 0.0026  0.6000   0.0102 +- 0.0066
24   0.5801 +- 0.011   0.6003 +- 0.0059  0.6005   0.0204 +- 0.011
fit  Z = 0.6043 +- 0.0016, M = 0.0027 +- 0.0011, thr = 0.0170
TERMINAL COULOMB_ORIENTATION
```

The supplied B3 record reports 16/16 byte-identical logs on x86_64 and
aarch64, an exact-heat-bath pilot cross-check at L8 (`logw` z = 0.73), and
four valid second-analysis variants returning COULOMB. That second analysis
was written after the result was known; it is not blind confirmation.
The raw logs are absent here, so none of these long-chain comparisons was
independently replayed for publication. The fitted M was positive at about
2.4 SE; its interpretation remains conditional on the fit ansatz.

The drift follow-up used 12 new cold chains at L24 and 8 at L32.
Its frozen reference was `P_ref = 0.602177`, with SE 0.0029 treated as fully
correlated. DRIFT_CONFIRMED required z > 3 at both sizes for
`P_ref - Delta_est(1)`. The supplied completed aarch64 analysis reports:

```text
L    new chains  Delta_est(1)      z      b_diag   c_diag
24   12          0.5962 +- 0.0040  1.21   0.6005   0.0043 +- 0.0040
32    8          0.6001 +- 0.0071  0.27   0.6005   0.0004 +- 0.0071
refit, B3 plus new points: Z = 0.6031 +- 0.0012, M = 0.0006 +- 0.0004
TERMINAL NO_DRIFT; x86_64 reproduction REPRODUCTION_BITWISE
```

`NO_DRIFT` means the specified drift was not detected at the stated
resolution. It proves neither zero drift nor a massless phase. The new L24
value differs from the B3 two-cold-chain value by 1.4 combined SE, compatible
with a sampling fluctuation. Under the B3 fit ansatz the predictions were
0.581 and 0.565. The new estimates lie 3.7 and 5.0 SE above those predictions
(post hoc, no decision weight). The new `c_diag` values are lower than the B3
value at L24; this remains a diagnostic comparison only.

## 5. What this supplies to P1

**Status: candidate-C, NON-CANONICAL; P1 open.** The data suggest an order-one
contrast along the sampled `q_min` sequence, subject to finite sampling,
conditioning and possible metastability. This can guide analytical work but
supplies no full-measure P1 bound.

For C-PHOTON-BCHI-DIRECT-BOUND-N (#1143), a proof need not recover the value
near 0.60. Any evaluated uniform inequality

$$
b_{\rm lower}-25\chi_{\rm upper}>0
$$

in the prescribed full-measure joint ordered-limit framework is sufficient
for this P1 step. Identifying the sampled diagnostics with that framework is
an additional obligation. The `q_min` path is not the ordered S7 limit
(#1125 closure audit). S1, P2 and S7 remain separate obligations.

Five of six hot starts at `L >= 12` froze into nontrivial flux sectors under
this local heat-bath in the supplied record. Their plane-averaged flux had
magnitude about 0.93 in one or three orientations over 8000 measurement
sweeps. This flags a sampling issue for #757, not an equilibrium sector-weight
result. The production engine's additional moves are not tested here.

## 6. No hypothesis adoption

The earlier proposed `PHOTON-T1-CONTRAST-ORIENTATION` H row is not adopted.
Its assertion concerned the already measured `L = 8..32` domain, while its
falsifier mostly concerned later, larger volumes. Failure outside the stated
domain does not falsify that historical finite-domain statement.

A prospective hypothesis requires a matching future domain for claim and
falsifier, a quantitative plateau or comparison definition, a frozen
uncertainty rule, the declared sampling law and known-result disclosure.
Relabeling this orientation supplies none of those. No registry row is
proposed here.

## 7. Reproduction and custody

[REPRODUCTION.md](REPRODUCTION.md) distinguishes the supplied records from
what a new replay must establish. Raw logs are not committed; their absence
cannot be bypassed by changing suffixes. The B3 and drift manifests identify
expected bytes but cannot replace them. The supplied records state that
v2 part A and v3 part A3 raw logs were lost in a host reboot; the frozen job
lists permit regeneration.

The published source files keep their original hashes. Run material belongs
outside the repository. The original summaries are retained to expose the
failed calibrations, conditioning, fit assumptions and pending reproduction;
the current interpretation is the corrected text above.

Python 3.12 changed built-in `sum()` over floats to compensated summation.
The archived B3 record reports last-digit differences in block tables between
Python 3.10 and 3.12, while rounded decision output matched. Reproduction
records must name the actual Python version and distinguish log identity,
analysis identity and terminal agreement.

## Files

```text
v1/PREREG-PART-A.md             0968b601ba3508f1cbc1ee321c46c3d75dcd2661ea7a60f925b8f7eb99e2f3b1
v1/PREREG-PART-B-VOID.md        ae586535e7fbbd1fa71236dc48897e97784df5ef89486c36759786cd23fa68d1
v1/RESULT-PART-A.md             d075d591d3d07cc03aba462d352b8de9485e05f970e445d5a29110130fa4645c
v1/CALIBRATION_STDOUT.txt       d518e1e7126563152000925cc13111f1336cceaa4556006aa80f32d3bc2c018e
v1/zlgt.c                       c019ca1e866ba6d31432b87cd091483bfd515323cf1a5996fdb5fb5a43c0021e
v1/run_controls.py              2c4f034beeaeb16f865e2a32bfd3ce2f40ed48e96533d4084ad70781c0198029
v2/PREREG-PART-A.md             950aaac24b475e954b4e13572af8a07647c5104d500c8d2d94613ce61fd50440
v2/PREREG-PART-B.md             9e92fb8e5fb090a78ee253eaa57dfca9ba617b730016493b646d4d2407c86e3b
v2/RESULT-PART-A.md             9e80c0124fd3de40a578a1e505d589e4863d94d511e081bb76de3bcaf5a434b6
v2/jobs_v2.py                   58e707108e96a3c4f85eea2aceda0dcfd5d309b0228b6a796dea34de1b230d94
v2/analyze_v2.py                2734fcea962aea3cf76c39383e89c09e5b40fb5f8d3aff5422621ad9bed4bb96
v3/PREREG.md                    b4799904e59fa870fc81aabcaf8a13efdc685ba2962cf3f6ec44b10cbb1bce29
v3/RESULT-A3.md                 32cb3bf39bb059e1cceb6b35630023437c3d87a21247e5af435c9614d920434a
v3/RESULT-B3.md                 645222712652dd06498b76f2ca62d0c09eab5347773bd436e41461691869ddbf
v3/ANALYSIS_A3.txt              99473994f5116fa543627f8e4c50b56b9ca4a1b2817afca047200fb82f8e5794
v3/ANALYSIS_B3.txt              5d870f10b66ef8c196be5881a0f76251ccab71ce5e770a08d1c2a9ecaa1dce3a
v3/LOGS_B3.sha256               ca004f0ce0d663419bf642af0d4bd1ac4f3187b830cd13866500b5684fa2c761
v3/SECOND_READING_B3.txt        df7717be0a7c6d36b8bc40f78a8b0dc4f5d9878b2ba736991b6e5756e326d81b
v3/break_check_b3_pilot.py      536017b3e8cf1e0f1600c01d73e0a64a61de211e390632faa761662aee284664
v3/break_check_b3_reanalysis.py 3f90ea01271f6c468ac229bd4fc1aac9c58921c52903d6b96590545d03570079
v3/CROSSCHECK_PILOT_SIDE.txt    c1ebd508a4f88bf491ca6033290ac69200c4e79e33f3a249fd3eefffc0b2699a
v3/CROSSCHECK_B3_SIDE.txt       bbd9fd7eda403cd05e2a534a8ca2d34c6ac4a0bc7d12daeb36f7409f2a94100d
v3/CROSSCHECK_COMPARE.txt       f0a52d7d4b4ca96d505a9c5ee4f0234710e91641e1b23e42eb6dfdf0308c79e3
drift/PREREG.md                 3a86ca2f0e771ffbeacd77004443953697cf03369f5e853630766c29489ffa62
drift/ADDENDUM-1.md             a7bc7dabc49454bce9d44252c54c83c6446cdde539e7ebdd1dade20d2d6aa228
drift/ADDENDUM-2.md             b461499eb87f1705eb55739737499358886908bc0f94185d8a22ef4f4f7ac007
drift/RESULT.md                 89ac75cdc745e0ba82c200299a4ba7675ac3ebf828a648f7273ea762134ae1d7
drift/ANALYSIS_AARCH64.txt      0ede6cdce7a37703ac0952759e9055376de4fe633d2cb6b05bfaae984f69e936
drift/LOGS_AARCH64.sha256       8fd4807378a65043266459fc56af8a6f4faba5f9ef52602a84ceeed71721bb96
drift/ENDS_AARCH64.txt          780bb01732e670a21b452f3e69dfc6d71be7c869636221a41a8fcf68abb87e62
drift/jobs_drift.py             7708c43e36d00e4daad2171b192d34adb5a8782c33fd27cb10495535f5e144b4
drift/analyze_drift.py          e5a022a5bef7624936216d86a9460471df70dd23d7eb2a84bd84ff7a321acfae
code/zlgt2.c                    62be81dc972596f10ff29636888b8b923c56c1c5c393627a24fba8cc1ab6d27c
code/jobs_v3.py                 3a9b280b3b1f0fb4e46a0baeaac7d5b096645791a0ff328b88b94c8b6f485f04
code/analyze_v3.py              8460818640313e30e3b3fde985222dc7f6ecc9f1abe0a870df39fc35e9dae377
```

`code/zlgt2.c` is the engine of both v2 and v3. The RESULT files carry short
custody notes that were appended after the verdicts.

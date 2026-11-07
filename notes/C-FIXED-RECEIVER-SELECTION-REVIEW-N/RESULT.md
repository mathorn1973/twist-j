# Result of the independent review of the #1930 receiver continuation

**NON-CANONICAL / L1.** Target: PR #1930, head
3d8d364cb981bb5d53bbede432fb5a4ac4181709,
`notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N`. Review lock: #1935.

## Verdict

No mathematical error was found in the target, and no frozen check fired.
All seven scopes are mathematically sound at their declared scope. Each
needs stated corrections before a Canon text uses it.

| Scope | Verdict | Required before a Canon wording (R = restriction, G = proof gap) |
| --- | --- | --- |
| S1 Operational distinction | Accept with stated corrections | none of kind R or G; wording E1-E3 |
| S2 Fixed receiver R | Accept with stated corrections | G: E4 O/2O=F_16 and j^c=1 mod 2 iff 5 divides c; E5 why every later stock contact admits |
| S3 Root clock V_m | Accept with stated corrections | G: E8 the Q>=2 bound, E9 the five-tick count off the neutral carrier. R: E11 padding sentence, E12 period 25 only on nonzero neutral states |
| S4 Relative phase and gauge | Accept with stated corrections | G: E14 derivation of B4. R: E15 V_m=j^mV_0 and D_m conjugacy only on the neutral amplitude carrier; E19 which coefficients multiply to j |
| S5 Linear obstruction over Q(j) | Accept with stated corrections | G: E22, E23. R: E20 no nonzero K^5 state is a pure mode, however produced; E21 only non-invertible commuting filters are excluded |
| S6 Positive H_m family | Accept with stated corrections | R: E25, the unitary no-cooling sentence holds only for unitaries commuting with V. G: E26 |
| S7 Stock census, minimum 22 | Accept with stated corrections | G: E29 missing derivation steps (j^3 S, B4 order). R: E30 (5,2,2,2) is not an equality case; E31 provenance wording for the value 22 |

MATHEMATICAL-REVIEW.md, pinned before the run, gives the derivations and
corrections E1 to E35. None of them changes a conclusion. The review found
one false equality in its own PREREG.md (R7). It was corrected before the
pin by PREREG-AMENDMENT-1.md and does not affect the target.

## Independent execution

review.py was written from the definitions alone, without the target's code.
It was pinned at fc384a5 and read back from GitHub before its single run
(RUN.md). The run gave exit 0, empty stderr, and one line of stdout:
1699 bytes, SHA-256 1160b89b…. That line reports 2,450,200 executed checks
and `"verdict":"PASS"`. Every frozen check R1 to R10 held:

- **R1.** The ring and contact law hold on the stated boxes:
  - C^5=I; C^4 equals the rho^-1 formula;
  - sum and Q are preserved, and refused pairs are fixed;
  - 16 of 256 pairs are admitted;
  - unit covariance holds for all of U10;
  - phi^2=phi+1 and Q(phi)=3;
  - Q^2-5B^2=4N on all 624 nonzero elements of [-2,2]^4;
  - B1 holds, and Q>44 on the whole outer shell of [-8,8]^4.
- **R2.** Readings (32,17,2,7,27). Also confirmed: the ten admission
  decisions, the states R_n, work (0,15,30,25,5), accounts 36/68 and the
  40-contact inverse.
- **R3.** All 1728 triples conserve Q and sum and are restored by the
  literal inverse. (1,j,0) is fully refused.
- **R4.** The pointer gives accounts 40/72 with R and 30/52 with T.
  Beyond that:
  - all 125 re-encodings;
  - the r=13 witness, labels (13,3,18,8,23) with readings (2,32,7,17,27);
  - five names on the unchanged state give one history, with reading 2.
- **R5.** For every m, on 69 neutral and 40 raw fixtures:
  - the compressed word equals the V_m formula;
  - the padded word has 23 attempts and 8 swaps;
  - five ticks equal j on the neutral carrier and C^3 on every pair off it;
  - least period 25;
  - minimum neutral account 4.
- **R6.** The six relative-frame tables equal the target's tables. Also
  confirmed:
  - one tick and thirteen ticks give pair 1 and pair 3;
  - accounts 4+Q(X) and 4+2Q(X);
  - the relative identity on complete final states;
  - simultaneous U10 covariance;
  - D_m conjugacy;
  - holonomy j.
- **R7.** 1811 candidates, 120 successes, levels {22:40, 28:40, 32:40}.
  None succeeds below 22. Also confirmed:
  - T reads (22,12,2,7,17), S reads (12,7,22,2,17) and j^3 S reads
    (22,2,17,12,7);
  - Q(T-1)=20 and Q((T-1)/2)=5;
  - accounts 26/48 and 30/52;
  - the minimum record Q=22, (-4,-2,-2,-3);
  - every success's inverse;
  - the digest a176b08e…, equal to the target's.
- **R8.** 625 stocks, 32 successes, {22:16, 28:8, 32:8}, digest c09ba2ca…,
  equal to the target's.
- **R9.** The rotation rule B4 holds on all 1811 candidates and all s.
- **R10.** Checked exactly in Z[zeta_25]:
  - Eisenstein at 5, lambda_t^5=j and the basis exponents;
  - eigenvectors and the left pairing 5/0;
  - nonzero projections, and reconstruction of 5z on every fixture;
  - commutant rank 20 and nullity 20 modulo both primes;
  - 242 nonzero filter determinants;
  - the H_m identities;
  - ground-mode argmin (0,4,3,2,1).

**Target verifier replays.** Both of the target's own verifiers were
replayed with the target's limits:
- verify_receiver.py reproduced RECEIVER-EXPECTED.txt byte for byte;
- verify_stock_census.py reproduced STOCK-EXPECTED.txt byte for byte.

**Informal rerun.** The two published informal scripts reproduced their
transcribed stdout exactly. That is a check that the published bytes
reproduce. It is not evidence about the target.

## Exploratory outputs

These are reported unchanged. They are not falsifiers.

| Output | Value |
| --- | --- |
| X1 successes by level, Q<=44 | {22:40, 28:40, 32:40, 38:80, 40:40, 42:20} |
| X1 all stocks by level | levels only at Q = 0, 2, 3 mod 5. The full counts are in EXPECTED.txt. |
| X2 closure | closed under negation, conjugation, j->j^2 and j->j^3 |
| X2 U10-orbits | 12 |

MATHEMATICAL-REVIEW.md recorded hand expectations for these outputs before
the run. The run confirms all of them:
- successes only at levels 0, 2 or 8 mod 10, with none at 30;
- closure under all four maps;
- 12 orbits.

The levels 38, 40 and 42 had no predicted counts.

## Limits

- **Not blind.** The coordinator had seen the target's results, and the
  hypotheses behind the stock census and the relative identity came from
  this reviewer's informal check (PREREG section 2). The independence is
  from the target's code, not from the origin of the hypotheses.
- **One architecture.** The run used x86_64 only. An aarch64 replay of
  the same pinned bytes is open.
- **One amendment before the run.** The pinned specification includes
  PREREG-AMENDMENT-1.md. The literal frozen R7 text would have fired as a
  checker defect.
- **Hand review only.** A computational pass confirms only the finite
  statements of PREREG section 6. Infinite and interpretive statements
  rest on MATHEMATICAL-REVIEW.md.
- **No physical interpretation.** Nothing here supports a reading of
  phase, energy, calorimetry or duration.

This review changes no target file, registry row, status, Canon text or
release. Accepting it, applying the corrections, and any merge or promotion
of PR #1930 are decisions for the Canon owner.

# Independent R1 review: CONFIRMED_IN_SCOPE

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Review session: Codex-R1-20261017-b053a37f.
Assignment: [R1 #1587](https://github.com/mathorn1973/twist-j/issues/1587).
Candidate: C-J-AREA-WEYL-INDEPENDENT-REVIEW-N.

## Verdict and target

**CONFIRMED_IN_SCOPE.** No counterexample or actionable mathematical/code
defect was found in the declared L1 claims of
[PR #1583](https://github.com/mathorn1973/twist-j/pull/1583) at immutable
head `e40b637b81f1a6fca99a543e970c83a4e0d45ebc`, with original source pin
`6b459a66d670656bd02a09c26da666bd16c077fb`.

The conclusion rests on the independently frozen universal proof and
separately authored exact breaker, followed by comparison with the author.
It does not assign Canon status, certify a native U implementation or
derive physical action, energy calibration, a photon, frequency or hbar.
The selected pair module, finite Weyl representation, character and cost
class remain mathematical assumptions at their stated scope.

## Independence and order of exposure

Before author-method exposure, our proof, breaker and custody files were
publicly frozen at `c82083d532cdb7e134288ea5eebe3bb488ece0a4`.
The [PINNED_R1 receipt](https://github.com/mathorn1973/twist-j/issues/1587#issuecomment-6241784815)
was created at 2026-10-17T21:52:14Z. The first independent execution
started at 21:52:42.862386Z and finished successfully at 21:52:43.045852Z.
The aarch64 reproduction also passed, before the author's files were
fetched for comparison beginning at 21:53:38.369849Z.

Initial reading was the original author PREREG, the R1 assignment and
allowed public Canon dependencies/metadata. [EXPOSURE.md](EXPOSURE.md)
discloses earlier result-exposed work on the distinct PR #1581 and the
fact that the advertised R1 conclusions were visible in PREREG. This is
method-blind relative to #1583, not result-blind. Same-session subagents
contributed proof, code and static review; they are not separate
independent scientific reviewers. The original authoring session and
this reviewing session are distinct.

After the initial run, all seven author files listed below were read at
the exact target head. The original PREREG and verify.py remain identical
between author pin and head. The source author's executable was inspected
but was not executed or imported in this review. All six of our own frozen
files remain byte-identical after exposure. [RUN.md](RUN.md) records the
own run chronology, hashes, environment and exact output.

## Claim-by-claim disposition

All author line links in this section fix the reviewed result head.

| Mandatory attack | Disposition and evidence |
|---|---|
| Infinite marked O^2, J phi=j, inverse, one step and fifth step | Confirmed. Independent PROOF sections 1-2 derive explicit unit inverses and omega(T^n u,T^n v)=j^n omega(u,v) for every integer n. The unit pair disproves one-step preservation; T^5 preserves the entire form. This agrees with [author PROOF lines 19-27 and 47-68](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/PROOF.md#L19-L68). Our audit checks both inverse directions on eight integral module basis vectors and 64 covariance/fifth-step pairs. |
| Ramified quotient and loss of complex phase | Confirmed. Independent PROOF section 3 derives the exact quotient O/(1-j)=F5 and rho(j,J,phi)=(1,2,3). A=diag(2,3) preserves area. All five scalar roots reduce to 1; a complex phase is not transported by rho. This agrees with [author PROOF lines 29-42 and 70-84](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/PROOF.md#L29-L84). The audit checks 16 ring-basis products and all 625 residue pairs. |
| Complete Weyl products, inverses, central phases and D | Confirmed. Independent PROOF sections 4-5 obtain W(a,b)W(c,d)=j^(-bc)W(a+c,b+d), W(a,b)^-1=j^(-ab)W(-a,-b), the commutator j^(ad-bc), and exact D covariance without an extra central factor. [Author PROOF lines 88-118](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/PROOF.md#L88-L118) uses the same rightmost-first convention and correct cocycle. Our dense matrix audit checks all 25 conjugations and two-sided inverses and all 625 ordered products and commutators. |
| All additive characters and physical selection | Confirmed. Independent PROOF section 6 classifies all five additive characters, including the trivial one; exactly four are faithful. The audit checks 125 addition identities and 2500 faithful-character area identities. [Author PROOF lines 120-126](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/PROOF.md#L120-L126) distinguishes the marked algebraic choice from a physical observation map. Neither proof selects a physical character. |
| Complete rational diagonal cost class and scalar intersection | Confirmed. Independent PROOF section 7 proves diag(h0,h1,h1,h1,h1) for all rational h0,h1, not merely sampled integers. Exact rational constraints have D/X/Z/shared ranks 3/4/0/4. All 3125 bounded witnesses agree; positive costs with gaps 1 and 2 both survive D and Z, while X invariance forces a scalar. This matches [author PROOF lines 130-155](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/PROOF.md#L130-L155). |
| Attempted implication to physical action or unnamed layer lift | No such implication is established, and the author does not assert one. Independent PROOF section 8 preserves countermodels with different gaps and the unselected character. [Author PROOF lines 162-188](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/PROOF.md#L162-L188) and [RESULT lines 91-106](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/RESULT.md#L91-L106) explicitly exclude native admission, physical action, SI calibration and L1-to-L6 promotion. These limits are part of the confirmed scope. |

Three apparent differences are not defects. First, the author's cost
condition h_(3k)=h_k and our direct conjugation condition h_(2k)=h_k
describe the same fixed space because the permutations are inverses.
Second, the author's scalar-commutant extension to arbitrary complex
matrices on the same V is valid: distinct Z eigenvalues force diagonality,
and X then forces a constant diagonal. It is not a no-go for arbitrary
physical decoders or enlarged systems. Third, "five-step return" in the
author's inventory concerns return of the form. Our proof makes explicit
that T^5 is not the identity on states. D has order four; that does not
conflict with the order-five central scalar or area multiplier.

## Executable comparison and finite evidence

The author uses four power-basis coefficients with polynomial reduction
([verify.py lines 35-46](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py#L35-L46))
and monomial basis permutations with phase exponents
([lines 81-100](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py#L81-L100)).
Our pre-exposure breaker uses cyclic five-coefficient convolution modulo
the all-ones relation, literal dense cyclotomic matrices, explicit
character multiplication and rational nullspace equations. It also checks
unit inverses, Weyl inverses, product cocycles and ideal witnesses.

The author's finite inventory and failure handling are consistent with
its claims ([verify.py lines 122-216](https://github.com/mathorn1973/twist-j/blob/e40b637b81f1a6fca99a543e970c83a4e0d45ebc/probes/P-J-RAMIFIED-AREA-WEYL-1/verify.py#L122-L216)).
Omission of our additional checks from that implementation is not a false
claim of a universal numerical proof: the author expressly relies on
written proof for infinite classes. Our two runs both produced explicit
scientific PASS, exit 0, empty stderr and identical six-line, 1061-byte
stdout, SHA-256
`7be152de96ce83d6c7042553b434fcf1a3d1f10142fe0e8ed8b52674778ac4a0`.
The exact output is [EXPECTED.txt](EXPECTED.txt).

Printed physical-status flags are summaries of the scoped argument,
not experimental tests of physical occurrence or an all-models no-go.

## Author provenance checked after the independent run

The author's [pin receipt](https://github.com/mathorn1973/twist-j/issues/1582#issuecomment-6238930475)
was created and last updated at 2026-10-17T18:50:38Z. Its RUN record
declares a pre-execution freeze and reports a local 520-byte output.
It distinguishes the initial temporary-directory invocation from the
later contract-path replay recorded in its fields. It does not supply
an exact first-local-run UTC, so this review does not
independently certify that local timestamp ordering from the record alone.
This limitation does not replace or invalidate the independently recorded
pin-before-run chronology and proof in the present review.

Public author CI logs were read after our run. Jobs
[x86_64 117476746976](https://github.com/mathorn1973/twist-j/actions/runs/39060312673/job/117476746976)
and [aarch64 117476746802](https://github.com/mathorn1973/twist-j/actions/runs/39060312673/job/117476746802)
report actual architecture, VERIFY PASS, verifier SHA-256
`bab58b9d4bef1aadb042a96479f893477644122817755c5d2988a5c8d5a72def`
and output SHA-256
`8b6b08e8ee764075d480e461d4c6696d25d301f9f05d5d48a9dfcbb28fff80a9`.
Their temporary merge checkout `5ccdc93887004af64497d1e0356ccba9d23fc381`
has tree `56c39313a19216f0d43b9039ceea8b5d4a3819d3`, equal to the reviewed
author head. The public [gate receipt](https://github.com/mathorn1973/twist-j/issues/1582#issuecomment-6239074480)
is additional provenance. These jobs execute the author's verifier, not
our independently authored breaker and not a physical experiment.

## Post-barrier source custody

All rows below refer to `probes/P-J-RAMIFIED-AREA-WEYL-1/` at the exact
reviewed author head. Fetch completed at 2026-10-17T21:53:42.574928Z.
The earlier allowed source manifest remains frozen in SOURCES.tsv.

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 6773 | d7f3900ede7eb09042ae808c6cac8443c2443d2ec10361f5e1feae10c98754ad |
| PROOF.md | 7349 | 250bd14199089c43a7d13610eab440689ade7e9910f939f743023724cdd0d201 |
| README.md | 2238 | e4c694adf29109f4e4940d8faddd1fa8ed05a2338a10531cb17cfe225c82c919 |
| RESULT.md | 4832 | e48b4df1794f9be2e19403d0ca8e085f68975b54cf2c6a504f3e27e1b2440572 |
| RUN.md | 1950 | a05de4ac0353c8a268ae04de218089e1eec92861f8868f757420b45542f6e0f3 |
| EXPECTED.txt | 520 | 8b6b08e8ee764075d480e461d4c6696d25d301f9f05d5d48a9dfcbb28fff80a9 |
| verify.py | 6867 | bab58b9d4bef1aadb042a96479f893477644122817755c5d2988a5c8d5a72def |

## Remaining obligations

METRO-EDGE-SCALE, QDD-INSTRUMENT-APPARATUS, native interface admission,
physical occurrence/dynamics, character selection, a complete coupled
energy account and SI/action calibration remain open at their existing
status. This review supplies neither R2 nor N. It is a draft independent
L1 review for external acceptance, with no Canon or merge authorization.

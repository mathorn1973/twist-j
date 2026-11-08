# Additive scope and reporting erratum for R2 at 4e708468

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

This is a result-exposed analytical audit of the existing R2 submission, not
a new method-blind review, a replacement of its owner, or a replay of its original scientific
execution. The new probe separately preregisters exact checks of the two
textual counterexamples identified analytically here. The author/reviewer sources, first output and original pins remain
unchanged. This document does not authorize a source merge or Canon promotion.

## Immutable scope and current ownership

At the 2026-10-18 readback, STATUS.md still declares ACTIVE Public Canon v103,
content commit `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`, Canon SHA-256
`d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`.

PR #1606 remains a draft at
`4e708468e6c22a0de8ce0f217f73e761d67d3d29`; its pre-execution pin is
`b7792774aa0a3f093d621220a1f7072115cc7e50`. The owner remains
`Antigravity-R2-20261017-8f0b47e9`. No correction commit or later owner response
was present after controller comments
[#1606/6247452093](https://github.com/mathorn1973/twist-j/pull/1606#issuecomment-6247452093)
and
[#1588/6247467010](https://github.com/mathorn1973/twist-j/issues/1588#issuecomment-6247467010).
The source PR #1585 remains at
`bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`, with original pin
`a4ec92176c9f8ace9f884254e05d57a5466b84e0`.

This erratum supersedes the incorrect statements below for downstream use.
It does not silently rewrite them in the foreign branch or its sealed files.

## 1. Evidence level and architecture

R2 RESULT.md section 1 says:

> conditional theorem-grade proof `T` and exact two-architecture computational verification `C`

Replace its meaning by:

> Conditional candidate-T analytical arguments, subject to the explicit scope
> corrections below, and one documented x86_64 finite reviewer-breaker run.
> Repository CI passed on two architectures; it did not run this notes/break.py
> on a second architecture. No public T/C promotion is asserted.

R2 RUN.md records exactly one scientific execution: Windows 11, x86_64,
Python 3.12.10, 2026-10-17T22:06:47.420440Z to
2026-10-17T22:06:48.391379Z, exit 0, empty stderr, 1109-byte stdout,
SHA-256 `960acb98ae13b517505b5d6832273a18c9721edab10d0f0f304d86f6f29e02f1`.
It expressly distinguishes this run from notes CI.

Policy run 39074226758 passed jobs architecture-x86_64 (117517947326),
architecture-aarch64 (117517947513), and check (117518104299) at the exact
result head. The changed files are confined to notes/. The pinned
tools/check_verifier.py selects changed probes/ directories, not notes/break.py.
Green infrastructure jobs are therefore not evidence of a second execution
of the R2 breaker. The source author's separate aarch64 execution of
probes/P-FUNDED-AREA-PHASE-RECORD-1/verify.py is also a different program/run.

## 2. Exact inverse, not involution

The PR summary and submission receipt say that all four elementary gates and
U_* are exact two-sided involutions. This is false.

For every raw state, including accepted and rejected branches,

    F_(axis,epsilon)^(-1) = F_(axis,-epsilon).

For output controller phase c', put c_prev=c'-1 modulo four. The inverse of
U_* first restores c_prev and then applies the opposite requested sign of
the letter L(c_prev,eta). These are exact two-sided inverses. They are not
claims that either map equals its own inverse.

For example, starting at `(0,0,1,-1,4,+1,+1,0)`, two elementary F_(Q,+)
applications produce `(2,0,1,-1,0,+1,+1,0)`, not the starting state.
For U_* the distinction is even immediate: U_* squared advances c by two
modulo four, so cannot be the identity on any complete state.

Preserve the recorded E=6 cycle spectrum `20:16, 52:32, 124:8, 188:4`.
No new enumeration of that spectrum was performed in this audit.

## 3. Reader preparation needs the universal quantifier

The PR summary and submission receipt omit the quantifier in
`(u_N^2-v_N^2)/4=A iff (u_0,v_0)=(1,-1)`.

The correct statement, already present in R2 RESULT.md and PROOF.md, is:

    [(u_0+A)^2-(v_0+A)^2]/4 = A for every integer A
        if and only if (u_0,v_0)=(1,-1).

Indeed the left side is

    (u_0^2-v_0^2)/4 + (u_0-v_0)A/2.

Equality as a function of all integer A requires zero constant term and
unit slope, giving u_0+v_0=0 and u_0-v_0=2. It is not an iff at an isolated
trajectory: at A=0 any equal initial references give equality. Nor does
the universal statement assert that every A is reachable at one fixed
finite bank.

## 4. Scalar Weyl words require closure modulo five, not integer closure

R2 frozen PROOF.md section 4 contains the false sentence:

> On an open path where (q_N,p_N) != (q_0,p_0), W_N is not a scalar phase.

This is a false exported lemma, not just an imprecise synonym. It must not
be used downstream. The correct formula in the same frozen Theorem 4.1 is

    W_N |k> = j^(k P + A - q_0 P) |k+Q>,
    Q=q_N-q_0, P=p_N-p_0, j primitive of order five.

Consequently

    W_N is scalar iff Q=0 mod 5 and P=0 mod 5.

Proof: a scalar operator cannot shift any basis vector, so Q must vanish
modulo five. Once Q vanishes, equality of the k=0 and k=1 diagonal factors
forces j^P=1, hence P=0 modulo five. Conversely both conditions give
W_N=j^A I, because q_0 P is a multiple of five. Integer closure is sufficient
but not necessary for this algebraic conclusion.

A fully funded exact counterexample to the false sentence is the elementary
word F_(Q,+)^5 from `(0,0,1,-1,25,+1,eta,0)`. After t steps, for 0<=t<=5,
the state is

    (t,0,1,-1,25-t^2,+1,eta,0).

Every bank is nonnegative. The endpoint has q=5, so the integer base path
is open, but A=0 and W=X^5=I. This is an allowed requested elementary word;
it is not being misrepresented as the four-phase autonomous U_* schedule.

The source PR #1585 does not make the false universal open-path claim.
Its PROOF.md section 4 explicitly distinguishes modulo-five and integer
closure. R2 break.py checks the full correct monomial formula and the
integer-closed implication, and contains no test of the false converse.
The recorded PASS therefore cannot certify the false sentence. Disposition:
`FALSE_EXPORTED_LEMMA_REJECTED; CORRECTED_SCOPE`.

## 5. Literal R2 preregistration differs from the equation actually checked

R2 REVIEW.md already discloses that frozen PREREG.md Attack 4 prints the
basepoint term `-p_0(q_N-q_0)`. The source proof, the R2 frozen proof and the
R2 implementation all instead use the correct `-q_0(p_N-p_0)`.

The literal preregistered formula has an exact counterexample. Take

    s=(1,-1,3,0,9,+1,+1,0), H=11, E=20.

Its next autonomous U_* step requests Q_+. The cost increase is 3, so it is
accepted and yields

    (2,-1,3,0,6,+1,+1,1).

Here A=0, Q=1, P=0. The literal Weyl word is X. The incorrect preregistered
formula gives j X. These differ since j is primitive of order five. This
initial state is also the seventh `init_configs` entry of the frozen breaker.
The breaker nevertheless compares to the correct formula in expected_weyl,
which is why its recorded run can pass without testing the erroneous formula.

PREREG.md section 5 says that a counterexample to an identity at its stated
scope triggers COUNTEREXAMPLE. Accordingly, the claim that every literal
preregistered identity passed is not supportable. The exact disposition is:

    R2_LITERAL_PREREG_ATTACK4: COUNTEREXAMPLE (analytical);
    SOURCE1585_OPEN_PATH_FORMULA: not falsified by this discrepancy;
    R2_IMPLEMENTED_OPEN_PATH_FORMULA: agrees with the source formula;
    ORIGINAL_EXECUTION_OUTPUT: preserved verbatim as evidence of the code run.

This does not retrospectively change the frozen target or manufacture a
failed program execution. It separates the false textual target from the
different, correct equation actually implemented. Intake of the entire R2
submission as an unqualified fulfilled preregistration must remain withheld
until this distinction is explicitly acknowledged. No rerun is requested.

## 6. Correct the scope of the 882 capacity checks

The PR summary and submission receipt say `882 reachable states on B<=200`.
The frozen breaker actually loops over E=2,...,15 and all q,p,u,v in the
complete square-cost bounds with u-v=2 and H<=E. It assigns B_equiv=E-2
and tests the capacity inequality independently of the control labels.

The precise description of its recorded 882 count is:

> 882 integer-and-bank tuples `(q,p,u,v,b=E-H)` with `u-v=2` and `E<=15`;
> no reachability restriction or claim was tested. The inequality is
> independent of sigma, eta and c, so their labels do not affect it.

The whole-carrier analytical bound remains
`|A_read| <= floor(sqrt((E-2)/2))` on u-v=2. The finite 882 count is from
the frozen stdout, and its domain is identified by static source inspection;
this audit did not re-enumerate it.

## 7. Already disclosed arithmetic erratum

R2 REVIEW.md already states that the unweighted total 781 in frozen PROOF.md
section 2.2 is 761. Its individual coefficient rows, weighted total 3605,
complete raw-state total 57680 and frozen stdout remain consistent. Preserve
this earlier disclosure; do not present it as a new numerical result or
rewrite the frozen table.

## Disposition and strongest usable conclusion

The reviewer's declared equations establish the exact inverse pairs, actual
reference increment law, correctly scoped area reader, correct chronological
Weyl formula and conditional funded-loop results on the chosen integer
carrier. Those source conclusions are not falsified by the discrepancies
identified here. This audit does not substitute for independently redoing
all six attacks and does not award a new CONFIRMED_IN_SCOPE verdict.

The report must distinguish a false frozen R2 lemma, a counterexample to the
literal R2 preregistered open-path formula, narrower implemented/run evidence,
and correct source identities. The source carrier, quadratic cost, preparation,
controller and algebraic representation remain declared choices, not a native
U implementation or physical phase measurement. These corrections provide
no missing common native carrier and do not close N's STOP_UNTYPED boundary.

## Source custody

The following Git blob identifiers were returned by exact-commit GitHub
readback. SHA-256 values below were published custody values at the analytical audit.
SOURCES.tsv additionally records their independent local byte hashing before
the new probe pin; this metadata operation executes no scientific verifier.

| Source | Git blob | Published SHA-256 |
|---|---|---|
| R2 PROOF.md | `8c6f72ac30531aa87d4180cf4ff46286c0921622` | `13d8a19ce3cd801e1f594406710c3c918b98984208df5abb32e103710987aad0` |
| R2 PREREG.md | `c223425679fccccd0b71870084b0cdf972db2044` | `65010bbbbf7350146317848f13c2afff49cdf3abc254521ff232888f56e6af0c` |
| R2 break.py | `ea4d6b5bd86b751ebe18ce49f080046015d69cee` | `d4896d76663653443b910bb70c308f38a548339d7e90e35f7716014545ae933b` |
| R2 RESULT.md | `f29c937f06a0b80cf1609e9dadac2322cff71c2b` | `6c169068e00b18f9d191d733fd2b1b4009f8868ed9f639bda10fff7e7feb9924` |
| R2 REVIEW.md | `1c1a8902e17f301644e0f48e3fba04c2b21e34c7` | `f08ffe045a2620744e85c83be221e877520b35f6e1f529b53556ba95b458b973` |
| R2 RUN.md | `2ff07d478fab46b33b955796e49cbad5c9aea6ca` | `38aee9de9c5015301a1c12662a6044ab427299f4d98a7b9498416ad758218b60` |
| R2 EXPECTED.txt | `6c12ce6874ba5a32fae8a46b18d4f2e4055de92b` | `960acb98ae13b517505b5d6832273a18c9721edab10d0f0f304d86f6f29e02f1` |
| Source PR1585 PROOF.md | `486b502442e2695615755e04a88b1a5b98bc12ad` | `c9e55f49b3a82cb51c8dbc5b88cd27cdeae0957fbc8cd56fc9d7d076b90c7318` |
| Source PR1585 PREREG.md | `5b8c29bc0c0612ce3f6b78910debf53c04be7f1b` | `a311e0ae92e61c16ca578d2c18d183f0f3e49720da9f918ae35e599ee6df4213` |

The reporting-audit contribution is this additive erratum. The encompassing
new probe also contains its separately preregistered construction and verifier.
No source/reviewer
branch, code, output, preregistration, proof or Canon file was edited.

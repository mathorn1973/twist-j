# P-RAPIDITY-GOLDEN-LADDER-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / TWO-ARCHITECTURE COMPUTATION GATE PASS / CANON UNCHANGED**

## Verdict

The frozen written proofs survive the one accepted exact audit. All eleven
gates passed, all five frozen negative controls fired at their preregistered
witnesses, and no falsifier against the frozen theorem package fired. The
universal statements are carried by the written proofs in `PREREG.md`; the
finite verifier is an exact audit of the frozen mechanisms and controls.

A later sealed Canon fold may decide whether to register

```text
RAPIDITY-GOLDEN-LADDER [T]
```

at the exact scope below. This probe itself changes no public row and proves
no RH or GRH statement.

## Exact result

Let `bold_mu` be the registered integral rapidity lift for `F = Q(sqrt5)`,
and for a unit `t` let `ev_t` send every split rapidity variable `X_p` to
`t`, with `tau = t + t^-1`.

**A. Evaluation family.** `ev_t(bold_mu(n))` depends on `t` only through
`tau`, is unchanged under `t -> t^-1`, and equals the multiplicative
function `m_tau` with local table

```text
split p:      m_tau(p) = 1 - tau,   m_tau(p^e) = 2 - tau   (e >= 2),
non-split p:  m_tau(p) = -1,        m_tau(p^e) = 0         (e >= 2).
```

No split orientation is selected by any diagonal evaluation.

**B. Integrality selection.** For `t` in `F^x`, every `m_tau(n)` lies in
`Z` iff `t = +-phi^(2k)`, `k` in `Z`, iff `tau = +-L_2k`. The integers
`m >= 0` with `m^2 - 5b^2 = 4` solvable are exactly the even-index Lucas
numbers. The ladder is selected by the registered unit group and its Pell
alternator, not chosen.

**C. Anchors.** `m_2 = mu` identically; on squarefree `n` with `a` split and
`b` non-split prime factors, `m_(-2)(n) = (-1)^b 3^a`; the shell ladder
`sigma_tau(n) = (1-tau)^omega(n)` on squarefree pure-split `n` satisfies
`sigma_3(n) = mu(n) a_F(n) 1_((n,5)=1)` for every `n >= 1`. The `mu` rung
is the unique squarefree-supported rung: `m_tau` is squarefree-supported iff
`tau = 2`.

**D. Layer decomposition.** With `B_a(x)` the non-split-signed count (including the ramified prime 5) of
squarefree `n <= x` carrying exactly `a` split prime factors,

```text
sum_(n<=x) mu^2(n) m_tau(n) = sum_(a>=0) (1-tau)^a B_a(x),
```

a finite sum with `a <= log x / log 11`; the nodes `1 - tau` at distinct
rungs are distinct integers, so any `A(x)+1` distinct rungs determine every
layer exactly by Vandermonde inversion over `Q`. At `tau = 2` this is the
Mertens function.

**E. Connecting units.** `m_tau = sigma_tau * w_tau` with `w_tau`
multiplicative, non-split local factor `1 - T`, and split local factor
`((1 - tau T + T^2)/(1 - T)) / (1 + (1 - tau)T)` whose coefficient of `T^e`
is `1 - (tau-1)^(e-1)` for `e >= 1`; at `tau = 2` the split factor is `1`.

These are exact identities of L1 arithmetic and formal Dirichlet series.
None of them is a cancellation estimate.

## Accepted exact audit

```text
pin_commit:       4cf730fea17561e3c8fb78db51ec0858fc7c256f
verifier_sha256:  d501dd73cbb870fe296ec31472ff6de1cdfc963d3016f8351430b5630b1fae04
stdout_sha256:    b1ea5b711ad0f6a167cbbd8e53e34bc598364c07685e8009889afc46350e6a2a
stdout_bytes:     1653
stdout_lines:     34
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 11/11 ALL PASS
```

Gate readout:

```text
G01 PASS  golden unit facts k<=6, Pell enumeration m<=322
G02 PASS  local tables tau=+-L_2k k<=4 e<=8 by exact Z[phi] division
G03 PASS  m_2 = mu through n=100000
G04 PASS  m_(-2) = (-1)^b 3^a on squarefree n through n=100000
G05 PASS  sigma_3 = mu a_F 1_(5nmid) through n=100000
G06 PASS  layer identity, taus 2,3,7,18,-2,-3, x=1000,10000,100000
G07 PASS  Vandermonde at nodes -1,-2,-6,-17 recovers B_0..B_3 at x=20000
G08 PASS  m_tau = sigma_tau * w_tau, tau=2,3, through n=100000; closed form
G09 PASS  frozen exact readouts
G10 PASS  stdlib-only exact-arithmetic source firewall
G11 PASS  all five production-path breakers
```

Frozen breakers fired at their preregistered witnesses:

```text
B1 wrong shell Lucas value tau=4:        first difference from s_5 at n=11
B2 non-split sign +1:                    first difference from mu at n=2
B3 odd unit powers phi, phi^3:           tau = 2phi-1, 4phi-2, non-integer
B4 Pell near-misses m=4, 8:              no solution of m^2-5b^2=4
B5 repeated node (-1,-2,-6,-1):          Vandermonde system singular
```

The `tau = 2` readouts reproduce the classical Mertens values
`M(10^3) = 2`, `M(10^4) = -23`, `M(10^5) = -48` as an internal
cross-witness of the `mu` anchor. All readouts are exact integers and gate
nothing analytic.

## Scientific boundary

Statements A-E are `candidate-T` at exact L1 arithmetic and formal
Dirichlet-series scope.

No RH or GRH result, zero or pole location, analytic continuation, summatory
estimate or cancellation for any ladder sum or layer, uniformity in `x` for
the layer inversion, Hecke or automorphic identification of any rung,
selected split orientation, probability, physical dictionary, SI statement,
or L1-L6 lift is claimed. The abscissa readings recorded in the fenced
boundary of `PREREG.md` section 6 are labeled classical imports and are not
part of the row.

`TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains unchanged. The merged
`P-O5-SQUAREFREE-CORE-1`, `P-O5-GOLDEN-AXIS-BAND-1`,
`P-O5-GOLDEN-PROFILE-TRANSFER-1`, and `P-O5-DEDEKIND-GRH-DIVISOR-READ-1`
lanes remain separate; this probe consumed no evidence from them.

## Evidence boundary

The accepted local formal leg is:

```text
platform:        Ubuntu 24.04
architecture:    x86_64
python:          Python 3.11.15
pin:             4cf730fea17561e3c8fb78db51ec0858fc7c256f
verifier SHA256: d501dd73cbb870fe296ec31472ff6de1cdfc963d3016f8351430b5630b1fae04
stdout SHA256:   b1ea5b711ad0f6a167cbbd8e53e34bc598364c07685e8009889afc46350e6a2a
stdout bytes:    1653
stderr bytes:    0
result:          VERIFY RESULT 11/11 ALL PASS
```

The required pull-request workflow (run 33739353913 on PR #792, head
`9b01afb6d626ec101738b72dd4aa43958c316167`) replayed the unchanged pinned
verifier from clean checkouts under Python 3.12.14. Job 100597369775
(`architecture-x86_64`) and job 100597369515 (`architecture-aarch64`) both
reported

```text
VERIFY PASS P-RAPIDITY-GOLDEN-LADDER-1 d501dd73cbb870fe296ec31472ff6de1cdfc963d3016f8351430b5630b1fae04 b1ea5b711ad0f6a167cbbd8e53e34bc598364c07685e8009889afc46350e6a2a
```

and aggregate job 100597443866 (`check`) passed. Both architectures
reproduced the same frozen verifier and the exact committed `EXPECTED.txt`
bytes, so the two-architecture computation gate is satisfied.

```text
CONFIRMED          SELECTED LOCALLY AND ON BOTH REQUIRED ARCHITECTURES
SCIENTIFIC-FIRED   NOT SELECTED
STOP               NOT SELECTED
ABANDONED-PIN      NOT SELECTED
ARCHITECTURE GATE  PASS
```

The written proofs, not architecture count, are the proposed theorem-grade
source. The verifier audits them.

No Canon, Registry, Frontier, dependency, gate, evidence, workflow, Note,
reproduction, or existing probe is changed by this result.
## Post-pin review clarification (2026-09-05)

Independent proof and verifier reviews found no mathematical defect in the
frozen statements A-E. The layer sign in D counts every non-split prime
factor, including the ramified prime 5; thus n=5 contributes -1 to B_0.
The earlier shorthand "inert-signed" has been corrected above to agree with
the unchanged frozen definition and verifier.

The ungated sentence in PREREG.md section 6 saying that no summatory bound
below abscissa 1 transfers "by this convolution route" is read only at the
scope justified by its argument: a direct black-box transfer requiring a
finite sum of weighted absolute coefficients of w_tau or its inverse.
Divergence of that absolute sum does not exclude a signed-convolution
argument exploiting cancellation, a truncation argument with controlled
error, or a different transfer mechanism. No such broader no-go is claimed
or available as a premise. This clarification changes no statement A-E,
frozen threshold, source constructor, or scientific decision.

The verifier's redundant G10 line-ending check reads through Python text
newline normalization. LF-only custody is therefore checked independently
on raw bytes and by the pin hashes; the text check alone cannot distinguish
CRLF. Actual PREREG.md, verify.py and EXPECTED.txt bytes are LF-only and
unchanged. No pinned verifier edit or new formal execution is made.

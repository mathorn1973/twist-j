# Independent comparison with author C

PUBLIC / NON-CANONICAL / L1. Verdict: **AGREE / ACCEPT within the frozen
five-cell comparison scope**. No scientific counterexample, actionable
proof defect or unresolved claim was found within that scope. This verdict
is independent of later Canon promotion and does not authorize a merge.

## Pins and exposure

- Assignment: #1548, 13858 bytes, SHA-256
  c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87.
- Author specification/proof/code pin:
  423c6f7488b35399ff40fcc30be01df526aba795.
- Reviewed author PR #1556 head:
  ed635a114bc52c4abbc16ea660bd4d89f2d2efde.
- Independent RC proof/code pin:
  105d22bfc457f5e3f29dfa7b3ca75694b21670fd.
- RC first-run record:
  8a6902c0dbbe81ea0a66d7d2af043371cac3b5f7,
  public fetch/readback completed at 2026-10-16T22:05:49Z.
- First opening of author PR body and result package began
  2026-10-16T22:06:12Z, after that public first-run record.

All six original author pin files are byte-identical at the reviewed head.
The only post-pin additions are EXPECTED.txt, RUN.md and RESULT.md. The
review read the full nine-file author package, its allowed lineage sources,
actual CI logs and record hashes after the barrier. It did not import or
execute the author verifier as an alleged independent implementation.

## Claim-by-claim comparison

| Frozen obligation | RC derivation/audit | Author source | Disposition |
|---|---|---|---|
| Exactly five actual CW incidences | Explicit ordered edges and closed face boundaries, DC=0 and C^t C checked | PROOF section 1 | AGREE; digons use distinct parallel edges |
| Active dimensions 2,2,4,4,4; raw dimensions 3,4,5,6,7 | Basis images, injective P and exact pullback | PROOF section 1 | AGREE; raw complement is rational, not universally integral |
| Characteristic formula | Second-order recurrence and block companion, independently audited by Newton traces | PROOF section 3 block determinant; verifier Leibniz determinant | AGREE for all five polynomials |
| Determinant one and full lattice inverse | Coordinate recovery and two integer shears | PROOF sections 3,4 | AGREE |
| Raw/active metric invariance and definiteness | Scalar energy polarization, completed square, spectra and rational Schur complements | PROOF section 4; principal-minor/rank audit | AGREE; first four positive definite, last PSD with nullity one |
| Minimal orders 4,3,6,5 | Characteristic-root orders and Cayley-Hamilton; all smaller positive powers audited | PROOF section 5, exact mode arguments | AGREE; matrix order is not every state's period |
| Infinite order for G33 | Nonzero Jordan chain and all-n formula on independent integer vectors | PROOF section 5 and exact chain checks | AGREE; no finite search or repeated-root inference |
| Full raw orders | Rational active/static decomposition and integral embedded witness | PROOF section 1 | AGREE without an integral-splitting claim |
| Sign markings | Uniform R,S conjugacies, 248 finite checks | PROOF section 2 | AGREE; whole-edge reversal leaves Gram unchanged, whole-face reversal changes offdiagonal sign |
| Actual canonical A_f and B_f | S=diag(1,-1), Q=diag(S,S), exact coordinate/metric identities | PROOF section 2; canonical verifier check | AGREE with canonical (a,b,c,d) marking |
| Bounded novelty and exclusions | Canon lineage audit before exposure, author lineage checked after | LINEAGE and RESULT | AGREE with the bounded claim, not a global historical-priority claim |

The explicit common result is:

| G | Characteristic polynomial | Order | Energy |
|---|---|---|---|
| (2) | X^2+1 | 4 | positive definite |
| (3) | X^2+X+1 | 3 | positive definite |
| [[2,1],[1,2]] | X^4+X^2+1 | 6 | positive definite |
| [[2,1],[1,3]] | X^4+X^3+X^2+X+1 | 5 | positive definite |
| [[3,1],[1,3]] | (X^2+1)(X+1)^2 | infinite | positive semidefinite, nullity one |

## Explicit proof clarification

Author PROOF section 5 displays its Jordan formula for k>=0, although its
PREREG uses the phrase "all-integer-time". This does not leave the infinite
order undecided: the author already proves the inverse, and a negative-time
identity would imply a positive-time identity. More explicitly, on the
chain span A=-I+N, N^2=0, so (I-N)^-1=I+N and

    A^n w=(-1)^n(w-nv),  n in Z,
    v=(1,1,-2,-2), w=(0,0,1,1).

RC PROOF section 2 supplies this extension before author exposure. Thus the
wording is resolved by the supplied mathematics and is not a fired
falsifier, an UNRESOLVED result or a reason to alter the author's frozen pin.

## Independence and implementation differences

Both implementations necessarily share the declared matrices and basic
integer linear algebra. They are not claimed blind to exposed targets.
The paths differ materially: author characteristic polynomials use Leibniz
expansion of XI-A, while RC uses Newton identities from power traces; author
constructs block matrices, while RC builds coordinate-update basis images;
author assembles energy blocks, while RC polarizes scalar energy; author
checks principal minors/rank, while RC uses rational Schur complements.
The principal RC recurrence proof was frozen before exposure. Same-session
helpers supplied analytic/static review, not another independent owner.

RC additionally preserves explicit rejected controls for an isolated
boundary-coefficient flip, a reversed update order with the old energy,
and order two at the parabolic boundary. The universal infinite-order
conclusion uses the separate Jordan proof. The author did not promise
these additional controls, so their absence from its stdout is not a defect.

The independent stdout is not expected to be byte-identical to the author's:
its format and audit route are different. Each implementation has its own
immutable exact stdout for same-program cross-architecture replay.

## Custody and actual author CI readback

Author verifier: 8679 bytes, SHA-256
b863c54fc060aa8ced19a5a6b48f2b1445b6de8915b7da99a7f95e6d2faed2e5.
Author stdout: 874 bytes, 8 lines, SHA-256
9a722d992c12eea57c9de5220c68b02877c688f92da5fd1a5801f15cf27107d3.
Both match the public file bytes and first RUN.md. The author first run
records Linux aarch64/Python 3.11.2, zero exit, empty stderr at
2026-10-16T21:05:36.424455+00:00 through 21:05:36.559939+00:00.
The public specification receipt preceded it. v102 release readback was
already successful. No later change to the six frozen author files occurred.

[Workflow 38967121084](https://github.com/mathorn1973/twist-j/actions/runs/38967121084)
has head ed635a114bc52c4abbc16ea660bd4d89f2d2efde and completed successfully.
The downloaded logs, not merely the badge, contain VERIFY PASS for the
exact verifier/stdout hashes above on both jobs:

- x86_64: job 117196232253, successful.
- aarch64: job 117196232345, successful.
- aggregate check: job 117196603337, successful.

RC's own first run is in RUN.md/EXPECTED.txt. Its exact PR-head CI must also
pass; the actual final CI receipt is recorded on the RC pull request and
#1567, rather than fabricating completion in advance in this file.

## Inheritance and retained boundaries

General inverse/invariance/energy thresholds and the two-triangle zero mode
are already in v102 CANON lines 7562-7610. Triangle order three is inherited
from lines 7614-7644. Canonical C, A_f, B_f, raw split and order-five proof
are inherited from lines 7882-8005. The author labels these appropriately.

The retained comparison contribution is the fixed five-case presentation,
digon/double-digon orders and incidences, exact orientation bookkeeping and
the explicit nonsemisimple infinite-order certificate. This is sufficient to
avoid a blanket NO_NEW_CLAIM disposition, while inherited components receive
no novelty credit. Neither author nor RC asserts priority over all literature.

Within the declared five-cell class there is no remaining UNRESOLVED or STOP
item. Physical selection of five, a native-U/J derivation, general complex
classification, contact, source transfer and apparatus realization are
outside this class and remain unestablished. Acceptance here neither closes
those questions nor promotes any Canon claim.

Post-barrier inspection of the five declared historical lineage files also
corroborated the inherited boundaries above. None explicitly supplies the
digon order-four case, digon-pair order-six case or the shared-triangle
Jordan-chain infinite-order certificate. The older four-dimensional A4
Cartan energy pullback is not the two-dimensional edge-face Gram G22 and
its order-six shear. RC did not repeat the author's broader search over all
current notes and probes; no global absence or priority claim is certified.

# Review of the common action and its discrete boundary

Candidate: P-RELATIONAL-MASS-JOINT-ACTION-1
Status: NON-CANONICAL, NEW_DECLARED L1
Ownership: https://github.com/mathorn1973/twist-j/issues/1686

The source, analytical and security reviews found no unresolved defect in
the frozen claim at its declared scope. The first formal local audit
completed with PASS. Its intended negative boundary is retained: the
separate discrete-gradient rule preserves total energy but generally
does not preserve the continuous GL(2) charge; the prescribed regular
finite branch is not canonical symplectic. Required public CI is pending
at this review's preparation. This review is not a Canon promotion.

## Prospective custody

The immutable pin is f19fa98dc1634ce1e17b9dec402c51920d2bea8d, based
on public main 4d345bf1c73da73c1922fdba9893ee5644742275. The public
pre-execution receipt is:

https://github.com/mathorn1973/twist-j/issues/1686#issuecomment-6296327470

That receipt records full six-file public readback, equality to local
committed bytes and matching Git blob identities before any scientific
execution. The coordinator read back the receipt before the first run.
The security reviewer independently fetched and read the public receipt,
checked the local file sizes and manifest, and found no changes to the
six frozen files relative to the pin. The frozen manifest is 380 bytes,
SHA-256 a77afe20096bf13b0a13e42bce91668eaf6f6b1d14cf1853cd89a338cee0b20a.
It binds PREREG.md, PROOF.md, SOURCE.md and the two programs. The source
document separately binds the five normative and three administrative
authority files; Public Canon v103 remains unchanged.

Pre-pin review used source reading, analytical derivation, AST parsing
and byte/whitespace checks only. No scientific dry run, import or fixture
evaluation preceded the public pin. Two wording issues were resolved
before pinning: field-exact finite audits were distinguished from the
real universal phase-space proof, and comparison of completed certificates
was distinguished from using companion output to derive scientific values.
Neither change followed an observed scientific execution.

## Analytical scope reviewed

The common action varies the full SPD inverse metric and symmetric
momentum, with the explicit positive kinetic choice tr(G Pi G Pi)/2.
Occupied covectors are continuously varied, while integer multiplicities
are fixed labels. The weighted term n_k p_k^T dx_k is essential: it gives
the stated individual velocity without an extra multiplicity factor.
The source is the derivative of E, namely T/2, rather than the distinct
mass-square derivative. Frobenius pairing includes both off-diagonal
entries. No scalar h-map, M0 transfer or old scalar Ward law is inherited.

The displayed variations yield reciprocal metric/matter energy exchange.
The GL(2,R) transformation preserves the common one-form and Hamiltonian;
the direct derivative of J=2G Pi+sum n_k x_k p_k^T vanishes. This is
coordinate covariance of the declared model, not an admitted physical
gauge or Lorentz interpretation.

The global argument uses conserved nonnegative energy to bound the metric
logarithmic rate. It keeps G uniformly positive on each finite interval,
bounds Pi and positions there, and supplies continuation of the smooth
vector field. The long-time conclusion uses the bounded monotone quantity
C=tr(G Pi), Cdot=-E/2, integrability of E and its relative derivative
bound. These are universal analytical arguments, not extrapolations from
the 224 finite trajectory cases. For full-span matter G approaches zero only
at infinite time; G is the inverse metric, so this is not a claim of
physical spatial collapse. No-equilibrium and no-periodic-full-orbit
statements do not constitute a universal gravity or binding no-go.

The exact time-one map is a sampled complete Hamiltonian flow. Analyticity
and symplecticity do not supply a rational formula or a native integer
update. The clock pair with constraint p_t+H=0 is separately declared;
it is not deduced from a free-lapse constraint H=0.

For the DG relation, rectangular-path polarization proves the kinetic
difference identity without assuming commuting matrices. Difference of
squares proves the matter identity. Their combination preserves H, while
the midpoint product identity gives the actual charge defect. The cubic
defect at initial Pi=0 applies to the unique small-step branch. The finite
witness gives a separate regular nonsymplectic branch: its scalar
Jacobian ratio differs from one, and the proof checks full metric
regularity with the traceless blocks before restricting the symplectic
form. Neither all-step solvability nor connection of that witness to the
small-step branch is claimed.

## Implementation independence and checks

Two isolated authors received the same current contract and proof. Neither
read a companion implementation or predecessor scientific program. The
primary uses rational-pair field arithmetic, binomial roots and triangular
coefficient recursion. The breaker independently uses normalized integer
triples, root-square/reciprocal recurrences and four formal Picard passes.
They share no scientific module or result table.

Full static source review checked the fixed case order, occupied-slot
handling, formal truncation, actual invariant calculation and payload
serialization. Both compute the state and invariant coefficients, including
nonzero coefficients, before checking the predicted balances. The breaker
certificate is compared only after the primary independently constructs
its own certificate. No expected payload digest is supplied to either
calculation. The finite audit includes equation residuals, derivatives,
covariance, a finite exchange witness and eight false alternatives; it
does not turn the analytical global theorems into finite enumerations.

The coordinator and reviewers read the proof and the completed sources
and knew the prospective predictions. This is same-session review with
isolated implementations, not external blind review or independent
discovery of the mathematical model. Reviewer access to both finished
programs does not erase the authors' implementation isolation, but the
common contract and proof remain shared assumptions.

## Security and file scope

The complete primary source was reviewed at 29132 bytes, SHA-256
64fa4fd8198d778185d5c5e4cd7429accfc2f2d002bf284746ffbc7df922e104.
The complete breaker source was reviewed at 33090 bytes, SHA-256
88adb0ddf7d4028673c4834b59c7f154dd5e4131d1596f989178f09a8c83e4d4.
Both are standard-library-only and read only the five fixed authority
files as data. They do not read EXPECTED.txt, run/result records,
predecessor code, network resources, environment secrets or private paths.
Neither writes files or dynamically evaluates code.

The primary's sole subprocess invokes the sibling breaker using the same
interpreter with -I, shell=False, closed standard input, captured standard
output/error, a fixed minimal environment and a 540-second timeout.
It requires exit zero, empty stderr and raw certificate equality. The
breaker launches no subprocess. Outputs are the declared certificate or
deterministic falsifier text on standard output. Unexpected primary
exceptions are not converted into scientific PASS or FAIL.

The prospective bundle contains only one probe directory. It changes no
Canon file, policy, workflow, dependency or external service. No secrets,
private infrastructure details or imported historical archive payload were
found in the reviewed files.

## First formal outcome and remaining gate

The reviewer directly read EXPECTED.txt, RUN.md, RESULT.md and the original
captured standard output and run metadata. Byte counts and SHA-256 of
EXPECTED.txt and the original stdout agree. The completed run began at
2026-10-20T16:54:33.441922Z, after the public pin receipt created at
2026-10-20T16:54:22Z, and finished at 2026-10-20T16:55:06.454291Z.
The first-run record reports Ubuntu 24.04.3,
x86_64, Python 3.12.14, elapsed 33.012 seconds, exit zero and empty stderr.
The exact standard output has 431 bytes and 17 LF-terminated lines,
SHA-256 a59dd2310ae9f3bface7a738c561a7290d9fe4af2e4d39a5f048b771f1ca2642.
It reports identical independent certificates and RESULT=PASS. The
2550-record in-memory payload has SHA-256
330fb22412f54c6dae1a434d74adf1f68d3e1cfea8b31bbcf59d6e2c0c01caee.

The positive finite result covers 32 count preparations, seven metric
momenta, 224 trajectory cases, order four, 1120 coefficient rows per
method, six covariance cases for both methods, one finite exchange case
and eight detected negative controls. The finite witness transfers
K:0->1 and E:6->5 while H stays six. Its charge change is
-(792/1921)I and its scalar Jacobian ratio is 528275/341526, not one.
These predicted defects are confirmed scope boundaries, not suppressed
failures or changed thresholds.

No additional scientific execution was needed for this review. Required
public x86_64 and aarch64 replay at one PR head, exact stdout comparison,
and policy/Canon/ledger/gate checks remain the publication gate. A later
separately declared public fold is required for any Canon promotion.
No physical metric selection, spatial propagation, stable particle,
native realization or inertial/gravitational mass equality is established.

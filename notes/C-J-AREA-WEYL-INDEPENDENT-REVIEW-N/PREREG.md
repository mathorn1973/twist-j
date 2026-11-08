# Six-field preregistration for independent R1 review

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Candidate: C-J-AREA-WEYL-INDEPENDENT-REVIEW-N.
Review session: Codex-R1-20261017-b053a37f.
Claim: https://github.com/mathorn1973/twist-j/issues/1587#issuecomment-6241658252
Target head: e40b637b81f1a6fca99a543e970c83a4e0d45ebc.
Source pin: 6b459a66d670656bd02a09c26da666bd16c077fb.
Authority: ACTIVE Public Canon v103, main/tag
 dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content
 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66.

## 1. Equations and claims under attack

Let O=Z[x]/(1+x+x^2+x^3+x^4), j=[x], J=1+j^2,
phi=-j^2-j^3. The marked O-bilinear form on O^2 is
omega((a,b),(c,d))=ad-bc, and T=diag(J,phi).
Independently prove J*phi=j, invertibility over O, covariance
omega(Tu,Tv)=j*omega(u,v), and preservation by T^5 on the entire
infinite O^2 class. Preserve the one-step counterexample u=(1,0),
v=(0,1). Fifth-step form preservation does not assert T^5=I.

Independently derive O/(1-j)=F5 and the quotient map rho by evaluation
at 1 modulo 5. Verify rho(j,J,phi)=(1,2,3), A=diag(2,3), and exact
finite-field area preservation. The nontrivial complex root j is erased
by reduction; a chosen complex character is additional structure.

On a separately selected five-state module, using rightmost-first
operator composition, define Z|k>=j^k|k>, X|k>=|k+1>,
W(a,b)=Z^a X^b, D|k>=|3k>. Derive the full product cocycle, inverses,
ZX=jXZ, DZD^-1=Z^2, DXD^-1=X^3 and the covariance of all W labels.
The commutator factor is j^(ad-bc) for u=(a,b), v=(c,d).
Classify every additive character F5 to mu5, including the trivial
character and the four faithful marked characters.

Classify the entire rational diagonal D-invariant cost space, not merely
a finite sample: H=diag(h0,h1,h1,h1,h1). Its intersection with full X/Z
commutation is scalar. Positive gaps 1 and 2 delimit energy-scale
nonselection at exactly this class; they establish no blanket physical
no-go or claim about all non-diagonal costs.

## 2. Independently authored code and exposure

The accepted executable is break.py in this directory, standard library
only, with no imports of source-author code or runtime data dependencies.
It represents cyclotomic elements by five cyclic integer coefficients
modulo the all-ones relation and uses exact dense five-by-five operator
matrices derived from basis actions. Rational costs use Fraction.

The code, PROOF.md, this preregistration, source custody and exposure
record are committed, pushed and publicly read back before the first
scientific execution or import. Only static source analysis, AST parsing,
compilation, file hashes and analytical derivation precede that pin.
No dry run or numerical scratch computation is allowed before it.

Only the author's original PREREG and registered Canon inputs have been
used. Exposure details are in EXPOSURE.md. The advertised conclusions
are already disclosed; the claim is method-blind relative to #1583,
not result-blind. Collaborating subagents belong to the same reviewer
session and do not add independent scientific authors.

## 3. Carriers and frozen finite inventory

The infinite theorem carriers are O^2 and the full rational diagonal
cost space. The independent proof carries their universal quantifiers.
Finite computation is an audit of that proof, not its replacement.

The mandatory finite inventory is:

- All 16 ordered products of the four integral ring basis elements for
  residue multiplicativity; exact cyclotomic relations and unit inverses.
- All 64 ordered pairs of the rank-eight integral basis of O^2 for the
  one-step covariance and fifth-step preservation, with inverse checks.
- All 625 ordered pairs of F5^2 vectors for A-area preservation.
- All 25 Weyl labels for D conjugation and inverses, all 625 ordered
  label pairs for the product cocycle and commutator, and generator
  identities evaluated as complete operator matrices.
- All four faithful characters, their additive laws, distinctness and
  kernels; all 625 ordered vector pairs for each character's A-area law.
- All 3125 rational diagonal costs with coordinates in {-2,-1,0,1,2},
  comparing matrix conjugation/commutation against the complete proven
  orbit criterion. A symbolic rational linear-constraint audit checks
  the full fixed space. Explicit positive gap-1 and gap-2 witnesses.

No random seeds, datasets, target measurements, floating-point scientific
assertions or runtime network/file inputs are used. Code fixes additional
algebraic consistency checks before the pin; it may not add a new gate
or adjust a threshold in response to execution.

## 4. Systematics and deliberate negative controls

Arithmetic is exact in Z, Q and F5; tolerance zero. Composition order and
central scalar phases must be tested explicitly. The cyclic-coefficient
representation is independently written from the author's mathematical
specification, not obtained by reading or copying the author's verifier.

Known negative controls are required outcomes: one T step need not
preserve the O-valued form; rho(j)=1 cannot transmit a nontrivial complex
phase; four faithful character choices coexist; D covariance allows
inequivalent positive cost gaps. These restrict conclusions and are not
scientific failures of the correctly scoped conditional claims.

Neither the chosen O^2 step T nor the Weyl module is identified with the
original autonomous native U. No physical character selection, native
contact, source realization, action S, h/hbar, frequency sign, SI scale,
common physical carrier or unnamed L1-to-L6 lift is admitted.

## 5. Failure threshold, pin and execution

Any false mandatory identity, wrong inverse/central phase, missing finite
case, mismatch with the complete cost class or contradicted scope is a
falsifier. Preserve the exact scientific FAIL or FALSIFIER output and do
not repair or reinterpret the pinned code. A Python exception, timeout,
nonzero exit or stderr is an execution failure, not a successful audit.
Explicit scientific PASS plus exit 0 and empty stderr are all required.
A failed independent pin remains public with its disposition; a repaired
question would require its own prospective protocol.

After public pin/readback and PINNED_R1 receipt, run from the repository
root with LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1:

`python3 notes/C-J-AREA-WEYL-INDEPENDENT-REVIEW-N/break.py`

The per-run timeout is 600 seconds. Capture stdout and stderr separately
as bytes. Record exact pin, code/input hashes, neutral OS/architecture/
Python version, start/end time, exit status, byte counts and hashes.
The first completed output becomes EXPECTED.txt without normalization.
Attempt explicit x86_64 and aarch64 executions of the same public pin;
report only architectures actually obtained and exact byte equality.
This notes-only executable is not selected by ordinary probe/reproduction
CI, and green CI must not be described as its execution.

Only after the own pin and initial run may the source-author proof,
verifier, result, stdout and run record be opened for comparison. Record
that later exposure and claim-by-claim dispositions in REVIEW.md.
CONFIRMED_IN_SCOPE requires both the independent proof and successful
frozen audit; a counterexample yields COUNTEREXAMPLE, and an unresolved
proof/custody/execution gap yields STOP_INCOMPLETE at its actual scope.
No finite PASS proves an unbounded claim by enumeration alone.

## 6. Action layer and handoff

L1 mathematical review only, PUBLIC / NON-CANONICAL. The output is a
separate draft PR, with REVIEW.md, RESULT.md and a scope-limited PROMO.md.
No author source, Canon, Registry, Gates, workflow, policy, old pin,
merge, tag or release is changed. Existing native/physical obligations,
including METRO-EDGE-SCALE, remain open. R2 and N are outside this claim.

Final checks are policy, infrastructure unit tests, Canon, ledger, gate
contract, changed-path probe/reproduction checks, whitespace and named
file security review. The latter changed-path checks are expected to be
NOT APPLICABLE for a notes-only change; state the actual results.
Post SUBMITTED_R1 with immutable result SHA and draft PR, and a metadata
link on parent #1586. Operational completion creates no Canon status.

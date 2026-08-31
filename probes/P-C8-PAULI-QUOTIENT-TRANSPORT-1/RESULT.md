# P-C8-PAULI-QUOTIENT-TRANSPORT-1 result

Status: SCIENTIFIC RESULT; LOCAL EXACT AUDIT PASS; REQUIRED TWO-ARCHITECTURE WORKFLOW PENDING; PUBLIC CLAIM UNREGISTERED.

## Recorded decision

    verdict: 7/7 ALL PASS
    exit: 0
    stderr: empty
    stdout: 664 bytes, 8 lines; identical to EXPECTED.txt

No frozen falsifier fired in the local audit. The negative statements in G5
and G7 are proved boundaries, not failures of the probe. The independent
universal proofs are in the immutable PREREG.md; the verifier audits their
finite field, exponent, and operator-basis ingredients.

## Earned mathematical scope

**Exact quotient.** Restriction gives a bijection
E/<sigma> -> Iso(F5*,mu4), with fibres {1,5} and {3,7}. On normalized generator
matrices these are exactly the left-Z classes. The extra equality
X P_k X=zeta8^k P_-k would merge the remaining orientations if input/output
frame relabelling were also adopted. It is not adopted here.

**Conditional positive transport.** The explicitly supplied dictionary
marking beta_+(2)=i determines exactly the first extension orbit, not one
extension. On the COMPLETE already registered C8-BILINEAR-SHADOW record,
all indices and contexts included, both extensions give exactly beta_+(V):

    Theta_n             -> i^s2(n),
    Y_n, s2(n) even     -> i^(3 s2(n)/2),
    Y_n Y_m, both odd   -> i^(3 (s2(n)+s2(m))/2).

No branch selector, new coordinate, lost component, or new physical gauge is
needed for this equality. The four-character readout family has exactly the
two displayed fibres; Theta_1=2 separates them. All these output scalars are
in mu4. Their diagonal gate realization is an S power, not a non-Clifford
output. This is a complete transport for this named multiplicative record,
not a quantum-state, apparatus, or universal-computation bridge.

**Exact scalar boundary.** A nonzero scalar monomial tau^n is invariant under
the character-branch flip iff n is even. For a product the total exponent
must be even. Mixed-parity Y products therefore do not descend. This is not
an assertion about all possible nonlinear readouts.

**One-copy readout obstruction.** In the complete frozen class of fixed
real-linear expectation readouts on one externally supplied qubit, branch
invariance for every density matrix is equivalent to [A,Z]=0, hence to
A=aI+bZ. It therefore destroys sensitivity to ALL diagonal phases. The
operators themselves are not equal: P_k|+> and ZP_k|+> are orthogonal.
A known correction bit can be tracked and compensated; forgetting an unknown
correction is a different operation.

**Two-use positive control.** Applying the SAME P_k to both factors of an
externally supplied Bell pair produces (|00>+i^k|11>)/sqrt2. A common Z tensor Z
branch acts trivially there, and fixed X tensor Y has exact eigenvalue +1 for
{1,5}, -1 for {3,7}. A branch change on only one factor reverses the result.
This is a comparison construction with a fixed reference and labelled
outcomes. It is not a physical implementation of V or a derived common-branch
law for TWIST-J.

**Involution and norm obstruction.** A faithful character cannot intertwine
source Frobenius (exponent 5) with complex conjugation (exponent -1): only
k=0,4 satisfy 6k=0 modulo 8. Specifically N(tau)=3 maps to -i under beta_+,
whereas every complex character image of tau has modulus squared 1.
The transport is not additive either. Multiplicative descent must not be
called a Born-norm or field embedding.

## Status and provenance boundary

I-BILOCATED remains [D]. G2 formalizes the marking; it does not prove that this
marking is forced by J or that the older witness already implemented this
complete map. The positive result is conditional on the existing dictionary
comparison and the exact declared source record. The source involution,
complex conjugation, global scalar sign, left Pauli correction, input/output
frame change, and common versus independent branches remain different types.

No Canon, Registry, Frontier, definition, gate, dictionary, physical claim,
workflow, previous probe, or L2-L6 status is changed. Issues #716 and #721
remain outside this result's disposition. Registration requires a separate
reviewed fold. The earlier claim that a branch could be discarded merely
because it is a Pauli operation is not used.

## Immutable pin and local record

    public lock: issue 724
    base: 9f88c4c93aab3139ee0a2e007f0e60891957aa21
    preregistration pin: 9a9a54abb09eb053e379b288214e16aaaa1165e9
    pin tree: 89e8948194cc6e0815233f65f5a43801adbbd5f3
    PREREG.md SHA-256: e14d76de51c9c2d666c8baba008d16a73c2c12a20da320ec0bbbbe97b822bd35
    verify.py SHA-256: 091c2c924ab4ce530e556ebd8c99a128abc8b76bfb7ac764217efb8de452de2f
    stdout SHA-256: 7b947696bae49095be87d37d6551825537b67c7833df5405953d9b75dc3e79c6
    stdout bytes/lines: 664 / 8
    local platform: Debian GNU/Linux 13 (trixie), x86_64, CPython 3.13.5
    exit/stderr: 0 / 0 bytes

RUN.md records the local payload-only audit honestly; it does not claim a full
local repository checkout. The pinned files matched their immutable public
blob IDs before execution and remain unchanged afterwards.

## Required two-architecture workflow

Pending at this result commit. No architecture count, repository checker,
or manual security review is inferred from the local mathematical audit.

# C-FIELD-J-ENERGY-READOUT-N

**PUBLIC, NON-CANONICAL. Prospective L1 candidate; no earned result or Canon
change.** Owner: A. M. Thorn / root/algebra_builder session, coordinated by
root. Original work under Apache-2.0. Prepared 1 October 2026.

Public reservation: [issue #1323](https://github.com/mathorn1973/twist-j/issues/1323).

## 1. Basis, custody and exposure

The admitted scientific basis is public main and dereferenced canon-v96 at
`44423153eee6259c7277eec5f5adbed9679f9146`, content commit
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`, CANON.md 873495 bytes,
SHA-256 `eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
The coordinator owns the live authority, collision, issue and pin checks.
The public issue reservation and immutable candidate commit must exist before
execution. This local document does not reserve an issue or create authority.

Read inputs at that basis: STATUS.md, POLICY.md, AGENTS.md, canon/CORE.md,
canon/FRONTIER.md, the relevant REGISTRY/EVIDENCE/DEPENDENCIES/GATES rows;
the complete shared proof of FIELD-CONSERVATIVE-CHAIN-LAW,
FIELD-CHAIN-FIRST-WORK and FIELD-LOCAL-WORK-RECORD in canon/CANON.md;
J-TWO-TRACE-RESIDUE-INVERSE, J-OBSERVED-SCALAR-CODE-CAPACITY,
U-NORMALIZED-SCALAR-READBACK, QDD-GALOIS-SUM-RATIO,
U-COUNTER-REACHABLE-AMPLITUDE-CLASS and the B0/LOW definitions there;
the public PROOF.md evidence of P-J-TWO-TRACE-RESIDUE-DECODER-1,
P-ZETA5-RESIDUE-STRIP-DECODER-2 and P-U-COUNTER-AMPLITUDE-CLASS-1.
Public verifier sources were inspected as inherited evidence, not imported
or executed by this candidate. The current tools/check_verifier.py procedure
was inspected. No other unpublished builder script is an input.

The dispatch brief is a noncanonical scope instruction. It exposes historical
targets: 291 states at H<=5, shell counts (1,20,30,60,60,120), maximum norm 31,
and the two LOW ratios 0 and 5/16. They are preregistered audit targets, not
new discoveries or justification for choosing a search box. The exploratory
note, script and output named in the brief were not supplied to this builder
and have not been read or rerun. No claim about their contents or custody is
made. No scientific execution has preceded this prospective pin.

## 2. Frozen carriers and equality

Use the unchanged active field matrices A_f, B_f, P and L in the v96 shared
proof, and call its Jcyc matrix C_cyc. Set O=Z[j] with
1+j+j^2+j^3+j^4=0, conjugation j -> j^4, phi=-j^2-j^3 and J=1+j^2.
The exact chart is y=C_cyc a, alpha=sum a_i j^i. Equality of fields or scalars
means equality of all four ordered integer coordinates, without phase or
sign quotient. The two virtual observations are e0=H(y), e1=H((I+A_f^2)y),
H(y)=y^T B_f y/2. No acquisition operation is presumed.

The bounded source domain is exactly K5={y in Z^4:H(y)<=5}, including zero.
The observation is (e0,e1,r), where r is the four canonical coefficient
residues of C_cyc^-1 y modulo 5, each in {0,1,2,3,4}. No external clock or
source label is supplied. The inverse returns the ordered scalar coefficients
and active field, or rejects. A syntactically accepted input is a tuple of
length three containing two genuine Python integers (booleans excluded) and
a tuple of four genuine canonical integers. Other input shapes reject.

For the additional mathematical QDD comparison, the context is the fixed
ordered B0=(1,j,j^2,j^3) and fixed LOW line Q(1+j+j^2+j^3), with the registered
trace pairing Tr(x bar(y))/5. For the two sources, the coefficients lie in
the registered balanced piston cube [-2,2]^4. This new identification of
field chart coefficients with those pistons is a stipulated L1 comparison,
not a physical field/QDD dictionary. QDD record equality and field equality
are distinct; no quotient by multiplication by j is used.

Receiver blindness refers exactly to the v96 positive preparation for every
finite N>=2, every integral H(w)=1, source (R,0,PLw,0), ZM intermediates,
receiver (R,0,0,0), zero channels and pointer p=0. Compare the complete
receiver 31-tuple and p, including every actual substep in the fixed
Ghat;A;B;F chronology. No reader receives the source field, initial seed or an
external log. The stronger comparison used in the proof is equality of all
stored coordinates except the source raw field. Every other preparation is
held exactly as stated; arbitrary preparations are outside this theorem.

## 3. Frozen claims and falsifiers

A. Prove for all integral y, by exact coefficient comparison, that
J_f C_cyc=C_cyc M_J, alpha bar(alpha)=u+v phi, e0=u+v, e1=u,
S(alpha)=e0+e1, S(J alpha)=4e1-e0 and
N(alpha)=-e0^2+3e0 e1-e1^2. Here J_f=I+A_f^2 and S=Tr/2.
Distinguish the actual conservative A_f from the virtual, generally
nonconservative J_f and exhibit an exact energy-changing vector.

B. Prove the containing coefficient box
[-3,3] x [-2,2] x [-2,2] x [-3,3] before enumeration. Prove N<=31 on
K5-{0} and the sufficient modulo-five injectivity inequality 5^4>16*31.
Provide a terminating exact image recognizer for every input, including zero,
malformed input, impossible traces and residues that fit no admitted scalar.
Check the exposed shell counts and norm maximum without changing the box.

C. With w1=(0,0,1,0), w2=A_f w1=(1,0,-1,1),
ell=(1-j)(1-j^2), prove the exact source chart alpha1=ell, alpha2=j ell,
their equal energies and traces, and q_LOW=(sum a_i)^2/[4 Tr(alpha bar(alpha))]
equal to 0 and 5/16 at the fixed context. This is not discrimination of a
global complex Hilbert-space phase, coherent transport or a probability law.

D. Prove by induction over every actual layer that all H(w)=1 positive
preparations have identical complete receiver histories for all forward
time. Explicitly cover the source AM-to-R reversals, resource returns,
funding rejections and later pointer wraps. A simulation is only an audit.
The source retains distinct field data; this is a scoped inability of the
unchanged chain to convey that distinction, not a theorem against all
admissible transport laws.

Any exact failure of A-D or a frozen census target fires its corresponding
claim. Zero tolerance applies. A malformed-input crash or false acceptance,
false rejection, wrong returned tuple, coefficient identity mismatch,
uncovered valid point, seed-dependent receiver substep or incorrect context
comparison must be preserved. No threshold/domain change repairs a fired
claim after the pin. A custody, authority or execution failure is separately
reported and is not relabeled a mathematical theorem.

## 4. Accepted verifier and declared finite audits

verify.py is a new self-contained Python 3.10+ standard-library program. It
imports no project implementation, reads no runtime scientific data, uses no
float, randomness, network or architecture-dependent stdout, and writes no
files. Sparse exact multivariate polynomials with rational coefficients
verify full identities, including cyclotomic conjugation and all quadratic
and quartic coefficients; checking finitely many selected vectors is not the
identity method. Exact matrix products certify the chart and the quadratic
form inverse used for the coefficient bound.

The finite audits are fixed as follows:

1. Scan all 1225 tuples in the proved box. Filter H<=5, compute all shell
   counts and maximum norm, compare every key and inverse, and require the
   disclosed (291; 1,20,30,60,60,120; 31).
2. Exhaust all 52500 typed keys e0=0,...,5, e1=0,...,13 and all 625 residues.
   Compare acceptance and reconstructed values with the independently built
   finite forward image. These bounds contain every valid key by the norm
   inequality proved in PROOF.md. Also test every residue with e0 in {-1,6}
   and e1 in {-1,0,1,13,14,10000}, and with e0=0,...,5 and e1 in
   {-1,14,10000}. The exact malformed-input list is part of the pinned code.
   A valid-to-valid residue replacement remains accepted.
3. Check the two declared sources, their equal full energy/trace data, exact
   ratios, and the explicit virtual energy-changing witness.
4. From all H(w)=1 seeds in the complete shell, run N=2,...,6 for exactly
   80 forward macrosteps, comparing all four layer boundaries and the initial
   state against w1. Use literal complete matter triples, six raw-field
   coordinates, spectators, resources, channels and p. Audit the induction
   invariant and total energy 42 throughout. Include all-time theorem's
   source accept/reverse/reject and receiver accept/reverse/reject branches
   in this audit, and require their coverage.
5. Test local rejected branches with fixed literal fixtures: nonendpoint
   matter, nonsplit raw field, each failed image congruence, unfunded R at
   h=0 and unfunded AM at h=1. Verify full input retention. Also test each
   accepted endpoint at h=0 and h=1 with precisely sufficient funding.

The chain audit is finite and does not establish any period, universal time
bound, arbitrary preparation theorem or complete classification. Counts from
it are audit metadata, not native resource or physical dimensions.

## 5. Freeze, independent review and execution

The coordinator freezes this preregistration publicly before commissioning
the fresh independent reviewer. The reviewer receives this file and the
admitted canonical input list, not builder verify.py, PROOF.md, outputs or
diff. Its own derivation and breaker are frozen before comparison. Known
public targets above remain disclosed; implementation blindness must not be
called result blindness. The independent reviewer owns no builder files.

Freeze PREREG.md, PROOF.md and verify.py in immutable Git with file SHA-256
before this verifier executes. The coordinator records issue and commit
links and performs public byte readback. No commit, push or execution is
authorized by this file itself. Before that signal, only static parsing or
compilation and source review are allowed. Do not amend a scientific pin.

Prospective command, from repository root in a Linux-compatible environment:

    python3 notes/C-FIELD-J-ENERGY-READOUT-N/verify.py

Use the repository's current 600-second per-verifier envelope and deterministic
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1.
Record actual pin/hash/command/neutral OS, architecture and Python version,
exit code, stderr bytes/hash and exact stdout bytes/hash. Only after execution
may EXPECTED.txt, RUN.md and RESULT.md be added under this directory, with
the exact output, actual scope and fired falsifiers. A notes verifier is not
automatically included by the probe-only changed-path runner. A formal probe
or promotion would require its own current procedures; no two-architecture
gate is claimed from a single local run or ordinary notes CI.

## 6. Status ceiling and interface boundary

A-D may warrant candidate-T only after complete proofs survive review. The
finite census is candidate-C evidence pending actual execution and required
reproduction. Current inherited rows keep their exact statuses; the
norm-941/3125-label scalar codebook still needs its registered full modulo-25
interface. This small H<=5 sector changes none of that theorem's domain.

The prospective transport interface is the literal active field y, its exact
scalar chart, and the K5 observation/inverse with fixed B0 context. Obtaining
the two energies and residue is an assumed mathematical observation. No new
dynamics, native-U realization, full instrument, post-state, physical energy,
occurrence/Born law, L2-L6 lift, apparatus reset, photon claim or existing
open physical owner is closed. No promotion proposal is made before review.

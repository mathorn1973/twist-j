# P-QDD-UNINTERRUPTED-RECORD-1

Status: prospective formal preregistration; candidate-T; NON-CANONICAL.
Owner: A. M. Thorn / record formalization session 2026-09-20.
Public lock: #1085. Branch: probe/P-QDD-UNINTERRUPTED-RECORD-1.
Action layer: L1 throughout; no physical L1-to-L5 or L6 lift.

Public source: main 963cb34d6a68a09d93b611f32211d9a3bdc547b7,
Public Canon v90 ACTIVE, tag canon-v90 at
c7223ba461e264bde96eaedee4430704580235d3, content commit
b67d27bb291ec820cbc862d44dc225d0be93df3b. CANON.md SHA-256
8ff757009ab1e46a66e0d341d7e9408f5c93cb966633b3e1755083b081c6665f,
676201 bytes. Authority, ancestry, checksum and the required main checks
were verified before this formalization.

## Exposure, prior work and collision boundary

This is result-exposed formalization of the accepted proof note in PR
#1084, not blind discovery. Its path is
notes/C-QDD-UNINTERRUPTED-RECORD-N/README.md, SHA-256
82bc8dcd45bce6c4cbeb3c5a2b46d8e45dc188ee63533cc6ff3d4caed84e49fa.
The source/code input is probes/P-U-GALOIS-FIBER-CODE-1/PROOF.md,
SHA-256 414539dd4822df390b6bd811a0811783e551079edc9b997156cb1d17142c036f.
No earlier probe pin is reused or altered.

Fresh main, all remote heads, issues, registry and probe paths were
searched. #1083 is the completed notes claim. The elementary signed port
law is already known from #1002; #997/#998 and #1038 own distinct actuator
and optical-comparison questions. This probe owns the complete controlled
write/native waiting/signed archive restoration theorem and its coherent
state interpretation. Fixed-reader no-write results remain intact.

The user explicitly requested full formalization after reviewing the
note. The connected GitHub identity is authorized for this public work,
as in the preceding accepted probes. The accepted verifier and separate
breaker have not been executed or imported before the public pin. Their
authors know the target conclusion; the breaker author does not read or
import verify.py. Static syntax inspection is allowed before the pin.

## 1. Equation

Freeze X=F5^6, x=(a,b,c,d,q,r), p=(a,b,c,d), s=sum(p), z=s+q+r.
Use exactly the five native generators and F_t(x)=g_(z+2t)(x), t in {0,1},
written in PROOF.md. The stable union is X14={z in {1,4}}. N_(n,k) is
the chronological k-step checkpoint propagator at native counter n;
k=0 is identity. The same formulas also apply to every finite bit word.

Define the paired translation and admitted controlled writer by

    T_delta(p;q,r)=(p;q-delta,r+delta),
    h_n(p)=(-1)^(n-3)s(p), n>=3,
    f=(0,1,2,2,2) on F5,
    C_n(x)=T_(f(h_n(p)))x.

On a fixed common stable sheet, propagate a source-independent reference
r_n^0 under the same bits. For the canonical endpoint code the reference
starts at z_3=1,r_3^0=0. With N=n+k, epsilon=(-1)^k and an explicitly
admitted passive F5 archive cell m, define

    S_N^epsilon(p;z,r;m)
      =(p;z,r_N^0+epsilon*m; epsilon*(r-r_N^0)).

The primary claims are:

G1. The stable selector uses only b,d,e. For both bits and every stable
    point, F_t T_delta=T_(-delta) F_t. Hence every finite word obeys
    N_(n,k)T_delta=T_(epsilon*delta)N_(n,k), with identical p,z and selected
    generators at every intermediate tick of the paired trajectories.
G2. h_n is transported unchanged. After C_n an initially ready port holds
    the inserted mark as (-1)^(j-n)(r_j-r_j^0)=f(h_n(p)) throughout
    n<=j<=N before the exit operation, arbitrarily long if exit is delayed.
G3. C_n is a global permutation and S_N^epsilon a global involution.
    With e=r_n-r_n^0, the complete admitted protocol gives
    (e,m)->(epsilon*m,e+f). Thus a blank cell and e=0 restore the full
    freely evolved checkpoint and archive f. The stronger pointwise
    identity S_N^epsilon (N_(n,k) x I)(C_n x I)
    =(N_(n,k) x I)S_n^+(C_n x I) holds for arbitrary e,m on the chosen
    common-z sheet and matching reference trajectory.
G4. For the canonical W_n, P_L=ones4/4 and P_H=I-P_L, the coherent output
    of a ready port and blank cell is
    W_N P_L v x |1> + W_N P_H v x |2> for every source amplitude v.
    Every HIGH/HIGH matrix unit is preserved. Formally discarding the
    archive removes exactly LOW/HIGH cross terms; pointwise restoration
    does not restore a general uncorrelated source/archive state.
G5. Repetition with fresh passive cells on the same transported observable
    yields W_N P_L v x |1,...,1> + W_N P_H v x |2,...,2>, not independent
    trials. Nonzero e contaminates the archive by e; nonzero incoming m
    returns its content to the port; an omitted odd-wait sign changes f
    to -f; outside X14 the c generator has a nonzero source displacement.

These are universal algebraic assertions with induction and full matrix
proofs. No bounded run stands in for the all-word or all-amplitude claims.
The admitted entrance and exit operations are not asserted to be native U
words, physical effects, or a read-only feeds_U=false implementation.

## 2. Code

Freeze PREREG.md, PROOF.md, verify.py, break.py, BREAK.md,
ENTRANCE-CONTRACT.md and FOLD-PROPOSAL.md together before any scientific
execution. The two programs use only the Python standard library, exact
integers modulo five and integer or Fraction arithmetic in Q[j]/(Phi_5).
They import no existing probe, use no network, floating point, sampling,
external library or mutable runtime authority file.

After byte-identical public readback, run from the repository root:

    python3 probes/P-QDD-UNINTERRUPTED-RECORD-1/verify.py
    python3 probes/P-QDD-UNINTERRUPTED-RECORD-1/break.py

The main verifier audits the full stable one-step carrier, global writer
inverses, reduced exact displacement/archive bookkeeping, bounded word
and actual-time witnesses, the cyclotomic W/Gram/projector identities,
all sixteen endpoint matrix units, repeated coarse records and deliberate
boundary failures. The independent breaker reconstructs affine homogeneous
matrices and reduced port/coherence identities separately. BREAK.md records
its methods and written proof review. No EXPECTED or RUN is inferred from
either author's static review.

## 3. Carrier and fixed finite audit data

Complete stable one-step audit: 6250 checkpoints, both driver bits and
all five delta values, 62500 cases. Global C_n inverse audit: all 15625
points and both n parities, 31250 cases. Signed exchange: both signs and
all reference, port and archive values, 250 cases.

The composition audit may represent p by its five sums, because C and S
depend on p only through that sum and the complete one-step audit already
checks the unchanged full p trajectory. It exhausts the stable z, both
writer parities, r_n^0,e,m and zero/one-step bit words: 7500 reduced cases,
representing 937500 choices with all 625 source points. The proof supplies
the induction to every longer word.

Bounded integration witnesses: every bit word of length 0 through 6 on
the four canonical endpoint bases; actual native start times n=3 through
35 inclusive, with waiting lengths k=0 through 16 inclusive. These fixed
ranges check conventions and composition, not universal time coverage.

For the coherent part reconstruct W_3 over Q(j) from the public Hadamard
and Galois formulas. Check W_3^dagger W_3=G, D_L W_3=W_3 P_L, and all
16 matrix units in the endpoint basis. Distinguish six off-diagonal HIGH
units from six LOW/HIGH units. Include an explicit cross-branch input
whose basis trajectories are restored but whose reduced source state
differs after discarding the archive. Include two sequential records of
one observable for every pair of bit words of lengths 0 through 3 on
all four code bases (900 cases), with no interpretation as independent
preparation.

All negative controls and bounds are fixed in the proof and code before
execution. No measured payload, normalization fit, empirical tolerance or
physical occurrence distribution is admitted.

## 4. Systematics

Keep source coordinates before W distinct from endpoint amplitudes after
W. Preserve the QDD source Gram and all cross terms, not only four basis
populations. The full joint source/archive equality is the coherent claim;
the reduced source generally changes on LOW/HIGH coherences. Partial trace
is a mathematical operation, not a new event-selection law.

Use the common-z reference appropriate to the starting sheet. Do not use
one reference across incompatible sheets, assume invertibility on their
union, replace the current ready by r=0, confuse a time-local propagator
with an origin-zero prefix, or omit parity in the exit exchange. The
global extension uses f(h_n), not f(a) away from the time-three code.

First executions use LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and TZ=UTC. Record stdout bytes, lines, SHA-256, exit code,
empty stderr, verifier and pin hashes, neutral platform, architecture and
Python version. Public acceptance needs the unchanged x86_64 and aarch64
workflow outputs matching the one committed EXPECTED.txt, plus aggregate
check. The independent breaker is not counted as another architecture.

## 5. Failure threshold

Any exact failure of G1-G5, any intermediate source/trace deviation inside
the stable paired-translation scope, an incorrect matrix unit, or failure
of any fixed finite audit rejects the affected candidate assertion. A
physical construction outside the stated admitted maps does not falsify
the algebraic theorem and is not counted as its realization.

A failed code/custody/incomplete run is STOP and follows POLICY.md's
consumed-pin rule. Preserve completed mathematical disagreements. Never
edit the frozen proof, code, scope, time ranges or threshold after first
execution to rescue the same identifier. The scope may not be narrowed
to basis populations if a coherence assertion fails.

## 6. Action layer and disposition

L1 only: finite native states, exact coefficient spaces, point permutations,
linear extensions and formal density matrices. No physical preparation,
primitive interaction, apparatus completeness, event, occurrence, passive
material archive, fresh source, SI scale or L1-to-L5/L6 gate is supplied.

If the proof and exact audits survive, deliver the accepted formal probe
and a bounded proposal for two mathematical T rows in a separate Canon
fold. QDD-INSTRUMENT-APPARATUS and its O1/O2 owners remain open without
partial physical discharge. ENTRANCE-CONTRACT.md is a typed predefinition
for the next physical question, explicitly STOP-DEFINITION where its class
and realization data are absent. It does not authorize an unpinned new
scientific execution or insert C_n among native primitives.

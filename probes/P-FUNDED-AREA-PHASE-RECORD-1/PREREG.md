# Six-field preregistration: a funded loop with a quadratic path record

PUBLIC / NON-CANONICAL / L1. Probe P-FUNDED-AREA-PHASE-RECORD-1.
Owner: ChatGPT-funded-area-record-20261017. Author A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.
Reservation: https://github.com/mathorn1973/twist-j/issues/1584
Basis: Public Canon v103, main/tag dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d;
content 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66; CANON.md SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. All five normative hashes and both ancestries were checked.
Main x86_64/aarch64/check run 39022927713 is successful.

This is an exposed constructive comparison designed to realize a path-area
record. It is not a blind experimental prediction, a native U construction,
or a derivation of physical action. No scientific code has run. No existing
probe, Canon, Registry, Frontier, GATES, policy or workflow is changed.
The preceding #1582/#1583 area-Weyl proof remains noncanonical at its own pin.

## 1. Equations

Complete state s=(q,p,u,v,b,sigma,eta,c) belongs to
Z^4 x N_0 x {+1,-1}^2 x C4. Define the chosen cost

    H(s)=q^2+p^2+u^2+v^2,       E(s)=H(s)+b.

The unbounded integer bijections are

    Q_h(q,p,u,v)=(q+h,p,u,v),
    P_h(q,p,u,v)=(q,p+h,u+h*q,v+h*q),  h in {+1,-1}.

For a requested letter (axis,epsilon), set h=epsilon*sigma and form the
candidate t by Q_h or P_h. Put Delta=H(t)-H(s). If b>=Delta, perform the
candidate with b'=b-Delta and sigma unchanged. Otherwise keep q,p,u,v,b
and flip sigma. Eta and c do not change in this elementary map F_axis,epsilon.

G1: every F is a total permutation with inverse F_axis,-epsilon, including
occupied references, zero bank, and rejected moves; E and u-v are invariant.
The unchanged controller eta chooses one word:

    c=0: Q+,   c=1: P_eta,   c=2: Q-,   c=3: P_-eta.

Apply its current F and advance c modulo four. The full map U_* is an
autonomous permutation, not the registered U. Its inverse decrements c
and applies the opposite requested sign for that previous letter. Finite
control bits are explicit resources with zero assigned cost in this model.

Once-only reference preparation is

    s_B,eta=(0,0,1,-1,B,+1,eta,0), B in N_0.

For every actual path, including rejected steps, put

    A_path=sum_i q_i (p_(i+1)-p_i),
    A2=sum_i(q_i p_(i+1)-p_i q_(i+1)).

These are proof/audit quantities, not extra machine registers. G2:
u=1+A_path, v=-1+A_path, so the fixed current-reference reader obeys

    A_read=(u^2-v^2)/4=A_path,
    u^2+v^2=2+2 A_path^2,
    2 A_path=A2+q_final*p_final

for paths from q=p=0. A2/2 is the signed polygon area only on closed base
paths. No open-path geometric invariance or physical q/p meaning is assumed.
For arbitrary occupied u0,v0, the same displacement A shifts both references;
Delta(u^2-v^2)=2(u0-v0)A. A nonzero marked reference difference is required
for this difference reader. No global readback from squared costs alone on
all unprepared states is asserted.

Independently compute a chosen algebraic Weyl word on five basis vectors:
X|k>=|k+1>, Z|k>=j^k|k>, j^5=1 primitive. Each ACTUAL q move is X^dq,
each ACTUAL p move is Z^dp, and rejection is I. Chronological products act
on previous basis images. For a path based at q=p=0, test the complete law

    W_path|k>=j^(k*p_final+A_path)|k+q_final>.

Consequently, on integer-closed q,p paths, W_path=j^A_read I. This is an
algebraic character of the realized path, not a physical phase measurement,
not a global Weyl representation of the state-dependent funded map, and
not a statement about the nominal controller word when a gate rejects.

G3: for B=4, eta=+1 and eta=-1 both complete one square. Their H histories
are (2,3,6,5,4), bank histories (4,3,0,1,2), and their entire histories of
(q^2+p^2,u^2+v^2,b,sigma,c) coincide. Ordered reference costs differ and
A_read=eta, W_path=j^eta I. Therefore those coarse energy histories alone,
which deliberately omit eta and the ordered reference split, cannot recover
the oriented phase. No impossibility is claimed when the program direction
or richer data are supplied to the reader.

G4: for each K>=1, all first 4K steps from s_B,eta are accepted iff
B>=2K^2+2. In that case q=p=0 at the Kth loop boundary, u=1+eta K,
v=-1+eta K, b=B-2K^2 and W_path=j^(eta K)I. At K=5,B=52,eta=+1,
phase is identity but references are (6,4), costs (36,16), bank 2 and
paid reference work 50. Phase closure is not complete state restoration.

G5 controls: equal zero reference preparation loses orientation in their
squared endpoint costs for the +/- squares; B=3 rejects and the nominal
square no longer describes the actual path. Failed moves must not be
silently counted as successful phase operations.

G6: every fixed E=N shell of the complete U_* carrier is finite (at most
16(2 floor(sqrt(N))+1)^4 states), and U_* is a permutation of it. Every
state is periodic. No unbounded fresh record at fixed energy is possible.
On the prepared reference-difference class, 2+2 A_read^2<=E, hence
|A_read|<=floor(sqrt(B/2)). This is this model's resource bound, not a
universal energy/information bound.

## 2. Code

The only runtime source is verify.py, Python standard library, exact
integers. It contains a direct candidate-energy transition and a separately
written expanded-work transition (Delta_Q=2 h q+1;
Delta_P=2 h p+1+2 h q(u+v)+2q^2). They must agree on the whole frozen
finite inventory. Both are by the same author, not a blind second agent.
No external import, runtime file input, random choice, float or network.
Freeze PREREG.md, PROOF.md and verify.py in one publicly pushed commit
before the first execution. Record all bytes/hashes and read the pin back.
No code, preregistration, proof target or threshold changes after the pin.
Static parsing and security review only before pin; no dry runs.

## 3. Carrier and complete finite audit inventory

A. Enumerate ALL raw states with E<=12: q,p,u,v integers, b>=0, both sigma,
both eta, every c in C4. The integer box [-3,3]^4 is complete because each
square is <=12. For each state check four elementary gates, alternate
calculation, energy and reference invariants, exact inverse including
rejection; check both full-controller inverse compositions. Report actual
state/gate/rejection counts, not a preselected output count.

B. Enumerate all words over Q+,P+,Q-,P- of lengths 0 through 8, with one
common ready and B=2*8^2+2*8^4=8320. Bound |q|,|p|<=n and |A|<=n^2
proves every prefix affordable. For every prefix compare actual current
quadratic reader, the shoelace accumulator using only q,p endpoints, and
literal monomial action on all five basis vectors. There are
sum_(n=0)^8 4^n=87381 prefixes and
sum_(m=0)^4 binom(2m,m)^2=5341 integer-closed words. Hash all prefix
states, operators and geometric values in fixed traversal order. The
universal claims rely on PROOF.md, not extrapolation from these words.

C. Execute the opposite B=4 four-step autonomous histories. Check and print
complete state sequences, ordered-reference records and phase exponents.
For both eta, every B=0..80 and K=1..6, execute 4K actual controller steps
and compare full acceptance to the sharp analytic B threshold. After any
rejection, use actual displacements for the path and phase tests. There are
972 budget cases.

D. Execute K=5,B=52; the two zero-reference B=4 squares; the B=3 insufficient
budget control. Independently follow both eta B=4 full autonomous orbits
until a previously seen complete state, with the proved finite-shell bound;
the first repeat must be the initial state. Report the exact periods, not
an a priori specified period.

## 4. Systematics and scope exclusions

The once-prepared reference values, ordered access to their squared costs,
unit shifts and simultaneous record shears, equal quadratic cost weights,
nonnegative bank, two control bits, four-phase clock, and the mathematical
character j are ALL selected additions. The unitarity of the abstract
five-state monomial operators is not a physical Hilbert-space or Born-law
selection. No physical phase detector or measured energy-time relation is
provided. A scalar energy history is narrower than all machine information.
The coefficient four in the reader comes from the selected reference gap
two, not from an unexplained appearance of h or a derivation from J.

The cost is positive and coercive on the integer coordinates, so this is
not an unbounded zero-cost history register. A finite zero-cost controller
is disclosed. Source return is not whole-state reset. No old record is
erased on an occupied continuation; reversing the actual complete path
restores all registers and refunds its work. Generic appended paths may
change the recorded aggregate area: this is a path-sum record, not a
persistent archive of every earlier event.

No covariance of this chosen positive cost under the predecessor's
reciprocal scaling is claimed. Its conformal area and ramified map are
not rederived or implemented here. J enters only through the inherited
fifth-root algebraic character. No native U compiler, physical locality,
experimental comparison, hbar, SI metrology, stationary-action principle,
Hamiltonian S=sum p Delta q-H Delta t, photon identity, sampling law or
L1-to-L6 lift follows. Existing physical/native owners remain open.

## 5. Falsifiers, execution and custody

Any single exact failure in G1-G6 at the declared scope fires a scientific
falsifier. The script prints FALSIFIER and AUDIT FAIL and exits zero so the
negative scientific transcript can be preserved. It must never print PASS
after that failure. Unexpected exceptions, nonzero process exit, nonempty
stderr, source drift or timeout are execution failures, not scientific PASS.
No corrective run on an altered pin is allowed; preserve the first outcome.

Run from the clean publicly pinned repository root:

    python3 probes/P-FUNDED-AREA-PHASE-RECORD-1/verify.py

Use LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1,
the unchanged repository 600-second limit, and capture stdout/stderr
separately. Record genuine UTC start/end, exact command, actual Python/OS/
architecture, exit, bytes, SHA-256 and the immutable pin in RUN.md.
EXPECTED.txt is the captured first complete stdout. Required PR checkers
must replay the same frozen source/output on x86_64 and aarch64; both jobs
and the aggregate must pass. Source/proof custody is distinct from science.

## 6. Action layer and ownership boundary

L1 only: exact conditional integer automaton, finite histories and a chosen
finite Weyl representation, not an L5 physical stream. Authored proof ceiling
candidate-T; finite exact execution candidate-C until appropriate acceptance.
Two architecture replays are reproduction, not independent authorship.
Predecessor P-J-RAMIFIED-AREA-WEYL-1 and #1419 are provenance only. Public
INTEGER-ENERGY-FUNDED-INVOLUTION and FORCE-WEYL-HOLONOMY are inherited
mechanisms, not new discoveries. METRO-EDGE-SCALE, native contact admission
and QDD-INSTRUMENT-APPARATUS retain their open status. No automatic promotion,
merge, release or change to any file outside this one probe directory.

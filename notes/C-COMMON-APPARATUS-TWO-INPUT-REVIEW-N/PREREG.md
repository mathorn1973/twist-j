# Independent implementation attack on the two-input common apparatus

Status: NON-CANONICAL / L1. Candidate C-COMMON-APPARATUS-TWO-INPUT-REVIEW-N.
Owner: Codex session /root, 2026-11-03.
Authority base: main 0c33e2b281e39127c269ef5dd7f5b529a62e9e65, v107.
Target: PR #1871, head 26731e2bd7f1394b4d274528525e6d78cbe6bbf9,
probe P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1, author scientific source
4e448bb3b13c4e8f0338524e7c69ade1c01caf0f.

## Exposure and source boundary

The user's announcement and PR body disclose the author's success, domain,
counts and output hashes. The review is result-exposed, not blind discovery.
The review author and checker writer may read the frozen PREREG.md,
CONTRACT.md, PROOF.md, SOURCE-MAP.md and PROVENANCE.md. They must not read
or import author verify.py, EXPECTED.txt, literal WORD535.txt, or scientific
logs before our own source is frozen. This independent checker reconstructs
the word from block equations and its ring arithmetic independently.

Publicly pin and read back this file and the accepted review.py before first
scientific execution. Only syntax compilation/static inspection is allowed
before that pin. Preserve a fired falsifier; frozen code and thresholds are
not repaired to match the announced outcome. A successor needs a new name.
Only after own execution finishes may author executable/output evidence be
opened and compared. An independent symbolic review reads no verifier.

## Exact carrier and independently reconstructed operation word

Use O=Z[j], rho=j^2, u=1-rho, w=1+rho, b=1+rho^2. The primitive C is
the total parity-admitted relative contact specified by CONTRACT.md.
SWAP(i,j) is a separate declared whole-slot transposition, not compiled C.
Both have exact inverses, C^4 and SWAP respectively.

The checker uses the rho basis, independent matrix arithmetic and exact
integer accounts. It independently expands the following chronological
zero-based blocks; exponents mean literal repeated contacts:

 O=C(1,5), A0=C(5,9), Bc=C(c,9), O2=C(9,10), T=C(3,4),
 Ec=A0 Bc A0^4 Bc^4, Ecinv=Bc A0 Bc^4 A0^4,
 Kp=C(3,q+2p)^4 C(q+2p,q+2p+1)^4 C(3,q+2p) C(q+2p,q+2p+1),
 SCANq=product_p=0..4 (C(3,10) Kp C(3,10)^4 T),
 WA=E6 O2 SCAN11 O2^4 E6inv, WB=E7 O2 SCAN21 O2^4 E7inv,
 D(c,d)=C(9,c)^3 C(9,d)^3 C(9,c) C(9,d) C(9,c),
 V(c,d)=A0 D(c,d) A0^4 D(c,d),
 R=O WA WB V(7,8) V(6,7) O^4,
 F=C(0,1)C(1,2), Finv=C(1,2)^4 C(0,1)^4,
 S=R Finv R F F T.

Lengths: R=261, S=535. Stage A uses original addresses. Stage B maps each
memory address 11..30 to i+20 and fixes 0..10. The complete fixed program
is S_A^10, five SWAP(i,51+i) for i=0..4, then S_B^10.
Its forward count is 10700 C and five SWAP; inverse 42800 C and five SWAP.
No edge, length or stage choice depends on observed data.

## Preparation and closed expected states

Construct Y phases analytically, not by substituting runtime endpoints:
Y0=(0,2,0), Ye=(1-rho^e,1+rho^e,0) and
Y(4+e)=(0,1+rho^e,1-rho^e) for e=1..4. A separate eighteen-contact fixture
checks their nine-cycle. Xk=(rho^k*w,-rho^k*w), k modulo five.
Blank M is (-b,b)^5; M[p] changes only pair p to (-rho*b,rho*b).

The complete input is (Yn,Xk,0,u,0,0,w,0,M,M,M,M,Ym,Xl), on 56 slots,
for every ordered (n,k,m,l) in {0,1}x{0..4}x{0,1}x{0..4}: 100 cases.
Check all 46 common auxiliary coordinates, their account 128, total account
156, ring sum 6, and common labelled residue vector. Both inputs are supplied
initially; the second is independent as a full Cartesian input choice.

At each read boundary compute the expected full state from analytic phases,
the declared event/selector law and the bank codes. Execute every contact
of the actual read word; never replace it with that expected transition.
Within one step, first read sees phase a, second read phase a-1; both restore
that presented source/clock. The step ends with phase (a+1,k+1). Stage event
steps are (0,1,9) for source zero and (0,8,9) for source one, writing A,B,
then skipping. Full read/step states must restore g=t=0, helper w, and the
predicted selector. At ten steps source is Y(s+10), clock Xr, selector A.

The first stage must leave the queued input and second memories untouched.
The reload swaps must park the actual first spent input in 51..55 while
loading the exact second prepared input. First-stage archives retain their
literal addresses. Check their structural support exclusion for every
second-stage primitive and their actual values at all full checkpoints.
The parked old input stays unchanged through stage two. No coordinate is
discarded from the expected reload or final states.

## Reader, timing, inverse and frozen audit

The reader receives only current slots 11..50, split into four ten-slot
banks. Each must be exactly one valid M[p]. Blank, multiple changed pairs,
or malformed bank values are invalid. For each label pair (x,y), difference
1 means source phase zero, difference 3 phase one, and k=-x mod5; all other
differences are invalid. Recover all four initial labels from actual banks,
then compare with inputs. The 100 complete record outputs must be distinct.
Audit the reader's strict rejection of blank, malformed, multiply occupied
and invalid-difference codes on a fixed small finite mutation set defined
by the accepted checker; these are standalone interface checks, not a
claim about arbitrary physical detector states.

Designated onset is the first contact of an active R, g:0->u; do not count
other internal marker changes as events. First two local contact onsets
are (1,805)/(270,4281), completions (261,1065)/(530,4541), gaps804/4011.
Stage B contact-only offsets add5350; all-operation offsets add5355.
Check onsets and completions against actual marker and complete R states.

Replay every primitive forward and backward for all 100 cases. Required
trajectory totals: 4000 R checkpoints, 2000 S checkpoints, 100 reloads,
600 designated events, 100 full-state inverses, 5350000 contact applications
and 1000 SWAP applications. The separate 18-contact fixture is excluded.
All distinct ordered contact pairs must preserve exact sum, Q, Hermitian
account and labelled residues and satisfy C^5=id. Swaps must preserve sum
and Q, and exchange equal residues on every reached loading pair.

Report deterministic edge/checkpoint/endpoint fingerprints in canonical j
coordinates. The accepted code fixes serialization before execution. It
may optionally write raw endpoint/checkpoint data to a scratch dump for
post-freeze comparison; no target execution or import is used to generate
expected states. Store actual stdout, environment, hashes, exit and stderr.
Local execution is one x86_64 lane. The author's two-architecture gate is
checked separately from official CI evidence after our source is frozen.

## Failure threshold and interpretation

Tolerance zero. Any wrong reconstruction, common preparation, complete
checkpoint, timing, archive disposition, protected-region support, strict
reader result, injection, invariant, primitive count or full inverse fires
the corresponding frozen prediction. An exception/timeout/nonempty stderr
is not a pass. Known successful target results never justify dropping a case.

Compare the declared finite contract with the actual current L1 common-
apparatus owner, without inventing raw-input, infinite-memory regeneration,
contact-only SWAP or empirical requirements absent from that owner. A
mathematical fit is distinct from a canonical fold. Do not close a registry
row, merge the original probe, infer physical realization/native U, or raise
its status by this review. Preserve the explicit preloaded inputs, spent
memory, fixed schedule, supplied swaps and finite two-experiment horizon.

# An explicit retained-integer-program source of fresh pairs

**NON-CANONICAL, L1. Candidate C-JM-RETAINED-PAIR-SOURCE-N.**
Analytical conclusions: candidate-T. Exact finite audit: candidate-C.
Owner: A. M. Thorn, session jm-retained-pair-source-2026-10-20, issue #1680.

## Result

A single explicit rational reflection, controlled by a retained digital
integer program z, prepares two identical anchored pure output states from
a program-independent ready pair. A finite addressed stock and swaps give
one reversible source law on occupied ports, with the complete old contents
and correlations retained. The source produces the HOLD block law rather
than assuming that law as its output primitive. No normalization square root,
postselection, hidden seam label, or probability generator is used.

This is a constructive result in a supplied mathematical apparatus class.
It does NOT derive the classical source access, metric, reference, pure ready
stock, exact controlled couplings, time counter, Born occurrence or a physical
energy Hamiltonian from J/U. It is not a hardware claim. The scope is stronger
than an unspecified prepare(rho_z) oracle and weaker than native physical
realization. State norm conservation must never be called energy conservation.

## 1. Source basis and exact choices

Public main basis: 5f20429944b409d912202d141e158fdfec145c41, Canon v103.
The predecessor PR #1679 remains an unmerged candidate at
87485fc66140a436bd6a337dd2ff452093ab607f. Its required comparison data are
restated, not promoted. Fix integers Q>=8 and K>=1. For z=(a0..a3,b0..b3)
let

    S={z in Z^8: b1-b2-b3=0 mod3},
    G=diag(5I4-ones4,4I4), q(z)=z^T G z,
    B_Q={z in S:0<q(z)<=Q}.

The earlier seam is ell z=0 mod41, ell=(1,10,18,16,-1,-27,-32,-3).
This predicate is not used by the source compiler or its gate. They work on
both sides without testing membership or importing desired detector weights.

One elementary output carrier is V=Q^9, with reference basis vector e0 and
positive metric G0=diag(1,G). Supply y_z=(1,z) and A_z=1+q(z). The desired
one-cell density is

    rho_z=y_z y_z^T G0/A_z.

A pair uses V tensor_Q V, dimension81, metric L=G0 tensor G0, and ready vector
e=e0 tensor e0 of norm1. The two factors here denote distinct prepared output
systems, not the earlier module R tensor_Z conjugate(R). No new number field
or physical spatial dimension is inferred. The quantum comparison is through
the real/complex extension of the fixed rational metric. The arithmetic and
all gate matrices remain rational.

The source program is a classical digital label. In the comparison Hilbert
space its basis labels are orthogonal. The integer value may be unknown to
the user/reader, but the source has computational access to its stored bits.
No device that learns z from an unknown nonorthogonal specimen is assumed.

## 2. Why two outputs remove a genuine rational obstruction

Let a nonzero rational unit vector lie on the ray y_z^(tensor k). It must
have the form c y_z^(tensor k) with c rational: its reference coordinate is c.
Normalization demands

    c^2 A_z^k=1.

Thus it exists exactly when A_z^k is a rational square. For an integer A_z
that is not a square this requires even k. For example z=(1,0,...,0) is an
admitted source with q=4 and A=5. One clean output cannot be reached from a
rational unit ready vector by a rational isometry on that output alone;
two can. This is restricted to real-rational matrices and no additional
program-dependent residual output. A complex extension, nontrivial auxiliary
output, destructive program, or general rational channel is a different class.

For two outputs, the vector

    t_z=(y_z tensor y_z)/A_z

is rational and has L norm1. Its density factors EXACTLY:

    t_z t_z^T L = rho_z tensor rho_z.

The factors can be read as individually normalized vectors after scalar
extension, but their square roots are neither stored nor computed. Partial
trace of the rational pair density gives rho_z on each output. When an odd
number of outputs is requested, retain the extra partner in the complete
state; it is not silently erased.

## 3. The exact preparation gate

Write A=A_z, w=y_z tensor y_z, v=Ae-w and d=A(A-1). On the supported source
A>1. Since e^T L e=1, e^T L w=1 and w^T L w=A^2,

    v^T L v=2A(A-1)=2d.

Define

    U_z = I - v v^T L/d.

It is a Householder reflection in the specified positive metric. Let r=Lv.
Then

    U_z^2=I,
    U_z^T L U_z=L,
    U_z e=e-v/A=w/A=t_z.

These follow by r^T v=2d and r^T e=A-1. This gives the COMPLETE operation
on every occupied or entangled pair input, not only its ready-state action.
For invalid digital labels, including zero, define U_z=I and mark the source
as having no admitted output. No zero denominator is evaluated.

The gate is controlled by a fixed classical program:

    W_Q=sum_z |z><z|_program tensor U_z,

where invalid codes use identity. This is one fixed block-diagonal isometry
for the finite program alphabet. Its coefficients are obtained from integer
z and the fixed metric, not fitted probabilities or a list of detector answers.
The program basis value is unchanged. An arbitrary coherent superposition
of program labels generally becomes entangled with the outputs; preservation
of its reduced offdiagonal density is not claimed. The HOLD probability
statement below assumes a classical diagonal program law explicitly.

Householder preparation itself is established mathematics, not a newly
invented general method: see Ivanov, Kyoseva and Vitanov, Phys. Rev. A74,
022323 (2006), DOI10.1103/PhysRevA.74.022323. The source here specializes it
to a rational PAIR target and supplies the integer and storage contract.
No laser/pulse realization from that paper is imported as a TWIST-J mechanism.

### A four-coordinate exact example

For z=(1,0,...,0), restrict to the span of reference and z. Its metric is
diag(1,4), and the pair metric is diag(1,4,4,16). The reflection is

    U=(1/5) [[1, 4, 4,16],
             [1, 4,-1,-4],
             [1,-1, 4,-4],
             [1,-1,-1, 1]].

It squares to identity and preserves that pair metric. It sends (1,0,0,0)
to (1,1,1,1)/5, whose norm is1. Both marginal densities are the requested
anchored z density. This subspace calculation illustrates the general81-
coordinate source; it is not a replacement of its complete carrier.

## 4. Integer certificates and exact executable representation

All coefficients before division are integral:

    N_z=dI-v r^T,
    N_z^2=d^2 I,
    N_z^T L N_z=d^2 L,
    N_z e=(A-1)w.

A rational amplitude vector a/b is updated by the exact integer operation
N_z a/(db), with optional canonical gcd reduction. This is a finite exact
algorithm, not floating-point simulation or a normalization approximation.
Here d<=Q(Q+1); |v_i|<=Q, and the maximum absolute row sum of L is49, so
|N_ij|<=Q(Q+1)+49Q^2. Gate coefficients therefore have O(log Q) bits. This
is a coefficient-description bound, not a hardware runtime bound or a claim
that arbitrary many-body states have efficient classical descriptions.

For each FIXED program there is also an invariant compiled lattice

    Lambda_z=Z^81+U_z Z^81,  Z^81 subset Lambda_z subset (1/d)Z^81.

U_z Lambda_z=Lambda_z follows from U_z^2=I. It contains both the common
ready vector and the prepared pair. On a basis of Lambda_z the same gate is
an integer involution; d^2 times the metric is integer-valued there. Tensor
products of this lattice are invariant under the same-program local gates
and swaps. This is an exact integral completion for a held-program session.
It is NOT the original R lattice, not one secretly selected universal lattice
for arbitrary changes of program, and not a derivation of physical energy.
The common all-program operator carrier used above remains the declared
rational vector space with one fixed metric.

## 5. Capture of an unknown integer record without destroying an old one

G>=I implies every coordinate of z in B_Q is between -floor(sqrt(Q)) and
floor(sqrt(Q)). Set m=2 floor(sqrt(Q))+1. Eight registers in Z_m store the
source injectively using balanced representatives. At Q=14112, m=237; eight
8-bit words suffice for this code, with unused patterns rejected. The exact
number of legal source labels is not claimed to be m^8 or enumerated here.

Let X be a supplied digital input, P the source program, and C a program
archive. The complete reversible load is

    SWAP(P,C), then P <- P+X mod m,
    (X,P,C) -> (X,C+X,P).

Its inverse is subtraction of X followed by the swap. If C starts at zero,
the new program is exactly X, the previous program is in C, and X remains.
A dirty C is handled reversibly but does not satisfy that ready-state promise.
No universal erasure or unnoticed overwriting is performed. Loading X from
the native U state is not supplied: X is the admitted integer input port.

The gate coefficients may be computed reversibly from the retained program
into scratch, used as controls, then uncomputed; the exact function is the
integer formula in section3. No probability or seam result is stored there.
The implementation here compiles the coefficients classically and evaluates
the resulting map exactly. Compilation into a fixed native gate alphabet,
its locality, physical time and pulse costs remain separate obligations.

## 6. One complete source law, including an occupied output

The carrier comprises a fixed program, an integer counter n in Z, one output
PAIR P, K pair cells B0,...,B(K-1), and arbitrary untouched spectators or
measurement records. On a forward tick with a valid program and 0<=n<K,

    V_(z,n) = SWAP_(P,B_n) (I_P tensor U_z^(B_n)).

Otherwise V_(z,n)=I. The total source step is

    T:(z,n,P,B,rest) -> (z,n+1,V_(z,n)(P,B,rest)).

The inverse first recovers n by decrementing the counter, then applies

    V_(z,n)^-1 = (I_P tensor U_z^(B_n)) SWAP_(P,B_n)

at that recovered address. Therefore T is bijective on the complete rational
state description and unitary in its declared quantum comparison. All n,
all occupied cells and all correlations are included in the inverse claim.
The counter is unbounded and explicitly counted as a control resource;
this is not a finite reversible machine with a fictitious absorbing halt.

For the useful forward protocol, start n=0 with every B_i in the SAME
program-independent pure e. Those ready cells are initially uncorrelated with
the remaining apparatus. P may contain any state, including entanglement
with old records. For fixed z and arbitrary joint old port/spectator density
sigma_(P,E), the full one-round identity is

    sigma_(P,E) tensor |e><e|_(B_n)
        -> (rho_z tensor rho_z)_P tensor sigma_(B_n,E),

with old P literally relabelled B_n. Here the metric-adapted pure ready
projector is understood; its coordinate formula is e e^T L. The swap moves
all old correlations to the archive and introduces none between the fresh
pair and old data conditional on z. This is stronger than checking only the
marginal of the output port. Earlier archive cells and spectators are untouched.

The SAME old-stock cell thus serves as pure preparation resource before the
round and as old-content archive afterward. No extra empty archive is assumed
for each pair beyond this explicitly supplied K-cell stock.

## 7. The HOLD law is now a consequence of the gate and supply

For a fixed z, induction on section6 gives2K conditionally identical pure
outputs. At boundary n=j>=1 with no intervening measurements, P carries the
latest pair, B0 carries the initial old port, and B1,...,B(j-1) carry previous
prepared pairs. Unused B_j,... remain in e. A capacity-K source therefore
has K pair outputs in P,B1,...,B(K-1) and the old port in B0. These all remain
part of the complete state. External output transport, when needed, is a
specified swap with a retained register, not deletion.

With a classical program law pi, even if the old port is conditionally
correlated with z, tracing away the program and the retained old contents
leaves

    Gamma_(2K)=sum_z pi_z rho_z^(tensor 2K).

Selecting k<=2K output factors gives HOLD_k. Any unused partner remains in
the full apparatus. The source has no pi-dependent gate and does not redraw
its program between emissions.

Interventions on previous outputs or their record registers may be arbitrary
quantum instruments in the adopted comparison model, provided they do not
alter the program or unused ready stock. The next output pair is still
rho_z^tensor2 conditional on z, independent of the prior output state. The
joint law for fixed measurement contexts is consequently the previously
specified held-label law, not the product of the one-copy mixture. The initial
pi and Born occurrence are still explicit model inputs. No independent
renewal between blocks is asserted unless a fresh loading protocol supplies it.

## 8. Resource ledger, exhaustion and reset

After j supported rounds, 0<=j<=K:

- the eight-integer source program has the same value;
- j ready pairs have been used, K-j designated ready pairs remain untouched;
- exactly j stock addresses retain old port contents;
- exactly2j fresh one-cell preparations have been generated;
- the digital counter is j, with the fixed program/graph supplying the address.

These are exact supply/capacity counts, not an energy model. The state metric
norm is conserved by every gate and swap, but it is a probability norm. A
nondegenerate Hamiltonian, pump work, thermal cost, material realization and
reference preparation cost have not been provided. Flat level energies could
be chosen in a comparison model, but would not account for physical control
work and are not presented as its solution.

When n>=K, T changes only the counter. No additional source output, reset or
fresh cell is claimed. The data remain available indefinitely in this ideal
model, at the declared cost of an advancing unbounded counter. Passive reading
is not another preparation event.

Unmeasured reversal of all K source rounds exactly restores the original
occupied P, every ready stock cell and the original counter. If the emitted
systems have interacted with measurement pointers or other systems, complete
reversal must include those interactions and records, or a new supply must
be used. Simply setting an old cell back to e while leaving its unknown
contents nowhere is forbidden by injectivity.

There is a tight elementary archive-capacity bound. If an arbitrary D-
dimensional old port must be replaced by one fixed pure output and the total
operation is an isometry with fixed initial environment, D orthogonal old
inputs must leave D orthogonal environment outputs. The environment therefore
needs dimension at least D. One same-size swap archive achieves that bound.
Here D=81 per pair port. This bound concerns arbitrary lossless replacement,
not every more restricted or destructive reset scheme.

Dirty readiness is a scientific boundary, not a check one can infer from a
classical occupancy flag. If a stock cell already contains t_z, applying the
same U_z returns it to e. The next port then contains e, not the requested
state. The all-state inverse still works; the supported preparation conclusion
does not. The current source does not purify arbitrary dirty stock for free.

## 9. Concrete interface to the seam experiment

At Q=14112, the predecessor's explicit one-sided test requests181 fresh
one-cell preparations. The source supplies them in91 rounds from91 common
ready PAIRS, generating182 one-cell states; one unused partner is retained.
The complete initial data allocation is one possibly occupied output pair
plus91 ready pairs, together with the program, loader archive and counter.
The number181 is the predecessor's explicit construction, not a proved minimum.

For the earlier specific opposite-seam collision, a SINGLE source pair
already supplies the two conditional copies. Using generated target vectors,
the exact two-reference-click difference is

    15936/1210262180216419.

The verifier calculates this from U_z e for the programs +/-40v,+/-41v,+/-42v,
not from a sampler given the desired probability. This proves compatibility
of the constructed source with that held-block comparison; actual detector
events still use the adopted Born rule. The full paired source can be used
without first revealing z or its norm to the reader.

## 10. No cloning or hidden recovery from a mixed specimen

The input resource is the complete digital instruction z, not one unknown
state rho_z. Different instructions are orthogonal program states. Hence the
construction does not violate unknown-state no-cloning. It cannot be invoked
on a common averaged density with no source program to recover preparation
correlations that have already been discarded. For context see Wootters and
Zurek, Nature299,802-803 (1982), DOI10.1038/299802a0.

The gate acts nonlinearly as a function of the classical integer instruction,
but the controlled operation is linear on its full program-plus-output
quantum carrier. Treating it as a universal nonlinear map on the output
specimen alone would change the declared input contract and is not allowed.
No specific native U capture, original-kernel preparation, new physical
occurrence law, or closure of QDD-INSTRUMENT-APPARATUS follows.

## 11. Evidence scope

The first public pre-execution pin is
760157f57495fb87059b3a8a8e7943be7d0793c1. source.py and verify.py were frozen
before any new scientific run. Their exact bytes and output are bound in
RUN.md and SHA256SUMS. The test suite checks2162 admitted ternary programs,
seven full integer matrix and product-density certificates, all81 occupied
port basis states, an explicitly correlated three-round archive, all-state
inverse controls, capacity exhaustion, dirty-readiness failure,495 complete
small modular capture cases, the rational odd/even boundary and the generated
held-pair response. It is not an enumeration of all B_Q or a physical trial.

All general statements follow from the proofs above. Matrix multiplication
of integer certificates is an audit of the rank-one formula, not a blind
second agent. Actual architecture and versions, including any departure from
the planned execution lane, must be reported honestly. Ordinary notes-only
CI does not run these scientific programs and is not their two-architecture gate.

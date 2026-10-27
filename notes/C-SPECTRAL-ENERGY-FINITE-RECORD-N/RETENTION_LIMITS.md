# Retention, export and cyclic-resource limits

**NON-CANONICAL, L1. New analytical extension; independent mathematical
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This note fixes the contracts needed to extend the physical record beyond
the previous clock return and to reuse the processing apparatus. It changes
none of the seventeen preceding files. Its negative results concern the
stated finite, closed, time-independent models. They do not forbid a long
specified finite record window, a counted fresh-memory bank, or an enlarged
device with explicitly supplied replacement cartridges.

The thermal source in THERMAL_CLOCK.md has a concrete boundary: its
cold-ground comparison density returns at 3T_h, with completion latch zero.
That return proof applies to its unchanged joint dynamics and specified
input family. Inserting an export or reset changes the continuation
contract. A separate proof must account for the retained record, reference,
old archive contents, donors, clock and reset resources together.

Throughout, D(rho,sigma)=||rho-sigma||_1/2. Entropies use natural logarithms.
Passive references are retained whenever a channel claim is made.

## 1. Exact permanent writing in a finite static closed system

Let the complete physical Hilbert space have finite dimension D, let H be
time independent and self-adjoint, and let U_t=exp(-itH/hbar). Include the
writer, retained memory, all finite baths, clocks and other interacting
resources in that space. An external reference may remain passive.

For a fixed initial density rho and fixed physical effect 0<=P<=I,

    p(t)=Tr[P U_t rho U_t^*]
        =sum_(lambda,mu) c_(lambda,mu)
                  exp[-it(E_lambda-E_mu)/hbar].          (R1)

There are only finitely many terms. Thus p is real analytic, with an
entire exponential-sum extension. If p(t)=c on any open time interval,
all derivatives of p-c vanish there; the analytic identity theorem gives
p(t)=c for every real t.

In particular, if a newly written physical record changes its occupation
from p(0) to a different value c, that occupation cannot then be exactly
constant forever under the same complete finite H. The same argument
applies separately to every matrix entry of a retained reduced state.
An exactly constant unconditional final reduced state on an interval
must equal the corresponding initial reduced state.

This conclusion concerns the unconditional physical state or effect
weight. A normalized accepted state may be constant while its acceptance
weight varies. For example, a substate w(t) Sigma can have the fixed
conditional density Sigma/Tr Sigma while w(t) later returns to zero.
Such a conditional identity is not permanent availability of a record.
It is compatible with the finite-window proofs in the preceding notes.

A simpler sufficient condition for permanent preservation is [H,P]=0.
Then p(t)=p(0) for every input. The same Hamiltonian cannot also write P
from an initially zero occupation. No converse commutator claim is inferred
from constancy for just one particular initial state.

## 2. Approximate permanence also has a recurrence boundary

There is an elementary quantitative recurrence bound. Let s be the number
of distinct eigenvalues of H. Fix any t_0>0 and integer Q>=2. For
lambda=2,...,s set

    alpha_lambda=(E_lambda-E_1)t_0/(2 pi hbar).

Partition the unit (s-1)-cube into Q^(s-1) cubes of side 1/Q. Among the
Q^(s-1)+1 points k alpha modulo integers, k=0,...,Q^(s-1), two lie
in the same small cube. Their index difference q satisfies

    1<=q<=Q^(s-1),
    distance(q alpha_lambda,integers)<1/Q.

At t_rec=q t_0 every relative eigenphase is therefore within 2pi/Q of
zero. Spectral decomposition gives

    t_0<=t_rec<=t_0 Q^(s-1),
    ||U_(t_rec)-exp(-it_rec E_1/hbar) I||
         <=2 sin(pi/Q)<=2pi/Q.                         (R2)

For s=1 take q=1 and the error is zero. The bound is an existence estimate,
not an efficient prediction of a laboratory recurrence time.

Purification, the pure-state trace-distance inequality and contractivity
show that the same bound holds for every initial density, jointly with
an arbitrary passive reference:

    D((U_(t_rec) tensor I_R) rho
          (U_(t_rec)^* tensor I_R),rho)<=2pi/Q.         (R3)

Choosing t_0 after any proposed retention deadline gives arbitrarily late
returns as close to the initial joint state as desired. In particular,
for an initially empty physical read effect,

    p(t_rec)<=p(0)+2pi/Q.                              (R4)

More generally let sigma_target be a fixed retained target and let
d_0=D(rho_retained(0),sigma_target)>0. Along such recurrences,

    D(rho_retained(t_rec),sigma_target)>=d_0-2pi/Q.     (R5)

Consequently a uniform guarantee D<=epsilon for all sufficiently late
times is impossible when epsilon<d_0. Increasing the finite dimension
can postpone this obstruction and permit a long useful window; it does
not remove it. An infinite bath, a changed Hamiltonian, a detached output
or an intervention changes the hypotheses and needs its own resource
and continuation account.

## 3. A clock return is not a joint reset

Equality of clock marginals does not imply return of data, resources or
their reference correlations. A pure clock can remain in |0> while a
unitary acts nontrivially on the data. Even its exact pure marginal return
only implies factorization from that clock, not restoration of the data.

For a mixed-clock example, the orthogonal Bell states

    (|00>+|11>)/sqrt(2),       (|00>-|11>)/sqrt(2)

have identical clock marginals I/2 and are related by a local phase flip.
Their joint states have trace distance one. Marginal return can therefore
miss a complete change of correlations.

The same distinction applies to thermal resources. A maximally mixed
qubit C and a blank bit B can be transformed by CNOT into

    (|00><00|+|11><11|)_(C,B)/2.

C is still maximally mixed, but it is correlated with the record. Copying
C to a second blank bit produces the same random bit, not a fresh
independent sample. Restoration of a Gibbs marginal is not restoration
of its independence from old outputs.

Accordingly a reusable-resource contract must specify which joint state
is returned, what correlations with prior records are allowed, and which
inputs are fresh. A previous half-period or clock-marginal calculation
cannot simply be appended after an arbitrary export operation. The
exported memory and the changed core correlations must enter the new
joint evolution.

## 4. Unknown quantum input cannot be restored while it is recorded

Let S be an arbitrary input system, A the apparatus and every initial
record/resource factor, and sigma_A a fixed state independent of S and
its reference. Let a unitary act on SA. Suppose the reduced S channel is
exactly the identity for every density on S, including all pure inputs.
Then every complementary output in A is independent of that input.

Here is a direct proof, including mixed apparatus states. Purify sigma_A
by a passive E. The resulting transformation is an isometry
V:S->S tensor A tensor E. Since each pure input |psi> must have the same
pure S output, it factorizes:

    V|psi>=|psi> tensor |e_psi>.

For an orthonormal input basis |i>, write the corresponding states e_i.
Apply the same requirement to (|i>+|j>)/sqrt(2). Linearity and comparison
of its two coefficients force e_i=e_j, up to a common phase already
absorbed into the factor. Hence one fixed vector e works for every input:

    V|psi>=|psi> tensor |e>.                           (R6)

The entire apparatus/purifier output is independent of psi. By linearity,
the same identity holds jointly with any input reference. No informative
record can be obtained under this exact input-restoration contract,
even with fresh initial apparatus resources.

Orthogonal classical inputs are a different promise. Their basis labels
can be copied while those basis states remain unchanged. Requiring
restoration only on that commuting family does not imply (R6). An
arbitrary unknown superposition or entangled input is not such a family.

A useful two-label quantitative version assumes exact nondisturbance of
the basis inputs:

    V|0>=|0>|e_0>,       V|1>=|1>|e_1>.

Put c=<e_1|e_0>. On |+>, the reduced input disturbance is
|1-c|/2. If it is at most epsilon<=1/2, then

    |c|>=1-2epsilon,
    D(record_0,record_1)
       <=sqrt(1-|c|^2)<=2sqrt(epsilon).                (R7)

The first record-distance bound follows from the pure complementary
states and contractivity to any accessible record subsystem. This is a
bound under the stated exact basis-restoration premise, not a general
optimal approximate information-disturbance theorem.

Quantum export by SWAP is allowed. It moves the unknown input and its
reference correlations into the output memory, while the original input
port receives that memory's old state. It does not restore the original
unknown input at the same time. The occupied-archive permutations in the
source model have exactly this transfer character.

## 5. The precise copy-and-uncompute condition

Let U be a computation on S and work register A, with A initially in
|0>. Let {P_y} be orthogonal output-label projectors summing to identity,
and let a new blank record B copy that orthogonal label. A finite cyclic
shift on B controlled by P_y extends this copy to a full unitary on all
record inputs. Applying U,
copying, and then U^* to SA gives the isometry

    |psi>|0>_A -> sum_y E_y(|psi>|0>_A) tensor |y>_B,
    E_y=U^* P_y U.                                    (R8)

This formula includes every branch. Uncomputing after the copy is not
the same operation as U^*U on a state without the copied record.

Let P_0=I_S tensor |0><0|_A be the ready-input code. The work register
returns to |0> for every input and reference if and only if

    (I-P_0)E_y P_0=0 for every y,
    equivalently [E_y,P_0]=0 for every y.              (R9)

Necessity follows because the different |y> records are orthogonal, so
leakage from the ready code cannot cancel between branches. Sufficiency
is immediate from (R8). Since E_y is self-adjoint, invariance of the
code implies the displayed commutation.

In this case the restrictions Q_y=P_0 E_y P_0 on S are orthogonal
projectors. The source channel after tracing B is exactly

    rho_SR -> sum_y (Q_y tensor I_R) rho_SR
                       (Q_y tensor I_R).             (R10)

It restores the admitted source/reference density precisely when that
density is block diagonal in these projectors. Thus a deterministic
reversible computation of f(x) on sharp orthogonal labels |x> permits
copying f(x), uncomputing the work, and retaining the original classical
label. Coherence between different f-values is then transferred into
source-record correlations, rather than preserved in the reduced input.

For a general probabilistic instrument the pulled-back projectors need
not preserve P_0. Its compressed effects need not be projections.
Equation (R8) then leaves branch-dependent work states, and the usual
classical copy-and-uncompute argument does not establish a reset.
An enlarged classical random seed can make an outcome deterministic
on a larger basis, but that seed and its correlations with the new
record remain resources.

For a minimal counterexample, prepare a work qubit by a Hadamard from
|0>, copy its computational label to a blank bit, and apply the Hadamard
again. The work marginal is then I/2, not |0><0|. Copying the probabilistic
flag prevented the purported uncomputation.

There is also a state-specific formulation without a pure work code.
For a complete initial machine density rho_M and a copied output label,
copy-and-uncompute leaves the machine marginal

    rho'_M=sum_y E_y rho_M E_y.                        (R11)

This equals rho_M if and only if [rho_M,E_y]=0 for every y. Even then
the joint output is generally correlated with the copied record. Its
machine marginal can return while its fresh-input contract fails.
For example, a thermal classical seed can be restored marginally while
every saved outcome remains correlated with that same seed.

## 6. Finite record capacity

Suppose K equiprobable classical histories are retained in a memory of
dimension D_R. Include every subsystem available to the decoder in that
memory; an uncounted correlated side register is not free decoding space.
Let rho_x be its encoded states and {F_x} a decoding POVM. Since
rho_x<=I,

    p_correct=(1/K) sum_x Tr(F_x rho_x)
              <=(1/K) sum_x Tr F_x=D_R/K.             (R12)

Therefore average decoding error at most epsilon requires

    D_R>=(1-epsilon)K.                                (R13)

For n independent L-valued histories, K=L^n. Exact retention requires
at least n log L of logarithmic memory dimension. This elementary bound
allows mixed records and a general decoder. It does not assume a literal
bitwise layout or that each individual record is independently read.

There is a corresponding quantum bound. Let d be the input dimension
and demand entanglement fidelity at least 1-epsilon after a decoder
acting on a D_R-dimensional retained system, including all its ancillary
side resources. Start with the input maximally entangled with a
d-dimensional reference. Before decoding, every pure component across
reference versus retained system has Schmidt rank at most D_R.
A local decoder cannot increase that Schmidt-rank bound in its Kraus
branches. A normalized vector of Schmidt rank k has squared overlap
with the d-dimensional maximally entangled state at most k/d, by
Cauchy-Schwarz on its Schmidt coefficients. Convexity therefore gives

    1-epsilon<=F_ent<=min{1,D_R/d},
    D_R>=(1-epsilon)d.                                (R14)

For n arbitrary independent q-dimensional quantum inputs, d=q^n.
The reference-fidelity contract is stronger than saving classical labels
from one chosen basis. A finite bank can support a declared finite number
of records; it is not an unlimited reusable output reservoir.

## 7. Reset consumes a joint resource, even when no heat law is asserted

Consider a d-dimensional register M, initially maximally mixed and
independent of a finite reset resource C in sigma_C. Suppose a unitary
on MC returns M exactly to a fixed pure ready state. The final pure
marginal factorizes, so entropy conservation gives

    S(C_final)=S(sigma_C)+log d.                       (R15)

Consequently the necessary entropy capacity is

    log dim(C)-S(sigma_C)>=log d.                     (R16)

If only D(rho_M,final,|0><0|)<=epsilon is required, with
0<=epsilon<=1-1/d, the bad-state weight is at most epsilon. Entropy
maximization at that weight gives

    S(M_final)<=h_2(epsilon)+epsilon log(d-1).

Subadditivity and conservation of the joint entropy then imply

    S(C_final)-S(sigma_C)
       >=log d-h_2(epsilon)-epsilon log(d-1).          (R17)

For a batch of n such registers, replace d by d^n when the guarantee
is a joint trace-distance guarantee. If the exact target is instead
a fixed mixed state sigma_M, the same argument gives the necessary
bound log d-S(sigma_M). These are entropy-capacity bounds, not a
minimum heat or work formula at an unspecified temperature.

The resource C must include every changed output or entropy store.
If data are exported into a fresh memory, that memory can be the store;
one must not count its initial blank state as free and also call the
operation an erasure. Conversely entropy alone does not certify cyclic
reuse: a mixed reset target may have the original entropy while its
correlations with old inputs have changed, as in Section 3.

## 8. A counted cartridge is a valid finite-use contract

Let C be a processing core in an arbitrary joint state rho_(C,R), and
let C' be an independent replacement cartridge with the same finite
Hilbert space and the specified ready density sigma. A complete SWAP
gives exactly

    SWAP_(C,C') [rho_(C,R) tensor sigma_(C')] SWAP_(C,C')
        =sigma_C tensor rho_(C',R).                   (R18)

The core is reset and decoupled from the old reference. All its former
information, entropy and correlations are in the spent cartridge.
This is a full-state identity, stronger than a clock-marginal return.
If sigma includes new input ports entangled with a new reference, the
same identity relocates those ports and their correlations; their
fresh-input contract must then be stated explicitly.

With a fixed matched identification of equal bare Hamiltonians, a
whole-core SWAP commutes with H_C+H_(C'). Gate-by-gate conservation,
geometric locality and the simultaneous internal interactions still
require the separate complete implementation. Equal endpoint spectra
alone do not prove a local autonomous schedule.

A bank of finitely many fresh cartridges can therefore support finitely
many uses of the same processing core. It does not make the entire
core-plus-bank cyclic: spent cartridges contain the old states, and
retained outputs occupy additional memory. Restoring that bank to its
original independent ready state is another reset task with all its
resources and correlations included.

The whole enlarged finite device remains subject to Sections 1-2.
It may retain outputs past the original core's return by using a new
proved finite window or a changed system boundary. It cannot acquire
an exactly permanent newly changed record solely by renaming part of
its finite closed state as external memory.

## 9. Scope and falsifiers

These proofs delimit a useful finite-use construction; they do not
replace its positive local Hamiltonian or resource ledger. The relevant
failure tests are an incorrect retained-state contract, misuse of a
clock marginal as a joint reset, a copy-and-uncompute step violating
(R9), an omitted record or spent cartridge in (R13)-(R18), or a claim
of permanent finite closed retention inconsistent with (R1)-(R5).

The processing apparatus, input port, retained quantum record, classical
flags, spent donors and replacement stock have different roles. Their
boundaries and initial independence promises must be named before
claiming repeatability. No scientific executable, expanded device
calculation or simulation was run for this analytical note.

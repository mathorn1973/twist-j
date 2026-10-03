# C-FIELD-J-PREPARATION-MECHANISM-N

**PUBLIC, NON-CANONICAL. Prospective controlled quantum preparation
candidate, L1 only. Public freeze and scientific execution pending.**
Owner: A. M. Thorn / algebra_builder. Reservation:
[#1331](https://github.com/mathorn1973/twist-j/issues/1331).
Original work, Apache-2.0. Prepared 2 October 2026.

## 1. One premise to discharge, exact dependencies and exposure

The exact reference is Stage C at
`024936502544c2ec45acc8890a052c7b3aca26be`, especially
`notes/C-FIELD-J-LOCAL-INSTRUMENT-N/{PREREG.md,PROOF.md,RESULT.md}` and
`notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/REVIEW.md`. Its accepted scope
is conditional L1 mathematics, with no preparation or occurrence mechanism.
Its author specification is `0ca0605bee475ed3ab86f9a7c1129ea00a09d86d`,
full source `61a98eb1732ddf3effff0b386953e2fa7844f15e`, and final independent
review `c3e31a5a201285c1d47c8f15520e7204e845a884`. Stage B is admitted through
that C reference, at `05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa`.
The C proof and verifier are unchanged inputs, not a new audit target.

The named input replaced here is C's independently supplied coherent even
pointer bank: one active pointer and K fresh archive pointers. We construct
an **approximate finite loader** for those existing pointer coordinates.
We do not supply the coherent source-code preparation, C context unitaries,
internal trial controller or an actual-outcome law. Approximate preparation
does not satisfy C's exact ready-state premise literally; its use is through
the separately proved error interface below.

Normative authority remains public main/canon-v96
`44423153eee6259c7277eec5f5adbed9679f9146`, content
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`, CANON.md 873495 bytes, SHA-256
`eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
The coordinator revalidated authority, five canonical hashes, required
checks and ownership; the correct repository is its managed Git checkout,
not the unrelated directory above it. The new work-order attachment was
read as scope, not as evidence or execution authority. The accepted C
records and relevant repository policy were read at the stated sources.

Known exposure includes C's E-ready uniqueness, diagonal-even negative
control, Fourier preparation and finite archive theorem. The coordinator
proposed local antisymmetric-to-symmetric collisions, an initial coarse
contraction argument, the joint-error discipline and finite dyadic
obstruction. The builder derived the sharper local-overlap bound below
on paper. This is disclosed author/coordinator design assistance, not an
independent review or computational observation. No new scientific code,
import, trajectory experiment or numerical gap calculation has run.

Local reservoir engineering motivates the mechanism: Diehl et al.'s
[pair jump, Eq. (3)](https://arxiv.org/pdf/0803.1482) recycles an
antisymmetric neighboring component into its symmetric component;
[Verstraete et al.](https://arxiv.org/abs/0803.1447) describe local
dissipative state engineering more generally. These are background sources.
Our finite collision model, constants, carrier and proof are specified
here; their Born-Markov approximations, many-body realization or empirical
claims are not imported.

## 2. Complete finite controlled carrier and the added locality

Keep C's complete N>=2 packet/latch/active-pointer/finite-archive carrier,
including every old channel and every dirty-state branch. Its pointer
modulus is M=1226=2L, L=613. Let m=K+1, with pointer index i=0 active and
i=1,...,K the existing archive pointers. Archive flags are separate C
coordinates and are untouched by loading. All other C coordinates and a
finite reference are denoted Z. They include any source/reference
correlations and any declared purification of an initial pointer state.

On each pointer declare a **new internal mode graph**, an L-cycle with
vertices j in Z/L embedded by

```text
|j>_even = |p=2j mod 2L>.
```

Neighbors mean j,j+1 in this new graph. They are not B-chain spatial
neighbors or physical positions deduced from the integer p. Each collision
couples these two internal modes to one fresh two-state bath cell. The
odd pointer subspace is retained and the collision acts as identity there.
The new adjacency, its physical realization and the mapping to the C
pointer basis are explicit model premises.

Choose finite integers n_i>=0. Pointer i receives n_i complete sweeps;
each sweep visits j=0,1,...,L-1 in that fixed order. There are exactly

```text
B = L sum_(i=0)^K n_i
```

distinct bath qubits, each addressed by (i,sweep,edge). Every input and
output bath is retained. There is no infinite cold bath, repeated bath
reset, implicit replacement, random edge selector or successful-branch
postselection. For equal n_i=n the budget is mLn. An exhausted supply
prevents another promised loading step; the finite external script stops
with RESOURCE_EXHAUSTED and retains the state. This is not an autonomous
absorbing state or a reversible erasure theorem.

For a fixed classical script, the complete quantum carrier is the C
Hilbert space tensor (C^2)^(tensor B) tensor its finite reference. The
script owns the order, addresses and pulse durations. Phase-aligned
classical coupling coefficients, a reference phase convention and an
external clock are boundary inputs of the effective controlled model.
They are not unlisted quantum states claimed to be freely prepared.
No closed microscopic model of the classical drive or its physical work
cost is asserted; deriving those controls remains a named premise.

## 3. Exact local interaction, Hamiltonian and all-state inverse

Initially define the supported ideal-phase interaction for any L>=3; the
C application is L=613. On an even edge write

```text
d_j=(|j>-|j+1>)/sqrt(2),
s_j=(|j>+|j+1>)/sqrt(2),
P_j=|d_j><d_j|,       Q_j=I-P_j,
J_j=|s_j><d_j|.
```

All vectors refer to the embedded even modes. The identity I acts on the
entire 2L-dimensional pointer. Define the normalized vector

```text
nu_j=(d_j tensor |0> - s_j tensor |1>)/sqrt(2),
U_j=I-2|nu_j><nu_j|.
```

This total unitary is a reflection: it exchanges d_j|0> and s_j|1>, and
fixes their orthogonal complement. Its inverse is itself, including dirty
baths, odd pointer states and arbitrary pointer/source/bath correlations.
It changes neither C packet fields/reserves/latch nor archive flags.

An explicit effective pulse Hamiltonian is
H_j(t)=hbar g_j(t)|nu_j><nu_j| with nonnegative pulse area
integral g_j(t)dt=pi. Its exponential is exactly U_j. This is a supplied
phase-sensitive coherent interaction. It is not the different exchange
Hamiltonian whose pi/2 pulse gives minus-i swap phases. Both the local
relative signs and the exact pulse area belong to the primitive premise.
There is no E-projector, global Fourier transform, C target projector or
source-dependent control in this local Hamiltonian.

For a fresh input bath |0>, the exact isometry is

```text
U_j(psi tensor |0>) = Q_j psi tensor |0> + J_j psi tensor |1>.
```

Thus the reduced channel is Phi_j(X)=Q_j X Q_j+J_j X J_j^*, with
Q_j^*Q_j+J_j^*J_j=I. This reduction is derived from the retained unitary;
the bath output is not measured or discarded in the complete state.
No conditional normalization is part of the loader.

For a sequence of all B collisions in script order, let W be their ordered
unitary product, each acting on its named pointer and distinct bath.
W^-1 is the reversed sequence of these same reflections. With arbitrary
joint initial pointer/Z operator Omega and all fresh bath bits zero, the
complete output is exactly

```text
Omega_out = W [Omega tensor |0^B><0^B|] W^*,
          = sum_(u,v in {0,1}^B) K_u Omega K_v^* tensor |u><v|,
K_u = ordered product of Q_j or J_j on the addressed pointer.
```

All bath ket/bra cross terms remain. This formula specifies the full
joint post-state and its inverse, not only populations or pointer energy.

## 4. Initial domain, resources and energy account

The nonempty loading domain contains every joint density Omega on all
m pointer **even subspaces** and Z, including arbitrary mixed dirty
pointer states and correlations with Z or other pointers. Every bath
qubit is initially the independent pure basis state |0>. In particular,
the clean basis-blank loading input is

```text
Omega = |p=0><p=0|^(tensor m) tensor rho_Z.
```

No E or O pointer, Fourier state or copy of the desired global coherence
is present in this input. Source and reference preparation rho_Z remains
whatever the C protocol separately supplied. The broader dirty-domain
theorem does not assume a hidden independent pointer preparation.
Archive flags must already be zero for a subsequent fresh C trial; this
loader does not erase a used flag or record. Off-even inputs and nonfresh
baths have the same total W but are outside the stated convergence promise.

Keep the C energy E_C, in which active and archive pointers and archive
flags are flat at energy one. Give each bath bit energy one for both of
its states. The complete selected ledger is

```text
E_extended = E_C+B,
```

with the untouched reference at zero as in C. Every U_j commutes with
this bare energy on the full carrier because all affected pointer/bath
states are degenerate. All B packet and reserve accounts remain unchanged.
The new operation consumes fresh **purity and storage**, not a proved
amount of thermal cooling energy. The coherent vector E is not selected
as a lower-energy state by this flat spectrum. The graph defect operator
used below is a diagnostic, not a newly inferred physical Hamiltonian.
Neither the scalar ledger nor the effective pulse proves a physical work
cost, a drive realization, a thermal reservoir model or an SI dictionary.

Bath states after loading may be dirty, correlated and entangled. They
are retained, counted and unavailable as fresh |0> inputs unless a new
preparation mechanism supplies that resource. Running W^-1 restores the
old pointer and bath state jointly; it is not a free reset that also
keeps all old records. Applying a loader to a used C archive alters its
record; such a request is outside passive C retention and is never silently
treated as a fresh blank cell.

## 5. Universal sweep contraction, without numerical gap fitting

Every operator, identity and inequality in this section is restricted to
H_even, with I=I_even. The full odd sector is untouched and is excluded
from the stationary-density uniqueness claim.

On the even L-cycle set

```text
E_L=L^(-1/2) sum_j |j>,       P_E=|E_L><E_L|,
Phi=Phi_(L-1) ... Phi_0,     A=Q_(L-1) ... Q_0,
lambda_L=1-cos(2pi/L),       r_L=1-4/L^3.
```

Every local channel fixes P_E. For any density rho on the even subspace,
one edge has the exact fidelity increment

```text
Tr[P_E Phi_j(rho)]-Tr[P_E rho] = (2/L) Tr(P_j rho).
```

The proposed uniform proof for every integer L>=3 proceeds by two exact
operator estimates, not simulation of L=613:

```text
Phi^*(P_E)-P_E >= (2/L)(I-A^*A),
I-A^*A >= (lambda_L/4)(I-P_E) >= (2/L^2)(I-P_E).
```

For the first estimate, expand the adjoint channel prefixes and keep their
positive no-jump terms; their losses telescope to I-A^*A. For the second,
take psi perpendicular to E_L, x_0=psi, x_(j+1)=Q_j x_j,
a_j=<d_j,x_j>, b_j=<d_j,psi>. The norm loss is
D=||psi||^2-||A psi||^2=sum_j |a_j|^2. Local overlaps give

```text
b_0=a_0,
b_j=a_j-a_(j-1)/2                   (1<=j<=L-2),
b_(L-1)=a_(L-1)-(a_(L-2)+a_0)/2.
```

The coefficient matrix has maximum absolute row and column sums at most
two, hence sum|b_j|^2<=4D. The cycle quadratic sum P_j has eigenvalues
1-cos(2pi k/L), so its gap is lambda_L. Finally
lambda_L=2sin^2(pi/L)>=8/L^2. The proof must establish these identities
and the sine bound exactly, including the wrap-around edge. No decimal
eigenvalue, estimated rate or fitted constant is admitted.

Consequently for every even-supported density, every integer n>=0 and
F_0=Tr(P_E rho),

```text
1-Tr[P_E Phi^n(rho)] <= r_L^n(1-F_0).
```

The sharper factor 1-lambda_L/(2L) is also a valid analytic bound, while
r_L supplies a rational, deliberately conservative certificate. These
estimates imply convergence and uniqueness of the even-sector stationary
density P_E, but make no claim that the bound is optimal. A fixed sequential
sweep has a chosen starting edge; only its local primitives are homogeneous.
The finite sweep channel is not asserted to be translation covariant.

## 6. Complete joint approximation and finite C-protocol error

Let Omega_out be the full retained unitary output of section 3. Let Z'
mean Z together with **all output baths**, and let
F_(i,0)=Tr(P_E rho_(i,0)) for the initial pointer marginal. Put

```text
delta = min(1, sum_i r_L^(n_i)(1-F_(i,0))),
epsilon(delta)=min(1, sqrt(delta)+delta/2),
R_ready = P_E^(tensor m).
```

The claimed full-state bound is

```text
D(Omega_out, R_ready tensor Omega_(Z',out)) <= epsilon(delta),
D(X,Y)=(1/2)||X-Y||_1.
```

The remainder is the **actual output marginal**, not an independently
fresh environment. It can retain every old pointer distinction and every
source/reference correlation. The proof uses the commuting-projector
union bound 1-Tr(R_ready Omega_out)<=delta, the gentle bound for the
unnormalized projection, and the remaining marginal of trace at most delta.
This is a joint decoupling estimate, not merely agreement of position
populations. The original Z marginal is exactly unchanged because W acts
only on pointers and the initially independent baths.

For basis-blank pointers, F_(i,0)=1/L. For arbitrary admitted correlated
dirty pointers the conservative bound uses F_(i,0)>=0. Given any prescribed
0<epsilon_target<=1, a sufficient finite loading budget chooses the n_i
so the un-clipped sum above is <=4 epsilon_target^2/9. For equal n this
is the exact rational condition m r_L^n<=4 epsilon_target^2/9 on the
worst dirty domain, or m(1-1/L)r_L^n<=4 epsilon_target^2/9 for basis blanks.
The proof of existence uses 0<r_L<1; no gigantic n-step simulation is needed.

After loading, fix any admitted Stage-C finite causal protocol of horizon
h<=K with the same source/context/control descriptor for the actual and
ideal comparisons. Output baths are retained as a finite untouched
reference. The protocol does not reuse, read, reset or couple to them, and
does not choose a control from their unrecorded contents. Every C outcome,
zero branch, declared status and bounded stopping leaf is retained. The
complete conditional read instrument with its explicit outcome register
is a CPTP map, even though no actual outcome selection is claimed.

Trace-distance contractivity gives the same epsilon(delta) bound for the
complete joint output, including the whole C archive and baths. There is
**no additional factor h** for this once-loaded finite bank. Tracing unused
resources or the baths preserves the bound. The formal branch-trace
distributions differ in total variation by at most epsilon(delta), and
the probability weight of every complete prefix event differs by at most
that amount. These are comparisons of quantum operator traces, not a newly
derived actual-record distribution or sampling law.

For a single unnormalized branch, trace-norm error is at most 2 epsilon.
Normalized positive branches can amplify error: a sufficient bound is
min(1,2 epsilon/min(p_actual,p_ideal)) when both traces are positive.
There is no uniform normalized-state bound on arbitrarily rare prefixes.
An ideal zero-weight branch may acquire actual weight up to epsilon and
is never silently removed. A different controller that accesses the
loading baths would require its own declared comparison law; the present
handoff does not substitute a source-marginal channel for those correlations.

## 7. Diagnostics independent of C target matching

Let q_t be the expectation of |1><1| in the fresh bath bit after collision
t, and F_t the pointer's E_L fidelity at that boundary. The local isometry
predicts exactly

```text
q_t=Tr(P_(edge t) rho_(t-1)),
F_t-F_(t-1)=(2/L)q_t,
sum_t q_t=(L/2)(F_final-F_initial).
```

The left side is the expectation of the sum of all retained bath-mark
projectors. It is not an assertion that a measured number of actual marks
equals this expectation, and bath |1> is not a claimed emitted energy quantum.
For a basis blank F_initial=1/L, so the asymptotic sum is (L-1)/2=306
at L=613; every finite sum has its exact fidelity relation and is bounded
above by 306. This is a consequence in a separate bath observable, not
a fitted C LOW/HIGH probability or an occurrence model.

The equal-population control is particularly sharp. P_E gives zero marks
and is fixed at every edge. For rho_diag=I_even/L, the first edge gives
q=1/L and creates its two off-diagonal neighbor entries 1/L while leaving
all position populations 1/L. Thus translation-conjugation invariance of
a density is not support on the invariant-vector line. The bath and
coherence predictions distinguish the two inputs without using the C
instrument-matching condition.

There is also a finite exact limitation of this mechanism. At zero edge
phases every entry of U_j, Q_j and J_j in the pointer/bath basis is dyadic
rational. Any finite unconditional sequence from a dyadic initial density
and basis baths has a dyadic reduced density. Since 1/613 is not dyadic,
it cannot equal P_E exactly. This covers the specified basis-blank loading
input, not arbitrary initial states, already supplied E, diagonal-even
inputs with denominator 613, postselected normalized branches, different
phase primitives or other preparation mechanisms. Infinite-sweep convergence
does not imply an exact finite implementation with finite baths.

## 8. Phase, dirty-bath and odd-sector controls

To expose the phase premise, replace each pair by

```text
d_j(theta)=(|j>-exp(i theta_j)|j+1>)/sqrt(2),
s_j(theta)=(|j>+exp(i theta_j)|j+1>)/sqrt(2)
```

and use the corresponding total reflection. A common nonzero dark vector
exists iff product_j exp(i theta_j)=1. The edge equations then determine
one line with equal magnitudes and successive phases
psi_(j+1)=exp(i theta_j)psi_j. Nontrivial cycle holonomy leaves no common
dark vector. A consistent nonconstant phase pattern generally prepares a
different line from E_L. This is a common-kernel statement, not an unproved
classification of every steady state of a phase-mismatched sweep. The
positive rate/interface theorem is frozen at theta_j=0 on every edge.

No bath freshness test is performed. A dirty input still follows U_j and
its inverse, but its channel need not equal Phi_j. For example E_L with
an incoming bath |1> gives output E_L fidelity (1-2/L)^2 after one edge,
so a reused bath can spoil readiness. An odd pointer is unchanged by all
loading pulses and cannot become the even E_L. Odd-sector leakage or a
dirty archive flag is not removed by postselection. On those inputs the
full state remains specified and the positive loading guarantee is absent.

## 9. Premise-discharge table and remaining physical boundary

| Ingredient | Disposition in this candidate |
|---|---|
| C pointer coordinates, code, B transport and conditional instrument | Inherited unchanged from the exact accepted C source. |
| Independent ideal E bank | Replaced by a finite local loader with the proved joint approximation, not exact finite readiness. |
| Pointer basis blanks | Supplied simple basis preparation for the clean loading slice; dirty even inputs are additionally covered. |
| Pure fresh bath bits and finite storage | Newly supplied, explicitly B=L sum n_i and fully retained after use. |
| Neighbor-mode graph and local phase-sensitive reflection | Newly selected effective microscopic interaction; no global E state or Fourier gate is supplied. |
| Phase alignment, pulse area, classical address/clock script | Explicit external control premises; physical control/work implementation remains open. |
| Complex quantum state/channel formalism and flat energy convention | Inherited/selected effective assumptions, not derived from native U or J. |
| C source-code loading, context controls, zero flags and trial schedule | Remain supplied; this pointer mechanism does not discharge them. |
| Actual parity occurrence, realized records and their measure | Remain open; no sampler or Born-origin claim. |

The construction proposes an effective, externally controlled local
purification mechanism, not a hardware demonstration or closed autonomous
integer law. It closes only its named mathematical loading task if the
proof and gates pass. QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS
and QDD-INSTRUMENT-CLASS-COMPLETENESS retain their full registered scope.

## 10. Exact audit, paths, stdout and execution envelope

The author source to be frozen after this specification is

```text
notes/C-FIELD-J-PREPARATION-MECHANISM-N/PROOF.md
reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/verify.py
reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/README.md
```

After an actual pinned execution, the coordinator records exact scientific
stdout in `reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/EXPECTED.txt`, its
custody/environment in that directory's RUN.md, and the scoped conclusion
in `notes/C-FIELD-J-PREPARATION-MECHANISM-N/RESULT.md`. Independent review
uses separately frozen author-blind sources and its own reproduction path
`reproduce/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/`, not this verifier.

The command from repository root is

```text
python3 reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/verify.py
```

The verifier is standalone Python 3.10+ standard library, with exact integer
and Fraction arithmetic, no external runtime data or predecessor imports.
Sparse complete-state amplitudes or exact source operator blocks are allowed;
floating point, estimated spectral gaps, empirical randomness and numerical
trace norms are not. Internal values use exact built-in structures; no
all-Python-object parser theorem is proposed. The required envelope is
120 seconds, exit zero and empty stderr. Existing `tools/check_reproduce.py`
will replay the registered reproduction without a workflow change. Actual
x86_64/aarch64 evidence and byte identity must be obtained rather than
inferred from notes-only checks.

The finite domains are fixed as follows. They audit universal proofs;
none is a simulation of the enormous sufficient L=613 cooling budget.

1. **Local dilation and all-state scope.** For L=3,4,5,7 and every edge,
   construct U_j on the complete 2L-pointer times two-state bath, check
   its reflection/generator identities, inverse, odd-sector identity and
   the flat-energy account. Check all complete basis vectors for the
   inverse (396 cases), and all (2L)^2 pointer matrix units with fresh bath
   zero against the reduced Q/J channel (2236 cases). Verify channel
   completeness. Include dirty bath one and its explicit loss of E fidelity.
2. **Uniform contraction certificate.** For every L=3,...,12, work with
   L-by-L matrices restricted to H_even and I=I_even. Construct rational
   Q_j, A, the no-jump loss decomposition, derivative rows and
   the lower-triangular overlap matrix. Check the stated exact row identity
   and absolute row/column bounds. Check, by exact rational positive
   semidefinite certificates, the graph bound
   sum P_j >= (8/L^2)(I-P_E), the loss bound
   I-A^*A >= (2/L^2)(I-P_E), the first-jump inequality and the resulting
   Phi^*(P_E)-P_E >= (4/L^3)(I-P_E). The universal trigonometric/gap proof
   remains analytic; these ten dimensions do not prove L=613 by extrapolation.
3. **Finite reduced preparation and bath identity.** For L=3,4,5, take
   every basis density, I/L, P_E, P_(d0) and P_(s0): L+4 states per L.
   Follow exactly four full sweeps, checking boundaries n=0,...,4
   (120 state/boundary cases, 392 edge collisions). Check positivity,
   trace one, the rational contraction certificate at every boundary,
   E stationarity and the exact cumulative bath-mark identity. Check the
   first-edge identical-population/unequal-coherence control explicitly.
4. **Full correlated two-pointer environment.** At L=3 load two pointers
   with one sweep each and six distinct fresh bath bits. Use the initial
   pure state (|0,0>|0>_R+|1,1>|1>_R)/sqrt(2), with reference dimension
   two, as well as the basis product |0,0>|0>_R. Retain every bath amplitude.
   Check full normalization, reversed-unitary recovery, unchanged reference
   marginal, agreement with the reduced two-pointer channel, both pointer
   fidelity bounds and the product-ready union bound. Check the projected
   remainder/partial-trace identities used in the joint error proof;
   no approximate eigenvalue or trace-norm routine stands in for that proof.
5. **Phases and finite exact boundary.** For L=3,4,5,7 and every edge-sign
   pattern exp(i theta_j) in {+1,-1} (184 patterns), check the common
   difference-matrix rank: L-1 for sign product +1 and L for -1. In the
   consistent cases construct its equal-magnitude dark line and check
   every local channel fixes that density; distinguish nonconstant phase
   patterns from the positive E-ready contract. Check dyadic closure of the
   zero-phase local matrices and all finite densities in item 3 when their
   inputs are dyadic. Check explicitly that 1/613 is not dyadic. The
   all-finite-sequence obstruction is a proof, not a bounded census.
6. **Approximate handoff accounting.** Check the commuting two-pointer
   projection union identity and positive remainder, and the unnormalized
   projection marginal decomposition, on the two full states in item 4.
   Their all-m proofs remain analytic. Audit finite budget
   and readiness descriptors at K=0,1,2, n=0,1,2: m=K+1, B=mLn, no duplicate
   bath addresses, explicit no-capacity disposition and no flag reset.
   At all 120 boundaries from item 3, embed each density rho in the full
   2L pointer and compare it with P_E. Apply the controlled shift
   |a><b| tensor X -> |a><b| tensor S_a X S_b^* for a,b in {0,1},
   followed by both diagonal pointer-parity branches. Check exactly that
   the actual-minus-ideal output equals this composed map applied to
   |a><b| tensor (rho-P_E), that the two-branch sum preserves trace,
   and that passive parity rereading keeps the same branch and gives zero
   on the opposite branch (960 source-unit/outcome cases). Retain both
   branches and no normalized postselection. These are exact composition
   identities, not numerical trace-norm estimates. The all-horizon C
   trace-distance bound is proved by CPTP contractivity; this small
   interface audit does not rerun or enlarge the C audit.

Scientific stdout will have one PASS summary per these six audit groups,
their stated finite counts, the fixed physical L=613 and m=K+1 resource
formula, and the explicit scope `approximate pointer preparation;
occurrence NOT DERIVED`. It will contain no host/time metadata, fitted
rate or precomputed successful result. EXPECTED.txt is populated only from
an actual pinned run. Any deterministic additional counters are limited
to the declared loops, not new searches or target fitting.

## 11. Gates, falsifiers and stopping discipline

Freeze and publicly read back this specification before the fresh reviewer
receives it. That reviewer sees only this contract and admitted sources,
and freezes its own derivation/breaker before author proof/code exposure.
The complete author proof and reproduction sources must then be committed,
pushed and publicly read back before any scientific import or execution.
Static syntax parsing is permitted. No frozen scientific file is amended
to conceal a failure. All run records use exact pins and the existing
repository runner and architecture procedures.

Any counterexample within the stated domain rejects the affected claim:
F1 failure of the all-state local unitary, inverse, carrier or resource
account; F2 incorrect complete joint channel or an unretained bath/control
resource; F3 incorrect analytic contraction constant or convergence
claim; F4 failure of joint decoupling or the finite C-protocol error bound,
especially with correlations or rare prefixes; F5 false bath diagnostic,
dyadic obstruction, phase or dirty-state control; F6 a concealed initial E,
Fourier replacement, postselection, purity refresh or output-driven tuning;
F7 interpreting approximation as exact readiness, an expectation as actual
occurrence, flat-energy commutation as physical work accounting, or the
new mode graph as already realized B spatial locality.

The intended handoff states the exact source pin, approximate-ready metric,
finite budget and untouched-bath interface, together with every surviving
source/control/occurrence premise. No merge, Canon promotion, gate change,
workflow change, release, hardware result or empirical confirmation is
authorized by this candidate.

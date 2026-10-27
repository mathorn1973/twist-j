# Locality, preparation and the complete resource contract

**NON-CANONICAL, L1. Conditional analytical candidate-T; independent
mathematical acceptance of this extension is pending.** Author: A. M. Thorn.
License: Apache-2.0. Public reservation: #1767.

The mathematical review of PR #1768 at
`d13851796d5e7a316e1f628407e1bedef04f9bad` accepted the earlier seven-note
package in its declared scope. Those seven files are unchanged here.
The [fixed-revision review](https://github.com/mathorn1973/twist-j/pull/1768#pullrequestreview-5642195943)
does not accept the new proofs below. This continuation supplies a local
qubit implementation and a preparation from specified product resources,
while retaining the preparation resources that it has not derived.

Read [PREPARATION.md](PREPARATION.md) for the exact product-to-packet map,
[LOCALITY.md](LOCALITY.md) for conserving local synthesis, and
[LOCAL_HAMILTONIAN.md](LOCAL_HAMILTONIAN.md) for the static generator,
geometry and physical record. [LOCAL_VALIDATION.md](LOCAL_VALIDATION.md)
records the new review obligations and integrity evidence.

## 1. What the construction implements

Keep the finite source family and complete word of FINITE_MODEL.md.
Its finite source energies obey

    q_phys=q_f+r_f,   [q_f,r_f]=0,   0<=r_f<=dI,
    q_f=d sum_(j=0)^m j P_j,        m=ceil(Delta/d).

Choose a joint eigenvector x_* of q_f,r_f and a complete unitary P_x
mapping x_* to the specified source vector x_0. Starting from x_*, the
compiled word prepares its own buffered battery, executes the single
lift of U_f(P_x tensor I), and reversibly writes the accepted memory into
an occupied archive. The new pointer is written last. All rejected
branches and the previous archive contents remain in the state.

This constructs a finite encoded device for the stated completed-word
contract. Its weighted label sites represent the finite compressed
source. It does not confine or reproduce the entire original spatial
walk, its interactions, or its continuous trajectory. The matrices U_f
and P_x, spectral labels and residual energies specify the device's
couplings. Their physical manufacture is not supplied by a dimension
bound or by existence of a finite gate decomposition.

## 2. Preparation and site counts

For a desired joint compensation error epsilon, take

    M=max{1,ceil(2m^2/epsilon^2)-1},   N=M+2m.

The battery uses N physical equal-gap qubits, initially

    |1>^m tensor |+>^M tensor |0>^m.

The exact conserving Householder map in PREPARATION.md prepares the
unary binomial packet. The single complete compensated word has joint
trace-distance error at most

    e_B=m sqrt(2/(M+1))<=epsilon,

including an arbitrary passive reference and the battery. This is one
whole-word estimate. The battery is neither renewed at each gate nor
assumed to return to its initial state.

Let s=dim X_f. There are ell<=s+m weighted label sites after inserting
missing integer charges. A binary encoding of the source information,
occupied archive and pointer needs

    f=16+3*327681+655392

qubits: three 26-dimensional factors, a pointer, 327681 five-dimensional
factors and 655392 binary factors. Invalid binary encodings receive the
complete unitary extensions specified in LOCALITY.md. They are not
deleted from the hardware Hilbert space. Additional acceptance flags,
control work and buses use the counted scratch padding.

For example the compiler uses b=ell+N+f and n=16b cells on each of three
tracks. Let J be its finite routed primitive count, including the final
pointer CNOT and any parity padding. LOCALITY.md provides a deliberately
loose finite synthesis bound; it is not an efficient circuit claim.
With W=3n and the clock choice

    L_c>=max{J(W+3)-1,512},   K=2L_c,

the exact total hardware count is

    S=3n(J+1)+K+1 qubits,       dim H_raw=2^S.

This counts all energy padding, weighted label padding, zero-energy
information and scratch, every future data row and every cursor site.
The containing rectangle has width at most W+K+3 and height 2J+1.
Interactions involve at most seven qubits in a radius-four lattice
ball, with a fixed degree bound of 64. A large site dimension or a
global controlled interaction is not used as the locality argument.

## 3. Initial state, purity and phase resources

The input logical label, old memory and occupied archive may be arbitrary
and correlated with the passive reference, within their encoded spaces.
They occupy 15 physical qubits. All remaining S-15 qubits have specified
pure input states in the ideal preparation contract:

- M qubits are common-phase |+> states;
- m battery buffer qubits, one chosen label site and the initial cursor
  are excited basis states;
- all other qubits are zero, including scratch, acceptance work, every
  pointer copy, other cursor sites and every unused future row.

There are no uncounted ready copies behind the row-transport construction.
The charged initial label and cursor are explicit resources even when
their role is to select a program rather than to deliver work.
The supplied pure qubits carry (S-15) ln 2 of entropy deficit relative
to maximally mixed qubits. This is a purity inventory, not a universal
work-cost formula at an unspecified temperature.

The M phases are fixed relative to the real couplings and the target-word
convention. A phase-averaged bank has a different state and does not
fulfil the joint approximation contract. Finite per-qubit preparation
errors may be summed to obtain a sufficient joint error bound; this
does not assume that separately good marginals exclude correlations.
The specification of arbitrary exact gate coefficients is a further
control resource, not a finite classical program of proved short length.

## 4. Energy, including the clock and unused rows

Choose the optional positive label and cursor gaps mu=kappa=d. On every
data row, an energy bit has gap d and a label bit has prescribed bare
gap mu+d j_i+r_i. Let N_X count occupied label bits over all rows,
N_C count occupied cursor sites, and set

    H_0=sum_(rows,i)[d n_(E_i)+(mu+d j_i)n_(X_i)]+kappa N_C,
    R=sum_(rows,i) r_i n_(X_i),
    E_phys=H_0+R,
    H=H_0+H_prop=E_phys+(H_prop-R).

Every raw gate conserves H_0 and N_X. The positive local H_prop commutes
with H_0. The onsite correction -R is part of the actual interaction;
dropping it changes the law. The full H is positive and conserved.
For every time and every raw input,

    -d N_X <= exp(itH/hbar) E_phys exp(-itH/hbar)-E_phys <= d N_X.

The ideal input has N_X=1, so its unconditioned bare-energy drift is at
most d at all times, including preparation. This conclusion is not
transferred to a selected successful ensemble. Raw multiple-label
defects require their actual expectation of N_X, even if rare.

For the ideal product readiness, with source rounded charge j_* and
residual r_*, the complete initial moments are

    <H>=mu+d j_*+d(m+M/2)+kappa+g,
    Var(H)=M d^2/4+g^2 K/(K+1)^2,
    <E_phys>=mu+d j_*+r_*+d(m+M/2)+kappa.

The original N-qubit battery capacity is Nd. The installed energy
capacity is larger because of padding and row copies. With

    C_D<=n(J+1)[mu+(m+1)d],

the full operator satisfies

    0<=H<=[C_D+kappa(K+1)+(K+1)g]I.

The bare energy capacity adds at most d n(J+1) to
C_D+kappa(K+1). These are hardware capacities, distinct from initial
mean energy. At fixed g, duration scales with K+1. Choosing a fixed
window [T_h,2T_h] instead requires g=pi hbar(K+1)/(3T_h).
The construction does not hold computation time, length and coupling
strength fixed simultaneously.

## 5. Joint readiness error and the recorded output

Let zeta bound the trace distance of the entire actual initial state
from the declared joint input, uniformly over the admitted input and
reference. All defective configurations then evolve under the same H.
No favorable part of a thermal mixture is silently selected.

Write p_0 for ideal source acceptance and Sigma_0 for its subnormalized
archive/reference output. On exact readiness, the local physical
pointer has subnormalized output w(t) Sigma, where Sigma is the
completed compiled-word output and

    w(t)>=1-beta,    beta=(3/4)^L_c<2^-128

throughout [T_h,2T_h]. This is a read of the final pointer, with no clock
postselection. The joint battery error changes the complete
accepted-plus-rejected comparison by at most epsilon. Thus

    p_actual(t)>=w(t)(p_0-epsilon)-zeta,
    D(rho_actual,acc(t),rho_ideal,acc)
       <=epsilon/p_0+zeta/[w(t)(p_0-epsilon)],

provided the lower success bound is positive. The second denominator
uses the completed compiled success, bounded below as displayed.
This conservative triangle bound includes false acceptance from
defective pointer, clock and auxiliary states.

For example take epsilon=2^-104 and

    zeta<=min{2^-104,1/[n(J+1)]}.

The source margins in FINITE_MODEL.md then imply

    p_actual(t)>1/20000,
    D(rho_actual,acc(t),rho_ideal,acc)<20000*2^-102,
    u_actual,acc(t)<1/1000000.

For the last statement include the compressed unwanted-band test in
the same comparison. It commutes with q_f; commutation with r_f is not
required or inferred. Extend its final-row original one-label operator
by identity on filler and other invalid source sectors. This counts
those invalid source outputs as unwanted, while agreeing with A_bad on
the admitted code. The extension still commutes with the rounded H_0,
whose free phases do not change its joint record statistics. This is still a
specified effect, not a constructed material detector of that effect.

The actual full joint endpoint carries free H_0 phases. The whole-word
approximation is in the corresponding interaction frame. The
archive/reference reduction and commuting band statistics used here
are unchanged by those free phases; the complete source state need
not be stationary on the final tail.

A joint zeta bound also gives

    <N_X>_actual<=1+zeta n(J+1).

Hence the above example bounds raw mean-energy drift by 2d, including
defects. To request a particular physical drift tolerance delta, set
d=delta/2 before choosing the circuit and then choose zeta as above
after its finite size is known. There is no assumption that a fixed
small error remains negligible against an arbitrarily large row bank.

## 6. What thermal preparation can and cannot supply

Products of onsite Gibbs states, including at different temperatures,
commute with the summed bare energy. Exact conservation preserves that
global energy symmetry, so preparation cannot create reduced battery
energy coherence from that input alone. Such products need not be
stationary under an interacting conserving Hamiltonian. PREPARATION.md
proves a quantitative separation from stationary battery states. The
M supplied plus qubits remove that hypothesis; they are not derived
from a temperature gradient by this construction.

With mu=kappa=d, every charged zero site has gap at least d. If those
zero sites are independently supplied in Gibbs states of inverse
temperature beta_T, their total excited-state weight is at most their
number times exp(-beta_T d). This is one possible approximate resource
for that part of the readiness. It does not prepare the excited seeds,
the coherent bank, or the zero-energy information/scratch bits: a Gibbs
qubit of zero gap is maximally mixed at every temperature. Providing
their purity needs an additional specified entropy sink or pure stock.
The estimate itself also presupposes the supplied product Gibbs states;
it is not a bath preparation mechanism.

A finite full-rank thermal closed input cannot evolve unitarily into
an exactly pure nontrivial ready marginal. Approximate initialization,
work, baths, reset and their interaction energies would require an
extended resource model. The current positive result starts from the
explicit resource list in Section 3 and does not close that further
thermodynamic preparation problem.

## 7. A separate contract can use a sharp battery

For the narrower target retaining only archive/pointer/reference and
the commuting unwanted-band statistics, PREPARATION.md proves an exact
alternative. Use N=2m, a sharp unary battery |m>, and the sharp source
x_*. Their complete total-charge fiber represents the whole word
exactly. Tracing the source and battery gives exactly the ideal record,
including its reference correlations. No M plus qubits are required.
The same local compiler and static clock can implement that word, with
its own smaller finite parameter list and e_B=0 for these outputs.

This alternative does not prepare a standalone coherent x_0 and does
not approximate the full source/battery product state. Source coherence
is represented by correlations within a fixed total-energy sector.
Pure sharp seeds, scratch, future rows and clock remain required.
It is therefore a useful narrower theorem, not a silent replacement
of the full joint-state contract or a thermal closure claim.

## 8. Precision, reversal and remaining physical obligations

The formulas above use exact couplings. For a bounded implemented
perturbation with norm at most nu, Duhamel's inequality gives a joint
state error at most |t|nu/hbar. On [0,3T_h], adding
3T_h nu/hbar to the readiness error is sufficient for the output
bounds. Finitely many local terms can be assigned individual tolerances
whose norm sum is nu. If those perturbations commute with H_0 and N_X,
the all-time residual-energy inequality is retained. Without that
symmetry the finite-time output estimate does not prove the same
uniform energy law. No experimental tolerance achievement is asserted.

At 3T_h the ideal one-cursor dynamics reverses the programmed word.
The archive/pointer/reference marginal returns to its initial value;
the new pointer is zero. Initial-state error zeta bounds its false
pointer probability at that time. There is a finite read window, not
permanent storage. A detached detector, lasting retention, reset and
individual occurrence remain separate physical interfaces.

The local and preparation claims are analytical existence results with
explicit large resource costs. No expanded circuit, physical experiment
or new scientific executable supplies additional evidence here. The
new proofs require independent review, and neither Canon nor the status
of their conditional source inputs is changed.

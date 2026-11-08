# Local compilation of two complete raw thermal-core endpoints

**NON-CANONICAL, L1. New analytical successor; independent mathematical
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1769.

The predecessor is frozen at
811daddc3b2f085ee5bc6f50261ac95a4c11fe44. Its twenty-two files under
C-SPECTRAL-ENERGY-FINITE-RECORD-N are unchanged. This note replaces its
large-support endpoint instruction by a finite product of local gates.
The approximation holds on the whole raw core and with any passive
reference, including all thermal defects. It does not rely on the
earlier compiler's one-label semantic code.

The primary construction includes the old rounded-energy phases exactly.
The resulting two-attempt word has an operator-norm error below 2^-119.
All coupling scales are fixed before its depth and geometry are chosen.
This note supplies the local instruction word and its error; the companion
geometric construction supplies contact transport, cursor routing and
the complete autonomous record window.

## 1. Frozen core terms and their raw symmetries

Let D be the predecessor's complete S-qubit thermal core. Its generator,
rounded onsite energy and occupation budget are

    H_D=Q_D+A_D,
    A_D=H_prop,D,
    C_D=N_X,D+n_fuel,D.

Use the exact operators of predecessor THERMAL_CLOCK.md, including its
special launch diagonal, completion contraction, all row copies and all
donors. Write K_D for its number of physical cursors and g_D for its
fixed propagation scale. Its interaction decomposes as

    A_D=sum_(l=1)^L h_l,             L=2K_D+1.           (L1)

The list contains K_D edge terms followed by K_D+1 potential terms,
in a fixed declared order. Zero coefficients, if any, are kept as identity
instruction positions. Each term acts on at most seven physical qubits.
The launch potential v_0 P_in is included; it is not replaced by an
incorrect ordinary fuel number potential. On the whole raw space,

    h_l=h_l^*,
    [h_l,Q_D]=[h_l,C_D]=0.                              (L2)

These identities were proved term by term for the frozen local law.
They include zero and multiple cursors, multiple labels, invalid binary
strings and dirty work registers.

For its frozen edge coefficients a_j and potentials v_j,

    ||h_edge,j||<=2a_j<=g_D,
    ||v_j V_j||<=v_j,
    sum_j v_j=(K_D+1)g_D-2 sum_j a_j.

Hence the useful norm-sum bound is

    Lambda_D:=sum_l ||h_l||<=(K_D+1)g_D.                (L3)

No expanded spectrum is needed for (L3). It is a termwise bound using
the complete raw positive blocks, including the partial-isometry launch
and completion edges.

The target endpoint is the literal predecessor unitary

    tau=pi hbar(K_D+1)/(2g_D),
    V=exp(-i tau H_D/hbar).                            (L4)

It acts on every raw state. In the new law tau specifies this target
matrix, not the physical time allotted to its later compiled execution.

## 2. First-order product bound with an explicit constant

For M>=1 define

    T_M=[exp(-i tau h_L/(hbar M)) ...
                         exp(-i tau h_1/(hbar M))]^M.   (L5)

The rightmost factor executes first. Each factor is an exactly specified
unitary on at most seven qubits, hence a matrix of size at most 128.
Its exponential does not enlarge its support. Equation (L2) implies
that each factor exactly conserves Q_D and C_D on all raw states.

For self-adjoint A,B and s>=0, differentiate

    F(u)=exp[-i(s-u)(A+B)] exp(-iuA) exp(-iuB),
    0<=u<=s.

The derivative contains the commutator [B,exp(-iuA)], whose norm is
at most u||[A,B]|| by integrating its own derivative. Therefore

    ||exp[-is(A+B)]-exp(-isA)exp(-isB)||
         <=s^2 ||[A,B]||/2.

Induction over the factors, using
||[sum_l A_l,B]||<=sum_l ||[A_l,B]||, gives the one-slice bound.
Telescoping the M unitary slices then yields

    ||T_M-exp(-i tau A_D/hbar)||
       <=tau^2/(2hbar^2 M) sum_(l<k)||[h_l,h_k]||
       <=tau^2 Lambda_D^2/(2hbar^2 M).                 (L6)

For the last inequality use ||[h_l,h_k]||<=2||h_l||||h_k|| and
2 sum_(l<k)||h_l||||h_k||<=Lambda_D^2.
There is no factor equal to the raw Hilbert-space dimension.

Substituting (L3)-(L4) gives

    delta_M:=||T_M-exp(-i tau A_D/hbar)||
           <=pi^2(K_D+1)^4/(8M).                      (L7)

Freeze the integer choice

    M=2^121 (K_D+1)^4.                                (L8)

The exact inequality pi<4 proves

    delta_M<=pi^2 2^-124<2^-120.                       (L9)

This is deliberately conservative. It is an analytical norm estimate,
not a numerical simulation or an optimized product-formula claim.

## 3. Exact onsite phases in the primary raw construction

The rounded onsite Hamiltonian is

    Q_D=sum_(u=1)^S q_u n_u,

with the fixed nonnegative integer-multiple gaps q_u of the predecessor.
All its terms commute. After (L5), execute the S one-qubit gates

    Z_u=exp(-i tau q_u n_u/hbar),       u=1,...,S.

Keep the identity positions q_u=0 in the stated schedule. Their product
is exactly exp(-i tau Q_D/hbar). Since [Q_D,A_D]=0, define

    V_tilde=[product_u Z_u] T_M,
    ||V_tilde-V||=delta_M<2^-120.                      (L10)

Equation (L10) is an operator statement on the entire raw core, without
an initial-state restriction. The onsite phases use Q_D, not the distinct
physical bare energy Q_D+R_D. They are diagonal gates and preserve both
the rounded energy and C_D exactly.

The primary ledger includes these S gates per run. No free-energy phase
is dropped from that raw operator comparison.

## 4. Two runs, exact exports and complete replacement

Supply the active core D, two same-spectrum S-qubit cartridges F_1,F_2,
and two seven-qubit output slots O_1,O_2. The source interface has three
admitted fifteen-qubit information inputs I_0,I_1,I_2, possibly jointly
entangled with a passive reference. They occupy the fixed row-zero input
sites of their packages. The output block B is instead the final-row
archive and pointer together with its separate completion latch.

Let E_i be the complete SWAP of B with O_i, and let R_i be the complete
SWAP of D with F_i. The exact and compiled words are

    W=R_2 E_2 V R_1 E_1 V,
    W_tilde=R_2 E_2 V_tilde R_1 E_1 V_tilde.             (L11)

Each export consists of seven corresponding one-qubit SWAPs. Execute
the five zero-gap archive swaps and the zero-gap pointer swap first;
execute the gap-d latch swap last. This ensures that a comparison slot
with initially zero latch is not made readable while its quantum block
is only partly transferred. No blank archive value is assumed.

Each replacement consists of S corresponding site SWAPs. Their product
is the complete core-cartridge SWAP on every raw state. Replacement is
unconditional, including rejected and dormant attempts. The second
replacement is retained so that the core is fresh after attempt two.
All previous output-slot contents and core/reference correlations enter
the spent cartridges.

The unpadded scheduled logical word has exactly

    P_0=2ML+14+4S
       =2M(2K_D+1)+14+4S                             (L12)

positions before contact routing and padding. The 4S count includes two
sets of onsite phases and two full-core replacements. Additional exact
transport operations must be counted by the geometric construction;
they are not absorbed into (L12) as unmentioned free gates. The local
controller denotes its padded stage count by P, with P_0<=P<=P_0+3.

Insert one hybrid word between W and W_tilde. Unitary multiplication
preserves operator norm, so (L10) gives

    ||W_tilde-W||<=2delta_M<2^-119.                    (L13)

For every joint initial density on the entire bank and any passive
reference, purification and contractivity imply

    D(W_tilde rho W_tilde^*,W rho W^*)<=2delta_M.       (L14)

The same estimate holds after any common output reduction or instrument.
There is no independence assumption between the two information inputs,
and no claim that the state left by the first run remains an independent
fresh input. The exact complete replacement is what supplies fresh
hardware for the next run while preserving the new input's correlations.

## 5. Exact energy symmetries of every programmed primitive

Let Q_bank sum the rounded energy over D,F_1,F_2,O_1,O_2, and put

    C_bank=C_D+C_(F_1)+C_(F_2).

Every factor of (L5) and every onsite phase conserves Q_bank,C_bank.
A corresponding-site reset SWAP conserves the sum of the two identical
onsite spectra and the corresponding occupation-budget coefficients.
Export acts only on archive, pointer and latch factors, none of which
contributes to C_bank, and exchanges equal onsite spectra. Consequently
every programmed prefix obeys

    [U_prefix,Q_bank]=[U_prefix,C_bank]=0.              (L15)

These are exact raw-space identities, independent of M and of the
product approximation. For the physical bare reading

    E_bank=Q_bank+R_bank,          0<=R_bank<=d C_bank,

the same elementary order argument gives

    -d C_bank<=U_prefix^* E_bank U_prefix-E_bank
                                      <=d C_bank.     (L16)

The approximation does not add a drift term per Trotter factor. For an
autonomous implementation preserving the enlarged rounded energy and
budget, (L16) extends to every time with all added copies included.
The geometric ledger must count those copies in its actual budget.
This remains an unconditioned energy statement, not exact conservation
of the original unrounded spatial energy on a selected successful branch.

## 6. A coupling cap fixed before program growth

Let E_* be the maximum physical onsite gap of the frozen old core. In
particular its fuel gap G+r_*>=4d is included. Freeze

    J_*=E_*+g_D+d,
    g_out=J_*/4                                      (L17)

before choosing M or the successor's clock geometry. These constants
depend only on frozen core parameters, not on the new program depth.

The old defining terms have norms at most g_D. In a standard positive
outer propagation block for one programmed unitary G,

    h_edge=a[(n_c+n_(c'))I
                   -s_(c')^+s_c^- G-s_c^+s_(c')^- G^*],

the norm is at most 2a. With the fixed outer scale in (L17), its spin
path coefficients obey 2a<=g_out and its potentials obey v<=g_out.
Even when G=(L5) acts on seven data qubits, the edge has at most nine
qubits and norm at most J_*/4. A sitewise SWAP edge has at most four.
The exponent in G is instruction data; it does not multiply the norm
of the outer propagation coupling.

The replicated bare sites have gaps at most E_*<J_*. New cursor gaps
2d,d, output latches d and an outer fuel gap 3d are also below E_*.
Residual counterterms have norm at most d. Keep onsite fields and cursor
potentials explicit rather than hiding a number of coincident terms in
one coefficient. The companion fixed site-incidence bound is part of
the strength account. Support nine, radius 256 and incidence 64 are the
declared successor geometry requirements; (L17) does not prove their
routing by itself.

If the final outer path has K_out edges, its spin-path window scale at
this fixed coupling is

    T_out=pi hbar(K_out+1)/(3g_out).                    (L18)

Increasing product depth or routing length increases this latency.
The construction does not keep the duration fixed by increasing g_out.
Nor are the gates in (L5) asserted to take physical time tau/M in that
new autonomous implementation.

## 7. Free frames, actual thermal inputs and an unused shorter option

The primary word comparison (L10)-(L14) includes the old Q_D phases.
An outer static law of the form Q_total+H_history nevertheless has its
own free factor exp(-itQ_total/hbar). For an arbitrary nonstationary
raw input that factor must remain in the final state. Multiplying both
compared words by the same free factor preserves (L13)-(L14).

For the actual declared input family the factor has no effect on the
joint density. Hardware Gibbs factors are diagonal in their onsite
physical energy basis, hence commute with their rounded onsite energies.
The fifteen information factors in each package have rounded energy
zero, even when their states are entangled across attempts and with R.
The output slots and thermal outer controller satisfy the same diagonal
condition. Therefore

    [rho_initial,Q_total tensor I_R]=0.

Every programmed gate and the complete history law preserve the rounded
energy. It follows that the free factor does not change the resulting
joint density. This is a symmetry proof for the actual thermal family,
not a statement that the raw source output is stationary for every input.

There is an optional shorter circuit, unused in (L12): omit the old
onsite phases and use T_M alone. At the start of each run the fresh
hardware Omega factors from all old systems, while its next information
input may remain correlated. Since Q_D acts trivially on that input,
the complete joint state commutes with Q_D. The actions of V and
exp(-i tau A_D/hbar) are consequently identical on it. Complete
replacement re-establishes the same premise before the second run.
That option saves 2S instruction positions, but its identification
with the original V word uses this state-family premise. The stronger
primary raw operator theorem and resource ledger do not use that saving.

## 8. Joint accepted comparisons and controller scope

Let p_12 be the probability of the specified two-record acceptance event
for the exact complete word W. For p_12>2delta_M, (L14), the complete
accepted-plus-rejected instrument, and normalization give

    |p_12,compiled-p_12|<=2delta_M,
    D(rho_12,compiled,acc,rho_12,exact,acc)
                                      <=2delta_M/p_12. (L19)

The record includes both exported quantum blocks and the passive
reference. Normalized one-use errors are not simply squared or treated
as independent output states.

For the actual thermal single-use channel, a uniform lower acceptance
bound p_min on every admitted conditional input implies

    p_12>=p_min^2.

This follows by conditioning the second use on the first outcome and
using the fresh-hardware replacement identity. It does not require the
two information inputs to be independent. Their conditional states
remain within the stated valid input code.

If one outer thermal launch executes both attempts, its activation
factor occurs once. With outer launch probability p_out, completed-tail
weight w and additional outer defect bound eta, the corresponding
probability comparison has the form

    p_both>=p_out w(p_12-2delta_M)-eta.                 (L20)

There is no second independent factor p_out. All old-core thermal errors
remain inside the actual one-use channels unless a separate comparison
to ideal source channels is made. The complete channel ledger must add
those and the outer readiness/window errors before applying a selected
joint-event denominator.

The unnormalized compilation contribution is below 2^-119. It therefore
fits inside a larger declared complete-channel budget such as 2^-96,
but does not by itself establish the latter budget or a numerical
conditional guarantee. Those depend on the actual outer resource count
and the stated joint acceptance event.

## 9. Scope and falsifiers

The result supplies an explicit finite-depth local instruction sequence,
raw operator and reference-uniform error bounds, exact primitive energy
symmetries, and a strength cap independent of the new program length.
It includes exact exports and two complete resets. It does not equate
the compiled intermediate trajectory with the original core trajectory.

Failure of a frozen local symmetry in (L2), the commutator estimate (L6),
the raw phase factorization (L10), the two-word comparison (L13), or
matched-spectrum conservation in (L15) would invalidate the corresponding
claim. A geometry that silently reuses high-degree contacts, omits
transport states, raises g_out with program length, or discards
noncanonical thermal sectors would not satisfy this successor contract.

No scientific executable, product-formula simulation, expanded circuit
enumeration or independent acceptance is claimed. The exact local
matrices and couplings remain supplied analytical data of this finite
construction.

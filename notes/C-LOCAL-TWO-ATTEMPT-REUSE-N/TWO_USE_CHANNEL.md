# Two attempts, fixed output sites and an exactly replaced core

**NON-CANONICAL, L1. Conditional analytical successor; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1769. The twenty-two predecessor files at
`811daddc3b2f085ee5bc6f50261ac95a4c11fe44` remain unchanged.

This note gives the complete two-attempt channel and its error budget.
The local compiler approximates each entire raw core propagator. Exact
export and replacement gates preserve the quantum records and restore
the hardware even when the propagator is approximate. A separate local
history carries out those gates, saves each output at fixed physical
sites, returns the working banks to their original sites and supplies
one shared thermal activation. Its finite read window is not permanent
storage under a recurrent Hamiltonian.

## 1. Fixed physical subsystems and the one-use channel

Let D be the S-qubit core specified by the frozen thermal construction.
Write D=T tensor I. Here I means the fifteen fixed physical row-zero
input sites for the logical label, old memory and occupied archive.
The other S-15 sites are T. The input on I has the declared valid-code
support and may be entangled with a passive reference R.

Let Omega_T be the declared product Gibbs hardware state. Its two
temperatures are those actually used by this successor. A colder
choice retains the predecessor's error bounds but is not silently
identified with a different numerical input state. Every charged and
zero-energy auxiliary in the core belongs to Omega_T; the information
input does not.

The output block B comprises the five archive bits and pointer in the
core's final physical data row, plus its separate completion latch.
All seven sites initially belong to T, not to I. Their physical bare
Hamiltonian is d n_L. Transport of an information value does not identify
its original row-zero tensor factor with its later physical output site.

Let

    V=exp(-i tau H_D/hbar),       tau=3T_h/2,
    E(sigma_I)=Tr_(D\B)[V(Omega_T tensor sigma_I)V^*]. (C1)

H_D is the complete old core generator. E is its actual complete
seven-qubit thermal output channel, including accepted, rejected,
dormant and defective components. It is extended by identity on every
passive reference. The source premises in the frozen package remain
conditional premises of this successor.

Use two full S-qubit cartridges F_1,F_2 with identical corresponding
physical spectra. Their fresh hardware states are Omega_T. The three
information inputs I_0,I_1,I_2 have an arbitrary joint valid-code state
rho_(I_0,I_1,I_2,R); they need not be independent. I_2 is the counted next
input left in D after the second reset, although a third attempt is not
executed. Every fresh hardware bank is independent of those inputs and
of the other hardware banks.

The two output channels have seven equal-spectrum sites each. Their
initial states need not be blank. The thermal implementation uses mixed
zero-gap bits and a cold, full-rank latch. The previous contents of each
output destination enter the core during export and then the spent
cartridge. They are never erased or omitted from the raw Hilbert space.

## 2. Exact word, full-core reset and reference correlations

Let X_i be the complete SWAP between B and output channel i, and let
R_i=SWAP_(D,F_i). The exact logical word is

    W=R_2 X_2 V R_1 X_1 V.                           (C2)

Each X_i is seven disjoint equal-spectrum pair SWAPs. They are scheduled
with the output-latch SWAP last. Each R_i is S pair SWAPs, without
conditioning on whether the preceding attempt succeeded. On the full
raw space a SWAP is a unitary relabelling, including invalid code strings
and arbitrary correlations.

For example, with an arbitrary old core/next-input/reference state chi,
and independent fresh hardware in F_i, complete replacement gives

    SWAP_(D,F_i)[chi_(D,I_i,R) tensor Omega_(T_Fi)]
                         SWAP_(D,F_i)^*
      =Omega_(T_D) tensor chi_(F_i,I_D,R).             (C3)

The old entire core and its reference correlations are now in F_i.
The new information input can remain correlated with R. Equation (C3)
does not call that input thermal or independent.

After (C2), trace the spent cartridges and keep the core, the two
outputs and R. The exact retained state is

    Xi=Omega_(T_D) tensor
       (E tensor E tensor id_(I_2,R))(rho_(I_0,I_1,I_2,R)),
                                                         (C4)

with I_2 relabelled as the original physical I sites of D. The two E
channels act on I_0 and I_1. This is a joint quantum channel identity,
not a product of separately computed output marginals. It includes
entangled input pairs and correlations of the next input with both
records.

Hardware T_D is exactly independent of the tape, the next information
input and every retained reference at the completed endpoint. The same
is true after conditioning on a tape event of positive probability.
The input I_D need not be independent. All spent states and old output
contents are still present outside the displayed reduction.

## 3. Full-raw local approximation and exact replacement

LOCAL_COMPILATION.md supplies two full-raw local approximations to V.
After an irrelevant global phase, require

    ||V_tilde_i-V||<=delta_i,           i=1,2.          (C5)

The literal rounded onsite phases are included in that approximation.
It is not an approximation only on a chosen one-label trajectory or
only on clean thermal histories. Each compiled primitive preserves the
specified rounded energy and occupation budget on every raw state.

For W_tilde=R_2 X_2 V_tilde_2 R_1 X_1 V_tilde_1,
unitary telescoping gives

    ||W_tilde-W||<=delta_1+delta_2.                    (C6)

Purifying an arbitrary input and applying (C6) proves the same upper
bound on trace distance of the joint output with any reference. The
partial traces used here cannot increase it. For the fixed product
formula depth of this successor,

    M=2^121 (K_D+1)^4,
    delta_i<2^-120,
    delta_1+delta_2<2^-119.                            (C7)

K_D is the frozen old core history length. This note does not obtain
that error by executing a scientific simulation or expanding the huge
circuit.

Define E_tilde_i by replacing V in (C1) with V_tilde_i. Because the
replacement gates themselves are exact, the compiled endpoint has the
stronger exact structural identity

    Xi_tilde=Omega_(T_D) tensor
       (E_tilde_1 tensor E_tilde_2 tensor id_(I_2,R))(rho),
    D(Xi_tilde,Xi)<=delta_1+delta_2.                   (C8)

In particular the final hardware factorization is exact despite the
run approximation. A nonzero delta does not become a reset error.
During the intermediate S pair SWAPs the replacement is only partial;
the statement applies after the complete second replacement and the
specified return transport to the original physical core sites.

## 4. The fixed-site transport interface

The local layout carries three complete core banks and two output
channels through its instruction slabs. At every step it transfers
the active factors by full equal-spectrum SWAPs before applying that
step's local instruction. The active factors, not a clean future row,
are what undergo the program. Future-copy contents can be arbitrary in
the exact permutation argument.

The following are necessary interface conditions, proved by the
companion geometry rather than assumed from an abstract wire diagram.

1. At export i the six archive/pointer pair SWAPs precede the seventh,
   latch SWAP. The geometry transfers all required record operands into
   the designated slab before that last instruction.
2. At that last SWAP, all seven output sites are fixed as the physical
   saved block O_i. Every subsequent forward gate and transfer acts
   identically on those sites. They are not routed through later work.
3. After replacement 2, all three core banks are returned along their
   own vertical columns to their original physical sites. The two saved
   output blocks are excluded. The original future-core-copy contents
   are restored by this permutation; unused output-copy junk may remain
   permuted and is retained in the physical inventory.
4. The outer completion latch F is raised only after both exports,
   both complete replacements and this return transport are finished.

Thus (C4) and (C8) identify D with the original core sites, and O_1,O_2
with the two fixed export slabs. A moving logical channel is not called
a fixed saved memory. The final routing is part of the compiled word;
no uncounted relocation is applied after the read window begins.

For every forward instruction after the first export, all operators on
the saved O_1 commute with that instruction. Later operations on other
systems therefore leave O_1 and every genuinely passive reference
unchanged. If a future input correlated with O_1 is subsequently acted
on, it is not a passive reference for this assertion; its changed joint
state is covered by the complete two-channel formula (C4).

The old export edge remains in the reversible history Hamiltonian.
Its possible later reverse action is why this forward protection does
not imply that every O_1 observable commutes with the entire Hamiltonian.

## 5. One thermal outer launch and the cold comparison

Let p_out be the excited probability of the one outer fuel. The declared
two-temperature preparation gives

    p_out>=1/3.                                       (C9)

It activates the entire two-attempt sequence once. There are not two
independent outer launches. Each E in (C4) already includes its own
old core's actual thermal activation and failures.

Let eta be the input trace-distance bound for replacing the nominated
outer and routing cold factors by their required zero configurations.
Include every outer cursor/sink/completion factor and every designated
future-copy or output-latch factor needed to exclude a false prewrite
read. The complete resource ledger counts them, with their actual
positive gaps. For C_aux such independent cold qubits with gaps at
least d,

    eta<=C_aux exp(-beta_c d).                        (C10)

All bad sectors remain in the physical evolution. Zero-gap future-row
copies are genuinely maximally mixed and need not be compared with a
pure zero state. Their exact transport identity is used instead.

The three core packages in (C4) retain their actual Omega_T states in
this comparison. Their own thermal errors belong to the optional
ideal-ready comparison in Section 8. This distinction avoids charging
the same cold defect twice. A larger inclusive cold-site count may be
used to choose beta_c conservatively, but the comparisons and their
targets must still be distinguished.

On the clean outer component, the dormant outer fuel leaves all
saved-output latches zero until any export and F zero throughout.
The latch-last ordering prevents a prewrite physical output from being
misread as a new record. An initial thermal excitation of a future saved
latch is a bad component counted in eta, not a silently rejected state.

## 6. An early first-record plateau and the final window

Write B_pad for the complete unbuffered path length, including launch,
both attempts, both resets, return of the three banks and raising F.
The geometry chooses B_pad>=512. Insert 4B_pad identity edges immediately
after the first fixed output export and append 5B_pad identity tail edges.
Then

    K=10B_pad>=5120,
    e_1<=B_pad<K/8,
    r_1>=4B_pad>3K/8,
    f=5B_pad=K/2.                                    (C11)

Here e_1 is the first saved-latch export index, r_1 is the first edge
of reset 1 after the inserted buffer, and f is final completion.
No useful gate is performed on the inserted holding detour.

The outer strength g_out is fixed by the local resource contract before
the product depth and enlarged path are used to set the latency. Put

    T_hold=pi hbar(K+1)/(3g_out),
    theta=g_out t/[hbar(K+1)].                        (C12)

The exact legal-history weights are those of
X distributed as Bin(K,sin(theta)^2). These are squared amplitudes of
the unitary history, not an additional stochastic evolution law.

At t_1=T_hold/2, sin(theta)^2=1/4. Exponential Markov bounds give

    Pr(X<K/8)<=[2(7/8)^8]^(K/8),
    Pr(X>3K/8)<=[(5/4)^8/8]^(K/8).                    (C13)

The two bases are respectively 11529602/16777216 and
390625/524288, both strictly below 3/4. Consequently the total weight
outside the first-record plateau e_1<=X<r_1 is less than

    2(3/4)^(K/8)<2^-128.                             (C14)

Already K>=4096 suffices: (3/4)^8<1/8 bounds the last expression by
less than 2^-191 at that value. Thus the first physical record is
available before reset 1 has appreciable history weight.

For a positive-width interval rather than only this midpoint, use the
outward interval

    I_early=[(3T_hold/pi) arcsin sqrt(15/64),
             (3T_hold/pi) arcsin sqrt(17/64)].         (C14a)

It contains T_hold/2. Its binomial mean is separated from K/8 and
3K/8 by at least 7K/64. The two elementary Hoeffding tails therefore
have total weight at most 2 exp(-49K/2048)<2^-128 for K>=5120.
For the final inequality, 49K/2048>=245/2>120, e>5/2 and
(5/2)^4>2^5 give 2 exp(-49K/2048)<2^-149<2^-128.
Throughout I_early the first export is complete and reset 1 has not
begun except for that stated active-history deficit. On the outward
half of the traversal, sin(theta)^2 increases and the weight
Pr(X>=e_1) cannot decrease. All later forward reset and second-attempt
instructions preserve that fixed output. Since sin(theta)^2>=1/4
throughout [T_hold/2,2T_hold], its completed-export weight stays at
least its value at T_hold/2 throughout that entire interval.

Throughout t in [T_hold,2T_hold], sin(theta)^2>=3/4. The completed-tail
weight satisfies

    w(t)=Pr(X>=f)>=1-beta,
    beta=(3/4)^(K/2)<2^-128.                          (C15)

The source word, both resets and return transport are complete at every
such tail vertex. Increasing the fixed-strength circuit length increases
T_hold; the construction does not silently raise g_out to keep a fixed
short latency. The midpoint is 3T_hold/2 and the clean full history
returns at 3T_hold.

## 7. Completed full joint channel, with the core at its original sites

Use the physical outer completion projector n_F. On a clean outer
history it accepts exactly the completed tail. Tracing the outer cursor
therefore gives the exact completed substate

    Sigma_comp(t)=p_out w(t) Xi_tilde.                (C16)

No initial output slot is assumed pure in this endpoint identity.
Every declared hardware factor is diagonal in its onsite energy basis,
so the joint input commutes with the summed rounded energy despite the
two temperatures. Passive zero-energy information and its reference
are retained.
Any alternative input carrying additional free-energy phases requires
its corresponding explicit free-evolution comparison.

Trace-distance contraction with an appended reject flag, followed by
normalization, yields for the actual preparation

    p_comp,actual(t)>=p_out w(t)-eta,
    D(rho_comp,actual(t),Xi)
      <=delta_1+delta_2+eta/[p_out w(t)].              (C17)

The target Xi contains both ACTUAL thermal one-use channels E, exact
fresh hardware Omega_T in the original D sites, and the next input's
joint correlations. No ideal-ready core error is needed in (C17).

For eta<2^-104, (C7), and w>99/100, the right-hand side is less than
2^-101 and in particular

    D(rho_comp,actual(t),Xi)<2^-96.                    (C18)

The completed-prefix factorization in (C8) is exact; the finite-time
actual statement (C18) includes possible false completion from bad
outer sectors. Without the physical final-completion condition, the
unfinished-history weight must be included when asserting that the
core is already reset at its original sites. Reading two exported
records alone does not certify that the subsequent reset/return has
finished.

## 8. Joint acceptance with correlated inputs

For each output define Q_i=n_(O_i,L)n_(O_i,P). Let A be the complete
one-use accepted map Q E(.) Q. Suppose uniformly on every admitted
valid input, including an arbitrary reference,

    Tr A(sigma)>=p_min,       p_min=1/60000.           (C19)

The frozen thermal theorem supplies a strict version of this bound.
For two correlated inputs,

    Tr[(A tensor A tensor id)(rho)]>=p_min^2.         (C20)

To prove this, apply the first accepted instrument. Its probability
is at least p_min. Conditional on that event, the second input still
has valid-code support, because the first operation acted on the other
input and independent hardware. Apply the same uniform bound to that
conditional second input, with the first record and R included in the
reference. Multiplying these two conditional probabilities proves
(C20). No product-input or independent-success assumption is used.

For a stronger comparison define E_id as the complete ideal-ready
source-output channel: the same prescribed source word and dormant
branch, with the nominated active readies exact. It is not a separately
chosen product of two ideal marginal states. Its complete one-use
reference-uniform error obeys

    D((E tensor id)(sigma),(E_id tensor id)(sigma))
       <=epsilon_in<2^-103,                           (C21)

using the predecessor's xi<2^-104 and inner cold-defect bound below
2^-104. A conservative sum suffices; the actual activation factor can
sharpen it. The actual and ideal-ready channel definitions include
their complete rejected branches. Both have the lower bound (C19).

Put A_id(.)=Q E_id(.) Q and define the subnormalized ideal joint output

    J_id=(A_id tensor A_id tensor id_(I_2,R))(rho),
    q_id=Tr J_id>=p_min^2.                            (C22)

Its normalized state J_id/q_id retains all quantum correlations
between the two outputs, the next input and R. Replacing it by a
product of its marginals would be a different and generally false
contract.

Use the fixed physical event n_F Q_1 Q_2. The clean ideal comparison
has weight p_out w q_id. Set

    e=eta+delta_1+delta_2+2epsilon_in<2^-101.           (C23)

This safe bound follows by two channel comparisons, (C6), and the
outer input comparison. Inserting the active/tail factor would only
reduce it. The accepted-plus-rejected instrument inequality gives

    p_both,actual(t)>=p_out w(t)q_id-e,
    D(rho_both,actual(t),
          Omega_T tensor J_id/q_id)
       <=e/[p_out w(t)q_id].                         (C24)

The one shared outer activation appears once. Substituting p_out^2
would incorrectly add another outer clock/fuel event.

Since p_out>=1/3 and w>99/100,

    p_out w q_id>11/120000000000>2^-34.

Together with (C23), this proves the conservative displayed goals

    p_both,actual(t)>1/12000000000,
    D(rho_both,actual(t),Omega_T tensor J_id/q_id)
       <2^-67<2^-60.                                (C25)

For the probability margin, e<1/120000000000 is sufficient; it follows
from (C23). The normalized bound is on a joint quantum state, not on
two unrelated marginal fidelities.

This does not automatically retain a one-use unwanted-band bound after
selecting both successes. The second selection can change correlations
in the first record or source. Such a stronger selectivity assertion
requires an input-independent acceptance proof or its own joint
inequality. It is not part of (C25).

For record-only reads Q_1Q_2 without n_F, the two fixed records are
already stable after the second export. Their accepted-output identity
can use the corresponding export-tail weight. The core and next input
need not yet occupy their final original sites, so this alternative
does not replace (C16)-(C25)'s completed joint contract.

## 9. All branches, reversibility and failure conditions

Each attempt consumes its full Gibbs/input package regardless of
acceptance. Both cartridges, all displaced future copies and both old
output contents remain in the finite state. The local gate and reset
identities are entire-space identities; the cold comparison is used
for probability bounds, not to remove bad configurations from the law.

Exact replacement does not replenish a spent cartridge or return its
correlations to an uncorrelated bath. Nor does the first record's
forward protection make the whole finite device irreversible. At the
outer return the inverse history can undo the exports and restore the
initial output contents. For initially cold saved latches, a return
read is bounded by the full defect weight including those latches;
an outer-cursor-only defect bound would omit a possible initial read.
External measurements would change this unmeasured evolution.

Decisive falsifiers include a failure of the full-raw operator bound,
a reset omitting a core site, a later transfer touching a frozen output,
an incorrect physical input/output-site identification, raising F before
the banks return, treating a future operated-on input as passive,
omitting a cold copied latch from the false-read account, normalizing
the joint accepted map by two marginal probabilities, or claiming
permanent retention from this finite forward window. No scientific
executable, expanded matrix or numerical simulation was run. All review
within this working session remains authoring review, not independent
mathematical acceptance.

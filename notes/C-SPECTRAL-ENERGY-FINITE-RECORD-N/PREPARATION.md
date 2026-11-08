# Preparation from coherent product qubits

**NON-CANONICAL, L1. New analytical extension; independent mathematical
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This note replaces the supplied sine packet and supplied abstract source
vector in [FINITE_MODEL.md](FINITE_MODEL.md) by an explicitly specified
product input and a complete conserving preparation. It leaves the seven
earlier candidate files unchanged. Acceptance of an earlier fixed head does
not accept this extension.

The main battery hardware consists of equal-gap qubits. Its useful unary
subspace is not counted as the whole physical Hilbert space. The preparation
unitary is specified exactly on that whole space; its local compilation,
clock, routing, auxiliary readiness and autonomous execution require the
separate implementation ledger. Pure charged seeds, coherent product inputs
and pure control registers remain supplied resources.

## 1. Physical battery and its complete preparation unitary

Use the same positive energy resolution d and charge bound m as
FINITE_BATTERY.md. Choose an integer M>=1 and put

    N=M+2m,
    H_B=(C^2)^(tensor N),
    B=d sum_(a=1)^N n_a,               n_a=|1><1|_a.     (P1)

Thus the physical battery has N qubits, raw dimension 2^N and capacity dN.
Define normalized unary states for every 0<=n<=N by

    u_n=|1>^(tensor n) tensor |0>^(tensor (N-n)).

Their span has dimension N+1. The initial battery is the product

    b_in=|1>^(tensor m) tensor |+>^(tensor M)
                          tensor |0>^(tensor m),
    |+>=(|0>+|1>)/sqrt(2).                              (P2)

All M plus states have the specified common phase relative to the chosen
target-word convention. A phase average is a different input state. There
are no additional copies of these M qubits: the same N physical qubits
become the battery used by the subsequent compensated word.

Let D_k^M be the normalized equal superposition of the M-bit strings of
Hamming weight k. Write

    t_k=|1>^(tensor m) tensor D_k^M tensor |0>^(tensor m),
    p_k=binom(M,k)/2^M,
    b_in=sum_(k=0)^M sqrt(p_k) t_k.                    (P3)

Both t_k and u_(m+k) have charge m+k. Their overlap is the positive real
number c_k=1/sqrt(binom(M,k)). Whenever they differ, define

    v_k=(t_k-u_(m+k))/sqrt(2(1-c_k)).

Omit indices where t_k=u_(m+k), including k=0,M. The remaining v_k are
orthonormal because they have different total charges. Consequently

    C=I-2 sum_(k:t_k!=u_(m+k)) |v_k><v_k|               (P4)

is a Hermitian unitary on all 2^N physical states. It is identity on the
orthogonal complement of the displayed vectors and commutes with B.
The identity

    <v_k,t_k>=(1-c_k)/sqrt(2(1-c_k))

proves C t_k=u_(m+k), with the omitted cases already fixed. Therefore

    C b_in=beta_M,
    beta_M=sum_(k=0)^M sqrt(binom(M,k)/2^M) u_(m+k).    (P5)

This is an exact full-space preparation, without a projection onto a
symmetric sector and without discarding a failed input. Defective inputs
are acted on by the same unitary. The product coherence is rearranged into
collective battery coherence; no auxiliary system is asserted to erase it.
The operator C is generally global. Equation (P4) specifies the target
for a conserving local compiler; it does not itself establish locality.

## 2. Buffered charge lift on the physical qubit space

Write the abstract finite source energy of FINITE_MODEL.md as

    q_f=d sum_(r=0)^m r P_r.

All logical, work, flag, archive and pointer factors have the degenerate
energies specified in that model. They can be included in the system
identity factors below. For m<=z<=N define

    J_z psi=sum_(r=0)^m P_r psi tensor u_(z-r),
    P_good=sum_(z=m)^N J_z J_z^*.

For every complete system unitary V set

    Gamma_B(V)=sum_(z=m)^N J_z V J_z^*+(I-P_good).       (P6)

This is an entire-space definition on the system times 2^N battery states.
Each J_z is an isometry with range in total charge z, and its ranges are
orthogonal. The complement includes incomplete unary boundary sectors
and every non-unary battery state. The identity action there is retained.
It follows directly that

    [Gamma_B(V),q_f+B]=0,
    Gamma_B(V_2)Gamma_B(V_1)=Gamma_B(V_2 V_1),
    Gamma_B(V)^*=Gamma_B(V^*).                          (P7)

The useful unary sector is invariant under every Gamma_B(V). The physical
degeneracy of a charge sector does not require projecting it away: (P6)
extends the unary action by a conserving identity on its complement.

Every battery level in (P5) lies in [m,N-m]. Hence every system charge and
every occupied initial battery level give a complete unary total-charge
fiber. Completeness here means that every source charge is represented;
the remaining physical degeneracy is still present in the identity block.
The finite-ladder comparison in FINITE_BATTERY.md applies after identifying
u_n with the abstract level |n>. That identification is used to prove the
bound, not to replace the raw dimension 2^N by N+1.

## 3. Exact binomial gradient estimate

Extend p_k by zero outside 0<=k<=M, and put b_k=sqrt(p_k). On an auxiliary
bilateral sequence space the nearest-neighbor difference obeys

    a_M^2=||(T_1-I)b||^2
         =sum_(j=0)^(M+1) (sqrt(p_j)-sqrt(p_(j-1)))^2.

Both endpoint terms are included. The scalar inequality

    (sqrt(p)-sqrt(q))^2 <= (p-q)^2/(p+q)

holds for nonnegative p,q with p+q>0. Let
q_j=binom(M+1,j)/2^(M+1). Pascal's identity gives

    p_(j-1)+p_j=2q_j,
    (p_j-p_(j-1))/(p_j+p_(j-1))=(M+1-2j)/(M+1).

The binomial mean and variance therefore yield

    a_M^2 <= 2 sum_(j=0)^(M+1) q_j (M+1-2j)^2/(M+1)^2
           =2/(M+1).                                   (P8)

This is an exact inequality. No numerical evaluation of a binomial tail
or factorial is used.

For completeness, the whole-word constant follows from the same operator
argument as the finite sine theorem. On the auxiliary bilateral ladder put

    S=sum_r P_r tensor T_(-r)
     =product_(j=1)^m [(I-Pi_j) tensor I+Pi_j tensor T_(-1)],
    Pi_j=sum_(r=j)^m P_r.

For each factor S_j,

    [S_j,V]=[Pi_j,V] tensor (T_(-1)-I),   ||[Pi_j,V]||<=1.

Expand the commutator of the product as m terms. The battery difference
commutes with every S_j and S^*. Each term on S^*(psi tensor b) thus has
norm at most a_M. Buffered support makes S V S^* agree with (P6) on
the prepared input. Including any passive reference gives

    ||Gamma_B(V)(psi tensor beta_M)-V psi tensor beta_M||
       <= m a_M <= m sqrt(2/(M+1))=:e_B.                (P9)

The ideal action V in this equation retains the battery untouched.
Purification and contractivity give the same bound, capped at one, for
joint trace distance, including the battery and reference. The actual
battery is not assumed to return exactly or remain independent.
Apply (P7) before (P9) for a finite word: there is no factor equal to the
number of gates and no fresh battery silently inserted between them.

## 4. A sharp source seed and one compensated source word

FINITE_MODEL.md defines the finite source space X_f, the fixed vector x_0,
the complete unitary U_f, and

    q_phys=q_f+r_f,         [q_f,r_f]=0,       0<=r_f<=dI.

Choose a common orthonormal eigenbasis x_a of q_f and r_f. Write

    q_f x_a=d j_a x_a,       r_f x_a=rho_a x_a,
    0<=j_a<=m,              0<=rho_a<=d.

Supply one specified basis vector x_*. It is a sharp state for both energy
readings. Fix a complete finite unitary P_x with P_x x_*=x_0; an isometry
between these one-dimensional subspaces always has a unitary extension.
Its remaining action is specified before execution and retained on all
inputs. It need not commute with q_f.

After the exact preparation C, execute the single compensated word

    Gamma_B(U_f (P_x tensor I_F)).                      (P10)

The original source's auxiliary readiness is still required. Arbitrary
admitted logical, old-memory, archive and reference correlations are
retained. Because P_x x_*=x_0, the ideal endpoint in (P9) is exactly the
finite source endpoint used in FINITE_MODEL.md, which in turn equals
the original complete source word on its specified source family.
The writer can be appended to the same word or applied afterward; it
commutes with q_f and therefore needs no additional compensation error.

Neither a standalone prepared x_0 nor a sine packet is an initial resource
of this construction. The comparison is applied once to the whole product
in (P10). Intermediate correlations are not replaced by a freshly prepared
source or packet. The specified finite spectral vectors and the matrix
P_x remain part of the abstract source encoding and supplied couplings.
This does not construct their spatial confinement in the original walk.

If the finite source basis is implemented by one-hot modes, x_* means
one occupied mode and all other modes zero. Its rounded excitation energy
is d j_* and its prescribed physical excitation energy is d j_*+rho_*.
That is an additional pure charged readiness resource, even when the
selected gap is zero. The preparation contract is in the valid one-hot
sector. A raw additive extension sum_a rho_a n_a can have width greater
than d on multi-occupation defects; a later hardware ledger must not apply
the one-hot residual bound to those raw states without a separate argument.

## 5. Resources, errors and entropy

For a target compensation tolerance 0<e<1 one may choose

    M=max{1,ceil(2m^2/e^2)-1},           N=M+2m.          (P11)

Then e_B<=e. The exact battery preparation and postpreparation moments are

    mean(B)=d(m+M/2),       Var(B)=M d^2/4,
    capacity(B)=d(M+2m),   raw dimension(B)=2^(M+2m).    (P12)

The input ledger contains M common-phase pure plus qubits, m pure excited
buffer qubits and m pure zero buffer qubits, all within the same N battery
qubits. It also contains the source seed x_*, the original program and
filter readiness, the new zero pointer, and every ready clock, zero flag,
row copy and routing auxiliary required by the later compiler. An occupied
archive may remain arbitrary under its stated input contract. Its dimension
is counted even though its prescribed bare energy is degenerate.

Equations (P11)-(P12) are not a low-cost substitute for the sine packet.
For m of order Delta/d, their leading capacity cost is of order
Delta^2/(d e^2), and their physical Hilbert dimension is exponential in N.
Exact gate coefficients, finite geometry, clock and program size are
additional resources. No operation in this note returns the entire input
bank to the product (P2) for free. Reuse and reset require a separate joint
state and energy analysis.

Let the actual entire initial state, including all readies and their
correlations with the admitted logical reference, be within trace distance
zeta of the specified joint initial state. This is a joint promise;
separate marginal purities do not imply it. Exact unitary preparation and
execution preserve that distance. Combining with (P9) gives

    D_tr(actual complete output,ideal complete output)<=e_B+zeta.   (P13)

Any additional error from an approximate compiler must be added separately.
All defective and rejected branches remain in this comparison. For a
common accepted-plus-rejected instrument with ideal acceptance p_0>e_B+zeta,
the same normalization bound as FINITE_BATTERY.md gives

    |p_actual-p_0|<=e_B+zeta,
    D_tr(rho_actual,acc,rho_ideal,acc)<=(e_B+zeta)/p_0.   (P14)

The states retain the declared reference. A clock availability weight or
a preparation-stage history has to be proved in the autonomous assembly;
it is not already included merely by writing down the circuit word.

The exact rounded conservation (P7), together with [C,B]=0, extends to
the whole preparation-and-computation circuit. On the declared abstract
source sector its original-energy residual remains between zero and dI.
Every conserving prefix therefore obeys the same unconditioned original
bare-energy drift bound d as FINITE_BATTERY.md. It is not exact conservation
of q_phys+B, a conditioned-energy bound, or an autonomous implementation
until the complete generator has been supplied.

The input (P2) is pure and has energy coherence. Unitary conversion
preserves total entropy; it does not obtain that purity or coherence from
a thermal distribution. If all preparation resources initially commute
with their complete additive energy, and preparation conserves that
energy, the output battery marginal is stationary for B. Products of
normalizable Gibbs states at different temperatures satisfy this premise.
They can support energy transfer but cannot produce (P5) under this law.

Indeed, for every stationary physical battery state sigma, charge-block
decomposition gives

    <beta_M|sigma|beta_M><=max_(0<=k<=M) p_k,
    D_tr(sigma,|beta_M><beta_M|)>=1-max_k p_k.            (P15)

Although B has degenerate charge sectors, beta_M has one normalized unary
vector in each occupied charge. The sum of sigma's populations on those
vectors is at most one, which proves the overlap bound. Thus degeneracy
does not evade the coherence obstruction. The wider aggregate source
width Md in (P2) is precisely an additional resource beyond the single
bounded asymmetric source considered in FINITE_BATTERY.md.

Separately, a finite full-rank thermal joint state remains full rank under
a unitary and has full-rank marginals. It cannot yield an exact nontrivial
pure ready marginal in a finite closed apparatus. This statement does not
exclude limiting cold baths, supplied pure states, entropy transfer with
different resources, or approximate readiness. Their costs must be stated.

## 6. Explanatory alternative with a large battery site

A different exact preparation illustrates the binomial coefficients but
is not the primary hardware count above. Supply M plus qubits and one
(M+2m+1)-state ladder initially in |m>. After j qubits, suppose its packet
has amplitudes sqrt(binom(j,k)/2^j). For the next qubit, rotate each block

    a_l=|0,m+l>,       b_l=|1,m+l-1>,       1<=l<=j+1,
    c_l=sqrt((j+1-l)/(j+1)),               s_l=sqrt(l/(j+1)),
    U_l=[[c_l,s_l],[-s_l,c_l]].                         (P16)

The incoming normalized vector in the block is c_l a_l+s_l b_l.
The displayed rotation sends it to a_l, while Pascal's identity supplies
the next binomial amplitude. Identity on all other blocks makes a full
two-site conserving unitary. Each specified source qubit ends in zero.
The initial ladder charge m can first be loaded from m excited qubits.

This yields an elementary two-site circuit with growing local dimension.
It neither counts the ladder as one qubit nor replaces (P1)'s physical
qubit construction. Its externally scheduled gate sequence alone is not a
time-independent autonomous device.

## 7. Separate sharp-fiber alternative for reduced outputs only

If the desired contract retains only the degenerate archive/pointer and
logical reference, a narrower exact construction needs no plus qubits.
Use N=2m battery qubits in the sharp unary state u_m, and the same sharp
source seed x_* of charge j_*. Set z=m+j_* and
V=U_f(P_x tensor I_F), including the writer when desired.
Then m<=z<=N is a complete unary fiber, and exactly

    Gamma_B(V)(x_* tensor f tensor u_m)
        =J_z V(x_* tensor f).                          (P17)

For every mixed admitted input with a passive reference, if sigma is the
ideal completed-word state before adjoining a battery, the actual output
is J_z sigma J_z^*. Orthogonality of different source charge sectors gives

    Tr_(X_f,B)(J_z sigma J_z^*)=Tr_(X_f)(sigma).         (P18)

To see this, expand J_z using P_r. Tracing X_f already kills every r!=s
term; on r=s the battery vector has norm one. Thus the entire retained
archive/pointer/reference state agrees, not just its separate marginals.
Acceptance probabilities and normalized accepted records agree exactly.

For any source effect A commuting with q_f, and any retained-register
observable Y, the same expansion gives

    Tr[(A tensor Y tensor I_B) J_z sigma J_z^*]
        =Tr[(A tensor Y) sigma].                       (P19)

This includes the specified compressed unwanted-band effect A_bad of
FINITE_MODEL.md, which commutes with q_f. It preserves its joint test with
the output record. It is not a claim that every original spectral test
has acquired a local material detector.

The source contract is different from a standalone coherent preparation.
After the lifted P_x alone, the reduced source is

    sum_r P_r |x_0><x_0| P_r,

with compensating battery correlations. The generally coherent spatial
marginal |x_0><x_0| has not been prepared. The complete output is not
asserted to approximate sigma tensor |u_m><u_m|. This alternative is an
exact encoding of a source word for the specified reduced outputs.
It does not inherit the full joint-state approximation claim of (P9).

Sharp charged seeds, one-hot source readiness, all pure control readies,
the spectral encoding and local/autonomous compilation remain resources.
If incorporated into a history construction, the prefix word and record
availability must still be proved there. Free evolution on traced source
and battery factors leaves (P18) unchanged; it does not make their whole
joint state stationary.

## 8. Scope and falsifiers

The new positive result is a complete conserving conversion of a specified
coherent qubit product to a buffered unary packet, with raw physical
dimension, energy moments and a reference-uniform whole-word error.
The sharp-fiber alternative instead proves exact reduced outputs under
an explicitly narrower source contract.

Failure of the Householder identities (P4)-(P5), an omitted raw-space
sector in (P6), violation of (P8)-(P9), or violation of (P18)-(P19) under
their stated hypotheses would invalidate the corresponding assertion.
No scientific executable, expanded matrix computation or physical
preparation experiment was performed. Fixed local interactions, complete
autonomous scheduling, thermodynamic readiness, reset, original spatial
confinement and independent acceptance remain distinct obligations.

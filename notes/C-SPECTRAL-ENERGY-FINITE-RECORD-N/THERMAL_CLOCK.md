# An all-qubit thermal launch and completed-record clock

**NON-CANONICAL, L1. New analytical extension; independent mathematical
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767. This note changes none of the twelve preceding
candidate files. Its claims are analytical construction claims, not an
executed finite-device verification or a Canon promotion.

The construction starts its only cursor from a finite-temperature fuel
qubit. That cursor executes the thermal reset panel, the sharp-fiber
source word and the occupied-archive writer. A separate completion latch
excludes the dormant branch even though its zero-energy pointer is
initially maximally mixed. The history generator is positive on the
complete raw qubit space, has bounded geometric support, and supplies a
predetermined finite record window. Every physical cursor is thermal;
there is no additional pure controller.

## 1. Input and complete-word contract

Use the highest-charge seed of [SHARP_THERMAL.md](SHARP_THERMAL.md):

    q_f x_*=b d x_*,       r_f x_*=r_* x_*,
    a=min spec(q_f/d),     b=max spec(q_f/d),
    0<=r_*<=d,            N>=b-a.                       (C1)

Here a,b are the actual occupied-sector extrema, not the former loose
ceiling. The battery starts in its vacuum on the cold comparison input.
The complete main word implements the conserving lift of
U_f(P_x tensor I), with P_x x_*=x_0, followed by the archive writer and
its final flag-to-pointer CNOT. Its retained archive/pointer/reference
state and commuting source effects have the sharp-fiber contract. The
full source/battery product-state approximation is not asserted.

Use the three interleaved data tracks of [LOCALITY.md](LOCALITY.md),
with n cells, W=3n data columns, label heights j_i and residuals r_i.
Set the previously free label offset mu=d. A label qubit has rounded
gap d(1+j_i) and physical gap d(1+j_i)+r_i. All E qubits have gap d;
all Z qubits have gap zero. The source seed occupies its specified
original label site, not a helper or padding label. The fifteen admitted
logical/old-memory/archive qubits keep their arbitrary valid-code joint
input, including reference correlations. All remaining Z qubits start
in their actual zero-gap Gibbs state I/2.

For the resource specialization choose the descending label order and
put x_* first among the maximum-height labels, at active cell 6. Adjacent
heights then differ by zero or minus one; reflecting the funded-hop
orientation gives the same conserving compiler and support bounds.
For j_i=j_(i+1)+1 the funded block is explicitly
|1,0,0>_(X_i,X_(i+1),E_i) <-> |0,1,1>: the downward label move
creates one energy-rail excitation. Its inverse funds the upward move.
Either orientation is admissible. The general seed-column geometry below
also applies to the original ascending order.

Let A=n-15. The reset panel of
[THERMAL_REGISTERS.md](THERMAL_REGISTERS.md) has r rounds, each using A
fresh pairs of gap-d hot/cold donors. It prepares all nominated basis
readies, including the pointer and compiler workspace. It does not reset
the fifteen input qubits. Future rows may have arbitrary contents; their
same-column SWAPs move the original active factors through the panel and
program while retaining the displaced contents.

Let J be the number of main row-transfer stages, including its final
pointer instruction, and put s=r+J. Add a main identity stage before the
last CNOT when necessary so s is odd. All scratch and routing are restored
before that CNOT. It is placed on the final outward guard after the last
row transfer. Thus the physical pointer in the final row is untouched
until the completed writer; the following latch transition is unconditional.

## 2. Local thermal launch and the completion latch

Introduce a hot fuel h, a cold sink c and a cold completion latch L.
Write s_u^+=|1><0|_u and s_u^-=(s_u^+)^*. The launch exchanges

    |1,0,0,0>_(h,c,X_*,C_1)
       <-> |0,1,1,1>_(h,c,X_*,C_1).                    (C2)

The first physical cursor C_1 has rounded gap 2d. The sink has gap d.
The rounded fuel gap and its actual physical gap are respectively

    G=(b+4)d,             G+r_*.                       (C3)

The output energy of (C2) is d+d(1+b)+2d=G; the residual r_* moves
from the fuel to the new source excitation. Thus (C2) conserves both
declared bare energies locally. Set

    beta_h(G+r_*)=log(2).                              (C4)

The fuel excitation probability is exactly 1/3. Each gap-d hot reset
donor at this same temperature has probability
p=1/(1+exp(beta_h d))>=1/3. All other charged hardware starts at one
positive inverse temperature beta_c. No fuel excitation is selected
externally.

There is a virtual history node 0 with the launch input and no cursor.
Physical nodes 1,...,K each contain their corresponding cursor. After
the reset panel and main word have finished, one edge exchanges

    |1,0,0>_(C_pre,C_post,L)
       <-> |0,1,1>_(C_pre,C_post,L).                   (C5)

Pre-completion cursors have gap 2d, post-completion cursors gap d,
and L has gap d. Equation (C5) therefore conserves rounded and physical
bare energy. It contains no success control. Rejected completed runs
raise L too; their correctly initialized final pointer remains zero.

The read predicate is the fixed physical projector

    Pi_read=n_L n_P,                                  (C6)

where P is the pointer in the final data row. No cursor measurement is
part of (C6). The latch excludes the dormant fuel-ground component,
whose pointer may still be maximally mixed.

## 3. Explicit geometry and finite counts

Number physical data columns c'=1,...,W. Put the same-spectrum row copies
at (4c',2t), t=0,...,s. Reset donors at target column c' and layer
t=1,...,r occupy (4c'-1,2t) and (4c'+1,2t). They are distinct physical
qubits. Define B=4W+4. The cursor rails lie at y=2t-1, t=1,...,s,
with outer guards x=0 and x=B. Alternating rails are joined by two
vertical edges at the outer guard. The right guard lies beyond every
reset donor, including the possible donor at x=4W+1.

The initial source edge (-1,1)->(0,1), s horizontal rails and their
connectors have

    b_path(s)=s(4W+6)-1                               (C7)

edges, ending at (B,2s-1) because s is odd. Unit identity edges fill
unused rail positions. Every data transfer and reset has the ordering
specified in THERMAL_REGISTERS.md; main transfer/gate stages use the
scaled LOCAL_HAMILTONIAN.md scaffold. The last pointer CNOT is on the
last outward guard, before completion.

If the seed has physical data column c_*, put q=4c_* and place

    X_*=(q,0),       h=(q,-1),
    c=(q+1,-1),      C_1=(q-1,-1).                    (C8)

This is a four-site local launch even when the highest-charge label is
far along the ordered track. No reversal of label energies or nonlocal
fuel contact is needed. From C_1 run the cursor down p_pad unit steps,
left q steps, then up p_pad+2 steps to (-1,1). This exterior lead has
q+2p_pad+2 edges. It is disjoint from the fuel, sink, data and donor
sites. Choose an integer p_pad>=0 so that

    L_c=q+4+b_path(s)+2p_pad>=512,      K=2L_c.        (C9)

One launch edge, the exterior lead, the sweep block, and one completion
edge then reach node L_c. Place the completion edge from (B,2s-1) to
(B+1,2s-1), and the latch at (B+1,2s). Append L_c rightward identity
edges at height 2s-1. Nodes L_c,...,K form the completed tail.
There are K physical cursor qubits, not K+1: node 0 is the already
counted fuel/sink/seed configuration with cursor vacuum.

The complete device fits in the integer rectangle
[-1,B+1+L_c] times [-1-p_pad,2s]. Its exact qubit inventory is

    S=3n(s+1)+2Ar+K+3,
    dim H_raw=2^S,
    C_c=2n(s+1)+Ar+K+2,
    N_hot=Ar+1,          N_zero-gap=n(s+1).             (C10)

The final three sites are fuel, sink and latch. C_c counts every E/X
data copy, reset cold donor, physical cursor, sink and latch once.
The zero-gap count includes the fifteen admitted information qubits;
the other zero-gap factors are Gibbs inputs. Every added lead or tail
site is already counted among the K cursors.

The reset propagation instruction uses at most four data sites plus two
cursor endpoints, in a Manhattan-radius-2 ball. A main instruction uses
at most five data sites plus its two endpoints. Scaling its horizontal
coordinates by four gives a Manhattan-radius-16 ball. The launch uses
four sites of radius 2; completion uses three of radius 2. Diagonal
terms have no larger support. Thus seven-site support, radius 16 and
site incidence at most 64 are conservative uniform bounds. All local
dimensions are two. The rectangle size and number of interactions grow;
these bounds do not encode the device in one large site.

## 4. A positive full-raw Hamiltonian

Let N_X sum the occupations of every X qubit in every row. Let H_D be
the sum of all rounded E/X data energies and the d(n_H+n_C) energies
of every reset pair. Set

    H_0=H_D+G n_h+d n_c+d n_L
        +2d sum_(j=1)^(L_c-1) n_(C_j)
        +d sum_(j=L_c)^K n_(C_j).                     (C11)

Every ordinary instruction G_j is a complete raw unitary, including
row transfers and identity edges. It preserves H_D and N_X. Define

    X_0=s_h^- s_c^+ s_(X_*)^+ s_(C_1)^+,
    P_in=X_0^*X_0,       P_out=X_0 X_0^*,
    D_0=P_in+P_out.                                    (C12)

For edges 1<=j<K other than ell=L_c-1 use

    X_j=s_(C_(j+1))^+ s_(C_j)^- G_j,
    D_j=n_(C_j)+n_(C_(j+1)).                           (C13)

On the completion edge use the same D_ell but

    X_ell=s_(C_(ell+1))^+ s_(C_ell)^- s_L^+.           (C14)

In particular its diagonal is not silently reduced to its enabled
subspace. Put V_0=P_in and V_j=n_(C_j) for 1<=j<=K, and choose

    a_j=g sqrt((j+1)(K-j))/(K+1),       0<=j<K,
    a_(-1)=a_K=0,       v_j=g-a_(j-1)-a_j>=0,
    H_prop=sum_(j=0)^(K-1) a_j(D_j-X_j-X_j^*)
           +sum_(j=0)^K v_j V_j,
    H=H_0+H_prop.                                     (C15)

Each launch block is [[1,-1],[-1,1]] times a_0 on its exchanged pair
and zero elsewhere. An ordinary edge has that positive block on its
10/01 cursor sector, zero on 00, and 2a_j I on 11. For completion,
s_L^+ is a contraction; the 10/01 block [[I,-s_L^-],[-s_L^+,I]]
is positive, and the other sectors remain nonnegative. Finally v_j>=0
follows from a_(j-1)+a_j<=g. Thus H_prop>=0 and H>=0 on the complete
raw qubit space, including multiple cursors and invalid data strings.
Every edge norm is at most 2a_j<=g; each v_j<=g.

All terms commute with H_0 and with

    C=N_X+n_h.                                        (C16)

The launch exchanges one fuel excitation for one label excitation;
subsequent instructions preserve both counts separately. No post-launch
reset of X is used. Set

    R=sum_(all data rows,i) r_i n_(X_i)+r_* n_h,
    E_phys=H_0+R,         H_int=H_prop-R.               (C17)

Then H=E_phys+H_int and 0<=R<=d C on the entire raw space. The residual
correction is onsite, including the fuel correction. Exact conservation
of H_0 and C gives, at every time,

    -d C <= U(t)^* E_phys U(t)-E_phys <= d C.           (C18)

For the actual Gibbs input, <C>=1/3 plus all cold label occupations.
This is an unconditional mean-energy bound after taking expectations;
it is not a bound obtained by first selecting the accepted ensemble.
The earlier finite spectral encoding and original-energy limitations
remain in force. There is no assertion that the actual original walk
or its continuous trajectory has been embedded into this local device.

## 5. Exact active path, dormant branch and return

For the comparison input set every cold charged qubit to zero, leaving
the hot Gibbs factors, all zero-gap Gibbs factors and admitted input
unchanged. Split only the actual diagonal fuel mixture: its excited
branch has weight 1/3 and its ground branch weight 2/3.

For any vector in the active branch, define its history by the launch,
then the ordered complete instructions, then completion and identities.
The cursor sites distinguish nodes 1,...,K, and cursor vacuum distinguishes
node 0. The launch output is exactly the required seed and battery vacuum.
The full inverse instruction word restores that seed before an inverse
launch. Each internal node has just its predecessor and successor edges.
At node 0 D_0=V_0=1, at node 1 D_0=1, and all other incidence terms
have their usual path values. Therefore no launch diagonal or handoff
potential is missing. On this invariant history,

    H_prop = g I - [2g/(K+1)] J_x,    spin J=K/2.      (C19)

The fuel is ground after launch and is never subsequently touched.
A second independent launch is impossible on this comparison branch.
The reverse launch requires C_1, which is absent at every later node.
An extra work head, loader, launch qubit or ready cursor is unnecessary.

On the dormant branch h,c and all cursors are zero. P_in=P_out=0,
every propagation term annihilates the state, and L remains zero.
This remains true for arbitrary zero-gap data and hot reset-donor
contents. Initial data may be dirty; the absence of a cursor prevents
any reset or main gate from acting. Thus (C6) rejects this whole branch.
Cold-defect branches need not be dormant and are kept in the error bound.

Write theta=gt/[hbar(K+1)]. The exact history probabilities are

    p_j(t)=binom(K,j) sin(theta)^(2j) cos(theta)^(2(K-j)),
    tau=pi hbar(K+1)/(2g).                             (C20)

The comparison input commutes with H_0, including its arbitrary reference
correlations in zero-energy input factors. Since [H_0,H_prop]=0, no
unaccounted free phase changes its density evolution. At 2tau the
propagation unitary is -I on every such history because K is even.
The complete comparison density returns exactly to its initial state.
In particular the latch is zero and the read probability is zero.

## 6. Record-only window and all-branch error

At every node j>=L_c the final archive/pointer/reference state is the
completed main output and L=1. Before that node L=0. Tracing the
orthogonal cursor states removes cross-node coherences. Consequently
the accepted record substate on the cold-zero comparison input is

    Sigma_comp(t)=(1/3) w(t) Sigma_prep,
    w(t)=Pr{Bin(2L_c,sin(theta)^2)>=L_c}.               (C21)

Sigma_prep is the complete accepted output after the imperfect thermal
reset panel, with all reset donors retained before the indicated output
reduction. Equation (C21) concerns the fixed record-only predicate (C6),
not a joint postselection on a favorable clock position.

For any prescribed holding time T_h>0 choose, before evolution,

    g=pi hbar(K+1)/(3T_h).                             (C22)

Throughout t in [T_h,2T_h], sin(theta)^2>=3/4. The elementary binomial
Chernoff bound gives

    w(t)>=1-beta,     beta=(3/4)^L_c<2^(-128).         (C23)

Here L_c>=512 suffices: (3/4)^4<1/2. The midpoint is tau=3T_h/2,
and exact comparison return occurs at 3T_h. Increasing the gate count
at fixed T_h increases g and the needed interaction strengths. Keeping
the coupling scale fixed instead increases the window latency and
return time. This cost is part of the construction.

Let p_0 be the ideal ready-source acceptance probability. On the
cold-zero input the reset-panel failure satisfies

    xi<=A(2/3)^r.                                     (C24)

Let q_c be the product probability that all C_c cold charged factors
are in their ground states. The actual input is exactly
q_c rho_comp+(1-q_c)rho_defect for an admitted residual state, with

    eta_c=1-q_c<=C_c exp(-beta_c d).                   (C25)

This counts the reset cold donors too; adding their failure again would
double count. Hot fuel and donor mixtures are unchanged in rho_comp.
Trace-distance contraction, the retained readiness mixture, and (C21)
give

    p_read(t)>=(1/3)w(t)(p_0-xi)-eta_c,
    D(rho_read(t),rho_ready,acc)
       <=xi/p_0+eta_c/[(1/3)w(t)(p_0-xi)],             (C26)

when p_0>xi. The target rho_ready,acc includes the arbitrary reference;
any previously declared source-to-ideal conditional error is added
separately. No favorable thermal sector is physically discarded.
The two mixture comparisons justify these denominators even though the
success probability is small.

Choose r after fixing A, then geometry and C_c, and finally beta_c.
For example choose xi,eta_c<=2^(-104). This order is finite and avoids
a circular temperature/site count. With the existing strict source
margin p_0>1/20000+1/1000000, (C23)-(C26) imply

    p_read(t)>1/60000,
    D(rho_read(t),rho_ready,acc)<60000*2^(-103).        (C27)

The latter is the added thermal-readiness error only. The actual return
bound is independent of reset success:

    p_read(3T_h)<=eta_c.                               (C28)

The entire cold-zero comparison component has returned with L=0,
including runs whose Z reset failed. External measurement would change
the evolution and is not covered by this unmeasured recurrence statement.

## 7. Initial nonstationarity and inclusive energy moments

Every initial hardware factor is Gibbs for its stated physical bare
onsite spectrum. The complete initial state commutes with H_0, but
need not commute with H. Put gamma=1/(1+exp(beta_c d)),
gamma_2=1/(1+exp(2beta_c d)), and
gamma_* =1/(1+exp(beta_c[d(1+b)+r_*])). The initial launch-sector
probabilities satisfy

    pi_in=(1/3)(1-gamma)(1-gamma_*)(1-gamma_2),
    pi_out=(2/3)gamma gamma_* gamma_2,
    pi_out/pi_in=2 exp[-beta_c(G+r_*)].                (C29)

For beta_c>beta_h, pi_in>pi_out. Partial trace of [H,rho_in] onto the
four launch sites removes every other off-diagonal cursor edge. Hence

    ||[H,rho_in]||_1>=2a_0(pi_in-pi_out)>0.            (C30)

The temperature contrast supplies this nonstationarity; there is no
initial energy-coherent battery or omitted coherent clock. This does
not identify the product input with a Gibbs state of the interacting H.

The diagonal part of H_prop has the exact full-raw identity

    A_prop=sum_j a_j D_j+sum_j v_j V_j
       =g sum_(j=1)^K n_(C_j)+g P_in
          +a_0(P_out-n_(C_1)).                        (C31)

In particular the interacting energy mean is not just <H_0>. For the
actual product input, set M_0=H_0+A_prop. All hopping means vanish,
and products of two distinct hops have zero expectation because they
do not return the cursor/fuel/latch configuration. Thus exactly

    <H>=<M_0>,
    Var(H)=Var(M_0)+sum_(j=0)^(K-1)
                  a_j^2 <X_j^*X_j+X_j X_j^*>.        (C32)

Only the four launch factors are correlated by A_prop; other diagonal
terms are independent. Formula (C32) therefore requires a local
sixteen-state expectation plus independent one-qubit moments, not an
enumeration of 2^S states. The launch hopping weight is pi_in+pi_out.
An ordinary edge with thermal endpoint occupations z_j,z_(j+1) has
weight z_j(1-z_(j+1))+(1-z_j)z_(j+1). Completion instead has weight

    z_pre(1-z_post)(1-gamma)
       +(1-z_pre)z_post gamma.                        (C33)

Here z_pre=gamma_2 and z_post=gamma. These are initial-state moments,
not a stationarity assumption for subsequent dynamics.

Explicitly, for v=(h,c,x,z) in {0,1}^4 define

    m(v)=G h+d c+d(1+b)x+(2d+g)z
          +g 1_(v=1000)+a_0[1_(v=0111)-z],
    w(v)=(1/3)^h(2/3)^(1-h)
          gamma^c(1-gamma)^(1-c)
          gamma_*^x(1-gamma_*)^(1-x)
          gamma_2^z(1-gamma_2)^(1-z).                 (C33a)

Let e_u be each remaining H_0 onsite coefficient and p_u its actual
thermal excited probability. Set e'_u=e_u+g on remaining cursor sites
and e'_u=e_u elsewhere. The complete local-sum formulas are

    <M_0>=sum_v w(v)m(v)+sum_(u outside launch) e'_u p_u,
    Var(M_0)=sum_v w(v)m(v)^2-[sum_v w(v)m(v)]^2
                 +sum_(u outside launch) (e'_u)^2 p_u(1-p_u).
                                                         (C33b)

Zero-energy admitted input factors contribute zero irrespective of their
reference correlations. Equations (C32),(C33),(C33a),(C33b) specify the
full interacting variance without a scientific numerical execution.

For completeness, put gamma_i=1/(1+exp(beta_c[d(1+j_i)+r_i])). The
rounded bare mean and residual mean are explicitly

    <H_0>=(s+1)[n d gamma+sum_i d(1+j_i)gamma_i]
           +Ar d(p+gamma)+G/3
           +2d(L_c-1)gamma_2+d(L_c+3)gamma,
    <R>=(s+1)sum_i r_i gamma_i+r_*/3.                 (C34)

The last gap-d count includes the post-completion cursor sites, sink
and latch. The physical bare mean is <H_0>+<R>; the total conserved
mean is (C32). Analogous independent Bernoulli sums give the bare
variances, whereas the full variance must retain the launch terms in
(C32). All reset donor energies, row-copy energies, entropy and discarded
old values remain in the finite device.

The exact maximum rounded and physical bare energies, including all raw
occupations, are

    E_0,max=(s+1)[nd+sum_i d(1+j_i)]+2Ard+G+d(3L_c+1),
    E_phys,max=E_0,max+(s+1)sum_i r_i+r_* .             (C35)

The clock contribution to E_0,max is 2d(L_c-1)+d(L_c+1);
the extra 2d counts the sink and latch. Termwise positivity and norms
give the conservative complete-generator capacity bound

    0<=H<= [E_0,max+(2K+1)g] I.                        (C36)

This is an explicit bound on the full raw spectrum, distinct from the
initial means and variances. It includes every padding row, donor,
controller site and history interaction.

## 8. Physical readout and the retention boundary

An actual two-outcome read instrument for (C6) can be specified by the
maps rho->Pi_read rho Pi_read and
rho->(I-Pi_read)rho(I-Pi_read), with a distinct external outcome register.
Its implementation, outcome selection and subsequent storage are not
additional actions of H. The construction proves the material
archive/pointer/latch state on the stated interval and its conditional
reference channel. Coherent registration alone is not an event-selection
mechanism or a completed macroscopic detector.

The latch also reverses. Neither it nor the archive is permanently
invariant under this finite autonomous writer. More generally, if a
memory projector P commutes with a time-independent Hamiltonian on the
complete finite space, its occupation is constant, so that same
Hamiltonian cannot write P from a zero-occupation input. A reversible
finite writer may supply a long prescribed window, as here, while its
unmeasured evolution subsequently returns. A permanent record needs a
different retained-system contract or a separately accounted physical
intervention.

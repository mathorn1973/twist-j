# A counted finite controller for export and repeated reset

**NON-CANONICAL, L1. New conditional analytical construction; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767. The seventeen preceding files are unchanged.

This construction retains exported records after the original core's
clock and other hardware have been restored from fresh cartridges. It
executes a prescribed finite number of attempts under one positive,
time-independent Hamiltonian and uses only the two declared temperatures
for its auxiliary input. Its complete-unitary interactions have explicitly
large support. Bounded geometric locality of this new autonomous
controller is an open compilation obligation. The earlier seven-site
locality theorem is not imported into this different law.

The original free half-period after export is not used as a reset:
export changes the core state and its correlations, and can leave its
previous invariant history. Instead a complete core-cartridge SWAP
restores the hardware and keeps all displaced states. The outer
controller continues advancing while those inner clock factors reset.
It too has a finite return, which ultimately reverses the exports.

## 1. The core endpoint and retained-cycle unitary

Let D be the complete S-qubit thermal device in THERMAL_CLOCK.md,
including its original clock, fuel, sink, latch, donors and data rows.
Distinguish its rounded onsite Hamiltonian Q_D, its residual R_D, and
its complete positive generator H_D:

    H_D=Q_D+H_prop,D,
    E_D=Q_D+R_D,
    [H_D,Q_D]=[H_D,C_D]=0,
    0<=R_D<=d C_D,       C_D=N_X,D+n_fuel,D.            (Y1)

Its physical record B consists of the five archive qubits, final pointer
P and old completion latch L. B has seven qubits, with onsite energy
d n_L. The first six have zero gap. Write

    V=exp(-i H_D delta/hbar),       delta=3T_h,D/2.    (Y2)

This is the old completed endpoint, where its comparison history has
tail weight one. V is a completely specified finite unitary on all raw
core states, not just the successful input sector. It commutes with Q_D
and C_D. In the new autonomous law below, V is an instruction; delta is
its definition and is not asserted to equal its physical execution time.
There is no independent continuously running H_D term in that new law.

Fix an integer nu>=1 of attempts. Supply nu fresh S-qubit cartridges
F_1,...,F_nu, with exactly the same onsite spectra as D. Also supply
nu output slots O_i, each with the same seven spectra as B. No output
slot is required to be blank. Its six zero-gap factors may be I/2, and
its latch is a gap-d Gibbs qubit. Previous slot contents are kept by
the exchanges below.

For attempt i perform the ordered complete unitaries

    V on D,
    E_i=SWAP_(B,O_i),
    S_i=SWAP_(D,F_i).                                  (Y3)

These are the three instructions of that attempt. Let W_nu be their
chronological product. Every instruction commutes with the sum of all
rounded onsite energies and with

    C_data=C_D+sum_i C_(F_i).                          (Y4)

The export is an unconditional seven-qubit SWAP. Its accepted logical
content is interpreted through the transported P,L flags. It moves the
unknown quantum record and its reference correlations rather than
cloning them. Whole-core SWAP then transfers the used core, including
the old output-slot contents, into F_i. Rejected attempts consume a
cartridge too. The final S_nu is included so that the core is fresh
after the last attempt, not only before intermediate attempts.

## 2. Exact reset and joint channel for arbitrary inputs

Factor each core/cartridge as H_hw tensor I, where I is the fifteen
admitted logical/old-memory/archive input qubits and H_hw comprises all
other hardware. Let Omega be its prescribed product Gibbs hardware
state at the selected temperatures. Admit an arbitrary valid-code
joint state

    rho_(I_0,...,I_nu,R),                              (Y5)

where R is passive throughout. Hardware banks are initially independent
copies of Omega, and the output slots are initially independent of (Y5).
The last input I_nu is a counted next-use information resource. It is
not an unmentioned pure preparation auxiliary.

Define the actual one-attempt channel

    E(sigma)=Tr_(D outside B)
                 V(Omega tensor sigma)V^*.            (Y6)

The thermal defects of the old device are already included in E. The
exact result after W_nu, tracing only the spent cartridges, is

    rho_(D,O_1,...,O_nu,R)
      =Omega_(H_hw,D) tensor
        [E^(tensor nu) tensor id_(I_nu,R)](rho),        (Y7)

up to the displayed factor order. Each E acts on I_(i-1) and outputs
O_i. Equation (Y7) is a joint channel identity including arbitrary
entanglement between different inputs and the passive reference.
It follows inductively from the exact SWAP identities; it does not
assume that the output margins factor.

The current hardware, including every original clock qubit, is exactly
Omega and independent of the retained tape and reference. This remains
true after conditioning on any tape outcome. The next information input
I_nu may remain correlated with the tape through (Y5); it is not falsely
declared reset or decoupled. All former hardware states and correlations
are in the spent F_i factors, which remain physical parts of the closed
unitary system. No entropy is erased.

## 3. A thermal outer clock without a pure seed

Use the same inverse temperatures beta_h,beta_c as the cores. Add an
outer fuel h_o of gap 3d, a sink c_o of gap d, a completion latch L_o
of gap d, and K_o physical cursor qubits. Before completion cursor
gaps are 2d and afterwards d. The only launch exchanges

    |1,0,0>_(h_o,c_o,C_1) <-> |0,1,1>.                (Y8)

The fuel excitation probability is

    p_o=1/(1+exp(3beta_h d))>=1/3,                    (Y9)

because the inherited choice beta_h(G+r_*)=ln 2 has G+r_*>=4d.
No third temperature is introduced. Every outer charged factor other
than h_o starts at beta_c. The initial cursor vacuum and sink/latch
zero states are comparison sectors of those actual Gibbs states, not
supplied pure factors.

Choose

    Lambda=max{512,3nu+2},       K_o=2Lambda,
    ell_pad=Lambda-3nu-2.                              (Y10)

Virtual node 0 has excited fuel, ground sink and no cursor. The launch
reaches physical node 1. Next come ell_pad identity edges, then the
3nu instructions in (Y3). Thus attempt i exports at node

    e_i=ell_pad+3i,                                   (Y11)

and resets at node e_i+1. The final reset ends at Lambda-1. A completion
edge then exchanges |1,0,0>_(C_(Lambda-1),C_Lambda,L_o) with |0,1,1>,
paying the latch energy by lowering the cursor gap. Lambda identity
edges finish the tail at K_o. Every completed-tail node therefore has
the output tape and restored core in (Y7).

## 4. Complete static law and its locality boundary

Let Q_bank be the sum of Q_D, all Q_(F_i), and d n_(O_i,L). Define

    Q=Q_bank+3d n_(h_o)+d n_(c_o)+d n_(L_o)
       +2d sum_(j=1)^(Lambda-1)n_(C_j)
       +d sum_(j=Lambda)^(K_o)n_(C_j).                 (Y12)

Let X_0=s_(h_o)^- s_(c_o)^+ s_(C_1)^+,
P_in=X_0^*X_0, P_out=X_0 X_0^*, D_0=P_in+P_out.
At every ordinary edge j>=1 put

    X_j=s_(C_(j+1))^+ s_(C_j)^- G_j,
    D_j=n_(C_j)+n_(C_(j+1)),                           (Y13)

where G_j is the exact instruction or identity specified above. On
j=Lambda-1 replace G_j by s_(L_o)^+ while retaining the same D_j.
Put V_0=P_in, V_j=n_(C_j) for j>=1 and

    a_j=g_o sqrt((j+1)(K_o-j))/(K_o+1),
    a_(-1)=a_(K_o)=0,       v_j=g_o-a_(j-1)-a_j>=0,
    H_hist=sum_(j=0)^(K_o-1) a_j(D_j-X_j-X_j^*)
              +sum_(j=0)^(K_o) v_j V_j,
    H_out=Q+H_hist.                                    (Y14)

This is a complete operator on the entire raw tensor product. The launch
term is positive on its exchanged two-state sector and zero outside;
ordinary edges have positive unitary blocks on cursor 10/01 and 2a_j I
on 11. The completion uses a contraction, whose [[I,-G^*],[-G,I]]
block is positive. All v_j are nonnegative. Thus H_out>=0 without a
projection onto valid histories or a discarding of thermal defects.
Every term commutes with Q and C_data.

The construction specifies these global couplings exactly. A V edge
uses at most S+2 sites; export uses 14+2=16; whole-core reset uses
2S+2. Launch and completion use three. Consequently

    maximum term support <= max{2S+2,16}.              (Y15)

The active core participates in multiple cycle instructions, and its
incidence grows with nu. No size-independent interaction radius or
bounded geometric degree is established here. Replacing (Y15) by the
earlier seven-site/radius-16 bounds would be unjustified: the input now
includes complete thermal core states with multiple-label defects,
and V is a new full-core endpoint unitary. A suitable exact local
compiler must count its own mediators, buses, preparation and timing.
That is an explicit remaining obligation, not a presumed consequence
of the previous one-label compiler.

## 5. Exact resource and energy account

The new complete raw qubit count is

    S_out=(nu+1)S+7nu+K_o+3,
    dim H_out,raw=2^S_out.                             (Y16)

For an old core with C_c cold hardware factors, H_h hot factors and
Z zero-energy factors, the inventory is

    N_cold=(nu+1)C_c+nu+K_o+2,
    N_hot=(nu+1)H_h+1,
    N_zero=(nu+1)Z+6nu,
    N_information=15(nu+1).                            (Y17)

The information count is a subset of N_zero. All other zero-energy
factors are Gibbs I/2. All nu output latches, all K_o cursor qubits,
outer sink and outer completion latch are included. Each cartridge
contains its full previous inventory of donors, row copies, fuel and
old cursor sites. None is a reusable fresh reservoir after its SWAP.

Choose beta_c after (Y16)-(Y17), for example

    beta_c d >= [104+ceil(log_2 N_cold)] ln 2.          (Y18)

Keep the old reset repetition count, which already gives xi<2^-104.
No dimension or instruction unitary depends on this final temperature
choice. The same colder beta_c is used everywhere, so the two-temperature
description is retained and all previous cold-defect bounds remain valid.

Define R_bank=R_D+sum_i R_(F_i). Output slots and outer controller
have no residual. The new physical bare reading and interaction are

    E_out=Q+R_bank,        H_int,out=H_hist-R_bank,
    0<=R_bank<=d C_data.                               (Y19)

The complete generator and Q are exactly conserved. Hence every raw
state satisfies at every time

    -d C_data <= U_t^* E_out U_t-E_out <= d C_data.     (Y20)

The initial expectation of C_data is (nu+1) times the old core
expectation. Output selection does not turn (Y20) into a conditional
energy-conservation statement. The physical comparison still concerns
the finite spectral encoding; it supplies no original-walk trajectory
intertwiner.

If E_Q,max and R_max are the old core's exact maximum rounded energy
and residual, respectively, then

    Q_max=(nu+1)E_Q,max+nu d+(3Lambda+4)d,
    E_out,max=Q_max+(nu+1)R_max,
    0<=H_out<=[Q_max+(2K_o+1)g_o] I.                   (Y21)

These bounds count the entire raw spectrum and all history couplings.
They do not replace the initial-energy account. With
gamma=(1+exp(beta_c d))^-1 and gamma_2=(1+exp(2beta_c d))^-1,

    <Q>=(nu+1)<Q_D>+nu d gamma+3d p_o
          +2d(Lambda-1)gamma_2+d(Lambda+3)gamma,
    <R_bank>=(nu+1)<R_D>.                              (Y22)

The diagonal history identity and full-generator moments are

    A_hist=g_o sum_(j=1)^(K_o)n_(C_j)+g_o P_in
               +a_0(P_out-n_(C_1)),
    M=Q+A_hist,
    <H_out>=<M>,
    Var(H_out)=Var(M)+sum_j a_j^2<X_j^*X_j+X_jX_j^*>. (Y23)

The initial cursor/fuel factors are diagonal, so hopping means and
distinct-edge cross terms vanish. The launch weight is
p_o(1-gamma)(1-gamma_2)+(1-p_o)gamma gamma_2. Ordinary-edge weights
are z_j(1-z_(j+1))+(1-z_j)z_(j+1); completion has the additional
latch factors (1-gamma) and gamma, exactly as in THERMAL_CLOCK.md.
Var(M) is an eight-state outer-launch expectation plus independent
one-qubit Bernoulli variances. It is not the bare variance alone.

Explicitly, for v=(h,c,z) in {0,1}^3, put

    m(v)=3dh+dc+(2d+g_o)z
           +g_o 1_(v=100)+a_0[1_(v=011)-z],
    w(v)=p_o^h(1-p_o)^(1-h)
           gamma^c(1-gamma)^(1-c)
           gamma_2^z(1-gamma_2)^(1-z).                (Y23a)

For every other site u let e_u be its Q coefficient, p_u its actual
excitation probability, and e'_u=e_u+g_o on a remaining cursor site,
e'_u=e_u otherwise. Then

    <M>=sum_v w(v)m(v)+sum_u e'_u p_u,
    Var(M)=sum_v w(v)m(v)^2-[sum_v w(v)m(v)]^2
                        +sum_u (e'_u)^2 p_u(1-p_u).   (Y23b)

The arbitrary correlated information factors have e'_u=0. Their input
correlations therefore change neither formula. No many-body enumeration
or scientific numerical execution is needed to specify these moments.
The launch probabilities obey

    pi_in=p_o(1-gamma)(1-gamma_2),
    pi_out=(1-p_o)gamma gamma_2,
    pi_out/pi_in=exp[-3d(beta_c-beta_h)].              (Y23c)

Thus beta_c>beta_h gives a strict forward imbalance. Partial trace onto
the three launch factors yields
||[H_out,rho_in]||_1>=2a_0(pi_in-pi_out)>0. The product Gibbs input
is not equilibrium for the interacting generator; its thermal contrast
supplies the initial nonstationarity without a pure outer clock.

All spent-cartridge entropy and correlations remain in the closed
device. Beyond the (nu+1) core hardware banks and the specified joint
information input, the slots add
nu[6 ln 2+h_2(gamma)] initial entropy. The outer controller adds
h_2(p_o)+(Lambda-1)h_2(gamma_2)+(Lambda+3)h_2(gamma).
These are finite initial resources, not a renewal procedure for an
unlimited number of attempts.

## 6. A record-only window after the original core resets

Compare only the outer sink/cursors/latch and the nu output latches
with their all-zero input. Leave the complete old cores, cartridges,
all hot factors and zero-energy slots in their actual states. The
comparison mixture has defect weight

    eta_out <= (K_o+nu+2) exp(-beta_c d) <=2^-104.      (Y24)

On its fuel-ground branch nothing launches. The output latches are
zero, so all record reads reject even though their pointers are I/2.
On its fuel-excited branch every data/reference vector has the exact
history of the unitary word W_nu. Unlike a partial source launch, (Y8)
places no seed constraint on those data. Inverting the word restores
the whole initial data bank before the reverse launch.

Both the actual initial density and this cold-zero comparison commute
with Q: every unknown correlated information factor has zero energy,
and all other initial factors are diagonal onsite Gibbs states or their
compared ground states. Since [H_hist,Q]=0, the density evolved by
H_hist continues to commute with Q. The free Q factor therefore cancels
exactly from its density evolution. This establishes (Y7), (Y28) and
the return statement without an omitted free-phase assumption. The
diagonal outer fuel mixture also has no active/dormant phase coherence.

The induced path Hamiltonian is g_o I-2g_o J_x/(K_o+1). Put
theta=g_o t/[hbar(K_o+1)]. For a prescribed T_hold>0 choose

    g_o=pi hbar(K_o+1)/(3T_hold).                      (Y25)

Then throughout [T_hold,2T_hold], the completed-tail weight satisfies

    w_tail=Pr{Bin(2Lambda,sin(theta)^2)>=Lambda}
          >=1-beta,       beta=(3/4)^Lambda<2^-128.    (Y26)

Every completed-tail node has already executed all nu whole-core
resets and has exactly (Y7). The physical original clock in the active
core is therefore fresh on that component, while all output slots retain
their records. The global completion latch L_o identifies this entire
completed state. Its substate is exactly p_o w_tail times (Y7) on the
comparison input. No pure external timing seed is omitted.

There is also a stricter local read statement. Use only the fixed
output projector

    Q_i=n_(O_i,L)n_(O_i,P).                            (Y27)

Before node e_i its latch is zero. At and after e_i, no later
instruction acts on O_i. Tracing the orthogonal outer cursor states
removes cross-history terms. Later operations cannot change its joint
state with the passive R. Thus, writing Sigma_i for the accepted
output of the actual one-use channel E on input i,

    Sigma_i,comp(t)=p_o w_i(t) Sigma_i,
    w_i(t)=Pr{Bin(2Lambda,sin(theta)^2)>=e_i}
           >=w_tail(t).                              (Y28)

This uses no clock projector and no global completion-latch selection.
The symbol R here does not include future input registers subsequently
acted on. Their full joint evolution is instead (Y7). The global latch
is useful when the claim includes the simultaneous fresh core and
complete tape, beyond an individual fixed output marginal.

If q_i=Tr Sigma_i and rho_i=Sigma_i/q_i, then

    p_read,i >=p_o w_i q_i-eta_out,
    D(rho_read,i,rho_i)<=eta_out/(p_o w_i q_i).         (Y29)

The mixture proof retains all outer thermal defects, including their
possible false positives. Each old core still has its actual internal
preparation error. From its previously proved margins q_i>1/60000
and D(rho_i,rho_source,i)<60000*2^-103, (Y24)-(Y29) imply the safe
uniform bounds

    p_read,i>1/200000,
    D(rho_read,i,rho_source,i)<200000*2^-103.           (Y30)

For example w_i>3/4 bounds the extra normalization error by
240000*2^-104; adding 120000*2^-104 from the old core is less than
the displayed 400000*2^-104. The much sharper (Y26) gives the success
margin in (Y30).

After reset i the corresponding old source lives in spent cartridge
F_i, not in the fresh active core. Define its unwanted-band effect on
those specified F_i factors. At the one history node e_i between export
and reset, the source is still in D, so a fixed F_i effect has an extra
possible discrepancy. Its normalized contribution is at most

    beta/(w_i q_i)<80000 beta.                        (Y30a)

Indeed that node is before Lambda, with probability at most beta, and
the common p_o cancels from numerator and denominator. After node e_i+1
the effect and record are both left unchanged by subsequent instructions.
Adding (Y30a) to the reference-uniform old-source and outer thermal
bounds still fits below 400000*2^-104. Thus the original unwanted-band
margin below 19/(20*1000000) remains below 1/1000000 for this explicitly
located source effect. Alternatively the global completion-latch read
eliminates (Y30a) entirely. These are effect comparisons, not a material
construction of the generally nonlocal band detector.

These are nu attempts, not nu guaranteed successful outcomes. Shared
outer-fuel uncertainty correlates their occurrence; it is not nu
independent outer launch probabilities. Any conditioning on a joint
tape event must use that event's actual probability. Equation (Y7)
is the unconditioned joint-channel statement from which such bounds
must be derived.

## 7. Reversal, control and the precise retained claim

At 3T_hold the comparison outer history returns. Its inverse W_nu
restores the original cartridges and output-slot states as well as the
active core. All compared output latches return to zero. Therefore

    p_read,i(3T_hold)<=eta_out.                        (Y31)

The retained window follows restoration of the inner clock by SWAP;
it does not survive the return of every controller in this finite
closed implementation. No autonomous permanent stopping is claimed.
At fixed g_o the time scale grows with K_o+1; holding the time scale
fixed increases the global interaction scale.

The construction supplies a complete autonomous finite law, thermal
controller preparation and a quantitative retained-output contract.
Its limitation is the explicit large-support coupling (Y15), together
with exact supplied spectra and instruction matrices. A local switched
implementation can run the original H_D, export through matched-spectrum
SWAP contacts and replace the core through pairwise cartridge SWAPs;
its timing/isolation controls and switching work belong to a separate
driven protocol. Such a protocol is not silently identified with (Y14).

Finally, Q_i and L_o define physical flags and output instruments, not
individual event selection by the Hamiltonian. Implementing a read,
keeping its outcome elsewhere and replenishing the spent cartridges
are additional physical operations. The finite tape, its previous
contents and the complete consumed resource bank are all retained in
the present count.

# Inclusive energy, thermal resources and the original-energy boundary

**NON-CANONICAL. L1. Conditional analytical candidate. Independent
acceptance pending.** Author: A. M. Thorn. Apache-2.0.

This note accounts for the autonomous apparatus with two completion flags.
It uses the complete finite gates and factor inventory in
[PROGRAM_RESOURCES](PROGRAM_RESOURCES.md), the full raw generator in
[STATIC_CONTROLLER](STATIC_CONTROLLER.md), and the actual input in
[THERMAL_CHANNEL](THERMAL_CHANNEL.md). The identities are analytical; no expanded circuit,
scientific executable or thermal enumeration was run. Same-session
cross-checks do not provide independent scientific acceptance.

## 1. The energy being conserved

The source occupation reading is the one in Public Canon v105 at
[`892a0b11089d34e241e1eb76d2c03247022d18e6`](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27479-L27504).
Its native occupation charge is

\[
 H_N=2\sum_{x,\alpha}h_{x,\alpha}^{2}.
 \tag{E1}
\]

Fix an energy scale \(\varepsilon>0\). Each apparatus occupation factor
uses the four genuine integer values \(h=0,+1,-1,2\), with energies
\(0,2\varepsilon,2\varepsilon,8\varepsilon\). In particular the fourth
level has energy \(8\varepsilon\); it is not another zero-energy code
for \(h=0\). The active source has charge eight and the admitted
26-dimensional memory code has charge two. Every memory/reference
input in that code has the same memory energy \(2\varepsilon\),
irrespective of its coherences or entanglement.

The source-to-occupation identification includes the fixed gauge
\(\mathcal I_0=\mathsf{Emb}\,\Gamma^{-1}D_2^*\), not only the map of
basis labels. See the
[Canon occupation intertwiner](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27986-L28021).
This gauge changes no occupation charge.

Use the finite reservoir parameters

\[
 Q_{\max}=8816,\qquad b_0=17632,\qquad B_{\rm bat}=26468.
 \tag{E2}
\]

Each reservoir factor has levels \(b=0,\ldots,B_{\rm bat}\) with energy
\(\varepsilon b\). Every zero-energy helper, synthesis bit and optional
zero-energy information setting has the declared zero Hamiltonian.
All hot and cold reset donors are two-level systems with the same gap

\[
 G=17643\varepsilon.
 \tag{E3}
\]

The fuel gap is also \(G\). Both flags \(A,B\) have gap
\(\varepsilon\). An occupied cursor has gap \(3\varepsilon\) before
the first flag, \(2\varepsilon\) between the flags, and
\(\varepsilon\) after the second flag.

Some physical cursor sites are qutrits with states \(0,F,R\).
Let \(P_j\) be the projector onto the physical site and color of
virtual history node \(j\), \(1\le j\le K\). Different nodes may
share a physical site only through different orthogonal colors. Define
the cursor energy by its physical-site spectral decomposition, or
equivalently by \(\sum_j e_jP_j\) when these are all its nonvacuum
colors. In particular \(F\) and \(R\) at one site are not two
independent thermal qubits.

With \(E_D\) the sum of all occupation, reservoir and reset-donor
energies over every physical row and rail, the full bare Hamiltonian is

\[
 H_0=E_D+G n_f+\varepsilon(n_A+n_B)+\sum_{j=1}^K e_jP_j.
 \tag{E4}
\]

Every physical factor is included once. The site inventory determines
the multiplicities in (E4); it must include future row copies, spent
donors, turn sites and all rail reservoirs. The largest onsite norm is
\(B_{\rm bat}\varepsilon=26468\varepsilon\). The high-gap donors
and fuel remain below this cap.

## 2. Resonant source loading and the two flag transitions

The known occupation seed corresponding to source port \(u_2\) has,
at physical site 97,

\[
 (h_2,h_3,h_5,h_{12})=(-1,-1,+1,-1).
 \tag{E5}
\]

The first two entries are the second object coin code. The last two
are the token label \(t_0\): the Canon's label rotation selects the
pair \((h_5,h_{12})\) with signs \((+1,-1)\). All four entries have
energy \(2\varepsilon\). Denote this four-factor ket by \(s_*\)
and their joint zero ket by \(s_0\).

Place the fuel, home reservoir and first cursor beside these four
occupation factors, as specified by the local layout. The launch is
the partial isometry

\[
 X_0=\zeta\,
 |0_f,s_*,b_0,1_{C_1}\rangle
 \langle1_f,s_0,0,0_{C_1}|,
 \qquad |\zeta|=1.
 \tag{E6}
\]

Here \(1_{C_1}\) means its designated first color. The phase can
incorporate the known scalar in \(\mathcal I_0u_2\); it is independent
of the unknown memory and reference. All unmentioned factors have the
identity. The edge has seven local factors: four occupation systems,
one reservoir, the fuel and the cursor. It does not test the vacuum
of the entire source lattice. The other vacuum entries belong to the
explicit cold-state comparison, while their actual thermal defects
remain in the full input state.

The two sides of (E6) have the same energy because

\[
 8\varepsilon+17632\varepsilon+3\varepsilon
   =17643\varepsilon=G.
 \tag{E7}
\]

The memory energy \(2\varepsilon\) and every spectator energy occur
unchanged on both sides. Consequently \([H_0,X_0]=0\) as an operator
on the entire raw tensor product, not just on the desired seed.

After the preparation and its return to the original physical ports,
the first flag edge replaces cursor energy \(3\varepsilon\) by
\(2\varepsilon\) and raises \(A\). After the three forward source
steps and their return to the original ports, the second flag edge
replaces \(2\varepsilon\) by \(\varepsilon\) and raises \(B\).
Both are resonant independently of success at the receiver.
They do not delete rejected source or memory branches.

The source, memory, returned working reservoir, two raised flags and
final cursor at an ideal ready-input completed endpoint have total energy

\[
 8\varepsilon+2\varepsilon+17632\varepsilon
       +2\varepsilon+\varepsilon=17645\varepsilon.
 \tag{E8}
\]

Before launch the same subtotal is \(G+2\varepsilon\). Reset donors
and every other resource have their own additional, retained energy.
On readiness-failure branches the individual endpoint entries need not
have these ideal values; their complete bare-energy sum is still
conserved by the full gates.

Whole-cell row transfers exchange identical occupation spectra.
Independent swaps of the two bits representing one occupation would
not in general conserve \(2h^2\). The same rule applies to whole
reservoir factors and matching donor factors. Each compiled data gate
has its complete finite energy-fiber lift, including identity on
incomplete boundary fibers. Thus every ordinary instruction commutes
with its relevant contribution to \(E_D\), on all raw inputs.

## 3. Positive full-space generator and inclusive conservation

Write
\(P_{\rm in}=X_0^*X_0\), \(P_{\rm out}=X_0X_0^*\), and
\(D_0=P_{\rm in}+P_{\rm out}\).
For every ordinary or flag edge \(j\ge1\), retain the complete diagonal

\[
 D_j=P_j+P_{j+1}.
 \tag{E9}
\]

The associated \(X_j\) transports the cursor, applies the specified
complete gate, and raises a flag when required. A turn between two
colors at the same physical qutrit also uses (E9). No diagonal is
silently reduced to only the enabled flag or data sector.

Let \(a_{-1}=a_K=0\) and use

\[
 a_j=\frac{g\sqrt{(j+1)(K-j)}}{K+1},\qquad
 v_j=g-a_{j-1}-a_j\ge0,\qquad g>0.
\]
\[
 V_0=P_{\rm in},\quad V_j=P_j\ (j\ge1),\qquad
 H_{\rm prop}=\sum_{j=0}^{K-1}a_j(D_j-X_j-X_j^*)
              +\sum_{j=0}^{K}v_jV_j,
 \quad H=H_0+H_{\rm prop}.
 \tag{E10}
\]

The launch is a positive two-state Laplacian and zero off its exchanged
pair. On the enabled two-color sector, an ordinary edge has block
\(\left(\begin{smallmatrix}I&-G_j^*\\-G_j&I\end{smallmatrix}\right)\)
for a unitary \(G_j\). If both endpoints are independently occupied,
the hopping vanishes and the diagonal is \(2I\). An onsite turn has
the same positive two-color block without an independently doubly
occupied sector. A flag edge replaces the off-diagonal unitary by a
contraction, and the block remains positive. The other raw sectors
remain nonnegative. Therefore

\[
 H_{\rm prop}\ge0,\qquad H\ge0,\qquad
 [H_0,H_{\rm prop}]=0.
 \tag{E11}
\]

All three observables \(H_0,H_{\rm prop},H\) are exactly conserved by
the autonomous evolution. This applies to the actual thermal mixture,
including malformed occupation strings, occupied future rows and
multiple cursors. Individual source, donor, fuel, reservoir and clock
energies can change. Their changes sum to zero in (E4); there is no
unlisted work term during evolution under this fixed \(H\).

Each propagation edge has norm at most \(2a_j\le g\), and each
potential has norm at most \(g\). If \(E_{\rm cap}\) is the sum of
the maximal onsite energies of all counted physical factors, a
conservative all-space capacity bound is

\[
 0\le H\le [E_{\rm cap}+(2K+1)g]I.
 \tag{E12}
\]

The count is finite and includes the capacity of every reservoir copy,
not only its small initial mean energy. Initial interaction energy is
part of the full energy account below. If a physical initialization
procedure first prepares the factors under \(H_0\) and then switches
on \(H_{\rm prop}\), its switching and mean work
\(\langle H_{\rm prop}\rangle\) are additional initialization
resources. The mathematical initial-state contract takes the declared
fixed Hamiltonian and product state as its boundary data; it does not
provide that preparation factory.

## 4. Actual local Gibbs inputs and a finite thermodynamic ledger

Choose \(\beta_hG=\log2\). The fuel and every designated hot reset
donor then have excitation probability exactly \(1/3\). Every charged
cold factor, including future copies of donor spectra, uses one finite
\(\beta_c>0\). Zero-energy thermal qubits have state \(I/2\) and
are not purified merely by lowering \(\beta_c\). Their reset panel
uses the counted fresh hot/cold donor pairs. A coherent setting, if
admitted as information, is excluded from the thermal-helper claim.

Let \(\mathcal T\) be the set of thermal physical factors. For factor
\(i\), with energy levels \(E_i(a)\), define

\[
 Z_i=\sum_a e^{-\beta_iE_i(a)},\quad
 w_i(a)=Z_i^{-1}e^{-\beta_iE_i(a)},\quad
 \mu_i=\sum_a w_i(a)E_i(a),\quad
 \nu_i=\sum_a w_i(a)E_i(a)^2.
 \tag{E13}
\]

The physical memory input is one encoded information block. Its
constituent occupation factors are not also counted as independent
thermal inputs. Its arbitrary joint state with a passive reference is
\(\rho_{MR}\), supported on the charge-two memory code. With an
optional zero-energy information setting included in that block, the
actual initial state is

\[
 \rho_{\rm th}=\bigotimes_{i\in\mathcal T}\tau_i\ \otimes\rho_{MR},
 \qquad \tau_i=\sum_a w_i(a)|a\rangle\langle a|.
 \tag{E14}
\]

The tensor expression means the fixed physical encoding of the memory
block. It does not dephase the memory or its reference. In particular
\([\rho_{\rm th},H_0]=0\).

For an occupation factor,

\[
 Z_h=1+2e^{-2\beta_c\varepsilon}+e^{-8\beta_c\varepsilon},\quad
 \mu_h=\frac{\varepsilon(4e^{-2\beta_c\varepsilon}
                         +8e^{-8\beta_c\varepsilon})}{Z_h},\quad
 \nu_h=\frac{\varepsilon^2(8e^{-2\beta_c\varepsilon}
                         +64e^{-8\beta_c\varepsilon})}{Z_h}.
 \tag{E15}
\]

For a reservoir, (E13) is the finite sum over \(b=0,\ldots,26468\)
with \(E_b=\varepsilon b\). For a gap-\(d\) qubit it gives
\(p=(1+e^{\beta d})^{-1}\), \(\mu=dp\),
\(\nu-\mu^2=d^2p(1-p)\). For a cursor qutrit with gaps
\(e_F,e_R\),

\[
 Z_C=1+e^{-\beta_ce_F}+e^{-\beta_ce_R},\qquad
 \mu_C=\frac{e_Fe^{-\beta_ce_F}+e_Re^{-\beta_ce_R}}{Z_C},
 \quad
 \nu_C=\frac{e_F^2e^{-\beta_ce_F}+e_R^2e^{-\beta_ce_R}}{Z_C}.
 \tag{E16}
\]

Its two occupied-color probabilities have their shared normalization.
The bare initial moments are exactly

\[
 \langle H_0\rangle=2\varepsilon+\sum_i\mu_i,
 \qquad \operatorname{Var}_{\rho_{\rm th}}(H_0)=\sum_i(\nu_i-\mu_i^2).
 \tag{E17}
\]

With natural logarithms, each thermal factor has entropy
\(S(\tau_i)=\beta_i\mu_i+\log Z_i\). The initial apparatus entropy
is \(S(\rho_M)+\sum_iS(\tau_i)\), including any admitted setting in
\(\rho_M\). This is finite because the apparatus is finite. Statements
including the reference entropy require that entropy to be defined;
the channel and energy identities do not require a finite reference
dimension. Evolution preserves total apparatus entropy and its mutual
information with the reference under the complete unitary.
Reduced donor or source entropies can change, with correlations retained.

For any counted thermal bank initially
\(\tau_D=\bigotimes_{i\in D}\tau_i\), its unconditional final reduced
state \(\sigma_D\) satisfies the exact finite Gibbs identity

\[
 \sum_{i\in D}\beta_i\Delta\langle E_i\rangle
  =S(\sigma_D)-\sum_{i\in D}S(\tau_i)
     +D(\sigma_D\Vert\tau_D).
 \tag{E18}
\]

It follows by inserting \(\log\tau_D=-\sum_i\beta_iE_i-\sum_i\log Z_i\)
in relative entropy. Correlations within the bank occur in the last
term. Unknown quantum memory is not a Gibbs reset resource in this
formula. The same resource account covers rejected and dormant runs;
conditional success is not used to discard their heat or entropy.

## 5. Full interacting mean and variance with colored cursors

Bare moments alone omit interaction energy. Define the diagonal operator
and the hopping operator

\[
 M_0=H_0+\sum_j a_jD_j+\sum_jv_jV_j,
 \qquad \mathcal A=\sum_j a_j(X_j+X_j^*),
 \qquad H=M_0-\mathcal A.
 \tag{E19}
\]

Collecting the incidence coefficients in (E9)--(E10) gives the exact
full-raw identity

\[
 M_0=H_0+g\sum_{j=1}^KP_j+gP_{\rm in}
                      +a_0(P_{\rm out}-P_1).
 \tag{E20}
\]

This identity also holds for shared-qutrit colors and onsite turns.
It uses their projectors, rather than treating the colors as independent
bits. Every hopping term changes a cursor color, cursor occupancy or
the launch fuel. The initial thermal state is diagonal in these factors;
memory coherences do not remove those changes. Hence

\[
 \langle H\rangle=\langle M_0\rangle,
 \qquad
 \operatorname{Var}_{\rho_{\rm th}}(H)
   =\operatorname{Var}_{\rho_{\rm th}}(M_0)
       +\operatorname{Tr}(\rho_{\rm th}\mathcal A^2).
 \tag{E21}
\]

Here \(\langle\mathcal A\rangle=0\) and the two mixed terms
\(\langle M_0\mathcal A\rangle,\langle\mathcal A M_0\rangle\)
vanish by the same physical-factor trace. The full square in (E21)
retains any cross terms between distinct edges. No independence
assumption about overlapping cursor sites is needed.

For an explicit finite product evaluation of the diagonal part, put
\(\widetilde E_i=E_i+g\sum_{j:\,j\text{ at }i}P_j\) at each cursor
site and \(\widetilde E_i=E_i\) elsewhere. Let \(L\) be the seven
launch factors in (E6), including the entire first cursor qutrit when
applicable, and define

\[
 m_L(x_L)=\sum_{i\in L}\widetilde E_i(x_i)
       +gP_{\rm in}(x_L)+a_0[P_{\rm out}(x_L)-P_1(x_L)],
 \qquad w_L(x_L)=\prod_{i\in L}w_i(x_i).
\]
\[
 \langle M_0\rangle=2\varepsilon+
       \sum_{x_L}w_L(x_L)m_L(x_L)
       +\sum_{i\in\mathcal T\setminus L}\langle\widetilde E_i\rangle_{\tau_i},
\]
\[
 \operatorname{Var}(M_0)=
       \sum_{x_L}w_L(x_L)m_L(x_L)^2
       -\left[\sum_{x_L}w_L(x_L)m_L(x_L)\right]^2
       +\sum_{i\in\mathcal T\setminus L}\operatorname{Var}_{\tau_i}(\widetilde E_i).
 \tag{E22}
\]

All sums are finite. The optional information setting contributes zero
to the diagonal expressions. A fully explicit finite-product expression
for the remaining term in (E21) is obtained as follows. For a thermal
basis configuration \(x\), let \(W_xv=|x\rangle\otimes\iota_Mv\)
insert the encoded information vector. With \(\rho_M\) the information
marginal, including a setting if needed,

\[
 \operatorname{Tr}(\rho_{\rm th}\mathcal A^2)
   =\sum_x\left[\prod_{i\in\mathcal T}w_i(x_i)\right]
       \operatorname{Tr}\!\left(\rho_M
                       W_x^*\mathcal A^2W_x\right).
 \tag{E23}
\]

The summands are nonnegative quadratic forms, since
\(W_x^*\mathcal A^2W_x=(\mathcal A W_x)^*(\mathcal A W_x)\).
This formula keeps all information coherences and all raw sectors.
It is an exact account, not a report of having enumerated these states.
For a simple uniform bound, \(\|\mathcal A\|\le\sum_j a_j\le Kg/2\);
alternatively (E12) gives
\(\operatorname{Var}(H)\le[E_{\rm cap}+(2K+1)g]^2/4\).
Both full energy moments in (E21) are conserved at every time.

## 6. Why the thermal launch is nonstationary, and which energy it uses

Let \(\pi_{\rm in},\pi_{\rm out}\) be the probabilities of the
seven-factor launch configurations in the actual product input. All
four source occupations, the home reservoir and first cursor are cold.
The fuel is hot with excited probability \(1/3\). The exact ratio is

\[
 \frac{\pi_{\rm out}}{\pi_{\rm in}}
   =2e^{-\beta_c(8+17632+3)\varepsilon}
   =2e^{-\beta_cG}.
 \tag{E24}
\]

At \(\beta_c\ne\beta_h\) these weights differ. The off-diagonal
launch matrix element therefore gives
\([H_{\rm prop},\rho_{\rm th}]\ne0\). This explicitly identifies the
initial nonequilibrium resource: independent local Gibbs states at the
two declared temperatures are not the Gibbs state of the interacting
Hamiltonian \(H\). A prepolarized cursor or supplied coherent battery
is not inserted into this argument.

For error comparisons only, set every charged cold factor to its unique
zero-energy state. Their joint probability is
\(q_c=\prod_{i\text{ cold}}Z_i^{-1}\), with

\[
 1-q_c\le\sum_{i\text{ cold}}(1-Z_i^{-1}).
 \tag{E25}
\]

Zero-energy mixed helpers are not included in this ground-state event.
They still require the reset panel and its donors. No cold-defect branch
is discarded from the actual state. The inventory is fixed first and
\(\beta_c\) is chosen afterwards to achieve the specified error,
so no pure initial clock or circular temperature count is assumed.

The nominated original spectral energy is instead
\(Q=E_0f(U_{\rm rec})\). The
[stationarity obstruction](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/RESOURCES_RESET.md)
continues to apply to a preparation covariant under that energy.
The present apparatus conserves (E4); it is not asserted to be
\(Q\)-covariant. A coherent state of the active source may have a
fixed \(H_N=8\) while failing to commute with \(Q\). This is exactly
why the sharp charge reservoir can supply the present gate compilation
without contradicting that obstruction.

Moreover the initial occupation vacuum is outside the original
one-pair/one-carrier Hilbert space on which \(Q\) was defined.
Using \(Q\) throughout loading would first require a declared
extension to vacuum, transient \(h=2\) states and invalid codes.
If such an extension \(\widetilde Q\) is asserted to be the actual
subsystem energy, then its proposed interaction account must include
the difference \(\varepsilon H_N-\widetilde Q\). No locality,
material interpretation or thermal preparation theorem for that
generally nonlocal difference is established here. It is not a hidden
counterterm in (E10), and the two energy dictionaries are not identified.

## 7. Return, resources and the remaining physical admissions

On the cold-zero comparison, the active history has
\(H_{\rm prop}=gI-2gJ_x/(K+1)\). For the controller's even
\(K\) and \(T_h=\pi\hbar(K+1)/(3g)\), its density returns at
\(3T_h\). The dormant fuel-ground comparison branch remains dormant.
Because the whole comparison input commutes with \(H_0\), this is
also the return of its full density under \(H\), including every
reference correlation and every initial hot-donor and mixed-helper
configuration.

The source is then vacuum again, the working reservoir is back at its
initial cold ground, both flags are zero, and the old memory is restored.
All forward computation, cooling and donor changes have been reversed.
This return erases the prepared source and receiver record. It is not
a regenerating cycle that retains an exported result.

For the actual finite-temperature input write
\(\rho_{\rm th}=q_c\rho_{\rm good}+(1-q_c)\rho_{\rm bad}\), without
changing the hot factors or information input. Only the good component
has the proved exact return. Consequently

\[
 D(\rho(3T_h),\rho_{\rm th})\le1-q_c,
 \qquad \Pr[A=1\text{ or }B=1\text{ at }3T_h]\le1-q_c.
 \tag{E26}
\]

An extraction before reversal changes the stated closed dynamics and
needs its own storage, coupling and reset account. Likewise the initial
thermal banks are consumed as prepared resources within a selected
forward window; no replenished bath or indefinitely reusable factory
is supplied by the finite construction.

The apparatus admits exact finite-dimensional local interactions.
The launch directly couples reservoir levels 0 and 17632. Spatial
locality of one reservoir factor does not derive that matrix element
from adjacent-rung transitions, a dipole selection rule or low-order
microscopic interactions. Its dimension 26469 and the exact coupling
are counted assumptions. Replacing that factor by qubits does not
automatically preserve the bounded-support gate claim. Similarly the
occupation four-level systems, cursor qutrits and their spectral SWAPs
are not an all-qubit implementation without further compilation.

The completed program cuts reproduce the specified preparation and
three original forward-step channels on the admitted occupation inputs.
Between cuts, the clock is correlated with partial circuits and may
visit transient occupation codes. This is not uninterrupted evolution
under the original spectral generator. Nor does it derive these gates
from the unchanged six-pentit rule. Physical selection of the energy
dictionary, finite-precision robustness, interaction fabrication and
initial thermal-bank preparation remain separate admissions.

Exact failures of the launch resonance, a purported conserving row
transfer, the full-raw edge positivity, (E20), or the Gibbs and moment
identities falsify the corresponding claims. All new conclusions in
this note remain NON-CANONICAL L1 conditional candidates.

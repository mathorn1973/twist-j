# A finite thermal source for the work head and cursor

**NON-CANONICAL, L1, conditional analytical candidate-T.** Independent
mathematical acceptance is pending. This note gives the resource and energy
account for [HAMILTONIAN.md](HAMILTONIAN.md), on the actual mixed input of
that law. No scientific executable or simulation was run.

The previous input is
[#1761 at 32c17259c4baf40bb6d08b521adc642956b57e94](https://github.com/mathorn1973/twist-j/tree/32c17259c4baf40bb6d08b521adc642956b57e94/notes/C-THERMAL-REGISTER-PREPARATION-N).
Its concentrated charged work seed and inverted master entry are replaced
here by finite positive-temperature Gibbs factors and a resonant conversion.
The new loader also starts cold. No added timing cursor is supplied in a
state concentrated on an occupied entry.

## 1. The three finite thermal inputs

The old payload and unused data rows retain the common-temperature Gibbs
inputs at

\[
 \beta_0\epsilon=\log2
 \tag{E1}
\]

specified by the predecessor. The admitted logical state and its passive
reference retain their fixed-charge interface; their information is not
used as expendable purity. Every previously counted unused row and head
remains in the system.

Let \(R=2Q\) be the predecessor's distinguished-head central level. The
physical head \(B\) has levels \(0,\ldots,2R\), energy \(\epsilon b\) at
level \(b\), and actual on-site dimension \(2R+1\). Its former concentrated
seed is not supplied.

The new hot system \(h\) and cold entropy receiver \(c\) each have a ground
state \(|0\rangle\) and \(D\) excited states \(|a\rangle\), \(1\leq a\leq D\).
Their Hamiltonians are

\[
 H_h=(R+3)\epsilon P_h,\qquad H_c=\epsilon P_c,
 \quad P_h=\sum_{a=1}^D|a\rangle\langle a|_h,\quad
 P_c=\sum_{a=1}^D|a\rangle\langle a|_c.
 \tag{E2}
\]

Choose

\[
 D=2^{84},\qquad
 \beta_h(R+3)\epsilon=\log2.
 \tag{E3}
\]

Thus the hot Gibbs density operator has probabilities

\[
 p_h(0)={2\over D+2},\qquad
 p_h(a)={1\over D+2},\qquad
 q_h=\operatorname{Tr}(P_h\rho_h)={D\over D+2}.
 \tag{E4}
\]

Its nearly certain *aggregate* excitation is due to the declared degeneracy.
Each individual excited state is less populated than the ground state.
There is no negative temperature or supplied coherent superposition.

The main cursor sites are \(m_0,\ldots,m_{3L}\), and the loader sites are
\(t_0,\ldots,t_{L-1}\), with

\[
 L=4B_{\rm old},\qquad K=4L.
 \tag{E5}
\]

There are exactly \(K+1\) physical cursor/loader qubits. Set

\[
 b_c=84+\left\lceil\log_2(D+K+3)\right\rceil,\qquad
 z=2^{-b_c},\qquad \beta_c\epsilon=b_c\log2,
 \qquad r={z\over1+z}.
 \tag{E6}
\]

The cold receiver, distinguished head, and every main/loader qubit are
independent Gibbs factors at this same positive inverse temperature
\(\beta_c\). Their exact probabilities are

\[
 p_c(0)={1\over1+Dz},\quad
 p_c(a)={z\over1+Dz},\quad
 Z_B=\sum_{j=0}^{2R}z^j,\quad p_B(j)={z^j\over Z_B},
 \tag{E7}
\]

and each cursor/loader qubit has excited population \(r\).

All these density operators are full rank on their entire physical spaces.
In particular the input includes every work level and every zero-, one-,
or multiple-cursor configuration. The large on-site dimensions \(D+1\)
and \(2R+1\), the gaps, and the finite cold temperature are physical inputs.
They are not a code-support promise hiding pure registers.

There are three declared temperatures, \(\beta_0,\beta_h,\beta_c\).
Preparing the thermal factors, their temperature contrast, spectra and
fixed coupling geometry is not itself derived. This is not one equilibrium
bath, an infinite reservoir, or a renewable supply. Thermal densities are
L1 input states; no realized-outcome law is inferred from them. An external
purification of those states is not silently supplied at zero resource cost.

## 2. The local conversion and its energy

For each \(a\), define the partial isometry

\[
 X_a=
 |0,a,R,1,1\rangle\langle a,0,0,0,0|_{h,c,B,m_0,t_0},
 \qquad X=\sum_{a=1}^D X_a .
 \tag{E8}
\]

The domains of its terms are orthogonal, as are their ranges. Therefore
\(X^*X=P_{\rm in}\), \(XX^*=P_{\rm out}\), and \(\|X\|=1\), with

\[
 \begin{aligned}
 P_{\rm in}
   &=P_h(I-P_c)|0\rangle\langle0|_B
                       (1-n_{m_0})(1-n_{t_0}),\\
 P_{\rm out}
   &=(I-P_h)P_c|R\rangle\langle R|_B n_{m_0}n_{t_0}.
 \end{aligned}
 \tag{E9}
\]

The reaction changes bare energy by

\[
 -(R+3)\epsilon+\epsilon+R\epsilon+\epsilon+\epsilon=0.
 \tag{E10}
\]

It transfers the label \(a\) into the cold receiver, charges the old work
head to \(R\), and creates both the actual old cursor entry and the new
loader excitation. The model does not supply a work state concentrated at \(R\) or an extra
timer with a nearly certain occupied entry.

The positive reaction term is

\[
 h_{\rm react}=a_0(P_{\rm in}+P_{\rm out}-X-X^*),
 \qquad a_0={g\sqrt K\over K+1}.
 \tag{E11}
\]

It acts on five nearby physical sites, has norm \(2a_0\), and is positive
on the whole raw space. Increasing \(D\) increases its physical site
dimension and specified matrix data; it does not multiply its norm by
\(D\). The exact many-level resonant coupling is an added physical primitive.

The loader and guarded first main hop described in HAMILTONIAN.md make
this reaction the first edge of one history path. The loader holds the
jointly prepared head and old entry before the inherited program runs.
The Hamiltonian contains the reverse reaction and reverse propagation
edges as required by Hermiticity.

## 3. Exact active mass and finite preparation error

The nominated initial component has the hot system in its excited
manifold, receiver and work head in their ground states, and every
main/loader qubit empty. Its exact weight is

\[
 q={D\over D+2}\,
      {1\over1+Dz}\,{1\over Z_B}\,(1+z)^{-(K+1)}.
 \tag{E12}
\]

Conditioned mathematically on this component, the hot label is uniformly
mixed over \(D\) values. The old payload, other row contents and logical
reference retain their original independent input. This is a component
decomposition of the supplied mixed state, not a discarded branch.

The finite geometric ladder has

\[
 {1\over Z_B}={1-z\over1-z^{2R+1}}>1-z.
\]

The cold receiver has wrong-ground weight at most \(Dz\), and each cold
qubit has excited weight less than \(z\). The union bound consequently gives

\[
 1-q\leq {2\over D+2}+(D+K+2)z
       <{2\over D+2}+(D+K+3)z
       <3\,2^{-84}<2^{-82}.
 \tag{E13}
\]

Write the full input as

\[
 \rho_0=q\rho_{\rm good}+(1-q)\rho_{\rm other}.
 \tag{E14}
\]

The two components have orthogonal initial support and
\(D(\rho_0,\rho_{\rm good})=1-q\), using trace distance
\(D(\rho,\sigma)=\|\rho-\sigma\|_1/2\). Unitary evolution retains this bound;
a reduced output or fixed instrument can only decrease it. The state
\(\rho_{\rm other}\) is not removed from the Hamiltonian or energy account.

On the good loader histories, the preparation is joint:

\[
 |0\rangle\langle0|_h\otimes{P_c\over D}
   \otimes|R\rangle\langle R|_B
   \otimes|\mathrm{entry}\rangle\langle\mathrm{entry}|_{\rm main}
   \otimes\rho_{\rm old\ payload,reference},
 \tag{E15}
\]

tensored with the appropriate loader packet before tracing that packet.
The work head and old cursor entry are therefore prepared together, with
the required payload/reference state. This is stronger than separate
marginal assertions. It is exact on the nominated histories; the full
actual state has both the thermal-tail error and the finite history-window
error quantified in [PREPARATION.md](PREPARATION.md).

The result approximates the predecessor's useful central work and entry
configuration. It does not reproduce the predecessor's deliberately
specified noncentral seed probabilities exactly. The inherited endpoint
contract and its error budget are stated separately in the preparation note.

## 4. Actual initial means, variances and entropy

The new thermal-source moments are

\[
 \begin{aligned}
 \langle H_h\rangle
   &=(R+3)\epsilon {D\over D+2},&
 \operatorname{Var}(H_h)
   &=(R+3)^2\epsilon^2{2D\over(D+2)^2},\\
 \langle H_c\rangle
   &=\epsilon{Dz\over1+Dz},&
 \operatorname{Var}(H_c)
   &=\epsilon^2{Dz\over(1+Dz)^2}.
 \end{aligned}
 \tag{E16}
\]

Define the exact dimensionless cold-head moments

\[
 \mu_B={\sum_{j=0}^{2R}jz^j\over Z_B},\qquad
 \nu_B={\sum_{j=0}^{2R}j^2z^j\over Z_B}-\mu_B^2.
 \tag{E17}
\]

Then its mean and variance are \(\epsilon\mu_B,\epsilon^2\nu_B\).
In particular \(0<\mu_B<z/(1-z)\). It is initially close to empty, not
close to level \(R\).

The complete main/loader bare energy has mean
\(\epsilon(K+1)r\) and variance
\(\epsilon^2(K+1)r(1-r)\). No single initially excited cursor is hidden in
this sum.

The new supplied entropies, with natural logarithms, are

\[
 \begin{aligned}
 S_h&=\log(D+2)-{2\log2\over D+2},\\
 S_c&=\log(1+Dz)-{Dz\over1+Dz}\log z,\\
 S_B&=\log Z_B-\mu_B\log z,\qquad
 S_{\rm cursors}=(K+1)h_2(r).
 \end{aligned}
 \tag{E18}
\]

All other thermal rows and the admitted logical state retain their previous
account. On the nominated conversion component, the hot label has entropy
\(\log D\). Equation (E8) transfers this label coherently to the receiver;
after the conversion the hot factor is pure ground and the receiver
retains entropy \(\log D\). No entropy label is erased or assigned to a
nonexistent sink.

For the actual mixed input, the complete unitary preserves the full
entropy. If a target group \(T\) and all retained resources \(A\) are
initially independent, then

\[
 \Delta S_A=S_T(0)-S_T(t)+I(T:A)_t.
 \tag{E19}
\]

The group \(A\) includes the hot/cold systems, loader, head, donors and old
rows whenever they are not included in \(T\). The mutual information is
part of the account. This construction is not a reset of the hot/cold
source or a cyclic restoration of the temperature contrast.

A finite full-rank preparation resource cannot yield an exactly pure
nontrivial marginal under a unitary. This is why (E13), the loader-window
error, and their accepted-channel corrections are retained. The statement
is scoped to those full-rank resources; it does not falsely label an
arbitrary supplied logical code state full rank on a larger raw carrier.

## 5. The residual nonstationarity is an exact thermal imbalance

Let the local reaction input and output probabilities be

\[
 \pi_{\rm in}
 ={D\over(D+2)(1+Dz)Z_B(1+z)^2},\qquad
 \pi_{\rm out}=2z^{R+3}\pi_{\rm in}.
 \tag{E20}
\]

These are probabilities of the *local* projectors (E9), with the other
cursor bits unrestricted. In particular \(\pi_{\rm in}\geq q\).
The reverse-to-forward ratio follows from the actual Gibbs weights:

\[
 {\pi_{\rm out}\over\pi_{\rm in}}
   =e^{\beta_h(R+3)\epsilon-\beta_c(R+3)\epsilon}
   =2z^{R+3}<1.
 \tag{E21}
\]

The actual input commutes with its additive bare Hamiltonian \(H_0\).
Nevertheless the reaction does not commute with that input. Tracing every
other site isolates its off-diagonal reaction block; all other hops have
a traced cursor endpoint. Equivalently the norm-one Hermitian witness
\(i(X-X^*)\) isolates the same block. It follows that

\[
 \boxed{
 \|[H,\rho_0]\|_1
  \geq2a_0(\pi_{\rm in}-\pi_{\rm out})
   =2a_0\pi_{\rm in}(1-2z^{R+3})>0 .
 \ }
 \tag{E22}
\]

The \(D\) orthogonal reaction-label blocks contribute additively to this
trace norm. The proof holds with the admitted mixed logical input and
passive reference. Other raw sectors can have additional commutator
contributions; (E22) does not claim that all nonstationarity is localized
on one bond.

Thus no bare-energy phase coherence or initially inverted timer was
supplied. Full-\(H\) nonstationarity is still a resource of the specified
initial state relative to the fixed interacting law. Here it follows from
the hot/cold population imbalance (E21).

For a single common Gibbs state of the full additive \(H_0\), a conserving
interaction would commute with that Gibbs state. A Gibbs state of the
complete \(H\) is also stationary. More generally \([H,\rho_0]=0\)
precludes any change under that fixed \(H\). The present construction
does not manufacture nonstationarity from a globally stationary input.
Its temperatures and initially uncorrelated resource factors are
additional nonequilibrium boundary conditions. No external switching
protocol is silently used to produce those conditions.

## 6. A positive inclusive input-energy account

The positive operator

\[
 H_{\rm in}=H_h+H_c+h_{\rm react}+v_0P_{\rm in},
 \qquad v_0=g-a_0,
 \tag{E23}
\]

is a convenient inclusive source-and-interface partition. Its complement
\(H-H_{\rm in}\) is positive, since it consists of the other positive
on-site, edge and potential terms. The reaction term spans the work and
cursor sites too; (E23) is a specified partition of interaction energy,
not an independent local thermal subsystem.

Its exact expectation on the actual initial Gibbs product is

\[
 \langle H_{\rm in}\rangle_0
  =(R+3)\epsilon{D\over D+2}
       +\epsilon{Dz\over1+Dz}
       +g\pi_{\rm in}+a_0\pi_{\rm out}.
 \tag{E24}
\]

This retains the reverse population and the small cold populations.

On the nominated good component, write
\(p_j(t)=\binom Kj\sin^{2j}\theta\cos^{2(K-j)}\theta\),
\(\theta=gt/[\hbar(K+1)]\). Adjacent history amplitudes have relative phase
\(i\), so the real expectation of \(X+X^*\) is zero. Thus

\[
 \langle H_{\rm in}\rangle_{\rm good}(t)
  =\epsilon+\bigl[(R+2)\epsilon+g\bigr]p_0(t)+a_0p_1(t).
 \tag{E25}
\]

At the exact path endpoint the first two history weights vanish.
The inclusive input partition has changed from
\((R+3)\epsilon+g\) to \(\epsilon\). Its loss

\[
 (R+2)\epsilon+g
 \tag{E26}
\]

funds the work/cursor bare-energy transfer and the relocation of propagation
energy. Initially the hot system supplies \((R+3)\epsilon\) on this
component. One \(\epsilon\) remains in the receiver; \(R\epsilon\) charges
the old work head and two \(\epsilon\) excitations start the old cursor and
loader. Later preparation redistributes the work charge into the old
payload, donors and head, without changing their total bare energy.

Equations (E25)--(E26) are conditional-component statements, not the full
actual endpoint transfer. If \(U(t)=e^{-itH/\hbar}\), the actual expectation is

\[
 \langle H_{\rm in}\rangle(t)
 =q\langle H_{\rm in}\rangle_{\rm good}(t)
    +(1-q)\operatorname{Tr}\bigl[
            H_{\rm in}U(t)\rho_{\rm other}U(t)^*\bigr].
 \tag{E27}
\]

The last term is retained. For example

\[
 0\leq H_{\rm in}\leq E_{\rm cap}I,\qquad
 E_{\rm cap}=(R+4)\epsilon+g+a_0,
 \tag{E28}
\]

implies that the difference between the actual and good-component means
is at most \(E_{\rm cap}(1-q)\) at any time. A small state weight alone is
not an energy bound independent of the finite capacity. No tail energy is
discarded because (E13) is small.

## 7. Exact whole-Hamiltonian moments on every raw sector

The following finite sums make the complete initial account explicit even
where the diagonal potential has a complicated many-cursor value. They
are formulas, not an executed numerical summation.

Let \(H_{\rm bg}\) contain every old payload and work-row on-site term
except the distinguished cold head. It includes all retained thermal rows
and the logical fixed-charge input. Write

\[
 \mu_{\rm bg}=\operatorname{Tr}(H_{\rm bg}\rho_{\rm bg}),\qquad
 \nu_{\rm bg}=\operatorname{Var}_{\rho_{\rm bg}}(H_{\rm bg}).
 \tag{E29}
\]

These are evaluated by finite Gibbs sums over the complete previous row
inventory, not only over the active row. Concretely, if the predecessor has
\(J+1\) rows, \(n\) payload qubits and \(n\) head sites per row, then with its
thermal-baseline moments \(\mu_{\rm row}^{\rm th},\nu_{\rm row}^{\rm th}\),
head moments \(\mu_B^{\rm th},\nu_B^{\rm th}\), logical site set
\({\cal L}\), and constant logical charge \(q_{\cal L}\),

\[
 \begin{aligned}
 {\mu_{\rm bg}\over\epsilon}
   &=(J+1)\mu_{\rm row}^{\rm th}-\mu_B^{\rm th}
          +q_{\cal L}-\sum_{i\in{\cal L}}\mu_i^{\rm th},\\
 {\nu_{\rm bg}\over\epsilon^2}
   &=(J+1)\nu_{\rm row}^{\rm th}-\nu_B^{\rm th}
          -\sum_{i\in{\cal L}}\nu_i^{\rm th}.
 \end{aligned}
 \tag{E30}
\]

For a spectrum \(\{e_a\}\) in units \(\epsilon\), the baseline terms in
(E30) are precisely
\(\sum_a e_a2^{-e_a}/\sum_a2^{-e_a}\) and its corresponding variance.
The removed head is added back below with its actual cold distribution.
The old concentrated head and polarized clock moments are not reused.

Write the full Hamiltonian of HAMILTONIAN.md as

\[
 H=H_0+A-\sum_{e=0}^{K-1}a_e(X_e+X_e^*),
 \quad
 A=\sum_ea_eD_e+\sum_{j=0}^Kv_jQ_j.
 \tag{E31}
\]

Here \(X_0=X\), \(D_0=P_{\rm in}+P_{\rm out}\), and the other \(X_e,D_e,Q_j\)
are the explicitly specified guarded or unguarded cursor edges and node
potentials. Every term of \(A\) is diagonal on the initial energy basis.
The matrices and full raw-space action are fixed in HAMILTONIAN.md.

For an explicit sum, let \(u,v\in\{0,1\}\) indicate excitation of the
*new* hot and cold systems; they are not clock coordinates. Use probabilities

\[
 {\cal P}(u=1)={D\over D+2},\qquad
 {\cal P}(v=1)={Dz\over1+Dz}.
\]

Let \(\ell\in\{0,\ldots,2R\}\) be the initial work level, and let
\(\xi\in\{0,1\}^{K+1}\) specify every main and loader bit. The product weight is

\[
 W(u,v,\ell,\xi)
 ={\cal P}(u){\cal P}(v)\,{z^\ell\over Z_B}\,
                   r^{|\xi|}(1-r)^{K+1-|\xi|}.
 \tag{E32}
\]

Degenerate labels have already been summed in \(u,v\). No diagonal energy
or guard depends on their particular value.

Evaluate \(A(u,v,\ell,\xi)\) using the raw projectors (E31), with

\[
 P_{\rm in}=u(1-v)\mathbf1_{\ell=0}(1-m_0)(1-t_0),
 \qquad
 P_{\rm out}=(1-u)v\mathbf1_{\ell=R}m_0t_0.
\]

Define the energy-valued function

\[
 F(u,v,\ell,\xi)
   =(R+3)\epsilon u+\epsilon v+\epsilon\ell
       +\epsilon|\xi|+A(u,v,\ell,\xi),
 \qquad
 M_s=\sum_{u,v,\ell,\xi}W(u,v,\ell,\xi)F(u,v,\ell,\xi)^s .
 \tag{E33}
\]

The sum has explicitly finite limits. Its coefficients are exact functions
of the stated integers, \(z,\epsilon,g\) and the specified square-root
couplings. It includes every cold-head level, hot/cold sector and
multi-cursor bit string.

The exact complete mean is

\[
 \boxed{\langle H\rangle_0=\mu_{\rm bg}+M_1.\ }
 \tag{E34}
\]

Its diagonal propagation mean can also be written without the large sum:

\[
 \begin{aligned}
 \mu_A={}&g\pi_{\rm in}+a_0\pi_{\rm out}
       +r(Kg-a_0)\\
       &+(r^2-r)\bigl[g+a_{L-1}+a_L\bigr],\\
 M_1={}&(R+3)\epsilon{D\over D+2}
       +\epsilon{Dz\over1+Dz}
       +\epsilon\mu_B+\epsilon(K+1)r+\mu_A .
 \end{aligned}
 \tag{E34a}
\]

Indeed, every ordinary cursor edge has diagonal mean \(2r\), while the
last loader and first main edge have their additional guard and mean
\(2r^2\). Every path-node potential other than the reaction input has
mean \(r\), except \(Q_L=n_{m_0}n_{t_{L-1}}\), whose mean is \(r^2\).
Using \(v_0=g-a_0\) and \(v_L=g-a_{L-1}-a_L\) gives (E34a).

For the variance, different edges cannot return a cursor/environment
basis configuration in two hops. Same-edge pairs contribute
\(X_e^*X_e+X_eX_e^*\), including their full raw controls. Therefore

\[
 \boxed{
 \operatorname{Var}_{\rho_0}(H)
   =\nu_{\rm bg}+M_2-M_1^2
       +\sum_{e=0}^{K-1}a_e^2\,
           \operatorname{Tr}\bigl[
              (X_e^*X_e+X_eX_e^*)\rho_0\bigr].
 \ }
 \tag{E35}
\]

The final same-edge sum has the explicit value

\[
 \begin{aligned}
 \kappa={}&a_0^2(\pi_{\rm in}+\pi_{\rm out})
       +2r(1-r)\sum_{e=1}^{K-1}a_e^2\\
       &-2r(1-r)^2(a_{L-1}^2+a_L^2).
 \end{aligned}
 \tag{E35a}
\]

The two guarded edges have jump-and-return probability \(2r^2(1-r)\);
the other nonreaction edges have probability \(2r(1-r)\). These statements
use the actual independent cold cursor factors, including configurations
with several excitations.

This contains the covariance of the bare energy with the diagonal
propagation potential inside \(M_2-M_1^2\). It is not an ideal-history
variance substituted for the actual Gibbs mixture. The diagonal initial
clock factors make the cross terms between \(H_0+A\) and the hop sum
vanish. Gate-dressed return pairs reduce to the identity on their data
sites, so no unknown logical state has been averaged away.

Since \(H\) is time independent and \([H,H_0]=0\), the full distribution of
\(H\), its moments (E34)--(E35), and the expectation of \(H_0\) are conserved.
The energy of all backgrounds, rows, old donors, head copies and interaction
potentials is present. No energy is supplied by a time-dependent switch
during the evolution.

## 8. What remains assumed

This step replaces a specially charged work seed and a specially inverted
timer by a concrete finite thermal conversion. It uses a hot manifold with
large declared degeneracy, a finite low-temperature receiver and vacuum
approximation, and an exactly specified resonant local coupling.

It does not derive the initial temperature contrast, the preparation of
the Gibbs resource factors, the many-level spectrum or the coupling
architecture from the unmodified native law. It does not prepare a Gibbs
state of the interacting whole and then make that equilibrium state run.
Neither a cyclic reset nor a realized-event law is supplied.

The complete input is physically mixed and retains every tail. Joint
readiness, accepted-channel thresholds and finite timing windows have the
errors stated in PREPARATION.md. Conditional or small-error conclusions
must not be rewritten as exact preparation of the actual full-rank input.

No scientific program was executed for this derivation. Same-session
cross-review is not independent mathematical acceptance.

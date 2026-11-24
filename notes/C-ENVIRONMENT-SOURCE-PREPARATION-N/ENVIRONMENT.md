# A mixed thermal environment that funds source preparation

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
Public reservation: [issue #1757](https://github.com/mathorn1973/twist-j/issues/1757).
This is an analytical finite construction. No scientific execution is reported.

Two finite thermal qubits supply the energy for both the old source
excitation and a loading timer. The environment is initially mixed and
full rank. Only one of its four configurations starts the apparatus;
all others remain in the complete state. Its useful weight is
\(q=4/15\), which multiplies every unconditional acceptance claim.

The reaction, loading, and experiment belong to one fixed Hamiltonian.
The environment is thermal for its stated bare qubit energies, not for
the complete interacting Hamiltonian. The source, timer and processor
vacuum remains a specified pure hardware preparation. This supplies a
concrete mixed source; it does not prepare a moving closed system from
a state stationary under that same complete law.

## 1. Bare energies and the supplied mixed state

Let \(\epsilon>0\). The hot qubit h has bare Hamiltonian \(3\epsilon n_h\)
and the cold qubit c has \(\epsilon n_c\), where
\(n=|1\rangle\langle1|\). Supply

\[
\rho_h=\frac23|0\rangle\langle0|+\frac13|1\rangle\langle1|,
\qquad
\rho_c=\frac45|0\rangle\langle0|+\frac15|1\rangle\langle1|.          \tag{E1}
\]

These are Gibbs states of the individual bare Hamiltonians, at inverse
temperatures in inverse-energy units

\[
\beta_h=\frac{\log2}{3\epsilon},\qquad
\beta_c=\frac{\log4}{\epsilon}.
\]

The environment is specified as the mixed density operator
\(\rho_h\otimes\rho_c\), initially independent of all data and its passive
reference. Its weights in order \(hc=00,01,10,11\) are

\[
(p_{00},p_{01},p_{10},p_{11})=\frac1{15}(8,2,4,1).                 \tag{E2}
\]

All are positive. The active configuration is 10, of weight \(q=4/15\).
This is not a prepared pure excitation of unit weight.

Let s be the actual source site of the preceding apparatus,
\(t_0,\ldots,t_{L-1}\) the loading timer, and
\(x_1,\ldots,x_{3L}\) the main processor cursor. All start in their vacuum
state. The data, including its old completion latch, has fixed excitation
number

\[
D=E_{\rm old}+1,\qquad E_{\rm old}=n_*+A_*+Q_*.
\]

The symbols \(x_r\) here are the main sites \(c_r\) of HAMILTONIAN.md;
its environment symbol b is the cold qubit c here.
The data density operator \(\rho_D\) may contain arbitrary admitted logical
messages and passive-reference correlations. The reference has zero
Hamiltonian. The full bare energy is

\[
H_0=\epsilon N_D+3\epsilon n_h+\epsilon n_c
 +\epsilon\left(n_s+\sum_{j=0}^{L-1}n_{t_j}
                         +\sum_{r=1}^{3L}n_{x_r}\right).          \tag{E3}
\]

The stated initial mixed state commutes with \(H_0\). Its bare energy is
not sharp, but it has no coherence between different bare-energy sectors.

These are supplied L1 density operators and unitary evolution, not a
derived law of individual thermal events. The arbitrary-reference claim
concerns the data input. No unspecified purification of the environment
is included. In particular, a coherent purification with a zero-energy
reference need not commute with \(H_0\); preparing and energetically
accounting for such a purification would be a separate construction.

## 2. A local resonant conversion

Use the four-site partial isometry

\[
B=s_h^-s_c^+s_s^+s_{t_0}^+,\qquad
s^+=|1\rangle\langle0|,\quad s^-=(s^+)^*.
\]

It converts the local occupation pattern \(1000\) into \(0111\).
The hot qubit loses \(3\epsilon\); the cold qubit, old source and first
timer site each gain \(\epsilon\). Hence \([H_0,B]=0\).

Its initial and final projectors are

\[
Q_0=B^*B=n_h(1-n_c)(1-n_s)(1-n_{t_0}),\qquad
R_1=BB^*=(1-n_h)n_c n_s n_{t_0}.                                 \tag{E4}
\]

For \(a_0>0\), define the positive reaction edge

\[
h_{\rm reaction}=a_0(Q_0+R_1-B-B^*).                              \tag{E5}
\]

On the converted basis pair it is
\(a_0\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\).
It vanishes on the orthogonal complement and has norm \(2a_0\).
Thus positivity holds on the full physical space, not only the prepared
sector. No measurement of \(Q_0\) or \(R_1\) is performed. The reaction output
projector \(R_1\) differs on raw states from HAMILTONIAN.md's first
loader vertex operator \(Q_1=n_{t_0}\); they agree on the first reached
converted vertex.

The other positive edges and history-node potentials are specified in
[HAMILTONIAN.md](HAMILTONIAN.md). A source-controlled last timer hop and
a timer-end-controlled first processor hop enforce the order. Once the
source excitation has left for the processor, the timer cannot reverse
out of its final site. Reverse processor motion first restores the source,
then permits reverse loading. These are coherent reversible controls.

The initial 00, 01 and 11 environment configurations have vacuum source,
timer and processor and are annihilated by both B and \(B^*\). They stay
inactive. In particular 11 cannot react because the cold site is occupied.

## 3. The active path and the retained inactive components

Use \(K=4L\) history edges and

\[
a_j=\frac{g}{K+1}\sqrt{(j+1)(K-j)},\quad 0\le j<K,\qquad
a_{-1}=a_K=0,\quad v_j=g-a_{j-1}-a_j\ge0.                         \tag{E6}
\]

The active path begins at node zero with
\(|10\rangle_{hc}|{\rm vac}\rangle_{s,t,x}\).
Nodes 1 through L have environment 01, source s occupied, and the timer
at \(t_0,\ldots,t_{L-1}\). The remaining \(3L\) nodes have environment 01,
timer at \(t_{L-1}\), source empty, and the main cursor at
\(x_1,\ldots,x_{3L}\). Every node has the same bare energy

\[
E_{\rm active}=\epsilon D+3\epsilon.                             \tag{E7}
\]

The positive edge and node terms make the propagation diagonal g on
this path. They do not replace it by g times the apparatus excitation
number: conversion creates two excitations but only one history position.
That distinction is necessary for the stated dynamics and energy account.

For the data prefix \(U_j\), the exact active evolution is

\[
|\Psi_{\rm act}(t)\rangle=
 e^{-it(E_{\rm active}+g)/\hbar}
 \sum_{j=0}^K\sqrt{\binom Kj}
 (i\sin\theta)^j(\cos\theta)^{K-j}
 |j\rangle_{\rm hist}\,U_j|\psi_D\rangle,\qquad
\theta=\frac{gt}{\hbar(K+1)}.                                    \tag{E8}
\]

Mixed data inputs follow by linearity. This active evolution has weight
q in the complete density operator. The other three components retain
weights \(8/15,2/15,1/15\) and their initial density operators. They are
orthogonal to the active history subspace and are not discarded.

On the good active loading histories, the old source is exactly
\(|1\rangle\), its processor remains empty, and its data is unchanged.
[PREPARATION.md](PREPARATION.md) quantifies approximation by an interior
timer wavepacket. This is not a pure-source claim for the unconditional
state. Environment 01 alone cannot certify loading: the inactive initial
01 component has that same environment value and empty apparatus.

## 4. Full initial energy, covariance and nonstationarity

The bare environment has exact moments

\[
\langle H_{\rm env}\rangle_0=\frac65\epsilon,\qquad
\operatorname{Var}(H_{\rm env})_0=\frac{54}{25}\epsilon^2,
\quad H_{\rm env}=3\epsilon n_h+\epsilon n_c.                     \tag{E9}
\]

For the variance, independence gives
\(9\epsilon^2(1/3)(2/3)+\epsilon^2(1/5)(4/5)\).
Write \(H=H_0+H_{\rm prop}\) for the one fixed law.
The active initial component has propagation mean g and variance \(a_0^2\).
Each inactive initial component has propagation energy zero. Therefore

\[
\langle H_{\rm prop}\rangle_0=\frac4{15}g,\qquad
\operatorname{Var}(H_{\rm prop})_0
 =\frac4{15}a_0^2+\frac{44}{225}g^2.                              \tag{E10}
\]

The bare and propagation energies are correlated. In the active component
the bare environment energy is \(3\epsilon\), so

\[
\operatorname{Cov}(H_0,H_{\rm prop})_0
 =qg(3\epsilon-6\epsilon/5)=\frac{12}{25}\epsilon g.              \tag{E11}
\]

The two operators commute and this covariance is real. The complete
initial physical moments are

\[
\boxed{\ \langle H\rangle_0=\epsilon D+\frac65\epsilon+\frac4{15}g\ },
                                                                    \tag{E12}
\]
\[
\boxed{\ \operatorname{Var}(H)_0=
 \frac{54}{25}\epsilon^2+\frac{24}{25}\epsilon g
 +\frac{44}{225}g^2+\frac4{15}\frac{g^2K}{(K+1)^2}\ }.             \tag{E13}
\]

Both are conserved. The data term \(\epsilon D\) counts the charged data
fuel, fixed information/work excitations, and completion latch. Source
and timer have no initial bare charge. Omitting the covariance in (E11)
would give an incorrect physical variance.

Only the off-diagonal reaction fails to commute with the initialized
density operator. In active-history notation,

\[
[H,\rho_0]
 =-q a_0(|1\rangle_{\rm hist}\langle0|
       -|0\rangle_{\rm hist}\langle1|)\otimes\rho_D,\qquad
\boxed{\ \|[H,\rho_0]\|_1=2q a_0=\frac8{15}a_0>0.\ }              \tag{E14}
\]

This proves nonstationarity also for mixed logical/reference inputs.
Variance alone would not prove that.

The states in (E1) are Gibbs states of the separate bare qubit energies.
They are not Gibbs states of H, or product Gibbs states of the comparison
Hamiltonian obtained by deleting only the off-diagonal reaction: that
comparison still contains occupation-dependent positive interface energy.
Deleting that off-diagonal term makes this particular initial state
stationary. It is an operator comparison, not an assumed switching
protocol between two Hamiltonians.

## 5. An inclusive positive input-region account

Define

\[
H_{\rm in}=3\epsilon n_h+\epsilon n_c+
                 h_{\rm reaction}+v_0Q_0,\qquad
H_{\rm rem}=H-H_{\rm in}.                                       \tag{E15}
\]

Both are positive: the remainder consists of the other positive bare
terms, edges and potentials. The input operator is supported on h, c, s
and \(t_0\). Its boundary shares the apparatus coupling, so this is a
selected partition of Hamiltonian terms, not two independently evolving
tensor subsystems.

Initially,

\[
\langle H_{\rm in}\rangle_0=\frac65\epsilon+qg,\qquad
\langle H_{\rm rem}\rangle_0=\epsilon D.                          \tag{E16}
\]

The term qg is actual initial interface energy. Quoting only the thermal
qubits' bare mean would omit it.

At \(t_*=\pi\hbar(K+1)/(2g)\), the active environment is 01, the source
and \(t_0\) are empty, the timer is retained at its last site, and the
main cursor is at its endpoint. Every reached component is annihilated
by the reaction edge and \(Q_0\). The environment becomes

\[
(p'_{00},p'_{01},p'_{10},p'_{11})=\frac1{15}(8,6,0,1),\qquad
p'_h=\frac1{15},\quad p'_c=\frac7{15},
\]
\[
\langle H_{\rm in}\rangle_{t_*}=\frac23\epsilon.                  \tag{E17}
\]

The inclusive input region therefore loses

\[
\boxed{\ \langle H_{\rm in}\rangle_0-\langle H_{\rm in}\rangle_{t_*}
 =\frac8{15}\epsilon+\frac4{15}g\ },                              \tag{E18}
\]

which is exactly the gain of the positive remainder.

The bare hot qubit loses \(3\epsilon q=4\epsilon/5\); the cold qubit gains
\(\epsilon q=4\epsilon/15\). The source-plus-timer/processor sector gains
\(2\epsilon q=8\epsilon/15\). Its active endpoint contains one timer and
one processor excitation. No initially excited timer was supplied.

For the active first two history weights
\(p_0(t)=\cos^{2K}\theta\) and
\(p_1(t)=K\sin^2\theta\cos^{2K-2}\theta\), the interference on the
reaction edge has zero real part. Consequently

\[
\langle H_{\rm in}\rangle_t
 =\frac23\epsilon+
 q\bigl((2\epsilon+g)p_0(t)+a_0p_1(t)\bigr).                      \tag{E19}
\]

This counts the interface energy while the first converted history
still has weight. Emptiness of one source site alone does not set that
shared-boundary energy to zero.

## 6. Environment entropy and retained information

Let \(h_2(x)=-x\log x-(1-x)\log(1-x)\).
The initial environment entropy is \(h_2(1/3)+h_2(1/5)\).
At the endpoint, the distinct initial 01 and 10 configurations have
the same environment value 01. Their distinction is retained in the
apparatus: the former has vacuum timer/processor and unchanged data,
whereas the latter has two apparatus excitations and completed data.

The exact environment entropy reduction is

\[
S(\rho_{\rm env}(0))-S(\rho_{\rm env}(t_*))
 =\frac25h_2(2/3).                                              \tag{E20}
\]

Active and inactive endpoint apparatus states have orthogonal support,
and both conditional data states preserve the input spectrum. The
apparatus entropy increases by \(h_2(q)\). The environment-apparatus
mutual information is

\[
I({\rm env}:{\rm app})_{t_*}
 =h_2(4/15)-\frac25h_2(2/3).                                    \tag{E21}
\]

For finite-entropy data these follow directly from block entropies.
The same mutual information is the finite classical information of the
active/inactive label; no subtraction of infinite reference entropies
is required. The full state evolves unitarily and retains its spectrum.
No thermal component or old-memory correlation is erased.

The environment transition pair has population ratio \(p_{10}/p_{01}=2\)
and energy gap \(2\epsilon\), corresponding to virtual inverse temperature
\(-\log2/(2\epsilon)\). This describes a finite inverted pair of levels.
It is not an unlimited bath, autonomous thermostat, cyclic engine, or
freely renewed source. The final environment is changed and correlated;
restoring the original thermal product would need another preparation.

The environment is full rank, but the empty source, timer and processor,
empty storage, and clean data/work are still low-entropy supplied hardware.
Mixed environment input does not eliminate those resources.

## 7. Full-generator coherence and the remaining boundary

Put \(\gamma=g/(K+1)\). The active energy values and initial weights are

\[
E_r=\epsilon D+3\epsilon+g-\gamma(K-2r),\qquad
b_r=2^{-K}\binom Kr,\qquad 0\le r\le K.                           \tag{E22}
\]

The full distribution also contains inactive atoms
\(\epsilon D,\epsilon D+\epsilon,\epsilon D+4\epsilon\), of weights
\(8/15,2/15,1/15\). The active weights are \(qb_r\); coincident energies
are combined when forming a scalar distribution.

Active and inactive states lie in orthogonal invariant subspaces. With
full-energy dephasing \(\Delta_H\), relative-entropy asymmetry is

\[
A_H(\rho_0):=D(\rho_0\Vert\Delta_H(\rho_0))
 =q\left(-\sum_{r=0}^K b_r\log b_r\right)>0.                      \tag{E23}
\]

The thermal mixing entropy is not counted as coherent asymmetry. The
active boundary vector supplies the binomial term; the mixed data/reference
factor cancels in relative entropy. Possible coincident active and inactive
energies do not change the formula because the input has no cross terms
between their invariant sectors.

Dephasing preserves all energy moments, including (E12)-(E13), while
making the state stationary. Those moments alone are thus insufficient
to supply the working preparation. Equation (E14) and its full-energy
coherence identify what the specified environment/contact/vacuum input
additionally supplies.

A full Gibbs state of H commutes with H and cannot initiate this process.
Any H-stationary state stays stationary, and an H-conserving preparation
unitary preserves that property. A product of local bare Gibbs states
with cold empty hardware is not a full Gibbs state of the coupled H.
There is no contradiction with the stationary-input obstruction.

This construction replaces the previously supplied old source excitation
by a specified mixed environment reaction and an included loading timer.
It does not derive the stated temperatures, empty hardware, charged data
fuel, clean work or joint contact condition from the unchanged native law.
No external switching protocol or free reset is hidden in that claim.

## 8. The useful weight belongs to the result

Inactive components never complete the latch or acceptance predicate.
The completion-qualified accepted channel therefore has the form

\[
\sigma_{\rm acc}^{\rm actual}(t)
 =\frac4{15}\,w_{\rm complete}(t)\,\sigma_{\rm ideal}.              \tag{E24}
\]

The normalized accepted channel preserves the ideal reference correlations
where the weight is nonzero. Its unconditional norm includes \(4/15\).

The old threshold \(1/20000\) cannot simply be copied. From the inherited
stronger bound \(p_{\rm ideal}>p_0\), with
\((99/100)p_0>1/20000\), a new window with
\(w_{\rm complete}>99/100\) instead gives

\[
p_{\rm acc}^{\rm actual}>
 \frac4{15}\frac1{20000}=\frac1{75000}.                           \tag{E25}
\]

These remain L1 weights, not a derived L6 occurrence law. The inactive
thermal components are part of the complete physical density operator;
their cost is not normalized away.

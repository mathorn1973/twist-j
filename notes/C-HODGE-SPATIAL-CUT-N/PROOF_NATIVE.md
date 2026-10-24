# Full native circuit across the physical cut 99.5

**NON-CANONICAL. L1. C-HODGE-SPATIAL-CUT-N. Conditional analytic derivation.**

The cut separates the physical sites \(x\le99\) and \(x\ge100\).
This proof first treats the complete native content law, including uncoded
occupations. It then identifies the smaller object/carrier/receiver sector
in which the source uses \(W\). The original source definitions and their
exact bytes are recorded in [SOURCES.md](SOURCES.md). No mathematical run
is reported by this proof.

## 1. Complete carrier and the conserved quantity

A site has 19 original native cells, or 38 content coordinates
\(h_{x,j}\in\mathbb F_5\), with their unchanged chart labels. Write

\[
 \ell(0,1,2,3,4)=(0,1,2,-2,-1),\qquad
 q_x=2\sum_{j=1}^{38}\ell(h_{x,j})^2.
 \tag{N1}
\]

The full content Hilbert space is the completion of finite-excitation
configurations, with the source's direct sum over chart fibres. The
diagonal operators are

\[
 H_N=\sum_xq_x,\qquad
 Q_R^{\rm nat}=\sum_{x\ge100}q_x,\qquad
 Q_L^{\rm nat}=\sum_{x\le99}q_x.
 \tag{N2}
\]

All identities below hold on the common finite-configuration core and
on each fixed total-charge sector. Since every defining gate preserves
the spectral subspaces of \(H_N\), they extend to the corresponding
operator domains. No finite value is assigned to an infinite-charge
configuration.

The local conservation law is for this native charge. It is not an
assertion that \(H_N\) equals the selected spectral energy
\(H_W=i\operatorname{Log}_{3\pi/10}W\).

### Complete ports of the crossing edge

Only the following content factors take part in the edge between 99 and
100. All other factors are retained as spectator tensor factors for this
edge.

| Factor | Left endpoint, site 99 | Right endpoint, site 100 | Full edge action |
|---|---|---|---|
| Object ports | \(L_{99}^{o}=(h_{99,1},h_{99,3})\in\mathbb F_5^2\) | \(R_{100}^{o}=(h_{100,2},h_{100,4})\in\mathbb F_5^2\) | SWAP of both contents, for all values |
| Pulse ports | \(B^1_{99}=(h_{99,7},\ldots,h_{99,11})\in\mathbb F_5^5\) | \(B^2_{100}=(h_{100,12},\ldots,h_{100,16})\in\mathbb F_5^5\) | 26 pulse-code rotations, with the completion below |
| Receiver control/content | No receiver factor is moved from the left | \(m=(h_{100,25},\ldots,h_{100,37})\in\mathbb F_5^{13}\) | Coded label exchange inside the pulse rotation; free pulse edge on uncoded memory |
| Clock controls | Chart clock \(c_{99}\) | Chart clock \(c_{100}\) | Enable the microscopic edge only when both equal 1 |

The other object and pulse ports can participate in other edges of the
same layer. They are not globally immobile: they simply do not cross
this cut. The coordinates \(h_{17},\ldots,h_{24},h_{38}\) are the
source's genuine identity factors. The token's coordinates \(h_5,h_6\)
are unaffected by this edge; local conversion can change them at their
own site. The token codes also use part of the active pulse-coordinate
range, so arbitrary active-bank occupations must not be replaced by a
separate freely propagating token tensor factor.

These port definitions come from source N, its complete-gate section,
and source R, section 5. Source N already uses the present pulse-bank
allocation. Its object SWAP is explicitly on all \(\mathbb F_5\)
values; only the object coin has a 21-pattern identity complement.

## 2. The full object tensor relation: all 625 patterns

Let
\[
 {\cal K}_o=\ell^2(\mathbb F_5^2),\qquad \dim{\cal K}_o=25,\qquad
 \nu(l)=2\bigl(\ell(l_1)^2+\ell(l_2)^2\bigr).
 \tag{N3}
\]

The crossing object gate is the tensor SWAP

\[
 {\mathsf S}_o|l\rangle_L|r\rangle_R
       =|r\rangle_L|l\rangle_R,\qquad l,r\in\mathbb F_5^2.
 \tag{N4}
\]

For arbitrary amplitudes with an arbitrary remaining-system vector
coefficient \(\xi_{l,r}\), its complete index relation is

\[
 \boxed{\eta_{r,l}=\xi_{l,r}
       \quad\hbox{for every }(l,r)\in
          \mathbb F_5^2\times\mathbb F_5^2.}
 \tag{N5}
\]

Equivalently,
\(({\mathsf S}_o)_{l'r';lr}=\delta_{l',r}\delta_{r',l}\).
This specifies every one of the \(25\cdot25=625\) basis patterns.
It includes simultaneous occupations on both sides, values 2 and 3,
and all coherent or entangled inputs. No one-particle assumption is
used.

The right-edge object charge is \(I\otimes\nu\). Hence

\[
 {\mathsf S}_o^\dagger(I\otimes\nu){\mathsf S}_o-I\otimes\nu
       =\nu\otimes I-I\otimes\nu=:J_o.
 \tag{N6}
\]

The flux on basis pattern \((l,r)\) is exactly

\[
                     \boxed{\nu(l)-\nu(r).}                 \tag{N7}
\]

For a general joint state, its expectation is
\(\sum_{l,r}[\nu(l)-\nu(r)]\|\xi_{l,r}\|^2\), with the norms retaining
the whole spectator Hilbert space. This is a consequence of the diagonal
charge and the actual permutation, not a deletion of off-diagonal
information from the state.

For example \(l=(2,0),r=(0,0)\) transfers charge 8. Assigning charge
2 to that raw input would already fail. The six possible two-coordinate
charges \(0,2,4,8,10,16\) have respectively \(1,4,4,4,8,4\) raw
patterns; equation (N5) covers every pairing of these patterns without
a numerical enumeration.

### Spatial regrouping retains tensor boundary data

The full object boundary space is
\({\cal K}_o\otimes{\cal K}_o\), not
\({\cal K}_o\oplus{\cal K}_o\). The four-leg gate tensor has two legs
on each physical side when input/output legs are regrouped spatially.
Its defining relation is still (N5), with all remaining indices retained.

In particular, an arbitrary \(\xi_{l,r}\) cannot be represented by two
independent one-particle amplitude vectors. Factorization into
\(\xi_L(l)\xi_R(r)\) is an additional product-state restriction and is
not imposed here. Contracting the gate tensor with the same complete
state on adjoining layers gives the spatial circuit relation.
A different flattening of that tensor is not, by itself, a physical
two-channel transfer matrix or a new time evolution.

## 3. Pulse codes, arbitrary receiver contents, and the full complement

Let \(p_0,\ldots,p_{25}\in\mathbb F_5^5\) be the source's distinct
two-unit pulse codes, each of charge 4. None is the empty code.
They are the first 26 signed two-position codes in the source's fixed
ordering, with the last selected code moved to index zero.
The receiver codes are
\[
 d_j=(-1)^{j\bmod2}e_{\lfloor j/2\rfloor+1},\quad
 0\le j\le25,
 \tag{N8}
\]
each of charge 2.

Let \({\cal M}=\ell^2(\mathbb F_5^{13})\) and
\({\cal M}_D=\operatorname{span}\{|d_j\rangle\}\).
On the label space \(\mathbb C^{26}\otimes{\cal M}\), define

\[
 {\mathsf J}_{\rm eff}|j\rangle|d_k\rangle
       =|k\rangle|d_j\rangle,\qquad
 {\mathsf J}_{\rm eff}=I
       \ \hbox{on }\mathbb C^{26}\otimes{\cal M}_D^\perp .
 \tag{N9}
\]

Thus \({\mathsf J}_{\rm eff}^\dagger={\mathsf J}_{\rm eff}\) and
\({\mathsf J}_{\rm eff}^2=I\). It commutes with the complete diagonal
receiver charge: coded receiver states all have charge 2, and the
uncoded subspace is fixed. The receiver remains at site 100, although
its internal code can change.

In the two complete pulse banks, define the orthogonal code space

\[
 {\cal P}=\operatorname{span}\{
 |p_j,0\rangle,\ |0,p_j\rangle:0\le j\le25\}.
 \tag{N10}
\]

With the order left-endpoint bank amplitude followed by
right-endpoint bank amplitude, write a vector in
\({\cal P}\otimes{\cal M}\) as \((a,b)\); both entries retain all
26 labels, the whole receiver space, and every other spectator.
The crossing pulse gate is

\[
 \begin{pmatrix}a'\\b'\end{pmatrix}
 =E_p\begin{pmatrix}a\\b\end{pmatrix},\qquad
 E_p=
 \begin{pmatrix}cI&-s{\mathsf J}_{\rm eff}\\
                 s{\mathsf J}_{\rm eff}&cI\end{pmatrix},
 \quad c=\frac1{\sqrt5},\quad s=\frac2{\sqrt5}.
 \tag{N11}
\]

It is the identity on
\({\cal P}^{\perp}\otimes{\cal M}\). This includes every other raw
pair of five-coordinate bank patterns. The block-plus-identity
definition is the full unitary completion, not a promise that extra
active-bank occupations have the one-carrier scattering dynamics.

On uncoded receiver contents, (N11) is exactly the original free
pulse rotation. It is not the identity pulse gate. On coded memory
it is the receiver's complete label-exchange rotation, including
the inverse process. These two clauses are stated separately in
source C, sections 4 and 5.

The full crossed-edge operator is therefore

\[
 E_\partial={\mathsf S}_o\otimes E_p\otimes I_{\rm rest},
 \tag{N12}
\]

with the pulse identity complement included in \(E_p\). The memory
factor is part of \(E_p\), not part of the unchanged spectator factor.
For raw pulse-bank indices \(\alpha,\beta\), memory index \(m\),
and remaining indices \(\kappa\), the tensor relation is

\[
 \eta_{r,l;\alpha',\beta';m';\kappa}
 =\sum_{\alpha,\beta,m}
 (E_p)_{\alpha',\beta',m';\alpha,\beta,m}
       \xi_{l,r;\alpha,\beta;m;\kappa}.
 \tag{N13}
\]

Equations (N5), (N9)--(N13) cover all crossed-edge contents and all
spectators. They do not add independent states for each mark or
each marginal.

### Pulse current and its limited invertible transfer chart

On the code space, the right pulse charge is
\(\operatorname{diag}(0,4I)\). The complete receiver charge commutes
with \(E_p\), so the pulse contribution to the increase of right
charge is

\[
 J_p=E_p^\dagger
       \begin{pmatrix}0&0\\0&4I\end{pmatrix}E_p
       -\begin{pmatrix}0&0\\0&4I\end{pmatrix}
   =\frac45
       \begin{pmatrix}4I&2{\mathsf J}_{\rm eff}\\
                       2{\mathsf J}_{\rm eff}&-4I\end{pmatrix}.
 \tag{N14}
\]

On the raw complement it is zero. Equivalently,

\[
 \langle J_p\rangle
 =4(\|b'\|^2-\|b\|^2)
 =4(\|a\|^2-\|a'\|^2).
 \tag{N15}
\]

The interference contribution is retained; it is not a sum of
classical transition probabilities.

Because \(s\ne0\), precisely this code block admits the spatial
regrouping

\[
 \begin{pmatrix}b'\\b\end{pmatrix}
 =T_p\begin{pmatrix}a\\a'\end{pmatrix},\qquad
 T_p=\frac1s
 \begin{pmatrix}{\mathsf J}_{\rm eff}&-c{\mathsf J}_{\rm eff}\\
                 c{\mathsf J}_{\rm eff}&-{\mathsf J}_{\rm eff}
 \end{pmatrix}.
 \tag{N16}
\]

For \(\Sigma=\operatorname{diag}(I,-I)\),
\[
 T_p^\dagger(4\Sigma)T_p=4\Sigma.                         \tag{N17}
\]
The factor 4 comes from the native pulse charge. No value of that
factor is chosen to match a Hodge form.

The uncoded bank complement instead has its complete identity
input/output relation. A transfer inversion from one side alone
cannot simply discard those unchanged channels. Likewise (N16)
does not replace the object tensor relation (N5), the joint
spectators, or the full circuit's compatibility conditions.

## 4. The complete circuit, clocks, and current balance

Use the source's right-factor-first ordering. In the native calibration
the object step is \(F=SM_{\rm nat}\Gamma\). Its local and edge
implementation, extended by the current homogeneous contact and pulse
codes, is

\[
 G_x=P_{{\rm obj},x}M_x\Gamma_x\Phi_{\beta,x}Q_{{\rm p},x}C_x,
 \qquad G=\prod_xG_x,\qquad
 U_{\rm nat}={\cal E}G .
 \tag{N18}
\]

Here \(C_x\) is the same homogeneous 26-label conversion at every
site. The pulse part of \({\cal E}\) includes the local receiver
modification (N9); its object part is the inherited full SWAP.
The tensor definition on the nine identity coordinates and the
complete receiver factor is the one required by source C.

Every local factor commutes with \(Q_R^{\rm nat}\). In particular,
a contact changes the local arrangement but preserves the local
total charge at its one physical site. All edges strictly within
one half also commute with \(Q_R^{\rm nat}\). Distinct edge factors
act on disjoint content banks, including separate receiver factors.
Consequently

\[
 {\cal E}^\dagger Q_R^{\rm nat}{\cal E}-Q_R^{\rm nat}
       =J_\partial:=J_o+J_p,
 \tag{N19}
\]
where the two summands carry the implicit identity tensor factors.
Thus at the beginning of the macrostep,

\[
 \boxed{U_{\rm nat}^\dagger Q_R^{\rm nat}U_{\rm nat}
             -Q_R^{\rm nat}=G^\dagger J_\partial G.}
 \tag{N20}
\]

The bare \(J_\partial\) is the current just before the edge layer.
Using it on the state before \(G\) would be the wrong phase of the
circuit. Conservation of total \(H_N\) gives the opposite change of
\(Q_L^{\rm nat}\), with positive current oriented left to right.

For the microscopic autonomous law, the unchanged native letter \(b\)
flips the chart clock and preserves contents. If \({\cal B}\) is that
global chart permutation and \({\cal V}\) applies \(G_x\) when \(c_x=0\)
and an edge when both endpoint clocks are 1, then

\[
 \widehat U={\cal B}{\cal V},\qquad
 \widehat U^{-1}={\cal V}^{\dagger}{\cal B}.
 \tag{N21}
\]

All these content operators leave chart controls fixed. Incident
site and edge factors have orthogonal enabling conditions; different
enabled edges use disjoint ports. Therefore the full law is unitary
also on unsynchronized and coherently superposed clock states.
With
\(\Pi_{11}=\mathbf1_{\{c_{99}=1,c_{100}=1\}}\), the microscopic
right-charge increment, on its pre-step state, is

\[
 \widehat U^\dagger Q_R^{\rm nat}\widehat U-Q_R^{\rm nat}
                =\Pi_{11}J_\partial .
 \tag{N22}
\]

The clock flip commutes with \(Q_R^{\rm nat}\). On synchronized
phase zero, two microscopic steps give (N18); (N22) then gives
(N20). The identity auxiliary contents contribute their unchanged
right charge and zero current, even when entangled with the active
contents. None of these statements supplies the selected spectral
energy reading on every asynchronous chart sector.

## 5. Correct comparison with the source \(W=\Gamma S M_2\)

The ordering difference between the native step and the source
walk must be handled explicitly. Put

\[
 D_{\rm coin}=\operatorname{diag}(1,i),\quad
 D_2=D_{\rm coin}\otimes D_{\rm coin},\quad
 M_{\rm nat}=D_2^\dagger M_2D_2=Q\otimes Q .
 \tag{N23}
\]

Both \(D_2\) and the contact phase \(\Gamma\) commute with all
physical position projectors. Let \(\mathsf{Emb}\) be the source's
native occupancy embedding (its \(\mathsf E\)), including the
common-parity coordinates
\(x_A=R+r,\ x_B=R-r\), the signed object colours, and the unchanged
carrier/receiver codes. On the declared encoded sector define

\[
 {\cal I}=\mathsf{Emb}\,\Gamma^{-1}D_2^\dagger .
 \tag{N24}
\]

The following identity is obtained in the encoded coordinates
before applying \(\mathsf{Emb}\):

\[
 \begin{aligned}
 (SM_{\rm nat}\Gamma)(\Gamma^{-1}D_2^\dagger)
       &=S D_2^\dagger M_2,\\
 (\Gamma^{-1}D_2^\dagger)(\Gamma S M_2)
       &=D_2^\dagger S M_2=S D_2^\dagger M_2.
 \end{aligned}
 \tag{N25}
\]

Thus \(F{\cal I}={\cal I}W\), with \(F=SM_{\rm nat}\Gamma\)
understood on the native occupancy sector. This is not obtained by
changing \(SM_{\rm nat}\Gamma\) to \(\Gamma SM_{\rm nat}\) without
the intertwiner.

The current source's homogeneous conversion uses \(iB\) and \(A\).
The source fixes
\(D_2^\dagger iB=(e_2-e_3)/\sqrt2\) and
\(D_2^\dagger A=(e_1+e_4)/\sqrt2\); the common \(\Gamma^{-1}\)
phase at contact cancels in their outer products. This is exactly
the rational native contact, not a new fitted phase. The pulse and
receiver factors commute with this object-only calibration.
Consequently the complete encoded source law and the native
synchronized macrostep obey

\[
                  U_{\rm nat}{\cal I}={\cal I}U_{\rm source}
 \tag{N26}
\]
on the two declared arrangement summands
\((--,T)\oplus(++,p)\), with one A, one B, one token or pulse,
all source directions and labels, and one coded receiver.
No extension of (N26) to arbitrary
many-body active occupations or asynchronous clocks is asserted.

On this sector define the physical right-side projectors
\[
 P_A=\mathbf1_{\{x_A\ge100\}},\quad
 P_B=\mathbf1_{\{x_B\ge100\}},\quad
 P_c=\mathbf1_{\{x_{\rm carrier}\ge100\}},\quad
 P_z=\mathbf1_{\{z\ge100\}} .
 \tag{N27}
\]
The carrier position denotes \(y\) in the token summand and \(x\)
in the pulse summand. Then
\[
              N_R=2P_A+2P_B+4P_c+2P_z .                 \tag{N28}
\]

The embedding and the two local gauge factors preserve this
position-weighted charge, so
\[
 Q_R^{\rm nat}{\cal I}={\cal I}N_R,\qquad
 {\cal I}^\dagger Q_R^{\rm nat}{\cal I}=N_R.             \tag{N29}
\]
For occupied identity auxiliaries, add their \(Q_R^{\rm aux}\)
on both sides of the first identity; it cancels from the current.
Combining (N20), (N26), and (N29) gives

\[
 \boxed{
 {\cal I}^\dagger G^\dagger J_\partial G{\cal I}
      =U_{\rm source}^{\dagger}N_RU_{\rm source}-N_R .
 }
 \tag{N30}
\]

This proves current compatibility without confusing the two gate
orders. Formula (N28) is the restriction of the full native charge,
not its definition on all raw occupations.

## 6. What a complete spatial relation must retain

At this concrete cut, the complete relation consists of:

- the tensor SWAP equations (N5) for all 625 object patterns;
- the entire 26-label and receiver rotation, and its uncoded-memory
  free continuation, in (N9)--(N16);
- the identity relations on all other raw pulse-bank patterns and
  spectator factors;
- the adjoining local layers in their actual order, with the same
  complete amplitudes contracted between layers;
- the clock controls if a microscopic, unsynchronized description
  is used.

The signed quadratic balance is the actual change of the native
right charge, (N20) or (N22). It includes the interference in
(N14), the larger charges of uncoded object values, and all
stationary channels.

One may use a charge-marked direct-sum enlargement on the encoded
sector, but its entries must come from one common physical state.
Such bookkeeping does not replace the tensor boundary relation
above by independent copies of the physical system.

The result supplies a complete local native crossing relation and
its conserved current. It does not identify that whole relation
with a four-dimensional Hodge action, select a Lorentzian metric
normalization, or extend the one-carrier scattering theorem to
arbitrary active-bank backgrounds.

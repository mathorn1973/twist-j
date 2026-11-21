# A local environmental reaction, source loader and complete Hamiltonian

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
Public reservation: [issue #1757](https://github.com/mathorn1973/twist-j/issues/1757).
This is an analytical construction; no scientific execution is reported.

The inherited data word and spatial layout are fixed by
[HAMILTONIAN.md in #1756 at 901c400][input]. That candidate starts with an
occupied source and otherwise empty main cursor. Here the source, main
cursor and an additional loader all start empty. A four-qubit reaction
creates both the source excitation and the loader excitation from one
component of a finite mixed environment. The loader holds the source until
handoff to the main cursor. No excitation is supplied to the loader initially.

The full Hamiltonian, its positive raw-space extension and the handoff gates
are specified below. The original gate word is preserved, but its autonomous
Hamiltonian is changed. Preparing its source state does not prove that the
old Hamiltonian subsequently runs unchanged. [PREPARATION.md](PREPARATION.md)
states the quantitative preparation and output interfaces, including the
thermal failure weight.

## 1. Fixed program and new registers

Use the pinned line width \(S_*\), actual line-gate count \(R_*\), and

\[
N=R_*(S_*+3)-1,\qquad a=N+1,\qquad L=2a.
\tag{H1}
\]

The old main cursor has completion at position L and endpoint 2L. Retain
its edge labels \(G_0,\ldots,G_{2L-1}\), including its initial idle
runway, full data program and completion-latch SWAP. Its completed data is
fixed on the final physical row; its subsequent labels are identity. Add
another L identity edges, giving main sites \(c_0,\ldots,c_{3L}\), with
\(G_j=I\) for \(2L\leq j<3L\). Write \(s=c_0\) for the original
source. In particular \(G_0=I\).

The data register D includes all \(N_{\rm data}=(R_*+1)S_*\) old row
qubits and the old two-qubit completion latch. It initially has sharp
excitation number

\[
E_D^{\rm num}=E_{\rm old}+1,\qquad E_{\rm old}=n_*+A_*+Q_*.
\tag{H2}
\]

The extra one counts the latch. All inherited \(G_j\) conserve the full
physical data number \(N_D\) on raw states. Arbitrary admitted logical
messages and reference correlations in \(\rho_D\) are retained.

Add L loader sites \(t_0,\ldots,t_{L-1}\), initially empty. All main
cursor sites, including s, also start empty. The environment consists of a
hot qubit h of gap \(3\epsilon\) and a cold qubit b of gap \(\epsilon\),
independent of \(\rho_D\), in the diagonal product state below. The symbol
\(b=c_{\rm environment}\) denotes the cold qubit called c in the companion
files; it is distinct from every main-cursor site \(c_r\):

\[
\rho_h=\tfrac23|0\rangle\langle0|+\tfrac13|1\rangle\langle1|,
\qquad
\rho_b=\tfrac45|0\rangle\langle0|+\tfrac15|1\rangle\langle1|.
\tag{H3}
\]

Only the input hb=10 participates in this construction, with weight
\(q=4/15\). The inputs 00, 01 and 11, with their empty loader and main
cursor, will remain inactive. They are not discarded or assigned zero cost.

## 2. Geometric placement and total hardware

Use coordinates relative to the original source \(s=(0,0)\), so the
first main site is \(c_1=(1,0)\). These relative coordinates are translated
by \((-a-1,1)\) in the pinned global layout. Place

\[
h=(-2,0),\qquad b=(-2,-1),
\]
\[
t_j=(-1,-1-j)\quad(0\leq j<a),\qquad
t_j=(0,j-2a)\quad(a\leq j<2a=L).
\tag{H4}
\]

This is a U-shaped nearest-neighbor loader: it goes down one column,
across one edge, then up the adjacent column. Its last sites are
\(t_{L-2}=(0,-2)\) and \(t_{L-1}=(0,-1)\), near s and \(c_1\).
The environmental reaction sites h,b,s,\(t_0\) fit within Manhattan radius
two of h. The final loader and first main controls also have bounded range.

All loader sites lie below the main input runway and left of the data
columns. A leftward main output tail occurs only for even \(R_*\geq2\),
at a different positive relative height. A one-stage circuit has a
rightward output tail. Thus the loader and environment collide with neither
the inherited layout nor the added L output-tail sites. These new tail
sites continue in the old final outward direction. A conservative bounding
rectangle has width \(S_*+5a+6\) and height \(2R_*+a\), with unused
positions omitted.

The total number of physical qubits is

\[
N_{\rm all}=N_{\rm data}+2+(3L+1)+L+2=N_{\rm data}+4L+5.
\tag{H5}
\]

The five groups are the old rows, old latch, main cursor, loader and two
environmental qubits. In particular all empty loader/cursor sites and all
copied battery rows count as hardware. The old fixed battery bank retains
\((R_*+1)Q_*\) physical qubits and raw capacity
\(\epsilon(R_*+1)Q_*\); its single-active-row code uses capacity
\(\epsilon Q_*\). The new environment does not replace that data battery
or its separately charged basis fuel.

## 3. Local edge operators on the entire raw space

For any physical qubit x, write \(n_x=|1\rangle\langle1|_x\),
\(s_x^+=|1\rangle\langle0|_x\), \(s_x^-=(s_x^+)^*\).
Define the global path length and completion index

\[
K=4L,\qquad B=2L=K/2.
\tag{H6}
\]

There is one reaction edge, L-1 loader edges and 3L main edges. For every
edge index \(0\leq i<K\), define a partial hopping operator \(X_i\)
and a positive diagonal operator \(D_i\) as follows. Identities on all
unmentioned factors, including D, are understood.

For the environmental reaction, in tensor order h,b,s,\(t_0\), put

\[
X_0=s_h^-s_b^+s_s^+s_{t_0}^+=|0111\rangle\langle1000|,
\qquad
D_0=|1000\rangle\langle1000|+|0111\rangle\langle0111|.
\tag{H7}
\]

It consumes hot energy \(3\epsilon\), creating cold, source and loader
excitations of energy \(\epsilon\) each. For \(0\leq j<L-2\), let

\[
X_{j+1}=s_{t_{j+1}}^+s_{t_j}^-,\qquad
D_{j+1}=n_{t_j}+n_{t_{j+1}}.
\tag{H8}
\]

The final loader edge is controlled by the occupied source:

\[
X_{L-1}=n_s s_{t_{L-1}}^+s_{t_{L-2}}^-,\qquad
D_{L-1}=n_s(n_{t_{L-2}}+n_{t_{L-1}}).
\tag{H9}
\]

The first main edge is controlled by the loader at its endpoint:

\[
X_L=n_{t_{L-1}}s_{c_1}^+s_s^-\otimes G_0,
\qquad
D_L=n_{t_{L-1}}(n_s+n_{c_1})\otimes I_D.
\tag{H10}
\]

Since \(G_0=I\), this is a three-qubit gate without hidden data support.
All remaining main edges use the inherited local labels:

\[
X_{L+r}=s_{c_{r+1}}^+s_{c_r}^-\otimes G_r,\qquad
D_{L+r}=(n_{c_r}+n_{c_{r+1}})\otimes I_D,
\quad 1\leq r<3L.
\tag{H11}
\]

Define the following local positive vertex operators:

\[
Q_0=|1000\rangle\langle1000|_{h,b,s,t_0},\qquad
Q_{j+1}=n_{t_j}\quad(0\leq j<L-1),
\]
\[
Q_L=n_s n_{t_{L-1}},\qquad
Q_{L+r}=n_{c_r}\quad(1\leq r\leq3L).
\tag{H12}
\]

They are full-space projectors, not outcomes of an energy measurement.
They need not resolve identity on arbitrary raw states; their one-vertex
property on the invariant history subspace is proved below.

Choose \(g>0\) and set

\[
a_i=\frac{g}{K+1}\sqrt{(i+1)(K-i)},\quad a_{-1}=a_K=0,
\qquad v_i=g-a_{i-1}-a_i\quad(0\leq i\leq K).
\]
\[
h_i=a_i(D_i-X_i-X_i^*),\qquad
H_{\rm prop}=\sum_{i=0}^{K-1}h_i+\sum_{i=0}^{K}v_iQ_i.
\tag{H13}
\]

The reaction term is a positive two-state Laplacian with eigenvalues zero
and \(2a_0\), and zero outside its displayed block. Each ordinary exchange
term is zero on cursor 00, equals \(2a_iI\) on cursor 11, and has a positive
10/01 block with unitary off-diagonals. The two controlled exchanges are
these same positive blocks multiplied by commuting control projectors.
Thus, on every raw input,

\[
0\leq h_i\leq2a_iI\leq gI,\qquad v_i\geq0,\qquad
0\leq H_{\rm prop}\leq(K+1)gI.
\tag{H14}
\]

The last inequality follows from
\(2\sum_i a_i+\sum_i v_i=(K+1)g\) and \(0\leq Q_i\leq I\).
It does not assume a prepared clock or discard any illegal sector.

## 4. One physical energy and explicit local bounds

Let \(N_C=\sum_{r=0}^{3L}n_{c_r}\) count the main excitation and
\(N_T=\sum_{j=0}^{L-1}n_{t_j}\) the loader excitation. Give every qubit
except h gap \(\epsilon>0\), and h gap \(3\epsilon\):

\[
H_0=\epsilon(N_D+N_C+N_T+n_b+3n_h),\qquad
H=H_0+H_{\rm prop}.
\tag{H15}
\]

All diagonal terms commute with \(H_0\). The reaction has zero net bare
energy change; all other exchanges move equal-gap excitations or apply an
inherited data-number-preserving gate. Therefore

\[
[H_0,H_{\rm prop}]=[H,N_D]=0,\qquad
0\leq H\leq[\epsilon(N_{\rm all}+2)+(K+1)g]I.
\tag{H16}
\]

The extra two in the bound account for the hot qubit's gap \(3\epsilon\)
in place of \(\epsilon\). Main and loader excitation numbers are not
separately conserved across the reaction. The conserved quantity is the
stated physical bare energy, together with the data number. No negative
term cancels the source or battery energy.

Each edge or vertex term has support on at most seven qubits and Manhattan
radius at most four. The maximum occurs in an inherited main gate, with two
main-cursor and up to five data operands. The reaction and its vertex term
use four sites; final loader and initial main control use three. A source
site belongs to at most six terms, \(t_0\) to at most five, and ordinary
inherited sites to at most four, including onsite terms.

The co-support graph still has degree at most 18. Inherited data sites
belong to at most three seven-site edges. The source has only the six
possible neighbors h,b,\(t_0,t_{L-2},t_{L-1},c_1\); new loader and bath
sites have fewer. Other main sites belong to two inherited edges. Onsite
terms add no neighbors. Every local dimension is two, every edge and
potential term has norm at most g, and the largest bare onsite norm is
\(3\epsilon\). These bounds do not hide a large clock state inside one site.

## 5. The invariant active path and the inactive thermal components

For every data vector, define mutually orthogonal history configurations:

- vertex 0: hb=10, source, loader and all main cursor sites empty;
- vertex j+1, \(0\leq j<L\): hb=01, source occupied, exactly loader site
  \(t_j\) occupied, every other main cursor site empty;
- vertex L+r, \(1\leq r\leq3L\): hb=01, source empty, loader parked at
  \(t_{L-1}\), and exactly main site \(c_r\) occupied.

There are K+1 vertices. The reaction connects the first two. Loader hops
connect successive loader configurations. The source control in (H9)
prevents the loader leaving its endpoint after the main cursor has departed.
The endpoint control in (H10) prevents the main source leaving before the
loader arrives. Both inverse moves are permitted exactly when their
corresponding preceding history vertex is available. All remaining main
hops connect their usual neighbors. Thus this whole subspace is invariant
and has exactly the single-path graph, in both time directions.

On each legal vertex, precisely its named \(Q_i\) in (H12) is one and
the others are zero. Precisely the adjacent edge diagonals contribute.
Their sum with \(v_i\) is \(a_{i-1}+a_i+v_i=g\). These checks also show
why omitting either handoff control or replacing \(Q_L\) by \(n_{t_{L-1}}\)
would give a different graph or a wrong diagonal.

Let \(\mathcal F_0=I\); for loader vertices let
\(\mathcal F_j=I\) for \(1\leq j\leq L\); and for main vertices let
\(\mathcal F_{L+r}=G_{r-1}\cdots G_0\). Under the history isometry
\(|j\rangle\psi\mapsto|\text{configuration }j\rangle\mathcal F_j\psi\),

\[
H_{\rm prop}\big|_{\rm active}
 \simeq gI-\sum_{j=0}^{K-1}a_j(|j+1\rangle\langle j|+|j\rangle\langle j+1|)
 =gI-\frac{2g}{K+1}J_x.
\tag{H17}
\]

The initial data is sharp in \(N_D\), and every active vertex has three
additional bare excitation units: hot energy three initially, then cold,
source and loader, or cold, main cursor and loader. Hence active bare energy
is the scalar

\[
E_{\rm act}=\epsilon(E_{\rm old}+4).
\tag{H18}
\]

The other three environmental inputs 00,01,11 with empty loader/cursor are
annihilated by every \(h_i\) and \(Q_i\). Their initialized density
operators remain exactly stationary. They have their respective bare
energies; they are retained components of the full state.

## 6. Exact complete evolution and its output interface

Put \(\theta=gt/[\hbar(K+1)]\). For any purified admitted data/reference
vector, the normalized active component evolves as

\[
|\Omega_{\rm act}(t)\rangle=e^{-it(E_{\rm act}+g)/\hbar}
 \sum_{j=0}^{K}\sqrt{\binom Kj}(i\sin\theta)^j(\cos\theta)^{K-j}
 |\text{configuration }j\rangle\mathcal F_j|\psi_D\rangle.
\tag{H19}
\]

The symmetric-spin expansion proves (H19) exactly. At
\(t_*=\pi\hbar(K+1)/(2g)\), its single remaining term is the final
vertex: source empty, loader parked, main cursor at \(c_{3L}\), cold qubit
occupied, hot qubit empty, and the complete target output on the final row.
The latch is true. No outcome is selected to establish this evolution.

For the full mixed environmental input, the complete density operator is

\[
\rho(t)=\frac4{15}\rho_{\rm act}(t)
 +\frac8{15}\rho_{00}+\frac2{15}\rho_{01}+\frac1{15}\rho_{11},
\tag{H20}
\]

with the three stationary components just described. This includes arbitrary
mixed logical/reference input by linearity. All components are bare-energy
stationary, so no \(\epsilon/g\) phase-matching condition is required.
This is not a claim of identity free phases on arbitrary energy-coherent
raw inputs.

For loader vertices 1 through L, the original source s is exactly in
\(|1\rangle\), all old main sites \(c_1,\ldots,c_{3L}\) are empty,
and all old data are unchanged. [PREPARATION.md](PREPARATION.md) uses the
slightly smaller set 1 through L-1, selected mathematically by
\(n_s(1-n_{t_{L-1}})\), to exclude the handoff vertex. It proves its
high-weight interval inside the active component and keeps the factor
\(4/15\) for the full thermal input. The loader's excitation was created
by the same reaction, not supplied as an additional running timer.

The old completion latch becomes true at main position L, hence at global
vertex \(B=2L=K/2\). It stays true on the identity tail. With the same
final-row flag projector \(F_{\rm out}\), define
\(\Pi_{\rm read}=n_{\lambda_1}F_{\rm out}\). Its reduction traces the
environment, both controllers, latch, empty rows, work, fuel, battery, inner
clock, system tally and auxiliary histories, then removes the specified
valid output encoding; the passive reference is retained. The exact map is

\[
\mathcal D[\Pi_{\rm read}\rho(t)\Pi_{\rm read}]
 =\frac4{15}\,w(t)\sigma_{\rm ideal},\qquad
w(t)=\sum_{j=B}^{K}\binom Kj\sin^{2j}\theta\cos^{2(K-j)}\theta.
\tag{H21}
\]

All inactive inputs have latch false, and all accepted active prefixes have
identical completed data. Orthogonal history configurations remove cross
terms in the controller trace. The pinned accepted-channel identity then
proves (H21), including every admitted reference correlation. Mathematical
traces and read projectors do not physically discard any branch or supply
a detector instrument.

For \(\pi/3\leq\theta\leq2\pi/3\), the same finite binomial estimate,
now with \(K=2B\), gives \(1-w(t)\leq(3/4)^B\). After a mathematical
accepted read at \(t_*\), backward excursions before B have weight at
most \((3/4)^B\) for delays \(0\leq u\leq\pi\hbar(K+1)/(6g)\).
On the remaining histories the endpoint data is unchanged. These are new
clock times. PREPARATION.md states the resulting conditional capture and
record bounds with the thermal prefactor; it does not promote the inherited
source or spectral candidate proofs.

## 7. The initial resource and the changed physical law

The active input has mean physical energy \(E_{\rm act}+g\) and variance
\(a_0^2=g^2K/(K+1)^2\). The full environmental mixture also contains its
classical energy variation. Its initial mean and variance are

\[
\langle H\rangle=\epsilon(E_{\rm old}+11/5)+\frac4{15}g,
\]
\[
\operatorname{Var}(H)=\frac{54}{25}\epsilon^2+rac{24}{25}\epsilon g
 +\frac{44}{225}g^2+\frac4{15}\frac{g^2K}{(K+1)^2}.
\tag{H22}
\]

Indeed the free environmental mean and variance are \(6\epsilon/5\)
and \(54\epsilon^2/25\). The propagation diagonal is g only in the
weight-4/15 active input, and its quantum off-diagonal squared norm there
is \(a_0^2\). The covariance of bare and propagation energies is
\(12\epsilon g/25\); both cross terms are included in (H22).

Initially only the local reaction fails to commute with the prepared state.
On the active/first-loader block,
\([H,\rho(0)]_{1,0}=-(4/15)a_0\rho_D\), so the full commutator norm is
\(2(4/15)a_0\). This establishes nonstationarity even for mixed logical
inputs. It is relative to the complete interacting Hamiltonian, despite
the environment being diagonal for its specified separate onsite energy.
[ENVIRONMENT.md](ENVIRONMENT.md) gives the positive input-region energy
partition and thermal resource interpretation. The full energy-coherence
distribution is not determined by locality of the reaction term alone.

All couplings are fixed. The source hold and release are encoded in the
local projectors (H9)-(H10), not in an external time-dependent switch.
The old source becomes occupied while its old data family is retained,
but the loader, coupling strengths and controls remain part of the new
Hamiltonian. No equality with the old autonomous generator is asserted.
The hot/cold mixed preparations, empty controllers, ready data, energy
reading and exact interactions are still supplied model data. A stationary
state of this full H cannot be turned into its nonstationary initialized
state by H-conserving evolution. No repeatable bath, native-law derivation,
material realization or occurrence rule is established here.

[input]: https://github.com/mathorn1973/twist-j/blob/901c400f85c427752e2e4367afb6cd00e59ac8c8/notes/C-LOCAL-CLOCK-SOURCE-N/HAMILTONIAN.md

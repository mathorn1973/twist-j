# Exact infinite carrier, finite-memory obstructions, and physical current

**C-HODGE-INFINITE-CARRIER-N. A. M. Thorn.**

**NON-CANONICAL, L1. Analytical candidate-T.** This is a written derivation
for the specified source. No scientific program was executed to obtain it.
It changes no canonical status and asserts no Hodge or Lorentz identification.

## 1. Frozen model and meaning of the result

The source is the homogeneous capture/receiver law at
[`twistj-handoff@0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md).
Its complete encoded physical current is defined in
[`C-HODGE-SPATIAL-CUT-N/PROOF_CURRENT.md@d221e10747e009cb1315295a258f1d48e8b75bce`](https://github.com/mathorn1973/twist-j/blob/d221e10747e009cb1315295a258f1d48e8b75bce/notes/C-HODGE-SPATIAL-CUT-N/PROOF_CURRENT.md).
The exact causal reduction and contact response are defined in
[`C-HODGE-OPEN-CHANNEL-N@b4696efa4fcb56cef8883fb593d2ab571bdcd047`](https://github.com/mathorn1973/twist-j/tree/b4696efa4fcb56cef8883fb593d2ab571bdcd047/notes/C-HODGE-OPEN-CHANNEL-N).

The gap used below is the complete-operator gap in canonical
`CONTACT-W-SPECTRAL-READING [T]`, at the public content commit
[`4a50e527d20018839f006ed312454b710e6486b4`](https://github.com/mathorn1973/twist-j/blob/4a50e527d20018839f006ed312454b710e6486b4/canon/CANON.md).
The present source has exactly the same object operator. A scalar phase
only rotates its spectrum. No positivity claim from (P24) is needed below.

The result supplies a spatially explicit, one-step-in-time realization of
the source with its original charge. Before ancillary factors its Hilbert
space is infinite dimensional and separable, with countably many basis
configurations; its set of complex-amplitude states is not countable.
It separately excludes (i) a finite invariant object carrier containing the
contact state, (ii) any finite time-independent linear realization of the
complete scalar contact response, and (iii) a finite-dimensional linear
factorization of the instantaneous physical-cut current on the full encoded
sector. These are three different statements with different hypotheses.

## 2. Exact lattice recurrence, with every position and label retained

Write the state as token amplitudes

\[
t_{m,d}(R,r,y;z,\sigma,\tau)
\]

and pulse amplitudes

\[
p_{m,d,b}(R,r,x;z,\sigma,\tau),\qquad d=1,2,3,4,
\quad b=1,2.
\]

Here \(x_A=R+r\) and \(x_B=R-r\) are the two physical object positions;
\(y\) is the token position, \(x\) the pulse position, and \(z\) the receiver
position. The carrier and old receiver labels \(\sigma,\tau\) each take all
26 values. All formulae tensor with an unchanged ancillary Hilbert space.
Nothing is traced out. The allowed position coordinates are integers, so
the two constituents lie in the source's common-parity sector.

Put

\[
a=i(e_2-e_3)/\sqrt2,\qquad b_0=(e_1-e_4)/\sqrt2,
\quad h=2/5,\quad\kappa=4/5,\quad\beta=4\pi/5,\quad g=2\pi/5.
\tag{I1}
\]

For every physical site \(n\), define the label-vector contact amplitudes

\[
u_m(n)=a^\dagger t_m(n,0,y=n),\qquad
q_m(n)=b_0^\dagger p_{m,1}(n,0,x=n).
\tag{I2}
\]

The receiver coordinate and both labels are retained in these vectors.
The contact-modified arrays are

\[
\begin{aligned}
\widehat t_m(R,r,y)
 &=t_m(R,r,y)-\mathbf1_{R=y,r=0}\,a[hu_m(y)+\kappa q_m(y)],\\
\widehat p_{m,1}(R,r,x)
 &=p_{m,1}(R,r,x)+\mathbf1_{R=x,r=0}\,b_0[\kappa u_m(x)-hq_m(x)],\\
\widehat p_{m,2}&=p_{m,2}.
\end{aligned}
\tag{I3}
\]

The omitted label/receiver arguments agree on both sides. This is the
orthogonal sum of the rotations \(\left(\begin{smallmatrix}3/5&-4/5\\4/5&3/5\end{smallmatrix}\right)\)
on the actual paired contact directions, with identity on their complement.

The object coin and the streaming displacements are

\[
M=\frac15
\begin{pmatrix}
1&2i&2i&-4\\
2i&1&-4&2i\\
2i&-4&1&2i\\
-4&2i&2i&1
\end{pmatrix},
\quad
(\delta R_d,\delta r_d)=(-1,0),(0,-1),(0,1),(1,0).
\tag{I4}
\]

Thus the token update is the explicit finite-range recurrence

\[
\boxed{
t_{m+1,d}(R,r,y)=e^{-i\beta}\gamma(r)
\sum_e M_{de}\widehat t_{m,e}(R-\delta R_d,r-\delta r_d,y),
\quad \gamma(r)=e^{-ig\mathbf1_{r=0}}.}
\tag{I5}
\]

For completeness, the pulse network can also be written without a Fourier
transform. Set \(c=1/\sqrt5\), \(s=2/\sqrt5\), and first apply

\[
\binom{v_1(x)}{v_2(x)}=
\begin{pmatrix}c&-s\\s&c\end{pmatrix}
\binom{\widehat p_{m,1}(x)}{\widehat p_{m,2}(x)}.
\tag{I6}
\]

All object and other arguments in (I6) are unchanged. Let \(\mathsf S\)
swap the carrier and receiver labels, and let
\(\mathsf S_x=\mathbf1_{z=x+1}\mathsf S+\mathbf1_{z\ne x+1}I\).
The disjoint pulse-edge layer gives

\[
w_1(x)=cv_1(x)-s\mathsf S_xv_2(x+1),\qquad
w_2(x)=s\mathsf S_{x-1}v_1(x-1)+cv_2(x).
\tag{I7}
\]

Finally,

\[
\boxed{
p_{m+1,d,b}(R,r,x)=e^{-i\beta}\gamma(r)
\sum_eM_{de}w_{e,b}(R-\delta R_d,r-\delta r_d,x).}
\tag{I8}
\]

Equations (I2)--(I8) are exactly the complete encoded source law, not an
approximation to its memory kernel. Each layer is unitary; its inverse is
the reversed sequence of adjoint layers. Consequently this recurrence is
equivalent to the source at every time and for arbitrary normalizable
encoded initial states, including dark object components and old memory.
It is local in the displayed configuration coordinates. The pair amplitude
has two object-position coordinates, not one physical position with four
internal components.

The square roots in the normalized contact vectors cancel from their outer
products. The two pulse rotations combine with coefficients in \(\frac15\mathbb Z\).
It follows directly from (I3)--(I8) that all complete-step matrix entries
belong to \(\mathbb Z[i,\zeta_5][1/5]\), with a common denominator dividing
\(125\). A finite-support initial array over this ring stays exactly in
this ring at every finite time. Multiplication by a common power of 125
permits integer coefficient bookkeeping; it does not turn the normalized
unitary dynamics into a newly derived integer permutation or establish a
native-U bridge.

## 3. The original physical charge is preserved by an explicit current

For the cut between \(\ell\) and \(\ell+1\), put
\(\chi_\ell(v)=\mathbf1_{v>\ell}\). On the token and pulse summands use

\[
N^T_\ell=2\chi_\ell(x_A)+2\chi_\ell(x_B)+4\chi_\ell(y)+2\chi_\ell(z),
\]
\[
N^P_\ell=2\chi_\ell(x_A)+2\chi_\ell(x_B)+4\chi_\ell(x)+2\chi_\ell(z).
\tag{I9}
\]

The unchanged ancillary charge may be added on its natural form domain.
On the displayed active sector \(0\le N_\ell\le10\).

Let \(C\) be (I3), and let \(D\) apply \(M\) on both arrangements and
also \(Q\) from (I6) on the pulse arrangement. The only charge-moving
layers are the object streaming and pulse edges. Their currents are

\[
j_{S,\ell}=2\sum_{d=1}^4
\bigl[\Delta_\ell(x_A,v_{A,d})+\Delta_\ell(x_B,v_{B,d})\bigr]
|d\rangle\langle d|,
\tag{I10}
\]

where \((v_A,v_B)=(-1,-1),(-1,1),(1,-1),(1,1)\) and
\(\Delta_\ell(v,+1)=\mathbf1_{v=\ell}\),
\(\Delta_\ell(v,-1)=-\mathbf1_{v=\ell+1}\). On pulse bank 1 at
\(\ell\) and bank 2 at \(\ell+1\),

\[
j_{E,\ell}=4
\begin{pmatrix}s^2I&sc\mathsf S_\ell\\sc\mathsf S_\ell&-s^2I\end{pmatrix};
\tag{I11}
\]

it is zero off that edge and on the token arrangement. The physical current
of one complete update is

\[
\boxed{\mathcal J_\ell=C^\dagger D^\dagger(j_{S,\ell}+j_{E,\ell})DC
              =U^\dagger N_\ell U-N_\ell.}
\tag{I12}
\]

**Proof.** The common phase, object contact phase, onsite coins and capture
preserve the charge at each physical site. The capture vectors have all
three active locations at the same site and equal charge 8. Pulse-edge and
object-streaming operations act on different factors and commute.
Telescoping the layers therefore leaves precisely (I12). Object streaming
changes each constituent's indicator by (I10). The pulse edge changes its
charge by \(4(\|w_2(\ell+1)\|^2-\|v_2(\ell+1)\|^2)\), giving (I11),
including its coherent cross term. This proves the identity for mixed
pairings as well as expectations. For physical site charge
\(n_\ell=N_{\ell-1}-N_\ell\), it yields

\[
U^\dagger n_\ell U-n_\ell=\mathcal J_{\ell-1}-\mathcal J_\ell.
\tag{I13}
\]

These statements concern native charge, not an automatic identification
with current of the separately chosen spectral energy.

## 4. Infinite invariant contact carrier without any density hypothesis

Fix token site zero and fixed spectator labels. On the object space put
\(T=e^{-i\beta}W\), with \(W=\Gamma S M\), and use the unnormalized
contact state

\[
\alpha'=|R=0,r=0\rangle\otimes i(e_2-e_3).
\tag{I14}
\]

**Theorem 1.** The vectors \(\{T^n\alpha':n\ge0\}\) are linearly
independent. In particular no finite-dimensional \(T\)-invariant
subspace contains the contact state.

**Proof.** Direct multiplication by the displayed coin gives
\(M i(e_2-e_3)=i(e_2-e_3)\). Thus the first positive-relative-position
amplitude is \(-i\) in coin 3 at \((R,r)=(0,1)\). To reach \(r=n\)
after \(n\) steps, every streaming displacement must increase \(r\).
After the first coin operation this uniquely requires coin 3 at every
step. Each subsequent coin-3 diagonal contributes \(1/5\), and no later
location has \(r=0\). Hence, for every \(n\ge1\),

\[
\boxed{\langle0,n,3|T^n\alpha'\rangle
       =-i\,e^{-in\beta}5^{1-n}\ne0.}
\tag{I15}
\]

Every \(T^k\alpha'\) is supported in \(|r|\le k\). In a finite
linear relation with largest index \(n\), the coordinate \((0,n,3)\)
therefore annihilates all lower powers and forces its coefficient to
vanish. Induction finishes the proof. The first coin operation includes
the interference of the two initial coin components; the uniqueness
assertion is about the subsequent extreme-direction path. No spectral
density, limiting absorption, decimal bound or numerical check is used.

The same support argument shows that no fixed finite interval in relative
position contains the source-generated orbit. A bound-state projection,
finite spatial truncation or finite-horizon approximation is therefore an
additional restriction, not this exact source recurrence.

## 5. Nonrational contact response without (P24)

For the normalized \(\alpha=\alpha'/\sqrt2\), let \(\mu_\alpha\)
be its spectral probability measure for \(T\), with convention
\(T\leftrightarrow e^{-iE}\). Define

\[
F(z)=\int\frac{1+ze^{-iE}}{1-ze^{-iE}}\,d\mu_\alpha(E),
\qquad |z|<1.
\tag{I16}
\]

**Lemma.** If a spectral probability measure on the circle has a nonempty
open gap in its support and its function (I16) is rational, then that
measure is supported on finitely many points.

**Proof.** On the corresponding open circle arc, the integral continues
analytically through the circle and has purely imaginary boundary values.
For a rational \(F\), the rational function

\[
F(z)+\overline{F(1/\bar z)}
\tag{I17}
\]

therefore vanishes on an arc and is identically zero. Away from the
finitely many circle poles of \(F\), its circle values consequently have
zero real part. On any compact arc avoiding these poles,
\(\operatorname{Re}F(\rho e^{iE})\) converges uniformly to zero as
\(\rho\uparrow1\). But the positive measures
\(\operatorname{Re}F(\rho e^{iE})\,dE/(2\pi)\) converge weakly to
\(\mu_\alpha\), by the Poisson-kernel expansion of (I16). Testing on
continuous functions supported inside each such arc proves that the
measure vanishes there. Only the finitely many poles can carry mass.

This lemma needs the gap. Rationality alone does not imply finite support:
normalized Lebesgue measure gives \(F=1\).

**Theorem 2.** The contact function \(F\) of the specified source is
nonrational. So is its exact scalar transfer function

\[
s(z)=\frac{4-F(z)}{4+F(z)}.
\tag{I18}
\]

To recover this response directly, write the token/contact system as
\(\tau_{m+1}=T(I-hP_\alpha)\tau_m-\kappa T\alpha q_m\) and
\(q'_m=\kappa\langle\alpha,\tau_m\rangle+(3/5)q_m\).
For zero independent object input and \(|z|<1\), set
\(m(z)=\langle\alpha,zT(I-zT)^{-1}\alpha\rangle=(F(z)-1)/2\).
The stationary contact amplitude solves
\(t=-m(ht+\kappa q)\). Consequently
\(q'/q=3/5-\kappa^2m/(1+hm)=(4-F)/(4+F)\).
All inverses exist in the disk, and \(\operatorname{Re}F>0\) prevents
the scalar denominator from vanishing.

**Proof.** The canonical whole-operator theorem supplies two spectral gaps
for the same \(W\), each of width at least
\(\arccos(7/25)-2\pi/5>0\). The phase \(e^{-i\beta}\) rotates these
gaps, so \(\mu_\alpha\) has an open gap. If \(F\) were rational, the
lemma would make its measure finite atomic. A polynomial vanishing at all
those finitely many eigenvalues would then satisfy

\[
\|p(T)\alpha\|^2=\int|p(e^{-iE})|^2d\mu_\alpha(E)=0,
\]

contradicting Theorem 1. Finally \(F=4(1-s)/(1+s)\), so rationality of
\(s\) would imply rationality of \(F\). This proof does not use the
candidate positive-density statement (P24).

**Corollary.** No finite-dimensional, time-independent linear system

\[
v_{m+1}=Av_m+Bq_m,\qquad q'_m=Cv_m+Dq_m
\tag{I19}
\]

can reproduce the complete scalar contact law for arbitrary driving
sequences and all times with the same zero-state response. Indeed its
transfer \(D+zC(I-zA)^{-1}B\) is rational by the adjugate formula.
The corollary does not assume that the internal realization is unitary;
allowing dissipation does not change it. It concerns the fixed-site
contact subsystem before reconnecting the complete free pulse network.
It does not address nonlinear encodings, time-dependent systems, finite
time windows, approximations, or finitely many components per site on an
infinite lattice.

## 6. Infinite physical-current index on the full encoded sector

**Theorem 3.** For every fixed physical cut \(\ell\), the bounded
instantaneous current operator \(\mathcal J_\ell\) has infinitely many
orthogonal positive directions and infinitely many orthogonal negative
directions. In fact it has eigenvalues \(+2\) and \(-2\), each with
infinite multiplicity.

**Proof.** Work just after the contact and onsite coins, and keep one token
position, receiver position, pair of labels and ancillary state fixed.
For each integer \(j\ge1\), let \(e_j^+\) be the token basis state with

\[
x_A=\ell,\qquad x_B=\ell-2j,\qquad d=3.
\tag{I20}
\]

It belongs to the common-parity sector. Constituent A crosses rightward,
whereas B is away from the cut. Thus
\((j_{S,\ell}+j_{E,\ell})e_j^+=2e_j^+\); the pulse-edge term vanishes
on the token summand. These states are mutually orthonormal. Similarly
let \(e_j^-\) have

\[
x_A=\ell+1,\qquad x_B=\ell+1+2j,\qquad d=2.
\tag{I21}
\]

Only constituent A crosses, now leftward, so
\((j_{S,\ell}+j_{E,\ell})e_j^-=-2e_j^-\).
Since \(DC\) is unitary, \((DC)^\dagger e_j^\pm\) are orthonormal
eigenvectors of (I12) with the claimed eigenvalues.

**Corollary.** There is no linear map from the complete encoded state
space to a finite-dimensional space and Hermitian form \(H\) there
such that

\[
\langle\psi,\mathcal J_\ell\varphi\rangle
   =\langle L\psi,H L\varphi\rangle
\quad\text{for all finite-support }\psi,\varphi.
\tag{I22}
\]

To see this without any continuity assumption on \(L\), take more than
\(\dim\operatorname{ran}L\) of the positive eigenvectors. A nonzero
linear combination lies in \(\ker L\), but its current is twice its
strictly positive squared norm. This contradicts (I22).

The theorem concerns arbitrary instantaneous source states. It does not
claim infinite signature for a fixed-energy space of stationary scattering
solutions, nor exclude a justified restriction of the allowed preparations.
The unbounded spectator coordinate in (I20)--(I21) exhibits concretely
why a physical cut has infinitely many channels even when the local
configuration-site coin has only four entries.

## 7. Valid cyclic restriction and normalization

Let \(\mathscr C_T\) be the closed reducing cyclic space generated by
all token contact vectors, and let
\(\mathscr S=\mathscr C_T\oplus\mathscr H_P\).
The free step reduces \(\mathscr S\); both \(C\) and \(C^\dagger\)
preserve it, and the contact is identity on its dark complement. Hence
\(\mathscr S\) reduces the full source unitary.
If \(I:\mathscr S\hookrightarrow\mathscr H\) is inclusion,
define \(U_S=I^\dagger U I\) and \(N_{S,\ell}=I^\dagger N_\ell I\).
Then

\[
I^\dagger\mathcal J_\ell I
 =U_S^\dagger N_{S,\ell}U_S-N_{S,\ell}.
\tag{I23}
\]

This follows from \(UI=IU_S\). No commutation of the cyclic projection
with \(N_\ell\) is required. Therefore preparing initial states in
\(\mathscr S\) in advance is legitimate. It is different from erasing
the dark component of an arbitrary state, which loses mixed charge terms.
Theorem 1 shows that this valid cyclic restriction is still infinite
dimensional. Theorem 3 is not silently asserted on this smaller sector.

The dark-state witness of the predecessor uses normalized \(\alpha,d\).
For their natural unnormalized representatives
\(\alpha'=\sqrt2\alpha\) and \(d'=2d\), the two displayed pairings
are consistent:

\[
\langle W^2\alpha',N_\ell d'\rangle=8/5
\quad\Longrightarrow\quad
\langle W^2\alpha,N_\ell d\rangle
 =\frac{8/5}{2\sqrt2}=\frac{2\sqrt2}{5}.
\tag{I24}
\]

The absence of \(\sqrt2\) from a chosen arithmetic representation does
not make the normalized expression inexact. Unnormalized pairings and
norms can be checked first and combined symbolically.

## 8. Exact boundary of the continuation

The local equations (I2)--(I8), charge (I9) and flux (I12) retain the
complete specified encoded source and remove the need to replace its
object branch by a finite temporal memory. They preserve a finite number
of internal entries at each configuration site, but all object positions,
relative separations, carrier positions and receiver data remain.

The three obstructions prove precise limits of compression. None rules
out an infinite spatial field with finitely many local components. Such a
field has an infinite total state space. Conversely the present two-object
configuration amplitude is not by itself a one-coordinate physical-space
field: any proposed reduction of its relative/spectator coordinates must
prove its domain and pull back the actual charge and current. The
full-domain linear current factorization (I22) is impossible.

No result here derives the chosen contact angle, the source's coherent
law, a physical 3+1 dimension, a Lorentz or Hodge form, a Born occurrence
measure, or an equivalence with the native deterministic update. Those
require their own declared carriers and comparisons.

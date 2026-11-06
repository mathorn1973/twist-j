# The contact Schur function and its open object radiation port

**A. M. Thorn. [candidate-T, NON-CANONICAL, L1]**

This proof uses the complete [homogeneous capture and receiver
law](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md)
at `0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`, especially equations
(1)–(10), (20)–(23), and (27)–(29). It is a mathematical derivation;
the identities below are not reports of executed scientific checks.

The exact time-domain reduction, including the independent initial token
state, is in [PROOF_REDUCTION.md](PROOF_REDUCTION.md). Its actual native
charge and spatial current are transported by the history kernels of
[PROOF_CURRENT.md](PROOF_CURRENT.md). The present proof constructs the
associated contact function and derives its missing object input/output
channel from a radiation jump. It does not identify a spectral probability
port with the full native current through a physical cut.

The rank-one formulas refer to the declared encoded active sector, with
all of its source channels retained. Other occupied native codes retain
their full source gates and native charge; the fixed constituent weights
used below are not substituted for that charge outside the encoded sector.

## 1. An actual conservative contact system

Fix a carrier position n and a carrier/memory label pair. Retain the whole
object space, with its original coordinates, four coins, contact phase,
and both physical constituent motions. Put

\[
\alpha=|R=n,r=0;iB\rangle,\qquad
\beta_n=|R=n,r=0;A\rangle,\qquad
T=e^{-i\beta}W,
\quad r_*=\frac35,\quad h=\frac25,\quad\kappa=\frac45.
\tag{P1}
\]

The energy offset beta in T is indispensable. The scalar pulse field is
`q=<beta_n,p_a(n)>` before contact and q' is that component immediately
after contact. All pulse directions perpendicular to beta_n and the whole
other pulse bank retain their contact identity action. Subsequent pulse
evolution, including W, both pulse layers, their phase and the receiver,
is reconnected as the full free pulse unitary in PROOF_REDUCTION.

Let `P_alpha=|alpha><alpha|`. Token propagation after contact and the pulse
contact output form the exact conservative colligation

\[
\binom{\tau_{m+1}}{q'_m}
=\begin{pmatrix}
\mathcal A&\mathcal B\\\mathcal C&r_*
\end{pmatrix}\binom{\tau_m}{q_m},
\quad
\mathcal A=T(I-hP_\alpha),\quad
\mathcal B=-\kappa T\alpha,\quad
\mathcal C=\kappa\langle\alpha|.
\tag{P2}
\]

This block operator is unitary on the object space plus one scalar port:
it is the source contact rotation followed by T on the token space. In
particular, \(\|\mathcal A\|\le1\). This is an exact rank-one interface,
not an assumption that the full token arrangement is a finite-dimensional
memory or has a bounded resolvent on the unit circle.

All n, all 26 carrier labels, all 26 receiver-memory labels and their
coherences are restored by the orthogonal sum of (P2). The receiver and
auxiliary factors are spectators in this contact function. There is one
copy of the complete moving-object continuum for each standing-token
position and label pair.

## 2. Disk convention and the exact Schur function

The physical stationary eigenvalue is `exp(-iE)`. Approach it with
`zeta=R exp(-iE)`, R>1, and use the disk parameter

\[
z=\zeta^{-1},\qquad |z|<1,\qquad
z=\rho e^{iE},\quad\rho=R^{-1}\uparrow1.
\tag{P3}
\]

Thus the retarded limit is taken from outside the unit circle in zeta,
or from inside it in z. Define

\[
F(z)=\langle\alpha,(I+zT)(I-zT)^{-1}\alpha\rangle,
\quad
m(z)=\langle\alpha,zT(I-zT)^{-1}\alpha\rangle=\frac{F(z)-1}{2}.
\tag{P4}
\]

In the source notation this is exactly `F_1(K,zeta)` with zeta=z inverse:

\[
F(z)=\int_{\mathbb T}
F_B^W(P,e^{i\beta}z^{-1})\,\frac{dP}{2\pi}.
\tag{P5}
\]

It is independent of n and K. In particular it is not the unshifted W
function evaluated at z inverse. The spectral measure of T in alpha has
total mass one; hence `Re F(z)>0` in the disk and F(0)=1.

Write `t=<alpha,tau>` and `u=h t+kappa q`. The stationary token equation
from (P2) is

\[
(I-zT)\tau=-zT\alpha\,u.
\tag{P6}
\]

With no independent object input, `t=-m u`. Consequently

\[
d(z)=1+hm(z)=\frac{4+F(z)}5,\qquad
t=-\frac{\kappa m}{d}q,
\]

\[
\boxed{s(z)=\frac{q'}q
=r_*+z\mathcal C(I-z\mathcal A)^{-1}\mathcal B
=\frac{4-F(z)}{4+F(z)}.}
\tag{P7}
\]

Every inverse in this disk derivation exists: `||z A||<1`, and `Re F>0`
prevents the scalar denominator from vanishing. The disk identity also
gives

\[
1-|s(z)|^2=\frac{16\operatorname{Re}F(z)}{|4+F(z)|^2}>0.
\tag{P8}
\]

The boundary deficit is the channel that must be retained, not a licence
to discard object norm. Equation (P7) is the contact response before the
complete free pulse network is reconnected. It is not by itself the
scattering matrix of the full homogeneous capture model; closing the pulse
propagation introduces its own source function F_2.

## 3. The object input and output arise from the radiation jump

Let

\[
\mathcal H_\alpha=
\overline{\operatorname{span}\{T^k\alpha:k\in\mathbb Z\}}.
\tag{P9}
\]

This is a T-reducing cyclic space. Its spectral representation is
`L^2(mu_alpha)` with T multiplication by `exp(-iE')`. On its absolutely
continuous part use the measure `dE'/(2pi)` and write

\[
F^+(E)=a(E)+ib(E),\qquad
a(E)=2\pi\frac{d\mu_{\alpha,\rm ac}}{dE}(E)\ge0.
\tag{P10}
\]

Here and below boundary statements are almost everywhere where the radial
limit is finite and the density has its Lebesgue value. In this normalized
representation the contact vector is `alpha_ac(E)=sqrt(a(E))`.
An incoming active object amplitude eta_in therefore has contact source
`f=sqrt(a) eta_in`. These amplitudes describe the spectral contact direction
among all open object branches; the density already includes their
velocity Jacobians. They do not select a Bloch momentum or a direction of
motion through the physical cut at 99.5.

To determine the output rather than postulate it, put

\[
G(z)=zT(I-zT)^{-1}.
\tag{P11}
\]

For `|z|<1`, `G(z)=sum_{j>=1} z^j T^j`: this is precisely the forward-time
response to a source switched on adiabatically in the past. The advanced
continuation for `|z|>1` is
`G(z)=-sum_{j>=0} z^(-j) T^(-j)`. In spectral coordinates their scalar
kernels have the distributional boundary values

\[
G^+(E;E')-G^-(E;E')=2\pi\delta(E-E'),
\quad m^-(E)=-1-\overline{m^+(E)},
\quad m^+-m^-=a.
\tag{P12}
\]

For example, the kernel of G inside the disk is
`rho exp(i(E-E'))/[1-rho exp(i(E-E'))]`. Its boundary value is
`-1/2+(i/2) PV cot((E-E')/2)+pi delta(E-E')`; the outside value has the
opposite delta term. This proves the jump and its sign directly from the
source time convention. The identities can first be paired with smooth
energy packets and taken as distributional limits; no inverse on the
whole on-shell object Hilbert space is asserted.

The two descriptions of one driven token field are

\[
\tau=\tau_{\rm in}-G^+(E)\alpha\,u
     =\tau_{\rm out}-G^-(E)\alpha\,u,
\quad u=ht+\kappa q.
\tag{P13}
\]

The contact equation and the jump (P12) give, respectively,

\[
t=\frac{\sqrt a\,\eta_{\rm in}-\kappa m q}{d},\qquad
u=\frac{h\sqrt a\,\eta_{\rm in}+\kappa q}{d},\qquad
\eta_{\rm out}=\eta_{\rm in}-\sqrt a\,u.
\tag{P14}
\]

Combining these with `q'=r_* q+kappa t` yields the actual contact port law

\[
\boxed{
\binom{q'}{\eta_{\rm out}}=
S_F(E)\binom q{\eta_{\rm in}},\qquad
S_F(E)=\frac1{4+F^+(E)}
\begin{pmatrix}
4-F^+(E)&4\sqrt{a(E)}\\
-4\sqrt{a(E)}&4-\overline{F^+(E)}
\end{pmatrix}.}
\tag{P15}
\]

The second channel has thus been obtained from the source radiation jump,
including its relative sign and phase. It is not an arbitrary unitary
completion of s. It acts in the open active object direction where a>0.
Where a=0 there is no such normalized ac direction; the scalar pulse
response is lossless at every finite boundary value, and the formally
adjoined second component of (P15) is just an identity.

Direct multiplication, or the contact norm balance together with (P14),
proves

\[
S_F^\dagger S_F=I,\qquad
|q'|^2+|\eta_{\rm out}|^2=|q|^2+|\eta_{\rm in}|^2,
\]

\[
1-|s(E)|^2=\frac{16a(E)}{|4+F^+(E)|^2},\qquad
\det S_F(E)=\frac{4+\overline{F^+(E)}}{4+F^+(E)}.
\tag{P16}
\]

In particular a pulse-only input has a strict pulse deficit wherever
`a>0`; it appears exactly in the outgoing object port. Singular spectral
components and initial token states are retained by the time-domain
reduction. They are not supplied by the ac formula (P15), nor discarded
because it is unitary almost everywhere.

## 4. The open object port is present across the original energy window

Set

\[
I_E=[8\pi/5-1/1000,\ 8\pi/5+1/1000],\qquad
\omega=E-\beta.
\tag{P17}
\]

The previous spatial-cut proof showed that the token compression has no
bounded inverse on this entire window. We can also show that its actual
contact-visible object continuum stays open there, rather than merely
exhibiting a remote Weyl sequence invisible to alpha.

At P=0 the exact free object characteristic polynomial is

\[
\det[\lambda I-S(0,q)M_2]
=(\lambda-1)^2\left[\lambda^2-
\frac{2(\cos q-4)}5\lambda+1\right].
\tag{P18}
\]

For every E in (P17) choose the positive root
`cos q=4+5 cos omega`. Since `cos beta=-phi/2`,
`3/2<phi<7/4` and `|cos omega-cos beta|<=1/1000`,

\[
-\frac{19}{50}<\cos q<\frac{51}{200},\qquad
\frac\pi3<q<\frac{2\pi}3.
\tag{P19}
\]

Also `omega` lies strictly between `3pi/4` and `5pi/6`. Hence the free
root is simple, its eigenvalue is nonreal and separated from 1, and

\[
\frac{d\omega}{dq}=\frac{\sin q}{5\sin\omega}>0.
\tag{P20}
\]

The source gives, in its Bell complement and with one eigenvector
component set to one,

\[
u_B(q)=\frac{i\sin q(d_0\lambda-1)}
{(\lambda-d_0)(\lambda-\cos q)},\qquad
d_0=-3/5,\quad\lambda=e^{-i\omega}.
\tag{P21}
\]

None of these factors vanishes throughout the compact window:
`sin q>0`, `|d_0 lambda-1|>=2/5`, `|lambda-d_0|>=2/5`, and the last
denominator is nonzero because lambda is nonreal. Thus the free B-contact
density is positive on the whole interval at P=0, with no energy selected
after the fact.

The integrated free contact resolvent commutes with interchange of the
two constituents, so its one-dimensional antisymmetric B block remains
separate for nearby P. If G_B denotes that free block at the outer radial
boundary and rho_B its density per unit energy, the exact source contact
correction is

\[
\operatorname{Re}(\lambda G_B)=\frac12+\pi\rho_B>\frac12,
\quad
K_B=1-(1-e^{ig})\lambda G_B,
\quad
\rho_B^W=\frac{\rho_B}{|K_B|^2}>0.
\tag{P22}
\]

Indeed `Re[1/(1-exp(ig))]=1/2`, so K_B cannot vanish when rho_B>0.
This is the source law's contact correction, including g; a free-band
density alone would not suffice.

Here the positivity extends to one common nonempty P interval for the
entire compact E interval (P17). To see why, the two free q roots at P=0
stay away from their thresholds by (P19)–(P20), and their eigenvalues stay
away from the flat eigenvalue 1. The implicit function theorem continues
these roots and their nonzero B overlaps in (P,E). The free boundary
resolvent is continuous there: near each simple root, changing from q to
its energy separates the explicit principal-value pole from a continuous
remainder; off these neighborhoods the resolvent integrand is regular.
The other free eigenvalues stay separated for sufficiently small P.
Thus (P22) and the corrected positive density are continuous in a
neighborhood of `{0} x I_E`. Compactness supplies a common p_0>0 and c_0>0
such that

\[
\rho_B^W(P,E-\beta)\ge c_0
\quad (|P|\le p_0,\ E\in I_E).
\tag{P23}
\]

This is an existence bound, not a numerical estimate of p_0 or c_0; p_0
can be further reduced to lie inside any predeclared positive-width
P interval containing zero. Integrating this genuine open interval in
(P5), and retaining all remaining spectral branches, gives

\[
\frac{d\mu_{\alpha,\rm ac}}{dE}(E)
\ge\frac{p_0c_0}{\pi},\qquad
a(E)\ge2p_0c_0>0
\quad\hbox{for almost every }E\in I_E.
\tag{P24}
\]

The Caratheodory boundary is finite almost everywhere, so (P15) is a
nontrivial open two-port relation almost everywhere on the whole original
window. `Re(4+F)>=4` prevents its denominator from vanishing at every such
point. We do not claim finite pointwise boundary values at exceptional
energies, or obtain a bounded inverse of the full token compression.
The causal reconstruction applies without either assertion.

## 5. A relative coherent phase is generated by the source return law

The source does more than provide an abstract complex function. Its first
two nonzero return moments can be obtained exactly by short paths.
Let `V=S M_2` be the free object walk, `u_g=exp(-ig)`, and
`P_0=1_{r=0}` in this section. The singlet coin is unchanged by M_2, so

\[
P_0V\alpha=0,\qquad
P_0V^2\alpha=\frac45\alpha,\qquad
\langle\alpha|VP_0=0.
\tag{P25}
\]

Consequently

\[
\langle\alpha,W^2\alpha\rangle=\frac45u_g,
\quad
\mu_2:=\langle\alpha,T^2\alpha\rangle
=\frac45e^{-i(2\beta+g)}=\frac45.
\tag{P26}
\]

Odd return moments vanish because both physical constituent positions
reverse parity at every object step. To obtain the next moment, first
calculate the free one-constituent return matrix after four steps, with
coin `(I+2iX)/sqrt(5)`. Enumerating the three returning paths for each
fixed final coin gives

\[
K_4=\frac1{25}\begin{pmatrix}8&-14i\\-14i&8\end{pmatrix}.
\tag{P27}
\]

For example, the diagonal path weights are `-4+16-4=8` and the off-diagonal
ones are `-8i-8i+2i=-14i`. Both constituents must return to their original
position. On the antisymmetric coin their product return amplitude is
`det K_4=52/125`.

Between steps zero and four, (P25) leaves only the intermediate contact
at step two in a path that can contribute to the final alpha amplitude.
The final contact contributes u_g. Therefore

\[
\langle\alpha,W^4\alpha\rangle
=u_g\left[\frac{52}{125}+(u_g-1)\frac{16}{25}\right]
=\frac{80u_g^2-28u_g}{125}.
\]

\[
\boxed{\mu_4:=\langle\alpha,T^4\alpha\rangle
=\frac{80-28e^{ig}}{125},\qquad
\operatorname{Im}\mu_4=-\frac{28}{125}\sin g\ne0.}
\tag{P28}
\]

The phase cancellations use the actual source values
`beta=4pi/5=2g`, so `2beta+g=2pi` and `4beta+2g=4pi`.
It follows that the actual contact function starts as

\[
F(z)=1+\frac85z^2+\frac{160-56e^{ig}}{125}z^4+O(z^6).
\tag{P29}
\]

There is an intrinsic relative phase here. A common change of rotating
frame sends `mu_j` to `exp(-ij gamma) mu_j`. Keeping the nonzero mu_2 real
forces `2gamma` to be an integer multiple of pi and hence leaves mu_4
unchanged. It cannot make both return coefficients real.

For the compressed contact memory define

\[
\nu_j=\langle\alpha,[T(I-hP_\alpha)]^jT\alpha\rangle.
\tag{P30}
\]

Then parity and (P26)–(P28) give

\[
\nu_0=\nu_2=0,\qquad \nu_1=\frac45,\qquad
\boxed{\nu_3=\mu_4-h\mu_2^2
=\frac{48-28e^{ig}}{125}.}
\tag{P31}
\]

Write P_free for the full free pulse unitary, including the receiver,
and P_b for the orthogonal projection onto all pulse contact vectors.
In the global block notation `U=[[A,B],[G,D]]` the first two nonzero
return kernels are therefore

\[
\boxed{GAB=-\frac{64}{125}P_{\rm free}P_b,\qquad
GA^3B=\frac{-768+448e^{ig}}{3125}P_{\rm free}P_b.}
\tag{P32}
\]

They first feed an earlier pulse back into the pulse arrangement after
three and five complete macrosteps, respectively. Their relative
coefficient is `(12-7 exp(ig))/25`, which is not real. The law has thus
supplied delayed coherent feedback with a source-fixed relative phase;
no extra phase or instantaneous rotation has been inserted.

This statement is precise about its scope. The source values of g, beta
and the contact rotation remain choices of the candidate law. Equation
(P28) does not derive that contact angle from J, nor does it imply
`Im F^+(E) != 0` at every on-shell energy. Hilbert-transform contributions
can cancel at individual energies. No sign or nonvanishing claim for
`Im F^+(E)` over all of (P17) is needed for the open-port or current result.

## 6. Which current the reduction actually preserves

The identity (P16) is an energy-normalized probability-flux identity for
the active contact channel. The physical half-space charge in the encoded
source sector instead contains

\[
N_R=2\mathbf1_{x_A>\ell}+2\mathbf1_{x_B>\ell}
 +4\mathbf1_{t>\ell}+2\mathbf1_{z>\ell}+N_{R,\rm aux}.
\tag{P33}
\]

Its current is `J_ell=U^dagger N_R U-N_R`, including simultaneous object
and pulse crossings. Neither F alone nor the two scalar port amplitudes
determine that spatially resolved quadratic form. The spectral measure
behind F retains `|alpha(E)|^2`; position-weighted coherences require
matrix elements such as
`<alpha,E_T(dE) N_R E_T(dE') alpha>` as well.

For a reduced solution reconstruct the full token field by the exact
retarded history, including its initial token component, as prescribed in
PROOF_REDUCTION. If R_m denotes that reconstruction together with the
current pulse field, the physical reduced observables are precisely

\[
N_{R,m}^{\rm red}=R_m^\dagger N_R R_m,\qquad
J_{\ell,m}^{\rm red}=R_m^\dagger J_\ell R_m.
\tag{P34}
\]

PROOF_CURRENT derives their explicit history kernels and bilinear
continuity identity. Thus this reduction retains the native 2+2 object
current and the carrier/receiver contributions, including all mixed
history terms; a bare norm-unitary S_F would not establish that result.
Stationary radiation formulas are paired with finite-energy packets or
regulated spatial windows before taking limits. No subtraction of two
divergent half-space norms is used.

There is also a genuine dynamically reducing sector: take the direct sum
of all token cyclic spaces (P9) and the full pulse space. The remaining
token space is T-reducing and contact-dark. If the initial state is
declared to lie in the coupled sector, compress N_R and J_ell to that
sector to obtain the correct observables. For general initial states the
dark token component must still be reconstructed. Spatial charge need
not respect the cyclic/dark decomposition; PROOF_CURRENT gives an
explicit pair with identical pulse histories but distinct native current
because of a dark-state coherence. Omitting it is not a current-preserving
reduction.

Equations (P7), (P15), (P24) and (P32) are the new source-derived contact
objects. Combined with (P34) they provide a retarded open-channel reduction
with its actual physical current. They do not produce a finite local
Lorentz transfer, a new contact-angle derivation, or an intertwiner with
the entire Hodge action and form.

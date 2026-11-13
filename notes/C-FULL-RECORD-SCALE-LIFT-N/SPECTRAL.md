# Full-circle spectrum and the locality boundary of the selected energy

**Status:** NON-CANONICAL, L1, candidate-T.

**Owner:** A. M. Thorn, session `C-FULL-RECORD-SCALE-LIFT-N`.

**Claim:** [#1771](https://github.com/mathorn1973/twist-j/issues/1771).

**Method:** self-contained analytical derivation and same-session analytical
review. No scientific executable was run for the results in this file.
Independent external acceptance and public promotion are not asserted.

## 1. Scope and pinned premises

This file concerns exactly the one-pair, one-carrier, one-receiver model of
`HOMOGENEOUS-CAPTURE-CURRENT-RECORD` in
[Public Canon v105 at its activation commit](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
The object logarithm is the nominated reading in
`CONTACT-W-SPECTRAL-READING` in the same pinned Canon. Its content commit is
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`; the Canon has 1,295,029 bytes and
SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.

The inherited working attachment, `twist_full_record_bridge/PROOF.md`,
SHA-256
`e9ac1a0dbc4b29eb7551584fc0af1a160985ce926bfdd79ef3a7b588878a80c2`,
states the full-circle and safe-window energy arguments. They are proved
below, together with the stronger locality obstruction. The arithmetic
scaling of the complete step is not a premise of this file.

The occupation coordinates, synchronized schedule, amplitudes, contacts,
receiver and spectral preparations remain supplied construction data.
Nothing here derives them from the original six-pentit update. The
configuration-distance condition defined below is explicit; it is not a
classification of every possible physical locality condition or every
Hamiltonian whose exponential is the same discrete step.

Identity factors on labels, occupied memory and admitted auxiliaries or
references are understood. For kernel statements one may fix an arbitrary
auxiliary/reference vector; the remaining internal dimensions are finite.

Put

\[
 a=\arctan 2,\qquad a_p=2a,\qquad b_p=\pi-a_p,
 \qquad \beta=4\pi/5,\qquad g=2\pi/5.
\]

In the object coin order \((++,+-,-+,--)\), define

\[
 M_2=\frac{(I+2iX)\otimes(I+2iX)}5,\qquad
 S(P,q)=\operatorname{diag}(e^{iP},e^{iq},e^{-iq},e^{-iP}),
 \qquad W_f=SM_2.
\]

The interacting object step is \(W=\Gamma W_f\), where
\(\Gamma=I+(e^{-ig}-1)P_0\) and \(P_0\) projects onto \(r=0\).
The pulse factors and their product are

\[
 Q=\frac1{\sqrt5}\begin{pmatrix}1&-2\\2&1\end{pmatrix},\qquad
 E(k)=\frac1{\sqrt5}
 \begin{pmatrix}1&-2e^{ik}\\2e^{-ik}&1\end{pmatrix},
 \qquad V(k)=E(k)Q.
\]

The reference step, the contact step and the receiver-calibrated step are

\[
 U_0=(e^{-i\beta}W\otimes I_{\rm tok})
       \oplus(e^{-i\beta}W\otimes V),\qquad
 U=U_0C,\qquad
 U_{\rm rec}=\mathcal T(U\otimes I_{\rm mem})\mathcal T^*.
\]

Here \(C\) is the identity except on the two contact ports at
\(r=0, R=c\), with \(c=y\) for a token and \(c=x\) for a pulse.
On each port pair it has matrix
\(\left(\begin{smallmatrix}3/5&-4/5\\4/5&3/5\end{smallmatrix}\right)\).
The half-line permutation \(\mathcal T\) exchanges carrier and memory
labels exactly when the carrier is at or to the right of \(z=100\).
These are the unchanged operators of the pinned Canon.

All steps have finite propagation in the configuration coordinates
\((R,r,c)\), with finite internal dimension. The completely free reference
used below is

\[
 U_f=e^{-i\beta}
     \bigl((W_f\otimes I_{\rm tok})\oplus(W_f\otimes V)\bigr).
\]

## 2. Full circle, including essential spectrum

**Proposition 1.** For the specified complete step,

\[
 \boxed{\sigma_{\rm ess}(U_{\rm rec})
       =\sigma(U_{\rm rec})=\mathbb T.}
\]

**Proof.** Factor the free object symbol using
\(k_1=(P+q)/2\), \(k_2=(P-q)/2\). The one-copy matrix

\[
 U_1(k)=e^{ikZ}(I+2iX)/\sqrt5
\]

has eigenvalues \(e^{\pm i\theta(k)}\), where
\(\cos\theta(k)=\cos k/\sqrt5\). Consequently
\(\theta(k)\) traverses \([a,\pi-a]\), and differences of the two
one-copy angles fill \([-b_p,b_p]\). The map
\((k_1,k_2)\mapsto(P,q)=(k_1+k_2,k_1-k_2)\) is onto the momentum
torus; the simultaneous sign change in the two one-copy matrices under
its twofold ambiguity leaves their tensor product unchanged.

The pulse eigenvalues are \(e^{\mp i\varepsilon(k)}\), with

\[
 \cos\varepsilon(k)=\frac{1-4\cos k}{5},\qquad
 \varepsilon(k)\in[0,a_p].
\]

Using the energy-angle convention \(e^{-iE}\), the pulse arrangement of
\(U_f\) therefore contains all angles in

\[
 \beta+[-b_p,b_p]+[-a_p,a_p]=\beta+[-\pi,\pi].
\]

This interval covers the full circle. For any \(\lambda\in\mathbb T\),
choose momenta and a normalized internal eigenvector of the finite free
Fourier matrix with eigenvalue \(\lambda\). Multiply the corresponding
plane wave by the indicator of a cube with side \(2N+1\), and normalize.
Translate the cube so that its center has \(r=4N\) and \(x=-4N\).
For sufficiently large \(N\), the support and its fixed-width one-step
neighborhood avoid \(r=0\) and lie left of the receiver. Thus
\(\Gamma\), \(C\) and both receiver calibrations act trivially on the
relevant support, and the actual step agrees with \(U_f\) there.

Finite propagation puts the approximate-eigenvector residual in a boundary
layer with \(O(N^2)\) sites. Normalization uses \(O(N^3)\) sites.
Hence the residual norm is \(O(N^{-1/2})\) and tends to zero. The
supports escape every finite set, so the normalized vectors also converge
weakly to zero. They form a singular Weyl sequence for the normal operator
\(U_{\rm rec}\). Every \(\lambda\in\mathbb T\) belongs to its
essential spectrum. Unitarity supplies the reverse inclusion. QED.

The proposition excludes a spectral gap for a single analytic branch of
the logarithm on a neighborhood of the complete spectrum. Full-circle
spectrum alone does not exclude a spatially local logarithm with additional
energy-branch information.

## 3. The nominated positive Borel energy and its safe channel

Fix the scalar Borel function

\[
 f:\mathbb T\longrightarrow[0,2\pi),\qquad
 e^{-if(z)}=z,\qquad f(1)=0,
\]

and define \(H_*=f(U_{\rm rec})\). Its only discontinuity is at \(1\).

**Proposition 2.** The nominated reading obeys

\[
 0\le H_*\le2\pi I,\qquad e^{-iH_*}=U_{\rm rec},\qquad
 \sigma(H_*)=[0,2\pi],
\]

and \(U_{\rm rec}^*F(H_*)U_{\rm rec}=F(H_*)\) for every bounded
Borel \(F\).

**Proof.** The operator identities follow directly from the spectral
theorem and the scalar identities. Every open subinterval of \((0,2\pi)\)
corresponds under \(E\mapsto e^{-iE}\) to a nonempty open arc. Proposition
1 implies that its spectral projection for \(U_{\rm rec}\) is nonzero.
Thus every interior energy belongs to \(\sigma(H_*)\), and both endpoints
belong by closure. In particular \(2\pi\) is a spectral limit even though
the scalar function takes values strictly below \(2\pi\). QED.

For comparison with the Canon, let

\[
 \alpha=3\pi/10,\qquad H_W=i\operatorname{Log}_\alpha(W),\qquad
 H_E=\beta+i\operatorname{Log}_\pi(V),
\]
\[
 H_0=(H_W+\beta)\otimes I_{\rm tok}
      \ \oplus\ (H_W\otimes I+I\otimes H_E).
\]

All identities on memory and labels are now included in the notation
\(H_0\) and \(U_0\). The branch \(\operatorname{Log}_\alpha\) has
argument in \((\alpha-2\pi,\alpha)\). The pinned Canon proves its
spectral gap and

\[
 \sigma(H_0)\subset
 [\pi/2-a_p,\,5\pi/2+a_p],\qquad e^{-iH_0}=U_0.
\]

Let \(P_{{\rm ch},0}\) be the Canon's direct-integral channel projection,
and define

\[
 J_{\rm safe}=(5\pi/4,7\pi/4),\qquad
 P_{\rm safe}=1_{J_{\rm safe}}(H_0)P_{{\rm ch},0}.
\]

The projections commute. The calibrated wave operators in the pinned Canon
intertwine \(U_0\) and \(U_{\rm rec}\). Intertwining bounded Borel
functions therefore gives the exact identity

\[
 \boxed{H_*\Omega_{{\rm rec},\pm}P_{\rm safe}
       =\Omega_{{\rm rec},\pm}H_0P_{\rm safe}.}
\]

Indeed \(f(e^{-iE})=E\) on \(J_{\rm safe}\subset(0,2\pi)\).
The stronger absence of a \(2\pi\)-translated representative in the
displayed enclosing spectrum is the Canon's unaliased energy condition.
The identity is preserved by all subsequent integer steps.

The difference \(H_*-H_0\) satisfies the elementary operator bounds

\[
 -(5\pi/2+a_p)I\le H_*-H_0\le(3\pi/2+a_p)I.
\]

For every \(\psi\in\operatorname{Ran}P_{\rm safe}\), wave asymptotics
also give

\[
 \|(H_*-H_0)U_{\rm rec}^{\,n}
       \Omega_{{\rm rec},\pm}\psi\|\longrightarrow0
       \quad(n\longrightarrow\pm\infty).
\]

To see this, apply the defining wave asymptotics to both \(\psi\) and
\(H_0\psi\), use the boxed identity, and subtract
\(H_0U_0^n\psi=U_0^nH_0\psi\). Boundedness of \(H_0\) controls the
remaining difference. This is a statement for each admitted safe-channel
state, not a uniform spatial locality estimate.

Multiplication by a specified \(E_0>0\) supplies the conserved reading
\(E_0H_*\). Its existence does not select \(E_0\), establish a physical
energy interpretation or pay for integer-register precision.

## 4. A strong-limit lemma for the fixed Borel branch

The locality proof requires more than polynomial functional calculus.
The following lemma states the exact additional condition.

**Lemma 3.** Suppose unitary \(V_N\) and their adjoints converge strongly
to unitary \(V\) and its adjoint. If the spectral projection of \(V\)
at \(1\) is zero, then

\[
 f(V_N)\longrightarrow f(V)\quad\hbox{strongly}.
\]

**Proof.** Continuous functions on the circle are uniformly approximable
by Laurent polynomials. The hypotheses therefore give strong convergence
for their functional calculi. For a small arc \(A_\delta\) about \(1\),
choose a continuous \(g_\delta\) with \(0\le g_\delta\le2\pi\) that
equals \(f\) outside \(A_\delta\). Choose a continuous
\(0\le h_\delta\le1\) equal to one on \(A_\delta\), supported in
a slightly larger arc shrinking to \(1\). Then, for each vector \(v\),

\[
 \|(f-g_\delta)(V_N)v\|^2
 \le(2\pi)^2\langle v,h_\delta(V_N)v\rangle.
\]

The right side converges to the expression with \(V\). That expression
tends to zero as \(\delta\downarrow0\), because \(V\) has no spectral
atom at \(1\). The same bound controls \((f-g_\delta)(V)v\).
The triangle inequality, with the continuous middle term
\((g_\delta(V_N)-g_\delta(V))v\), proves the claim by first taking
\(N\to\infty\) and then \(\delta\downarrow0\). QED.

## 5. The translated free limit has no atom at the cut

Let \(S_N\) be the unitary translation, in both arrangements,

\[
 (R,r,c)\longmapsto(R,r+N,c-N).
\]

Finite support and finite propagation show

\[
 S_N^*U_{\rm rec}S_N\longrightarrow U_f,
 \qquad S_N^*U_{\rm rec}^*S_N\longrightarrow U_f^*
 \quad\hbox{strongly}.
\]

For each fixed finite support, the translated interaction and contact planes
eventually miss its required neighborhood, and the translated receiver
calibration is the identity there. Uniform boundedness extends convergence
from finite support to the entire Hilbert space.

**Lemma 4.** The spectral projection of \(U_f\) at \(1\) is zero in
both the token and pulse arrangements.

**Proof.** Each Fourier matrix has Laurent-polynomial entries. The
determinant after subtraction of the identity is not identically zero.
For the pulse arrangement evaluate at \(P=q=0\), \(k=\pi\). Then
\(W_f=M_2\) and \(V(\pi)=I\); the eigenvalues are

\[
 e^{-i\beta}\{e^{ia_p},1,1,e^{-ia_p}\}.
\]

None equals one. Here \(0<a_p<3\pi/4<\beta<\pi\);
\(a_p<3\pi/4\) follows from
\(2<\tan(3\pi/8)=1+\sqrt2\). The token arrangement has the identical
test at \(P=q=0\), without a pulse momentum. Identity label and memory
factors only repeat these eigenvalues different from one at the test point.

A nonzero Laurent polynomial has a Haar-null zero set on a finite torus.
For completeness, multiply by a monomial and induct on the number of
variables. Outside the null set where a chosen nonzero coefficient
polynomial vanishes, the resulting polynomial in the last variable is
nonzero and has finitely many zeros. Fubini's theorem completes the
induction. Thus eigenvalue one occurs only on a Haar-null set of momenta.
The multiplication operators have no nonzero vector supported there, so
their spectral projections at one vanish. The direct sum, and any
identity extension to a reference, retain this property. QED.

Lemmas 3 and 4 now yield

\[
 \boxed{S_N^*H_*S_N\longrightarrow f(U_f)
        \quad\hbox{strongly}.}                         \tag{S1}
\]

## 6. A uniform exponential configuration bound is impossible

The precise locality condition tested here is the existence of constants
\(C,\mu>0\), independent of position and internal indices, such that
the pulse-to-pulse kernel obeys

\[
 \left|\langle R,r,x,\eta|H_*|R',r',x',\eta'\rangle\right|
 \le C\exp\bigl(-\mu(|R-R'|+|r-r'|+|x-x'|)\bigr).       \tag{S2}
\]

The indices \(\eta,\eta'\) include the object coin, pulse bank, carrier
label and memory label. In particular a uniform finite-range bounded
operator satisfies (S2), with suitable constants. The stronger uniform
off-support norm estimate used for the object logarithm in the Canon
would also imply (S2).

**Proposition 5.** The nominated operator \(H_*\) does not satisfy
(S2). In particular it is not finite-range in the configuration lattice.

**Proof.** If (S2) held, the translations in (S1) would preserve its
constants, and entrywise limits would transfer it to \(f(U_f)\).
The pulse block of the latter is translation invariant. Exponential
summability of its matrix kernel on \(\mathbb Z^3\) would make its
matrix-valued Fourier series absolutely and uniformly convergent. Its
Fourier symbol would have a continuous representative.

There is an explicit obstruction to such a representative. At
\((P,q)=(\pi,\pi)\), streaming is \(-I\), so \(W_f=-M_2\).
The eigenvalue \(-e^{-ia_p}=e^{ib_p}\) is simple. Its object eigenenergy
for the nominated object branch is \(-b_p\).

Here \(b_p<\alpha=3\pi/10\), as required for that branch. An exact
verification is the Canon's gap inequality: put
\(\delta=\pi-2b_p\). Then \(\cos\delta=7/25\), whereas
\(\cos g=(\sqrt5-1)/4>7/25\), since \(3125>2809\).
Both angles lie in \((0,\pi)\), so \(\delta>g=2\pi/5\) and
\(b_p<3\pi/10\).

Combine a smooth eigenvector for this simple object eigenvalue with the
smooth pulse eigenvector having eigenvalue \(e^{+i\varepsilon(k)}\).
The product has energy angle

\[
 E(k)=\beta-b_p-\varepsilon(k).
\]

Since

\[
 \beta-b_p=a_p-\pi/5\in(0,a_p),
\]

there is a \(k_0\in(0,\pi)\) at which \(E(k_0)=0\).
The crossing is transverse because

\[
 \varepsilon'(k)=-\frac{4\sin k}{5\sin\varepsilon(k)}\ne0
 \quad\hbox{at } k_0.
\]

Expectation of the Fourier symbol of \(f(U_f)\) in this smooth tensor
eigenvector is \(f(e^{-iE(k)})\). Its limits from the positive and
negative sides of \(E=0\) are, respectively, zero and \(2\pi\).
The object eigenvalue remains simple in a neighborhood of
\((\pi,\pi)\), and the transverse crossing persists there. On the two
open sides, a continuous representative would have the continuous scalar
expectations \(E\) and \(E+2\pi\), since it agrees with them almost
everywhere. Their incompatible limits at the separating surface give a
contradiction. Altering a symbol on a null set cannot repair this jump.
QED.

This is an obstruction for the fixed scalar reading in \([0,2\pi)\).
It does not show that every self-adjoint logarithm of \(U_{\rm rec}\)
fails (S2). It also does not replace the declared physical locality
question by a classification of configuration kernels. A different
generator carrying information about aliased energy branches remains an
independent construction problem.

## 7. The energy difference does not uniformly vanish away from contact

Let the completely free additive generator be

\[
 H_{W,f}=i\operatorname{Log}_\alpha(W_f),\qquad
 H_{f,0}=(H_{W,f}+\beta)\otimes I_{\rm tok}
       \ \oplus\ (H_{W,f}\otimes I+I\otimes H_E).
\]

The object spectra of \(W\) and \(W_f\) have a common gap about the
chosen cut. A continuous function on the circle can therefore agree with
\(i\operatorname{Log}_\alpha\) on both spectra. Continuous functional
calculus for the translated object steps gives

\[
 S_N^*H_0S_N\longrightarrow H_{f,0}\quad\hbox{strongly}.   \tag{S3}
\]

**Proposition 6.** There are normalized states \(\psi\) such that

\[
 \boxed{\lim_{N\to\infty}
        \|(H_*-H_0)S_N\psi\|=2\pi.}                  \tag{S4}
\]

Thus the full difference from \(H_0\) does not uniformly disappear
under these translations away from the object contact and receiver.

**Proof.** On the branch in Proposition 5, the minimum of the free
additive energy is

\[
 \beta-b_p-a_p=\beta-\pi=-\pi/5.
\]

Choose an open interval \(I\) with closure in \((-\pi/5,0)\), for
example \(I=(-\pi/10,-\pi/20)\). The free additive spectral projection
\(1_I(H_{f,0})\) is nonzero: the smooth band just displayed takes
values in this interval on an open set of momenta. For every normalized
\(\psi\) in that spectral subspace,

\[
 (f(U_f)-H_{f,0})\psi=2\pi\psi,
\]

because \(U_f=e^{-iH_{f,0}}\) and \(f(e^{-iE})=E+2\pi\) on \(I\).
Subtract (S3) from (S1) and apply the strong limit to \(\psi\).
Unitary invariance of the norm gives (S4). QED.

For the dimensional difference \(E_0(H_*-H_0)\), the limit is
\(2\pi E_0\).
The surviving difference is an energy-branch shift, present even in the
translated free limit. It is not caused by residual encounter with the
receiver or the contact. Proposition 6 is compatible with the statewise
safe-window scattering limit in Section 3: the states used in (S4) occupy
a different, explicitly negative additive-energy interval.

## 8. What is established and what remains open

The complete step has full essential circle spectrum. The fixed positive
Borel reading is a conserved bounded logarithm and agrees exactly with the
declared additive energy on the calibrated safe channel. For this same
reading, a uniform exponential configuration-kernel bound is impossible,
and its difference from the additive reference energy need not disappear
far from the contact.

No theorem here excludes another local generator for the complete step,
selects a physical energy or unit, supplies a local current of this
spectral energy, derives the supplied geometry and gates from the original
checkpoint dynamics, or accounts for preparation, clocks, reset or integer
precision. Those questions retain their distinct scopes.

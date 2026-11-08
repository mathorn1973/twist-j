# Active-contact calibration under the same complete step

**PUBLIC / NON-CANONICAL / L1.** Analytical candidate under
[reservation #1775](https://github.com/mathorn1973/twist-j/issues/1775).
This note is a hand derivation. It supplies no scientific executable run,
formal computational reproduction, independent external acceptance or
Canon promotion. Author: A. M. Thorn. Apache-2.0.

The operator is exactly the Public Canon v105
[HOMOGENEOUS-CAPTURE-CURRENT-RECORD](https://github.com/mathorn1973/twist-j/blob/b8cdfd6ea58ae798545bc6000c817147fa0f0dcc/canon/CANON.md#homogeneous-capture-current-record-t)
model, content pin `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`, activated
tag target `892a0b11089d34e241e1eb76d2c03247022d18e6`.
This is a second calibration of the law used in
[EXPERIMENT.md](EXPERIMENT.md). It activates the actual token/pulse
contact. It uses different source states and does not inherit the
primary experiment's equal-spectral-distribution conclusion.

## 1. Fixed ports, preparation and old memory

Use \(\zeta=e^{2\pi i/5}\), \(\beta=4\pi/5\), and the Canon object
coins

\[
 A=(e_1-e_4)/\sqrt2,\qquad B=(e_2-e_3)/\sqrt2,
 \qquad (e_1,e_2,e_3,e_4)=(++,+-,-+,--).
\]

Freeze the two contact ports at \(99\), with carrier label zero:

\[
 \alpha=|R=99,r=0,iB;\ y=99,t_0\rangle,
 \qquad
 \gamma=|R=99,r=0,A;\ x=99,1,p_0\rangle.
 \tag{1}
\]

They are orthonormal because token and pulse are orthogonal arrangements.
The admitted source input is

\[
 |\psi\rangle=u\alpha+v\gamma,
 \qquad |u|^2+|v|^2=1.
 \tag{2}
\]

It is initially a product with the same arbitrary occupied-memory and
reference state

\[
 |\mu\rangle_{D\mathsf R}
 =\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle,
 \qquad \sum_j\|\phi_j\|^2=1.
 \tag{3}
\]

The receiver is at \(z=100\). Its ready subspace is
\(K=\operatorname{span}\{d_1,\ldots,d_{25}\}\), and \(d_0\) is the
reserved new-write flag. The reference vectors need not be orthogonal;
mixed inputs are included by purification. No old memory or reference
information is reset during preparation.

The fixed phase comparison is

\[
 u=3/5,\qquad v=4\eta/5,\qquad \eta\in\{+1,-1\}.
 \tag{4}
\]

These two inputs have the same token/pulse populations \(9/25,16/25\)
and the same basis configuration probabilities. The variable is their
relative coherent phase. This is an admitted coherent preparation of
two different arrangements; it is not a token-only source. In the
configuration basis its four nonzero raw coefficients can be written

\[
 (3i,-3i,4\eta,-4\eta)
\]

with one common normalization \(\sqrt{50}\). Preparation of this
superposition is a supplied source resource, not an operation derived
from the original six-pentit TWIST update.

## 2. Complete one-step derivation

The unchanged contact acts as

\[
 C\begin{pmatrix}u\\v\end{pmatrix}
 =\begin{pmatrix}a_C\\b_C\end{pmatrix},\qquad
 C=\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix},
 \quad
 a_C=\frac{3u-4v}{5},\quad b_C=\frac{4u+3v}{5}.
 \tag{5}
\]

The Canon order is \(U=U_0C\), with
\(U_0=\zeta^{-2}(W\otimes I_{\rm tok}\oplus W\otimes V)\).
It is essential to apply (5) before object and pulse streaming.

The object coin is

\[
 M_2=\frac15\left[I+2i(X\otimes I+I\otimes X)-4X\otimes X\right].
\]

Both \(A\) and \(B\) are annihilated by
\(X\otimes I+I\otimes X\) and have eigenvalue \(-1\) under
\(X\otimes X\). Thus \(M_2A=A\) and \(M_2(iB)=iB\).
The prescribed streaming and the phase \(\Gamma\) at \(r=0\) give
the normalized outgoing object states

\[
 A_{\rm out}=\frac{\zeta^{-1}}{\sqrt2}
 \left(|R=98,r=0,e_1\rangle-|R=100,r=0,e_4\rangle\right),
\]
\[
 B_{\rm out}=\frac{i}{\sqrt2}
 \left(|R=99,r=-1,e_2\rangle-|R=99,r=1,e_3\rangle\right).
 \tag{6}
\]

The first vector samples \(\Gamma\); the second does not. Keeping
these phases is necessary for the spectral check in Section 5.

For a pulse starting at \((99,1)\), the unchanged pulse operator gives

\[
 |99,1\rangle\longmapsto
 \frac{-4|98,1\rangle+|99,1\rangle+2|99,2\rangle+2|100,2\rangle}{5}.
 \tag{7}
\]

Put
\(\widetilde\mu=\sum_{j=1}^{25}|p_j\rangle|d_0\rangle|\phi_j\rangle\).
The complete one-step state, including the common phase, is

\[
\begin{aligned}
 U_{\rm rec}(|\psi\rangle|\mu\rangle)=\zeta^{-2}\Bigg[\;&
 a_C|B_{\rm out};y=99,t_0\rangle|\mu\rangle\\
 &+\frac{b_C}{5}|A_{\rm out}\rangle
   \bigl(-4|98,1\rangle+|99,1\rangle+2|99,2\rangle\bigr)
   |p_0\rangle|\mu\rangle\\
 &+\frac{2b_C}{5}|A_{\rm out}\rangle|100,2\rangle
   |\widetilde\mu\rangle\Bigg].
\end{aligned}
 \tag{8}
\]

All branches are specified. Their total norm is
\(|a_C|^2+|b_C|^2(16+1+4+4)/25=1\).
The last branch transfers the complete unknown old memory/reference
state to pulse labels/reference and leaves the receiver in \(d_0\).
The other branches preserve the old state in the receiver.

Reading \(P_W=|d_0\rangle\langle d_0|\), with its complementary
projector retained, gives

\[
 t_W=\frac{2b_C}{5}=\frac{8u+6v}{25},\qquad
 \boxed{p_W=\frac{|8u+6v|^2}{625}}.
 \tag{9}
\]

The source effect on \(\operatorname{span}\{\alpha,\gamma\}\) is

\[
 E_W=\frac1{625}\begin{pmatrix}64&48\\48&36\end{pmatrix}.
 \tag{10}
\]

It has rank one and largest eigenvalue \(100/625=4/25\).
This is the same declared local instrument as in the primary experiment;
its occurrence and Born interpretation are not derived from the unitary.

## 3. Dark and bright settings, with a contact control

For \(u=3/5,v=4\eta/5\), direct substitution gives

\[
 a_C=\frac{9-16\eta}{25},\qquad
 b_C=\frac{12(1+\eta)}{25},\qquad
 t_W=\frac{24(1+\eta)}{125},
\]
\[
 \boxed{p_W=\frac{1152(1+\operatorname{Re}\eta)}{15625}}.
 \tag{11}
\]

| Input phase | Token amplitude after \(C\) | Pulse amplitude after \(C\) | Receiver write probability |
|---|---:|---:|---:|
| \(\eta=+1\) | \(-7/25\) | \(24/25\) | \(2304/15625\) |
| \(\eta=-1\) | \(1\) | \(0\) | \(0\) |

At the negative phase the input is exactly \(C^*\alpha\); the contact
outputs a pure standing token. At the positive phase its pulse probability
is \(576/625\). The object and carrier labels and the old receiver state
are the same across the comparison.

The negative setting is dark only for this first conversion and reading,
not an invariant dark sector: the object return amplitude
\(\langle99,0,iB|W^2|99,0,iB\rangle=4\zeta^{-1}/5\)
allows the standing token to reach an active contact port again and
convert on a later step.

As a mathematical control on which factor causes the contrast, omitting
\(C\) would leave the token/pulse alternatives orthogonal and give

\[
 p_W^{\text{without }C}=\frac4{25}|v|^2=\frac{64}{625}
\]

for both phases. This counterfactual is not a second implemented law in
the experiment. It identifies the role of the actual \(C\): relative
token/pulse phase changes conversion, and the unchanged pulse transport
and receiver exchange convert that difference into the local record.

The chosen phase pair has an exactly dark setting. It is not the pair
of largest contrast over all fixed source populations. Equal populations
\(u=1/\sqrt2,v=\eta/\sqrt2\) give
\(p_W=(50+48\operatorname{Re}\eta)/625\), whose contrast is
\(96/625\). No optimum claim is attached to the \(3{:}4\) pair.

## 4. Reference preservation and continuation

After a written outcome in (8), the pulse is at \((100,2)\).
On the next step it is orthogonal to the contact pulse port, which uses
bank 1; hence \(C\) is inactive on this conditional input. The object
may still evolve under its full \(W\). The pulse evolution is exactly

\[
 |100,2\rangle\longmapsto
 \frac{-2|99,1\rangle-2|100,1\rangle+|100,2\rangle-4|101,2\rangle}{5}.
\]

Whenever the first write has nonzero probability, the next receiver
reading consequently obeys

\[
 P(W\mid W)=21/25,\qquad P(N\mid W)=4/25.
 \tag{12}
\]

The returning branch restores the old memory/reference state to the
receiver, and sets the pulse label back to \(p_0\). The surviving
branches retain the old information in pulse labels/reference. These
are conditional continuation statements for the declared two-reading
protocol; they do not replace an uninterrupted two-step evolution by
a classical mixture.

The finite-buffer retention and reverse-leakage boundary were already
proved in the distinct
[#1741 finite protocol](https://github.com/mathorn1973/twist-j/issues/1741#issuecomment-6385322783).
No permanent record or reset follows here. The exact 25-dimensional
ready-space capacity and the full-26-dimensional perfect-flag obstruction
are proved in [EXPERIMENT.md](EXPERIMENT.md#6-inverse-arbitrary-reference-closure-and-exact-flag-capacity)
and apply unchanged.

## 5. Exact spectral distinction of the two contact inputs

Both preparations are normalized and have active occupation charge 10.
Their full \(U_{\rm rec}\) spectral distributions are nevertheless
different. The following second-moment calculation is an exact witness.

Let \(P\) project onto the two initial ports (1), tensored with the
identity on memory/reference. Initial and tested final carrier positions
are both 99. Thus \(\mathcal T P=P\), and

\[
 P U_{\rm rec}^{\,2}P=P(U^2\otimes I_D)P.
 \tag{13}
\]

The two-step free return amplitudes of the object are

\[
 \langle 99,0,iB|W^2|99,0,iB\rangle=4\zeta^{-1}/5,
\]
\[
 \langle 99,0,A|W^2|99,0,A\rangle=4\zeta^{-2}/5.
 \tag{14}
\]

For the first, the paths through relative positions \(-1,+1\) return
through the opposite coin with coefficient \(-4/5\); the minus sign
in \(B\) changes this to \(+4/5\), and only the final contact phase
is sampled. For the second, the analogous returns through object centers
98 and 100 also give \(+4/5\), and both contact phases are sampled.
The pulse bank-1 on-site two-step return is

\[
 \langle99,1|V^2|99,1\rangle=-7/25.
 \tag{15}
\]

There is no missing return contribution from the intervening \(C\).
After a first free step from \(\alpha\), the object has \(r=\pm1\),
so no contact acts. After a first free step from \(\gamma\), the only
component overlapping a contact pulse port is at \(R=x=98,r=0\),
bank 1. Its contact-generated token stays at \(y=98\), so cannot return
to \(\alpha\) at \(y=99\). Its changed pulse component is again bank
1 at 98; one pulse step cannot move right into bank 1, so cannot return
to \(\gamma\) at \((99,1)\). The component at \(R=x=100\) has pulse
bank 2 and is orthogonal to the contact port. These exhaust the possible
intervening contact corrections.

Including the two common phases \(\zeta^{-4}\), equations (14)--(15)
therefore give, in the ordered initial basis \((\alpha,\gamma)\),

\[
 \boxed{
 P U_{\rm rec}^{\,2}P
 =\begin{pmatrix}4/5&0\\0&-28\zeta^{-1}/125\end{pmatrix}
   \frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix}
   \otimes I_{D\mathsf R}.}
 \tag{16}
\]

With \(\psi_\pm=(3\alpha\pm4\gamma)/5\), this yields

\[
 \boxed{\langle\psi_-,U_{\rm rec}^{\,2}\psi_-\rangle=12/25},
\]
\[
 \boxed{\langle\psi_+,U_{\rm rec}^{\,2}\psi_+\rangle
       =-84/625-2688\zeta^{-1}/15625.}
 \tag{17}
\]

The same values hold for every normalized old memory/reference state.
They are unequal, so the two full spectral distributions cannot coincide.
This proves that the equal-spectrum argument for the primary odd-pulse
family must not be transferred to this contact family. Equality of any
particular mean Hamiltonian reading would require its own proof; neither
equality nor inequality of that mean is inferred solely from (17).

## 6. Arithmetic and physical scope

The two frozen source vectors have finite coefficients in
\(\mathbb Z[\zeta_{20}]\) with the one common normalization
\(\sqrt{50}\). Their subsequent evolution is the inherited single
\(\mathcal A=25U_{\rm rec}\) recurrence, as in
[#1741](https://github.com/mathorn1973/twist-j/issues/1741) and
[#1771](https://github.com/mathorn1973/twist-j/issues/1771).
There is no extra phase operation between macrosteps and no normalization
of separate physical branches. Arbitrary old-memory/reference amplitudes
are included as an identity-tensored operator statement, not asserted to
have finite integer descriptions.

This calibration establishes exact finite contact interference, pulse
transport, and coherent occupied-memory exchange, with a local reading
and its complementary branch explicitly declared. The initial object is
already at contact, and the input includes a coherent pulse component.
No incoming scattering preparation is constructed and no bound-state
projector is tested. Hence it proves neither incoming-unbound-to-bound
capture nor the finite realization of the Canon's asymptotic joint
capture event. Geometry, coherent source preparation, the receiver
reading and its occurrence remain admitted resources of this model.

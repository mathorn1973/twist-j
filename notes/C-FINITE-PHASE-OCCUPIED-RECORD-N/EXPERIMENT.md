# Exact finite phase-to-occupied-record experiment

**PUBLIC / NON-CANONICAL / L1.** Analytical candidate under
[reservation #1775](https://github.com/mathorn1973/twist-j/issues/1775).
This is a self-contained hand derivation, not a scientific executable run,
a formal computational reproduction, independent external acceptance or a
Canon promotion. Author: A. M. Thorn. Apache-2.0.

The source operator is the unchanged Public Canon v105 model
[HOMOGENEOUS-CAPTURE-CURRENT-RECORD](https://github.com/mathorn1973/twist-j/blob/b8cdfd6ea58ae798545bc6000c817147fa0f0dcc/canon/CANON.md#homogeneous-capture-current-record-t).
The content pin is `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`; its activated
tag target is `892a0b11089d34e241e1eb76d2c03247022d18e6`.
The occupied-memory exchange was already present in
[#1619](https://github.com/mathorn1973/twist-j/pull/1619). This note derives
a finite phase-controlled input/output instrument for that law.

## 1. Fixed input, complete nominal preparation and fixed law

Write \(\zeta=e^{2\pi i/5}\), \(\beta=4\pi/5\), and let
\(e_1,e_2,e_3,e_4\) denote the ordered object coins
\((++,+-,-+,--)\). Freeze

\[
 o_+=|R=0,r=3,e_1\rangle,\qquad
 o_-=|R=0,r=-3,e_1\rangle,\qquad
 \chi_-=(o_+-o_-)/\sqrt2.
\]

The carrier is a pulse at \(x=99\), label \(p_0\), and the receiver is
at \(z=100\). For \(\eta=e^{i\theta}\), set

\[
 v_\theta=(|1\rangle+\eta|2\rangle)/\sqrt2.
\]

The two frozen comparisons are \(\theta=0,\pi\), denoted \(+,-\).
They have the same initial configuration probabilities and differ only
in the relative pulse-bank phase. In particular, neither preparation
places the receiver in its write-flag state.

The receiver/reference input is arbitrary in the declared proper subspace

\[
 K=\operatorname{span}\{d_1,\ldots,d_{25}\},\qquad
 |\mu\rangle_{D\mathsf R}
 =\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle,
 \qquad \sum_j\|\phi_j\|^2=1.
\]

The vectors \(\phi_j\) need not be orthogonal. An arbitrary mixed input
on \(K\otimes\mathsf R\) is included by purification, with the purifying
factor retained as part of \(\mathsf R\). The source preparation is
initially a product with this same unknown old memory/reference state:

\[
 |\Psi_\theta(0)\rangle
 =\chi_-\otimes|99,v_\theta,p_0\rangle\otimes|\mu\rangle.
 \tag{1}
\]

A complete finite *nominal loader* for the known source factor can be
specified explicitly. On the four-dimensional space
\(\operatorname{span}\{o_+,o_-\}\otimes
\operatorname{span}\{|99,1,p_0\rangle,|99,2,p_0\rangle\}\), use the
single joint block

\[
 G_\theta=H_o\otimes H_\theta,\qquad
 H_o=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad
 H_\theta=\frac1{\sqrt2}\begin{pmatrix}1&1\\\eta&-\eta\end{pmatrix}.
 \tag{2}
\]

Extend this joint block by the identity on its full orthogonal complement,
including all other pulse labels and token configurations, and tensor the
result with \(I_{D\mathsf R}\). All four columns are specified and
orthonormal; thus this defines a complete unitary, with inverse
\(G_\theta^*\). It sends the marked orthogonal basis input
\(o_+\otimes|99,1,p_0\rangle\) to the source factor of (1). For the
two frozen phases its joint-block coefficients are rational \(\pm1/2\),
although the two displayed factor matrices separately contain
\(1/\sqrt2\).

This loader is a supplied finite source operation before the first
macrostep. Its implementation, spatial cost and phase-control resource
are not derived from the original six-pentit TWIST update or from powers
of \(U_{\rm rec}\). It is not inserted into the subsequent evolution.
The unknown old memory is supplied, not reset or prepared by this loader.

The unchanged pulse step, in the convention
\(|x\rangle\mapsto e^{-ikx}\), is

\[
 V(k)=\frac15
 \begin{pmatrix}
 1-4e^{ik}&-2-2e^{ik}\\
 2+2e^{-ik}&1-4e^{-ik}
 \end{pmatrix}.
 \tag{3}
\]

The unchanged complete operator is
\(U_{\rm rec}=\mathcal T(U\otimes I_D)\mathcal T^*\),
\(U=U_0C\), with the Canon contact, object step and half-line label
swap. The only proposed receiver reading is the fixed local instrument

\[
 P_W=|d_0\rangle\langle d_0|,\qquad P_N=I_D-P_W.
 \tag{4}
\]

Here \(W\) in a recorded outcome means "written"; the object operator
is also conventionally called \(W\) in the Canon. The context distinguishes
them. The instrument in (4), its Born reading and any occurrence of an
individual outcome are additional reading assumptions; unitary evolution
alone supplies the coherent joint state below.

## 2. Why the prescribed contact stays inactive in the primary experiment

Define the object reflection \(P_o\) by \(r\mapsto-r\), together with
\(e_2\leftrightarrow e_3\); it fixes \(R,e_1,e_4\). The object coin,
streaming and contact phase commute with \(P_o\), so the object operator
\(W\) preserves its odd subspace. The initial \(\chi_-\) is odd.
At \(r=0\), an odd object vector is orthogonal to the contact pulse
coin \(A=(e_1-e_4)/\sqrt2\). Hence the pulse port \(\gamma\) has
zero amplitude, and \(C\) acts as the identity. This remains true at
every time, including under the inverse. The receiver swap acts only on
labels and commutes with \(P_o\).

The odd pulse space is therefore a reducing subspace of the same complete
\(U_{\rm rec}\). No contact is deleted from the operator. Within this
subspace the object evolves independently. Put

\[
 O_n=\zeta^{-2n}W^n\chi_-,\qquad \|O_n\|=1.
\]

For the first two steps, \(|r|\ge3\) initially and object displacement
in \(r\) is at most one per step, so the object contact phase at
\(r=0\) is also never sampled. The formulas below use the full \(O_n\)
and do not replace the law by another step.

## 3. Complete one-step state and its receiver instrument

First allow an arbitrary normalized pulse coin \(a|1\rangle+b|2\rangle\).
Multiplication of (3) gives exactly four outgoing components:

| Pulse configuration | Amplitude |
|---|---:|
| \((98,1)\) | \((-4a-2b)/5\) |
| \((99,1)\) | \((a-2b)/5\) |
| \((99,2)\) | \((2a+b)/5\) |
| \((100,2)\) | \((2a-4b)/5\) |

Define

\[
 L(a,b)=\frac{(-4a-2b)|98,1\rangle+(a-2b)|99,1\rangle
                    +(2a+b)|99,2\rangle}{5},
 \qquad t(a,b)=\frac{2a-4b}{5},
\]
\[
 |\widetilde\mu\rangle_{pD\mathsf R}
 =\sum_{j=1}^{25}|p_j\rangle|d_0\rangle|\phi_j\rangle.
\]

The complete joint output is

\[
 |\Psi(1)\rangle
 =|O_1\rangle\otimes
 \left[L(a,b)|p_0\rangle|\mu\rangle
       +t(a,b)|100,2\rangle|\widetilde\mu\rangle\right].
 \tag{5}
\]

The two spatial sectors are orthogonal and
\(\|L\|^2+|t|^2=|a|^2+|b|^2\). Equation (5) specifies the
complementary outcome as well as the written outcome; it involves no
discarded branch or branch-specific normalization in the evolution.

The written outcome has probability and source effect

\[
 p_1=|t|^2,\qquad
 E_W=\frac1{25}\begin{pmatrix}4&-8\\-8&16\end{pmatrix}
     =\frac45|w\rangle\langle w|,
 \qquad w=(1,-2)^{\mathsf T}/\sqrt5.
 \tag{6}
\]

This is rank one, with eigenvalues \(4/5,0\); \(E_N=I-E_W\).
For arbitrary old memory/reference the written branch transfers
\(\mu\) isometrically into pulse labels/reference and leaves the receiver
in \(d_0\). The nonwritten branch leaves \(\mu\) unchanged. Conditional
normalization, when an outcome has nonzero probability, is the ordinary
normalization of that stated instrument and does not change \(U_{\rm rec}\).

For \(a=1/\sqrt2,b=\eta/\sqrt2\), (6) becomes

\[
 \boxed{p_1(\theta)=\frac{10-8\cos\theta}{25}},\qquad
 p_1(+)=\frac2{25},\quad p_1(-)=\frac{18}{25}.
 \tag{7}
\]

The phase contrast is \(16/25\). Among phase-only variations of a
normalized single-site coin with fixed bank populations, the largest
possible contrast is \(32|a||b|/25\le16/25\), attained here. The
probability changes because the two bank amplitudes interfere in the
same outgoing \((100,2)\) component; the initial memory and all initial
configuration probabilities are the same.

For a mixed old state \(\sigma_{D\mathsf R}\), tracing the outgoing
carrier and configuration gives

\[
 \sigma'_{D\mathsf R}
 =(1-p_1)\sigma_{D\mathsf R}
   +p_1|d_0\rangle\langle d_0|\otimes\sigma_{\mathsf R}.
 \tag{8}
\]

The correlations absent from the second term are present in the pulse
labels/reference in the full state. Equation (8) is not an erasure of
the old information by the complete unitary.

## 4. Two uninterrupted steps

With no reading between the two steps, \(\mathcal T^*\mathcal T=I\)
allows direct use of \(V^2\), followed by the one final half-line label
swap. The eight possible pulse components from \(x=99\) are:

| Pulse configuration | Numerator of its amplitude, over \(25\) |
|---|---:|
| \((97,1)\) | \(16a+8b\) |
| \((98,1)\) | \(-12a+4b\) |
| \((98,2)\) | \(-8a-4b\) |
| \((99,1)\) | \(-7a+4b\) |
| \((99,2)\) | \(-4a-7b\) |
| \((100,1)\) | \(-4a+8b\) |
| \((100,2)\) | \(-4a-12b\) |
| \((101,2)\) | \(-8a+16b\) |

Their squared norms sum to \(|a|^2+|b|^2\): the squared column
numerators each sum to \(625\), and their scalar product is zero.
Multiply this table by the common object factor \(O_2\); use
\(|p_0\rangle|\mu\rangle\) on \(x<100\) and
\(|\widetilde\mu\rangle\) on \(x\ge100\). This specifies the complete
uninterrupted two-step state, including memory and reference.

The final write probability is consequently

\[
 p_{2,\mathrm{unread}}=
 \frac{|-4a+8b|^2+|-4a-12b|^2+|-8a+16b|^2}{625},
\]
\[
 E_{2,\mathrm{unread}}
 =\frac1{625}\begin{pmatrix}96&-112\\-112&464\end{pmatrix},
\]
\[
 \boxed{p_{2,\mathrm{unread}}(\theta)
              =\frac{280-112\cos\theta}{625}},\qquad
 p_{2,\mathrm{unread}}(+)=\frac{168}{625},\quad
 p_{2,\mathrm{unread}}(-)=\frac{392}{625}.
 \tag{9}
\]

## 5. Read at both times: a distinct, fully specified experiment

Now apply the local Lüders instrument (4) after each step. The first
outcome is written first in the following joint probabilities. From a
first written branch, the pulse starts the next step at \((100,2)\):

\[
 |100,2\rangle\longmapsto
 \frac{-2|99,1\rangle-2|100,1\rangle+|100,2\rangle
                       -4|101,2\rangle}{5}.
 \tag{10}
\]

On the returning \((99,1)\) branch the same receiver swap restores
the complete old memory/reference state and returns the pulse label
to \(p_0\). On the other three branches the receiver remains in
\(d_0\) and the pulse retains the old information. Whenever the first
write has nonzero probability, this gives

\[
 P(W\mid W)=21/25,\qquad P(N\mid W)=4/25.
 \tag{11}
\]

From the first nonwritten branch, the only second-step crossing amplitude
is

\[
 \frac{2(a-2b)-4(2a+b)}{25}=\frac{-6a-8b}{25}
\]

at \((100,2)\). Therefore the four joint probabilities, without
postselection, are

\[
\begin{aligned}
 P(W,W)&=21|2a-4b|^2/625,\\
 P(W,N)&=4|2a-4b|^2/625,\\
 P(N,W)&=|6a+8b|^2/625,\\
 P(N,N)&=1-|2a-4b|^2/25-|6a+8b|^2/625.
\end{aligned}
 \tag{12}
\]

For the two frozen phases this gives the complete table:

| Source phase | \(W,W\) | \(W,N\) | \(N,W\) | \(N,N\) |
|---|---:|---:|---:|---:|
| \(+\) | \(42/625\) | \(8/625\) | \(98/625\) | \(477/625\) |
| \(-\) | \(378/625\) | \(72/625\) | \(2/625\) | \(173/625\) |

Each row sums to one. With \(c=\cos\theta\), the corresponding
numerators are \(210-168c,40-32c,50+48c,325+152c\).
The second-time write probability after the first reading is
\((260-120c)/625\), distinct from (9).

This distinction follows directly at \((100,2)\). With no first reading,
the amplitudes \((2a-4b)/25\) from a first-written path and
\((-6a-8b)/25\) from a first-nonwritten path add coherently. The Lüders
reading removes their cross term. No mixture of these two protocols is
used to claim a single table. In either protocol a record can return to
its old contents: the finite experiment does not establish permanent
retention, a historical event counter or a reusable erased receiver.

## 6. Inverse, arbitrary-reference closure and exact flag capacity

Before a projective reading, the whole output has the exact inverse

\[
 U_{\rm rec}^*=
 \mathcal T\,(C^*U_0^*\otimes I_D)\,\mathcal T^*.
 \tag{13}
\]

It recovers the source and the old memory/reference jointly. This states
unitary reversibility; it does not assert that a forward macrostep performs
a reset or that applying the inverse after an unrecorded irreversible
Lüders dephasing recovers the lost coherence. Every state identity above
tensors with the identity on an arbitrary additional reference. Neither
the receiver nor the carrier silently discards old labels.

The proper subspace \(K\) is necessary for a perfect receiver-only
new-write flag. Let \(0\le F\le I_D\) be any effect that must report
"not newly written" with certainty on every admitted unchanged old
state, and "newly written" with certainty on the written state \(d_0\).
For all \(k\in K\), these requirements imply

\[
 \langle k,Fk\rangle=0,\qquad Fd_0=d_0.
\]

Positivity gives \(K\subseteq\ker F\), and self-adjointness gives
\(K\perp d_0\). Consequently

\[
 \dim K\le25.
 \tag{14}
\]

This bound is attained exactly by the chosen \(K=d_0^\perp\) and
\(F=P_W\). If every state of the full 26-dimensional old memory is
admitted, \(F=0\) is forced, contradicting \(Fd_0=d_0\). Concretely,
old memory \(d_0\) is indistinguishable at the receiver from newly written
\(d_0\). This obstruction concerns a perfect receiver-only event flag;
the coherent label swap itself works on all 26 old labels. An additional
history register, different ready-space contract or access to outgoing
carrier information changes the resources and must be declared separately.

The imperfect-flag behavior on an arbitrary full 26-dimensional old state
is also exact. Let \(q=\operatorname{Tr}(P_W\sigma_D)\) be its initial
population in \(d_0\). The unchanged one-step swap still has physical
crossing probability \(p_1(\theta)\), but the observed receiver flag has
probability

\[
 p_{\mathrm{flag}}(\theta)
 =p_1(\theta)+(1-p_1(\theta))q.
 \tag{15}
\]

Thus the phase contrast is attenuated to
\((1-q)16/25\). Old memory \(d_0\) gives flag probability one for
both phases. This does not prevent coherent storage exchange or every
phase-dependent observation on full old states; it prevents a uniformly
perfect new-write indication from the receiver alone.

## 7. Exact arithmetic and scope

For the two frozen phases, the four source coefficients in (1), before
the old-memory/reference factor, are \(\pm1/2\). They can be represented
by four integer coefficients \(\pm1\) with one common normalization
\(2\). The supplied loader (2) has rational half-integer coefficients;
it is a separate preparation resource, not a new term in the step.

The complete step retains the inherited
\(\mathcal A=25U_{\rm rec}\) over \(\mathbb Z[\zeta_{20}]\).
Thus a prepared finite coefficient vector can be advanced by
\(a_{n+1}=\mathcal A a_n\), with the single read factor
\(25^n\|a_0\|\). The pulse tables alone have denominators \(5\)
and \(25\); the full object/pulse operator has denominator bound
\(25^n\) relative to its initial common normalization. No claim that
every branch attains this bound is needed. Arbitrary complex old-memory
or reference amplitudes are not thereby converted into finite integer
inputs: their inclusion is the exact operator/reference extension.

The arithmetic is inherited from
[#1741](https://github.com/mathorn1973/twist-j/issues/1741) and
[#1771](https://github.com/mathorn1973/twist-j/issues/1771), including the
separation between a finite-time exact representation and an all-time
bounded-precision claim. All configurations here have active charge
\(4+4+2=10\), and the state norm is one. Neither fact by itself identifies
a physical energy. The separate spectral analysis of this same primary
family in [SPECTRAL.md](SPECTRAL.md) is required for the stated equality
of full-step energy readings of the two frozen phases.

The earlier
[#1741 finite protocol](https://github.com/mathorn1973/twist-j/issues/1741#issuecomment-6385322783)
already proves finite-buffer retention and its sharp reverse-leakage
boundary. Equations (10)--(12) are an explicit local finite instance,
not a new permanent-memory theorem. Its additional bound-branch filter
is not inserted as a gate in the present evolution.

The present result is an exact finite phase-to-position-to-occupied-record
instrument of a declared spatial model, with both outcomes and continuation
specified. It does not derive the spatial model, loader, coherent amplitudes,
reading or empirical occurrence from the original six-pentit update. The
primary odd-pulse experiment does not activate the contact and does not
prove bound capture. The separate active-contact calibration is stated in
[CONTACT.md](CONTACT.md).

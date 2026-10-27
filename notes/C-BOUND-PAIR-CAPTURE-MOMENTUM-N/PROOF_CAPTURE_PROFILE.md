# A fixed-source momentum profile of the complete capture probability

**NON-CANONICAL / L1 / conditional analytical candidate.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: [#1812](https://github.com/mathorn1973/twist-j/issues/1812).

## 1. Fixed model and exact meaning of the scan

All inherited definitions are pinned in `SOURCES.md`. Use exactly the
accepted `HOMOGENEOUS-CAPTURE-CURRENT-RECORD` model:

\[
W=\Gamma_gSM_2,\quad \mu=2,\quad g=2\pi/5,\quad \beta=4\pi/5,
\qquad C_{\rm core}=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\tag{CP-1}
\]

The object has center and relative coordinates `(R,r)`, with constituent
positions `R+r,R-r`. Keep the full standing-token/moving-pulse carrier,
all 26 labels, receiver at `z=100`, both arrangement spaces, the complete
Caratheodory functions `F1,F2`, and the joint outgoing event `Q_win`.
That event retains the original bound branch with outgoing center
momentum `|P_out|<=1/100`, the right-moving positive pulse branch, the
original energy and total-momentum windows, and the receiver write. It
includes every outgoing label carrying arbitrary old memory/reference
correlations. A bare receiver label is not a binding herald.

The initial token stays at `y=0`, with label 1. The input is a relatively
unbound pair plus that token; the selected output is a bound pair plus
an outgoing pulse and a record. This is not isolated two-body capture.

Let `P` denote incoming **pair center momentum**, and let `K=P+k` modulo
`2*pi` denote conserved total pair/carrier momentum. They are distinct.
Freeze

\[
\delta=h=1/1000,\quad E_*=8\pi/5,\quad \omega_*=E_*-\beta=4\pi/5,
\quad I_E=[E_*-h,E_*+h],\quad I_\omega=[\omega_*-h,\omega_*+h],
\tag{CP-2}
\]
\[
|p|\le999/1000,\qquad I_p=[p-\delta,p+\delta].
\tag{CP-3}
\]

Only the center `p` of the incoming window changes. Thus every incident
`P` lies in `[-1,1]`. Its full energy distribution stays flat on the
same `I_E`. Localizing the token at zero keeps the same uniform `K`
weight as in the inherited preparation. The original source is exactly
`p=0`. The lower-case `p` is a dimensionless lattice momentum label,
not an SI photon momentum or a general change of beam energy.

## 2. Expanded incoming continuum rectangle and density identity

Write

\[
u=\cos\omega,\quad s=\sin\omega,\quad v=\cos P,\quad
h_0=v-u,\quad t=v-5u,\quad c=\cos(\omega-g),\quad B=\sqrt{t^2-16}.
\tag{CP-4}
\]

On the entire rectangle `|P|<=1`, `omega in I_omega`,

\[
-41/50<u<-4/5,\quad 0<s<3/5,\quad 3/10<c<1/3,
\quad v\ge1/2,\quad h_0>13/10,\quad 9/2<t<51/10,\quad B>2.
\tag{CP-5}
\]

Indeed `161/100<phi<13/8`, `cos(omega*)=-phi/2`,
`cos(omega*-g)=(phi-1)/2`, and cosine is one-Lipschitz. Also
`cos P>=1-P^2/2`. The energy quadrant is `(pi/2,pi)`, so `s>0` and
`u<-4/5` gives `s<3/5`; the phase difference lies in `(0,pi/2)`.
These rational bounds prove (CP-5) without sampling the rectangle.

The inherited odd-sector Schur formula is

\[
D=u-v=-h_0,\qquad d=-4s/h_0,\qquad x=u-ds=u+4s^2/h_0.
\tag{CP-6}
\]

Its exact algebra gives

\[
1-x^2=\frac{s^2(t^2-16)}{h_0^2},\qquad
X=\frac{s+d(u+x)}{\sqrt{1-x^2}}=\frac{B}{h_0}>0.
\tag{CP-7}
\]

Thus `D` never vanishes and `|x|<1`. Moreover

\[
\partial_\omega x=-s\left(1-\frac{8u}{h_0}+\frac{4s^2}{h_0^2}\right)<0.
\tag{CP-8}
\]

The original radiation branch, positive real part and odd-sector scalar
Schur elimination therefore extend across this connected larger
rectangle without a threshold or pole. The contact vector
`a0(P)=delta_(r=0) iB_coin`, with
`B_coin=(|+->-|-+>)/sqrt(2)`, lies in the odd exchange sector. The
coincidence contact in that sector is one-dimensional; using its scalar
formula does not discard the even bound sector from the complete
scattering functions.

For `tau=tan(g/2)`, substitution into the inherited Mobius density gives

\[
\begin{aligned}
\rho(P,\omega)
&=\frac{(1+\tau^2)X}{2\pi[(1-\tau d)^2+\tau^2X^2]}\\
&=\frac{(1+\tau^2)Bh_0}
 {2\pi[(h_0+4\tau s)^2+\tau^2B^2]}\\
&=\boxed{\frac{\sqrt{(\cos P-5\cos\omega)^2-16}}
 {2\pi[\cos P-5\cos\omega+4\cos(\omega-g)]}}.
\end{aligned}
\tag{CP-9}
\]

For the last equality use `B^2=h0^2-8u h0-16s^2` and
`8 tau(s-tau u)/(1+tau^2)=4 cos(omega-g)-4u`.
Equation (CP-9) is the actual absolutely continuous spectral density of
`W(P)` on `a0(P)` in this rectangle. It is not an independently chosen
weight. Its denominator is positive by (CP-5).

The inherited separation condition also extends:

\[
\frac{|\partial_Px|}{\sqrt{1-x^2}}
=\frac{4s|\sin P|}{h_0B}<\frac{12}{13}<1.
\tag{CP-10}
\]

Together with (CP-8), this keeps both free constituents separated from
the standing token in the backward asymptotic incoming limit. It is not
a new finite-time preparation theorem.

## 3. One prescribed normalized source family

Let `P_in,p` be the direct integral over `P in I_p` of the relative
absolutely continuous projections `P_ac(W(P))`. For `H1=H_W+beta`, put

\[
\rho_p(E)=\int_{p-\delta}^{p+\delta}\rho(P,E-\beta)\frac{dP}{2\pi},
\qquad
\psi_p=\mathbf1_{I_E}(H_1)
 [2h\rho_p(H_1)]^{-1/2}P_{{\rm in},p}a_0.
\tag{CP-11}
\]

The density is strictly positive. Borel functional calculus gives

\[
\|\psi_p\|^2=\int_{I_E}\frac{\rho_p(E)}{2h\rho_p(E)}dE=1.
\tag{CP-12}
\]

Its energy density is `1/(2h)`, and its incoming relative point-spectrum
weight is zero. Tensor with the localized token `|y=0,t1>` and the same
arbitrary normalized receiver/reference state. In total-momentum/energy
fibers the input is `(2h)^(-1/2) 1_IE(E) xi_p(E)`, independent of `K`,
where `xi_p` is the unit spectral direction of `P_in,p a0`.

The two continuum roots and their source overlaps are included in this
spectral direction. A bare plane wave has not been substituted for it.
Source normalization changes according to the displayed formula fixed
before the scan, rather than according to the observed capture result.

## 4. The complete capture functional

Let `P_win(p)` denote the exact asymptotic probability of the original
joint event for the source (CP-11). The inherited full stationary kernel
gives

\[
\mathsf P(p)=\int_{I_K}\frac{dK}{2\pi}\int_{I_E}\frac{dE}{2h}
 \frac{64\pi^2\rho_p(E)\rho_{2,b,+}(K,E)}
 {|4+F_1(E)F_2(K,E)|^2}.
\tag{CP-13}
\]

Here `F1,F2` remain the **complete** port resolvents of the fixed law.
In particular `F1` is not replaced by the restricted incident density,
and `F2` is not replaced by the selected outgoing bound branch. Only
`rho_p`, the prepared incident overlap, changes. The outgoing density,
receiver and success projection are all unchanged.

Equivalently,

\[
\mathsf P(p)=\int_{I_E}A(E)\rho_p(E)dE,\qquad
A(E)=\frac{64\pi^2}{2h}\int_{I_K}
 \frac{\rho_{2,b,+}(K,E)}{|4+F_1(E)F_2(K,E)|^2}\frac{dK}{2\pi}.
\tag{CP-14}
\]

This nonnegative weight is independent of `p`. It is nonzero on a set
of positive measure, since the accepted source theorem gives
`P_win(0)>2/10^28`. All integrals are understood with the inherited
almost-everywhere boundary values. No pointwise replacement of their
denominator or radial numerical limit is made.

## 5. Evenness, positivity and strict momentum dependence

At fixed `omega`, set `f(t,c)=sqrt(t^2-16)/(2*pi*(t+4c))`. Then

\[
\partial_tf=\frac{2(ct+4)}{\pi\sqrt{t^2-16}(t+4c)^2}>0.
\tag{CP-15}
\]

As `t=cos P-5cos omega`, the density is even in `P` and strictly
decreases with `|P|` for `0<|P|<=1`. Thus `rho_p(E)` is even in `p`,
and for `p>0`,

\[
\frac{d\rho_p(E)}{dp}
=\frac{\rho(p+\delta,E-\beta)-\rho(p-\delta,E-\beta)}{2\pi}<0.
\tag{CP-16}
\]

The inequality uses `|p+delta|>|p-delta|`, including `0<p<delta`.
The positive functional (CP-14) proves that `P_win(p)` is positive,
even, continuous and strictly decreasing for `0<p<=999/1000`.
Uniform bounds below justify dominated convergence where a derivative
is used. This is a theorem on the continuous family, not an inference
from the finite grid.

## 6. Ratio bounds for the whole probability

The positive measure

\[
d\nu(E)=\frac{A(E)\rho_0(E)}{\mathsf P(0)}dE
\tag{CP-17}
\]

has total mass one and is independent of `p`. Hence

\[
\inf_{I_E}\frac{\rho_p}{\rho_0}
\le\frac{\mathsf P(p)}{\mathsf P(0)}
=\int_{I_E}\frac{\rho_p(E)}{\rho_0(E)}d\nu(E)
\le\sup_{I_E}\frac{\rho_p}{\rho_0}.
\tag{CP-18}
\]

All unresolved open and virtual channels remain in `nu`. In particular
(CP-18) is not an equality to a single-energy density ratio.

For an explicit envelope define

\[
r(p,\omega)=\frac{\rho(p,\omega)}{\rho(0,\omega)}
=\sqrt{\frac{t_p^2-16}{t_0^2-16}}
 \frac{t_0+4c}{t_p+4c},
\quad t_p=\cos p-5\cos\omega,\quad t_0=1-5\cos\omega.
\tag{CP-19}
\]

For fixed `p>0`, this ratio is strictly increasing in `omega` on
`I_omega`. To see this, let

\[
L=\partial_t\log f=\frac{4(ct+4)}{(t^2-16)(t+4c)},
\quad
L_t=-\frac{t^2+16}{(t^2-16)^2}+\frac1{(t+4c)^2}<0.
\tag{CP-20}
\]

At fixed `omega`, the expression

\[
\partial_\omega\log f
=5\sin\omega\,L+\frac{4\sin(\omega-g)}{t+4c}
\tag{CP-21}
\]

strictly decreases with `t`. Since `t_p<t_0` for `p>0`, subtracting
(CP-21) at `t_0` from its value at `t_p` proves the assertion.

## 7. Finite-width source error without numerical quadrature

The elementary global box (CP-5) implies

\[
0<L\le16/17,\qquad |L_t|\le580/289,
\quad |\partial_P\log\rho|\le16/17,
\quad \frac{|\rho_{PP}|}{\rho}\le1108/289<4.
\tag{CP-22}
\]

For the first bound use (CP-20) with the extreme rational bounds of
(CP-5). For the second, `(t^2+16)/(t^2-16)^2` decreases for `t>4`.
Finally

\[
\partial_P^2\log\rho=-\cos P\,L+\sin^2P\,L_t,
\qquad \rho_{PP}/\rho=\partial_P^2\log\rho+
 (\partial_P\log\rho)^2
\tag{CP-23}
\]

gives `(272+580+256)/289=1108/289`.
For `|P-p|<=delta`, the first derivative bound yields
`rho(P,omega)/rho(p,omega)<=exp((16/17)delta)<1/(1-delta)`.
Taylor's theorem and the symmetric average therefore give

\[
\left|\frac1{2\delta}\int_{p-\delta}^{p+\delta}\rho(P,\omega)dP
 -\rho(p,\omega)\right|
\le\frac{\delta^2}{6}\sup|\rho_{PP}|
\le\frac{2\delta^2}{3(1-\delta)}\rho(p,\omega)
<\delta^2\rho(p,\omega).
\tag{CP-24}
\]

Put `e=delta^2=1/10^6`. Applying (CP-24) to numerator and denominator
of (CP-18), and using the energy monotonicity of (CP-19), proves

\[
\boxed{
\frac{1-e}{1+e}r(p,\omega_*-h)
\le\frac{\mathsf P(p)}{\mathsf P(0)}
\le\frac{1+e}{1-e}r(p,\omega_*+h).
}
\tag{CP-25}
\]

For `p=0`, the exact ratio is one. No quadrature of `F1,F2` or
zero-width source approximation occurs in (CP-25).
For additional width control, differentiating (CP-21) in `t` gives

\[
0\le\partial_\omega\log r(p,\omega)
\le7(1-\cos p),
\tag{CP-26}
\]

since its derivative magnitude is at most
`3*(580/289)+400/3249<7`. The upper bound is strict for `p!=0`;
at `p=0` both sides vanish.
At the central energy the exact point shape is

\[
r(p,\omega_*)=
\frac{9\varphi-2}{\sqrt{45\varphi-35}}
\frac{\sqrt{(2\cos p+5\varphi)^2-64}}
 {2\cos p+9\varphi-4}.
\tag{CP-27}
\]

Equation (CP-27) describes a point-density shape; (CP-25), not (CP-27)
alone, is the certified statement about finite prepared packets.

## 8. Positive absolute lower bound and its limitation

On the frozen rectangle `B_p>2`, `B_0<16/5`, and `t_p<=t_0`, so
`r(p,omega)>5/8`. Combining this with the inherited reference bound gives

\[
\mathsf P(p)>
\frac{1-e}{1+e}\frac58\frac2{10^{28}}>rac1{10^{28}}.
\tag{CP-28}
\]

This is a guaranteed conservative lower bound. It is not an estimate
of the actual magnitude. The complete absolute profile would require
evaluating or more tightly bounding the full boundary functions in
(CP-13); that calculation is not performed here.

## 9. Scope and connection to the port construction

The companion port construction embeds this entire inherited apparatus
in its minus sector, so (CP-13)--(CP-28) remain exact there. Preparing
and repeatedly reading a computational port instead changes the
operator and requires a new capture problem. The golden contact weight
is not substituted for the capture probability.

The law, energy window, output event, widths and receiver have been
fixed before the finite audit. The input source family is explicitly
supplied. The conclusion is asymptotic, retains its bound projector and
does not prove finite physical preparation or a finite-time binding
detector. The unchanged source theorem carries the safe-window spectral
energy account and separate complete occupancy current; no new local
spectral-energy current is claimed.

No photon polarization, electron charge/spin/statistics, elementary
particle identification, SI scale, native source, or occurrence law is
derived. A next bound-object plus incident-pulse scattering problem
would be a distinct source and event on this same law.

# A concrete original-source energy certificate

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1780](https://github.com/mathorn1973/twist-j/issues/1780).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`9f7b175341e5267113dfbe42f96db47299e27f52`.
This is an analytical derivation, not an executed moment calculation,
numerical spectral estimate, or independent acceptance.

The operator is the unchanged Public Canon v105
`HOMOGENEOUS-CAPTURE-CURRENT-RECORD` model at
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The source is the active
pair of PR #1777 at `191ab035be823bd9d6fdc9effba81528fa026e49`.
The finite-source criterion being strengthened is
[PR #1779 ENERGY_CERTIFICATE.md](https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/ENERGY_CERTIFICATE.md).
Its source identities and preparation scope remain conditional premises.

This note supplies an explicit, extremely large passing choice of its
parameters. It does not propose a feasible matrix enumeration or a small
apparatus. The central new estimate is on the actual source spectral
measure near the nominated logarithm cut, rather than on a fitted density.

## 1. Source and Caratheodory conventions

Write

\[
 g=2\pi/5,\quad \beta=4\pi/5,\quad
 B=(e_2-e_3)/\sqrt2,\quad A=(e_1-e_4)/\sqrt2.
\]

The normalized seed is the token contact port
\(\chi=|R=97,r=0,iB;y=97,t_0\rangle\otimes\Xi\), with arbitrary
normalized old-memory/reference input \(\Xi\). The phase \(i\) does not
change its spectral measure. The receiver calibration is identity on
this seed. Its conjugation therefore removes the memory/reference
factors from every seed spectral expectation, including resolvents.

For a unitary \(V\) and unit vector \(v\), use

\[
 F_{V,v}(\zeta)=\langle v,(\zeta+V)(\zeta-V)^{-1}v\rangle,
 \qquad |\zeta|>1.                                      \tag{S1}
\]

It has positive real part. A spectral density with respect to angle
\(d\omega\) equals the radial boundary real part divided by \(2\pi\).
An atom of weight \(w\) at \(e^{-i\omega_b}\) contributes
\(2iw/(\omega-\omega_b)+O(1)\) when
\(\zeta=e^{-i\omega}\) approaches it from \(\operatorname{Im}\omega>0\).

Joint center/carrier translation decomposes the uncalibrated full step
over total momentum \(K\), with measure \(dK/(2\pi)\). The localized
seed has constant unit fiber weight. The free token port function is

\[
 F_1(\zeta)=\int_{-\pi}^{\pi}
 F_B(P,e^{i\beta}\zeta)\,\frac{dP}{2\pi},\qquad
 F_B(P,\lambda)=F_{W(P),\delta_0B}(\lambda).          \tag{S2}
\]

It is independent of \(K\). The free pulse port function is denoted
\(F_2(K,\zeta)\); only its positive real part will be needed.
Thus \(\zeta=1+\eta\) in the full step corresponds to a radial
approach to the object energy angle

\[
 \omega_0=-\beta=-4\pi/5.                            \tag{S3}
\]

## 2. Exact object-port function

The exchange reflection sends \(r\) to \(-r\) and interchanges
the two coin factors. It commutes with \(W(P)\). The seed \(\delta_0B\)
is odd under this reflection. At \(r=0\), its entire odd coin space
is the one-dimensional span of \(B\). Consequently the contact
phase is a rank-one phase perturbation on this reducing sector.

Here is a direct free-resolvent calculation fixing the coefficients and
branches. In the Bell coin order \((A,S,T,B)\), where
\(S=(e_1+e_4)/\sqrt2\), \(T=(e_2+e_3)/\sqrt2\), the free coin is
identity on \(A,B\), while its \((S,T)\) block has diagonal
\(d_0=-3/5\) and off-diagonal \(i h_0=4i/5\).
Put \(C=\cos P\). Eliminating the two center-streaming channels
\(A,S\) in \(\lambda-W_f(P)\) gives the effective relative coefficient

\[
 v=\frac{d_0\lambda^2-(1+d_0)C\lambda+1}
          {\lambda^2-(1+d_0)C\lambda+d_0}.
\]

The free \(B\)-resolvent is therefore

\[
 \langle\delta_0B,(\lambda-W_f(P))^{-1}\delta_0B\rangle
 =\int_{-\pi}^{\pi}
 \frac{\lambda-v\cos q}
 {\lambda^2+v-\lambda(1+v)\cos q}\,\frac{dq}{2\pi}.    \tag{S4}
\]

This identity initially holds where the eliminations are invertible;
both sides then continue as the same resolvent. The elementary cosine
integral and its numerator reduction give

\[
 I_0=\int\frac{dq/(2\pi)}
 {\lambda^2+v-\lambda(1+v)\cos q}
 =\frac1{\sqrt{(\lambda^2-1)(\lambda^2-v^2)}},
\]
\[
 R_{BB}=\frac{\lambda^2-v^2}{\lambda(1+v)}I_0
       +\frac{v}{\lambda(1+v)},\qquad
 F_0=2\lambda R_{BB}-1
 =\frac{v-1}{v+1}
  +\frac2{v+1}\sqrt{\frac{\lambda^2-v^2}{\lambda^2-1}}.
\]

The square root in the last expression is continued from its value
approaching 1 at infinity. For a real boundary angle
\(\lambda=e^{-i\omega}\), write

\[
 c=\cos\omega,\quad s=\sin\omega,\quad
 d=\frac{4s}{c-C},\quad x=c-ds,\quad
 N_s=s+d(c+x).
\]

The cosine integral in (S4), or squaring its selected root, gives

\[
 F_0^2-2idF_0=1+2(c/s)d,
 \qquad x^2-1=-sN_s.                                \tag{S5}
\]

All formulas at removable denominators are understood by continuation
from \(|\lambda|>1\). The rank-one contact phase gives

\[
 F_B=\frac{F_0+i\tau_g}{1+i\tau_gF_0},\qquad
 \tau_g=\tan(g/2).                                  \tag{S6}
\]

This is also the contact-port formula in the Canon. Substituting its
inverse into (S5), and using the half-angle identities, yields

\[
 (b-C)F_B^2-8i\sin\alpha\,F_B
       -(5c+4\cos\alpha-C)=0,
 \quad \alpha=\omega-g,\quad b=5c-4\cos\alpha.       \tag{S7}
\]

The discriminant divided by four is
\((C-5c)^2-16\). Put \(a=5c+4\). In a neighborhood of (S3),
\(-1<b<a<1\), \(\sin\alpha>0\), and the physical boundary root is

\[
 F_B=
 \begin{cases}
 \displaystyle\frac{\sqrt{(C-5c)^2-16}-4i\sin\alpha}{C-b},
       &a<C\le1,\\[6pt]
 \displaystyle-i\frac{\sqrt{16-(C-5c)^2}+4\sin\alpha}{C-b},
       &-1\le C<a,\ C\ne b.
 \end{cases}                                       \tag{S8}
\]

To check the root choice, the exterior approach has
\(\operatorname{Im}\omega>0\). Near (S3), the imaginary part of
\((C-5\cos\omega)^2-16\) is negative to first order, since
\(10\sin\omega(C-5\cos\omega)<0\). Its root is positive on
the continuum side and approaches \(-i\sqrt{|\cdot|}\) on the
gap side. The continuum real part is positive. This fixes the branch
in (S8), including the pole rather than its canceled alternative.

## 3. The complete local spectral measure of the free token source

The only source-visible gap pole in this neighborhood is \(C=b(\omega)\).
Its numerator in (S8) is \(-8i\sin\alpha\), since the square root
at that point equals \(4\sin\alpha\). Also

\[
 b'(\omega)=-5\sin\omega+4\sin(\omega-g)>0.
\]

At fixed \(P\), comparison with the atom convention in (S1) gives
the fiber weight

\[
 w(P)=\frac{4\sin\alpha}{b'(\omega)}.                \tag{S9}
\]

There are two momentum roots, with
\(|dP/d\omega|=b'(\omega)/\sqrt{1-b^2}\). Their pushforward under
\(dP/(2\pi)\) has density

\[
 \rho_b(\omega)=\frac{4\sin\alpha}{\pi\sqrt{1-b^2}}. \tag{S10}
\]

At (S3), \(b=c=-\cos(\pi/5)\),
\(b'=-9s\), and \(\sin\alpha=-s\). In particular the fiber weights
are \(4/9\), the absolute band velocities are \(1/9\), and
\(\rho_b(\omega_0)=4/\pi\). The fixed-energy fibers have measure
zero in \(P\); they do not give a global atom.

The continuum contributes boundary real part

\[
 R_c(\omega)=\frac1\pi\int_a^1
 \frac{\sqrt{(C-a)(C-5c+4)}}{(C-b)\sqrt{1-C^2}}\,dC. \tag{S11}
\]

These contributions exhaust the local seed measure. For each fiber,
(S8) is an algebraic resolvent with only its displayed square-root
threshold and simple pole in this neighborhood. After subtracting the
displayed atom's Caratheodory term, the remaining function is locally
bounded up to the circle, including the square-root threshold. The
Poisson-kernel bound therefore excludes any remaining singular measure
there. The pole pushforward is absolutely continuous because \(b'>0\)
and \(b\in(-1,1)\). Thus the full token source has local density

\[
 \rho_1(\omega)=\rho_b(\omega)+R_c(\omega)/(2\pi).   \tag{S12}
\]

## 4. Explicit bounds, including the complex resolvent

Fix \(h=1/1000\) and \(|\omega-\omega_0|\le h\).
The elementary inequalities
\(4/5<\cos(\pi/5)<5/6\),
\(1/2<\sin(\pi/5)<3/5\), and the Lipschitz bounds of sine and cosine
give

\[
 -172/1000<a<5/1000,\qquad
 -843/1000<b<-791/1000,\qquad
 49/100<\sin\alpha<61/100,
\]
\[
 a-b>3/5,\quad 1+a>4/5,\quad 1-b^2>1/4,\quad
 9/10<1-a<6/5,\quad b'>4,
 \quad |a'|\le5,\quad |b'|\le9.                     \tag{S13}
\]

Consequently \(\rho_b>1/\pi\), its boundary real part
\(R_b=2\pi\rho_b\) is less than 10, and

\[
 |R_b'|\le8\left(2+9\cdot8\right)=592.              \tag{S14}
\]

For a direct differentiable bound on (S11), set
\(A_0=1-a\), \(C=a+A_0t\). Then

\[
 R_c=\frac1\pi\int_0^1\sqrt{\frac{t}{1-t}}\,G(\omega,t)\,dt,
 \qquad
 G=\frac{A_0\sqrt{8+A_0t}}
 {(a-b+A_0t)\sqrt{1+a+A_0t}}.                       \tag{S15}
\]

The bounds in (S13) imply \(0<G<8\). The four logarithmic derivative
terms are bounded respectively by \(6,1,32,4\): use
\(|A_0'|\le5\), \(|(a-b)'|\le14\), and
\(|a'+A_0't|=|a'(1-t)|\le5\). Hence
\(|\partial_\omega\log G|<43\).
Since \(\int_0^1\sqrt{t/(1-t)}\,dt=\pi/2\), differentiation is
dominated and gives \(R_c<4\), \(|R_c'|<172\).
In particular throughout the window,

\[
 \rho_1>1/\pi,\qquad
 0\le\rho_1<20/(2\pi),\qquad
 |\rho_1'|<800/(2\pi)<200.                          \tag{S16}
\]

The bounds must control the imaginary part too; a density bound alone
does not do that. Take \(\zeta=1+\eta\), \(0<\eta\le h\), in (S2).
Split the token measure into the symmetric angle window
\([\omega_0-h,\omega_0+h]\) and its complement. The real part of
the local integral is at most 20, since the Poisson kernel has total
angle integral \(2\pi\). Its imaginary kernel is odd about the
center and has magnitude at most \(2/|\omega-\omega_0|\).
Subtracting the constant density \(\rho_1(\omega_0)\), whose odd
integral vanishes, bounds the local imaginary part by
\(4\cdot200h=4/5\).

On the complementary arc, its distance from the unit-circle center
point is at least \(2h/\pi\). Since \(1+\eta\le2\), the complete
Caratheodory kernel there has magnitude at most
\(3\pi/(2h)<6000\). The token measure has total mass one.
Thus

\[
 |F_1(1+\eta)|<10000.                               \tag{S17}
\]

On \(|\omega-\omega_0|\le\eta\), the Poisson kernel is at least
\(1/(2\eta)\): its numerator is at least \(2\eta\) and its
denominator at most \(4\eta^2\). Equation (S16) therefore also gives

\[
 \operatorname{Re}F_1(1+\eta)\ge1/\pi>1/4.          \tag{S18}
\]

## 5. Transfer through the actual token-pulse contact

On the two contact ports the contact matrix is
\(C_0=\left(\begin{smallmatrix}3&-4\\4&3\end{smallmatrix}\right)/5\).
The free resolvent is diagonal between token and pulse arrangements.
Writing \(m_j=(F_j-1)/2\), the rank-two resolvent inverse is
\(I-\operatorname{diag}(m_1,m_2)(C_0-I)\), whose determinant is
\((4+F_1F_2)/5\). Its first diagonal Caratheodory entry is

\[
 F_{\rm src}(K,\zeta)=\frac{4F_1(\zeta)+F_2(K,\zeta)}
                              {4+F_1(\zeta)F_2(K,\zeta)}.             \tag{S19}
\]

This concerns the original seed before a step, not an outgoing port.
For \(t=F_1\), \(w=F_2\), positivity of \(\operatorname{Re}w\)
and (S18) give

\[
 \left|\frac{w}{4+tw}\right|
 =\frac1{|t+4/w|}\le\frac1{\operatorname{Re}t}<4.
\]

Using \(F_{\rm src}=t+(1-t^2)w/(4+tw)\) and (S17), uniformly in
\(K\),

\[
 |F_{\rm src}(K,1+\eta)|
 <10000+4(1+10000^2)<5\cdot10^8.                    \tag{S20}
\]

Integration in \(K\) gives the same bound for the original seed.
If \(|1-z|\le\eta\), its radial Poisson kernel is at least
\(1/(2\eta)\), again by the triangle inequality. Therefore

\[
 \mu_\chi\{|1-z|\le\eta\}<10^9\eta,
 \qquad 0<\eta\le1/1000.                            \tag{S21}
\]

In particular the actual seed has no atom at 1. This conclusion uses
the complete coupled contact, not just the free translated limit.

The common source-pair law is
\(d\mu_{\psi_\pm}=(3-z^4-z^{-4})d\mu_\chi/Z\),
where \(Z=(39521+154\sqrt5)/15625\ge1\). Its multiplier is at
most 5. For the actual prepared family, including its retained setting
and arbitrary old-memory/reference input, this proves

\[
 \boxed{\mu_{\psi_\pm}\{|1-z|\le\eta\}
        <5\cdot10^9\eta\quad(0<\eta\le1/1000).}     \tag{S22}
\]

## 6. An explicit moment bound and passing choice

For the unchanged polynomial
\(p_n(z)=(1+z+\cdots+z^n)/(n+1)\), put
\(a_n=\|p_n(U)\psi_\pm\|^2\), with \(U=U_{\rm rec}\).
The geometric sum gives

\[
 |p_n(z)|^2\le\min\left(1,\frac4{(n+1)^2|1-z|^2}\right).
\]

For \(n\ge2000\), split the layer-cake integral
\(a_n=\int_0^1\mu\{|p_n|^2>u\}\,du\) at
\(u_0=4/[(n+1)^2h^2]\). Below \(u_0\) use mass at most one;
above it use (S22) with \(\eta=2/[(n+1)\sqrt u]\). This gives

\[
 a_n\le\frac{2\cdot10^{10}}{n+1}
       +\frac{4\cdot10^6}{(n+1)^2}
       <\frac{3\cdot10^{10}}{n+1}.                 \tag{S23}
\]

No moment has been enumerated to obtain (S23). Choose the fixed integers
and rational parameter

\[
 \boxed{n=10^{20},\quad D=10^{25},\quad
 r=1-1/D,\quad N=1024D.}                            \tag{S24}
\]

Use the predecessor's Abel truncation

\[
 h_{r,N}=\pi I-i\sum_{k=1}^N\frac{r^k}{k}(U^k-U^{-k}),
 \quad \tau=\frac{2r^{N+1}}{(N+1)(1-r)},
 \quad q=\frac{\pi}{\pi+\tau}(h_{r,N}+\tau I).      \tag{S25}
\]

It is a fixed Laurent polynomial of degree \(N\), and
\(0\le q\le2\pi I\). The positive normalization changes the
unscaled polynomial by at most \(2\tau\). Thus the predecessor's
argument, with this extra normalization error, gives on every admitted
source/reference input

\[
 \|(q-f(U))\psi\|
 \le4n\frac{1-r}{1+r}+4\pi\sqrt{a_n}+4\tau.          \tag{S26}
\]

Every term has an explicit bound. Equation (S23) and
\(3\cdot10^{10}\cdot57600^2<10^{20}\) give
\(16\sqrt{a_n}<1/3600\). Also
\(4n(1-r)/(1+r)\le4n/D=4\cdot10^{-5}<1/3600\).
Bernoulli's inequality gives
\((1-1/D)^{-D}=(1+1/(D-1))^D>2\), so \(r^D<1/2\).
Consequently \(r^{N+1}<2^{-1024}\),
\(\tau<2^{-1033}\), and \(4\tau<1/3600\).
Using \(\pi<4\) in (S26) proves the strict, concrete certificate

\[
 \boxed{\|(q-f(U))\psi\|<1/1200.}                   \tag{S27}
\]

The commutation with \(f(U)\) then bounds continuous-time error by
\(|s|/1200\) for \(s=E_0t/\hbar\). At \(s=3\), the original
source contrast remains greater than \(1/50-6/1200=3/200\)
under \(E_0q\). The exact complete energy distributions of the two
settings still agree, because \(q\) is one fixed function of \(U\).

The [physical block construction](PHYSICAL_BLOCK.md) can use this degree
and its box half-width \(L=127N+3\). That construction supplies its
own finite-box error and occupation support account. Equation (S27)
alone is not a physical-locality theorem. The degree \(1024\cdot10^{25}\)
and the resulting region are enormous. This proof establishes a finite
passing instance and an existence bound; it supplies no practical
apparatus, efficient computation, thermal preparation, new source
admission, or identification with the separate 140-gate Hamiltonian.

## 7. Separate review obligations

Review must check: (1) the normalized source, receiver conjugation and
\(\beta\) shift; (2) exchange-odd rank-one contact reduction;
(3) the free Schur complement and cosine resolvent; (4) the contact
Möbius transform, quadratic and exterior root; (5) pole weight and both
momentum roots; (6) completeness and local differentiability of the
spectral measure; (7) every rational window and derivative bound;
(8) the complex radial bound, including the distant measure;
(9) rank-two source transfer, chord mass and reference uniformity;
(10) the layer-cake estimate, normalized Abel polynomial and explicit
integer inequalities; and (11) the finite-degree, physical-support and
unexecuted-computation boundaries. Same-session checks do not constitute
independent scientific acceptance.

# A smaller actual-source spectral bound by exact pole subtraction

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1782](https://github.com/mathorn1973/twist-j/issues/1782).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`d69ff34274ffce191055df7fd44e092366e20819`.
Independent scientific acceptance is not asserted.

Keep the original source, original unitary U_rec, receiver calibration,
memory/reference convention and energy cut of the contract. The frozen
[PR1781 spectral certificate](https://github.com/mathorn1973/twist-j/blob/5f7301e4d891596628cb25c6e735a7e4cd9004a8/notes/C-FINITE-OCCUPATION-ENERGY-N/SPECTRAL_CERTIFICATE.md)
supplies the exact object-port formula, its source-visible bound band,
and the rank-two token-pulse contact identity used below. These are
conditional candidate premises, not independently accepted inputs.
The source identities from PR1777 retain their own conditional scope.

The old estimate bounded a distant spectral arc by its distance from
the cut, producing a large imaginary-part allowance. Here the bound
pole is integrated exactly before taking absolute values. No spectral
or moment computation is used.

## 1. Exact subtraction of the source-visible pole

Use the exterior Caratheodory convention

\[
 F_{V,v}(\zeta)=\langle v,(\zeta+V)(\zeta-V)^{-1}v\rangle,
 \qquad |\zeta|>1.
\]

Let g=2pi/5, beta=4pi/5, omega_0=-beta. For the exchange-odd
object contact port, put

\[
 \lambda=e^{-i\omega},\quad C=\cos P,\quad c=\cos\omega,
 \quad \alpha=\omega-g,
\]
\[
 b=5c-4\cos\alpha,\qquad d=5c+4\cos\alpha,
 \qquad R^2=(C-5c)^2-16.
\]

The selected object-port formula from the predecessor is

\[
 F_B(P,\lambda)=\frac{R-4i\sin\alpha}{C-b}.        \tag{S1}
\]

This is the exterior continuation of the exact resolvent quadratic,
not an extension of a density formula by itself. Its coefficients are
analytic in omega, and the selected exterior root is specified below.
The polynomial identity

\[
 R^2+16\sin^2\alpha=(C-b)(C-d)
\]

gives the exact rationalization

\[
 \boxed{F_B(P,\lambda)
  =-\frac{8i\sin\alpha}{C-b}
    +\frac{C-d}{R-4i\sin\alpha}.}                 \tag{S2}
\]

There is no spectral projection or deletion of the pole in (S2): both
terms are retained in the full resolvent. Below their denominators are
nonzero on the exterior radial line, so the identity holds pointwise
there without a principal-value convention.

## 2. Exterior root and uniform complex bound

Fix h=1/1000 and 0<eta<=h. For the full-step radial parameter
zeta=1+eta, the object parameter is
lambda=e^(i beta)(1+eta)=exp(-i(omega_0+iu)), where

\[
 u=\log(1+\eta),\qquad 0<u\le h.
\]

Write a_0=cos(pi/5), s_0=sin(pi/5). The elementary brackets

\[
 4/5<a_0<5/6,\qquad 1/2<s_0<3/5
\]

give the exact identities on this radial line

\[
 c=-a_0\cosh u+i s_0\sinh u,
 \qquad \sin\alpha=s_0\cosh u-i a_0\sinh u,
\]
\[
 b=-a_0\cosh u+9i s_0\sinh u,
 \qquad d=-9a_0\cosh u+i s_0\sinh u.               \tag{S3}
\]

In particular Im b>0, so C-b is nonzero for every real C in [-1,1].
The imaginary part of the radicand is

\[
 \operatorname{Im}((C-5c)^2-16)
 =-10s_0\sinh u\,(C+5a_0\cosh u)<0.               \tag{S4}
\]

The last factor exceeds -1+5(4/5)=3. Therefore the selected square
root has Re R>0 and Im R<0. As u decreases to zero, it approaches the
positive real root on the continuum side and the negative imaginary
root on the gap side. These are exactly the predecessor's exterior
boundary choices. No alternative root is substituted in (S2).

For u<=1/1000, the exponential series gives
e^u<=1/(1-u)<=1000/999<101/100. Consequently

\[
 \cosh u<101/100,\qquad \sinh u<1/100.
\]

Here sinh u<e^u-1, since e^u+e^(-u)>2. Thus (S3) implies

\[
 |b|^2
 <\frac{25}{36}\left(\frac{101}{100}\right)^2
   +\frac{729}{25}\left(\frac1{100}\right)^2
 <\frac34,
\]
\[
 |\sin\alpha|
 <\frac35\frac{101}{100}+\frac56\frac1{100}<\frac23,
 \qquad
 |C-d|
 <1+9\frac56\frac{101}{100}+\frac35\frac1{100}<9. \tag{S5}
\]

Since Im R<0, the imaginary part of the second denominator in (S2)
is less than -4s_0 cosh u. Hence

\[
 |R-4i\sin\alpha|\ge4s_0\cosh u>2.               \tag{S6}
\]

The full free token source function is the momentum average

\[
 F_1(1+\eta)=\int_{-\pi}^{\pi}
     F_B(P,e^{i\beta}(1+\eta))\,\frac{dP}{2\pi}.
\]

For Im b>0, the elementary cosine resolvent identity is

\[
 \int_{-\pi}^{\pi}\frac{dP/(2\pi)}{b-\cos P}
   =\frac1{\Gamma(b)},\qquad \Gamma(b)^2=b^2-1,    \tag{S7}
\]

where Gamma is the analytic branch on the upper half-plane continued
from Gamma(b)/b tending to one at infinity. For example, substituting
w=e^(iP) reduces the integral to its one pole inside the unit circle;
the branch is fixed by the asymptotic integral 1/b. Inserting (S7) into
(S2) retains the entire bound-pole contribution explicitly:

\[
 F_1(1+\eta)=\frac{8i\sin\alpha}{\Gamma(b)}
  +\int_{-\pi}^{\pi}
       \frac{C-d}{R-4i\sin\alpha}\,\frac{dP}{2\pi}. \tag{S8}
\]

Since |Gamma(b)|^2=|b^2-1|>=1-|b|^2>1/4, equations (S5)-(S6)
bound the two terms separately by 32/3 and 9/2. Therefore

\[
 \boxed{|F_1(1+\eta)|<91/6<16,
        \qquad0<\eta\le1/1000.}                    \tag{S9}
\]

This bounds the full complex function. It is not inferred from a bound
on its real part or from a density estimate alone.

## 3. A stronger positive real-part bound

On the real angle window |omega-omega_0|<=h, the predecessor's rational
window bounds give

\[
 b<-791/1000,\quad |b|<1,\quad
 \sin\alpha>49/100.
\]

Thus sqrt(1-b^2)<5/8, since
1-(791/1000)^2<25/64. The source-visible bound-band density from that
same proof is

\[
 \rho_b(\omega)=\frac{4\sin\alpha}{\pi\sqrt{1-b^2}}
 >\frac{4(49/100)}{\pi(5/8)}>\frac3\pi.            \tag{S10}
\]

This is a positive component of the token source measure; all other
components contribute nonnegatively to its radial real part. No upper
bound or differentiability of the remainder is needed here.

For R_0=1+eta, the radial Poisson kernel is

\[
 P_{R_0}(t)=\frac{R_0^2-1}{R_0^2+1-2R_0\cos t}.
\]

Direct integration, using tan(t/2), gives its exact mass on the window:

\[
 \int_{-h}^h P_{R_0}(t)\,dt
  =4\arctan\left(\frac{2+\eta}{\eta}\tan\frac h2\right)
  >\pi.                                            \tag{S11}
\]

Indeed tan(h/2)>=h/2 and eta<=h make the argument strictly greater
than one. Combining (S10)-(S11) with the positive measure representation
of F_1 proves

\[
 \boxed{\operatorname{Re}F_1(1+\eta)>3,
        \qquad0<\eta\le1/1000.}                    \tag{S12}
\]

The factor pi in (S11) is a kernel integral, not an extra normalization
of the spectral density. The density rho_b is with respect to d omega,
as in the frozen predecessor.

## 4. The complete coupled source and the phase pair

For each conserved total momentum K, let F_2(K,zeta) be the free pulse
port function. Its real part is positive for |zeta|>1. The unchanged
rank-two contact identity from the predecessor is

\[
 F_{\rm src}(K,\zeta)
  =\frac{4F_1(\zeta)+F_2(K,\zeta)}
         {4+F_1(\zeta)F_2(K,\zeta)}.              \tag{S13}
\]

For t=F_1 and w=F_2,

\[
 F_{\rm src}=t+(1-t^2)\frac{w}{4+tw},\qquad
 \left|\frac{w}{4+tw}\right|
 =\frac1{|t+4/w|}\le\frac1{\operatorname{Re}t}<\frac13.
\]

We used Re(1/w)>0, which follows from Re w>0. Equations (S9) and
(S12) therefore imply, uniformly in K,

\[
 \boxed{|F_{\rm src}(K,1+\eta)|
   <16+\frac{16^2+1}{3}=\frac{305}{3}<128.}         \tag{S14}
\]

The localized original token seed has unit fiber weight. Averaging in
K preserves (S14). The receiver calibration is identity on this seed,
so its conjugation leaves this seed spectral law independent of the
old-memory/reference input.

If |1-z|<=eta, then |1+eta-z|<=2eta, and the radial Poisson kernel
at zeta=1+eta is at least 1/(2eta). Consequently

\[
 \mu_\chi\{|1-z|\le\eta\}<256\eta.               \tag{S15}
\]

For the unchanged normalized phase pair, the exact spectral multiplier
is

\[
 d\mu_{\psi_\pm}(z)
  =\frac{3-z^4-z^{-4}}Z\,d\mu_\chi(z),\qquad
 Z=\frac{39521+154\sqrt5}{15625}.
\]

The numerator is between 1 and 5 on the circle. Since
2*39521>5*15625, one has Z>5/2, and the multiplier is strictly less
than 2. Thus

\[
 \boxed{\mu_{\psi_\pm}\{|1-z|\le\eta\}
       <512\eta,\qquad0<\eta\le1/1000.}           \tag{S16}
\]

The bound includes any atom at the cut, so letting eta decrease to zero
again proves that the actual phase sources have no atom there. This is
a statement about the full original coupled source, not merely the free
translated limit. The source vectors, energy branch and cut value have
not been changed.

The common measure is independent of every admitted old-memory state
and arbitrary passive reference. Retained orthogonal settings, even
when correlated with that memory and reference, have the same measure
because the setting-block spectral probabilities add. All 26 memory
labels are admitted for this estimate. The separate 25-label condition
on fresh receiver writes is not broadened by it.

## 5. Scope and separate review obligations

Equation (S16) replaces the predecessor's sufficient constant
5*10^9 by 512 on the same chord-radius window. It is an upper bound,
not a fitted density or a claim that 512 is optimal. Its use in a
smaller polynomial or a physical interaction requires the separate
approximation and realization arguments of this successor.

The proof is analytical. No numerical integration, matrix expansion,
spectral search, moment enumeration or simulation was run. It does not
prove microscopic locality, preparation, readout, renewal or original
six-pentit derivation. No predecessor result receives wider acceptance.

Independent review should check separately:

1. The fixed source and exterior Caratheodory conventions, beta shift,
   and use of the exact predecessor object-port formula.
2. The pole subtraction identity (S2), including retention of both terms
   and the absence of denominator singularities on the radial line.
3. The root choice (S3)-(S4), the elementary complex bounds (S5)-(S6),
   the cosine integral branch, and the full complex estimate (S9).
4. The bound-band density normalization, rational lower bound (S10),
   exact Poisson-window integral and real-part estimate (S12).
5. The complete token-pulse contact identity and uniform estimate (S14),
   without discarding any pulse channel or exceptional total momentum.
6. The chord Poisson estimate, the sharper normalization Z>5/2, and
   the numerical constant 512 in (S16).
7. All-26-label memory and passive-reference uniformity, retained-setting
   coherence, no-cut-atom conclusion, and preservation of the unchanged
   energy/source/physical-scope boundaries.

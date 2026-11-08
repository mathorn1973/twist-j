# Prime-norm polarization classes on the full circle

Status: **NON-CANONICAL; proof-only classical specialization.**
No RH or GRH is assumed. Section 3 identifies the imported analytic
theorems; their original proofs are not reproduced here.

Throughout,
\[
F=\mathbb Q(\sqrt5),\quad \mathcal O_F=\mathbb Z[\phi],\quad
\phi=\frac{1+\sqrt5}{2},\quad L=\log\phi.
\]
The fixed geometric model is the principally polarized surface
\(B=\operatorname{Jac}(y^2=x^5-1)\), with endomorphism ring
\(\mathbb Z[\zeta_5]\) and Rosati involution equal to conjugation.
Its polarization/ideal dictionary [G] is an input, not a conclusion
of the analytic argument.

## 1. Statement and conventions

The narrow class number is \(h_F^+=1\). Choose a totally positive
generator \(\eta\) of a fractional ideal \(\mathfrak a\), and define
\[
t(\mathfrak a)=\frac12\log\frac{\sigma_1\eta}{\sigma_2\eta}\pmod{2L},
\qquad \theta(\mathfrak a)=\frac{t(\mathfrak a)}{2L}\in\mathbb R/\mathbb Z.
\tag{1}
\]
Positive generators differ by \(\phi^{2k}\), so this is well-defined.
Haar measure has total mass one. Conjugate ideals are counted separately.

**Theorem 1.** Fix \(0<a,b<1/5\) and \(0<\nu<1/3\). Set
\(h=X^{1-b}\), \(r=X^{-a}\), and
\[
I_X(\theta_0)=\{\theta:\|\theta-\theta_0\|_{\mathbb R/\mathbb Z}<r\}.
\]
For sufficiently large \(X\), this arc has measure \(2r<1\).
There is \(c>0\) such that, uniformly in \(\theta_0\),
\[
\sum_{\substack{\mathfrak p\ {\rm prime},\ N\mathfrak p=p\ {\rm prime}\\
 X\le p<X+h,\ \theta(\mathfrak p)\in I_X(\theta_0)}}\log p
 =
 2X^{1-a-b}\left(1+O_{a,b,\nu}(e^{-c(\log X)^\nu})\right),
\tag{2}
\]
\[
\#\{\mathfrak p\text{ in (2)}\}
 =
 \frac{2X^{1-a-b}}{\log X}
 \left(1+O_{a,b,\nu}(e^{-c(\log X)^\nu})\right).
\tag{3}
\]
The fixed field and character basis are allowed in the constants.

Under [G], this is also the number of
\(\operatorname{Aut}(B,0)\)-classes of polarizations with \(D^2/2=p\)
and the stated angular condition. They all have type \((1,p)\).

The center may depend arbitrarily on \(X\), by Section 8.
This uniformity is a consequence of the proof, not a quotation of
[K, Theorem 1.1], whose center is fixed.
The bounds on \(a,b\) are strict. Neither the endpoint \(1/5\) nor
an exponent \(0.235\) on the full circle is asserted.

## 2. The full character family

Set
\[
\epsilon_m\in\{0,1\},\quad \epsilon_m\equiv m\pmod2,\qquad
\mu_m=\frac{\pi m}{2L},
\]
\[
\Xi_m((\alpha))=
 \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^m
 \left|\frac{\sigma_1\alpha}{\sigma_2\alpha}\right|^{i\mu_m}.
\tag{4}
\]
For a positive generator this becomes
\[
\Xi_m(\mathfrak a)=e^{2\pi i m\theta(\mathfrak a)}.
\tag{5}
\]

The definition in [K, Section 1.1, printed p. 2] uses totally positive
principal generators. With finite modulus \((1)\), the norm-neutral
archimedean exponents satisfy \(v_1+v_2=0\). Its character on positive
generators therefore has the form
\[
\lambda((\eta))=
 \left(\frac{\sigma_1\eta}{\sigma_2\eta}\right)^{iv}.
\]
Positive-unit invariance is equivalent to
\[
e^{4iLv}=1
 \quad\Longleftrightarrow\quad v=\frac{\pi m}{2L},\quad m\in\mathbb Z.
\tag{6}
\]
Since \(h_F^+=1\), this determines the ideal character uniquely.
Making a general generator positive by multiplication by a unit
recovers the sign in (4). There is no additional nontrivial narrow
class character.

The full multiplicative basis in [K] may thus be chosen as
\(\lambda_1=\Xi_1\), whose powers include the odd modes.
Choosing \(\Xi_2\) selects an index-two subfamily, observing
\(\theta\) modulo \(1/2\) and rapidity modulo \(L\).

Every \(\Xi_m\) has finite conductor \((1)\); for odd \(m\), both real
places occur in the sign modulus. Those signs belong to the complete
character even when the finite-order narrow class character in [K]
is trivial. Equal finite conductors alone would not establish odd-mode
density. We use the full-family statement of the cited theorem.

## 3. Analytic inputs and normalization

Write \(L_m(s)=L_F(s,\Xi_m)\). The normalization [N] gives
\[
\Lambda_m(s)=5^{s/2}
 \Gamma_{\mathbb R}(s+\epsilon_m+i\mu_m)
 \Gamma_{\mathbb R}(s+\epsilon_m-i\mu_m)L_m(s),\qquad
\Lambda_m(s)=\Lambda_{-m}(1-s)=\Lambda_m(1-s).
\tag{7}
\]
Its root number is \(+1\). For \(m\ne0\), \(L_m,\Lambda_m\) are entire.
For \(m=0\), \(L_0=\zeta_F=\zeta L(\,\cdot\,,\chi_5)\) has a simple
pole at one. This pole supplies the main term.

The literature inputs are:

1. **Zero-free region:** [K, Theorem 2.5, printed p. 10] applies to
   the full family of its Section 1.1. For sufficiently large
   \(V=\max(|m|,|\Im s|)\), its width has order
   \((\log V)^{-2/3}(\log\log V)^{-1/3}\), with fixed finite conductor.
   A possible exceptional zero is confined to a real finite-order
   character, thus the principal mode here, and is fixed.

2. **Density:** [K, Theorem 2.6, printed p. 10] specializes to
   \[
   \sum_{|m|\le T}N_m(\sigma,T)
       \ll T^{5(1-\sigma)}(\log T)^B,\qquad
       0\le\sigma\le1,\ T\ge2.
   \tag{8}
   \]
   Here \(N_m\) counts nontrivial zeros with multiplicity in
   \(\Re s\ge\sigma,\ |\Im s|\le T\). The exponent is \(5n/2=5\)
   for \(n=[F:\mathbb Q]=2\). The finite-order character is fixed
   to the trivial narrow class character, while \(m\) runs through
   every integer.

3. **Local zero count and explicit formula:** [K, Lemma 2.7 and
   equation (10), printed p. 11]. The local zero count is per
   \(L_m\), at sufficiently large height:
   \[
   \#\{\rho:|\Im\rho-T|<1\}\ll\log(2+|T|+|m|).
   \tag{9}
   \]
   A sum over modes has the additional factor \(O(M)\).
   We shift the contour separately for each mode and then sum;
   no common contour gap for the whole family is assumed.

4. **Interval approximation:** [K, Theorem 2.2 and Lemma 2.3,
   printed p. 8] give the one-dimensional periodic Selberg
   majorants and minorants used below.

The first two statements are attributed in [K] to Coleman.
Their original proofs were not independently audited in this module.
Constants may depend on the fixed field and basis; fixed rescalings
of the frequency cutoff only affect constants.

Two explanatory details of [K] need correction in this specialization.
After equation (7), printed p. 9, real gamma parities are assigned
only to the finite-order character. Here both equal \(\epsilon_m\).
The trivial-zero discussion on printed p. 12 does not accommodate
their imaginary shifts \(\pm\mu_m\).
We use (7) and the direct trivial-zero bound below instead.
These corrections do not change the full family specified in
[K, Section 1.1 and Theorems 2.5--2.6].

## 4. Radial and angular approximation

Choose fixed
\[
\max(a,b)<\tau'<\tau<\frac15,\qquad
M=\lfloor X^\tau\rfloor,\qquad u=X^{1-\tau'}.
\tag{10}
\]
Then \(u=o(h)\) and \(M^{-1}=o(r)\).

Choose nonnegative smooth cutoffs \(g^-,g^+\), bounded by one,
with \(g^-\le\mathbf1_{[X,X+h)}\le g^+\).
The lower cutoff is supported inside the norm window, the upper
inside its \(u\)-enlargement. Away from transition intervals of length
\(O(u)\), the cutoffs equal one on their respective interiors, and
\[
\int g^\pm(y)\,dy=h+O(u),\qquad
|(g^\pm)^{(j)}(y)|\ll_j u^{-j}.
\]
Their supports have length \(O(h)\) and lie in \([X/2,2X]\) for
large \(X\). The Mellin transforms \(G^\pm\) are entire, with
\[
|G^\pm(\sigma+it)|\ll hX^{\sigma-1}\qquad(0\le\sigma\le1).
\]
In the high-height range, integration by parts gives
\[
|G^\pm(\sigma+it)|
 \ll_\ell h u^{-\ell}X^{\sigma+\ell-1}(1+|t|)^{-\ell}.
\tag{11}
\]

Let \(F^-\le\mathbf1_{I_X(\theta_0)}\le F^+\) be the real
trigonometric approximants, with
\[
F^\pm(\theta)=\sum_{|m|\le M}c_m^\pm e^{2\pi i m\theta},\qquad
c_0^\pm=2r+O(M^{-1}),\qquad |c_m^\pm|\ll r+M^{-1}\ll r.
\tag{12}
\]
The coefficient bounds are uniform under interval translation.

Put \(\Lambda_F(\mathfrak q^k)=\log N\mathfrak q\) for prime ideals
and \(k\ge1\), and zero otherwise. For
\[
S(X,I)=\sum_{\mathfrak a}\mathbf1_{[X,X+h)}(N\mathfrak a)
       \mathbf1_I(\theta(\mathfrak a))\Lambda_F(\mathfrak a)
\]
positivity gives
\[
\sum_{\mathfrak a}g^-(N\mathfrak a)F^-(\theta(\mathfrak a))
                 \Lambda_F(\mathfrak a)
 \le S(X,I)\le
\sum_{\mathfrak a}g^+(N\mathfrak a)F^+(\theta(\mathfrak a))
                 \Lambda_F(\mathfrak a).
\tag{13}
\]
A negative minorant outside the arc causes no difficulty: the radial
minorant is nonnegative and supported in the norm window.
Endpoint choices are addressed in Section 8.

## 5. Exact explicit formula

For \(\Re s>1\),
\[
-\frac{L_m'}{L_m}(s)
 =\sum_{\mathfrak a}\Lambda_F(\mathfrak a)\Xi_m(\mathfrak a)
                    (N\mathfrak a)^{-s}.
\]
Mellin inversion and the cited smoothed contour argument give
\[
\sum_{\mathfrak a}g(N\mathfrak a)\Xi_m(\mathfrak a)\Lambda_F(\mathfrak a)
 =\mathbf1_{m=0}G(1)
   -\sum_{\rho\ {\rm nontrivial}}G(\rho)-T_m(G).
\tag{14}
\]
The zeros carry multiplicity. This integrates the logarithmic
derivative of the finite \(L_m\), not its completion.

For \(m\ne0\), the simple trivial zeros in [N] give
\[
T_m(G)=\sum_{k\ge0}
 \left(G(-\epsilon_m-2k+i\mu_m)+G(-\epsilon_m-2k-i\mu_m)\right).
\tag{15}
\]
For \(m=0\), \(\zeta_F\) has a simple zero at zero and double zeros
at negative even integers. Thus
\[
T_0(G)=G(0)+2\sum_{k\ge1}G(-2k).
\tag{16}
\]
The zero at zero is counted exactly once in (16).
There is no additional residue from the entire function \(G\).
The sole pole of the finite \(L_0\) already contributes \(G(1)\).
Rapid Mellin decay and the local zero estimates justify the sums.

Multiplying by \(c_m^\pm\) and summing, the principal contribution is
\[
c_0^\pm G^\pm(1)=2rh+
 O\left(rh\left(X^{b-\tau'}+X^{a-\tau}\right)\right).
\tag{17}
\]

## 6. Zero estimates

### 6.1 Low nontrivial zeros

First handle bounded parameters. Euler products give, for \(\sigma>1\),
\[
\zeta_F(\sigma)^3 |L_m(\sigma+it)|^4
                  |L_{2m}(\sigma+2it)|\ge1,
\tag{18}
\]
using \(3+4\cos v+\cos2v=2(1+\cos v)^2\ge0\).
For \(m\ne0\), both twisted functions are entire.
A zero at \(1+it\) would force the left side to zero as
\(\sigma\downarrow1\), a contradiction.
For \(m=0,t\ne0\), the same proof applies; for \(m=t=0\), the
Dedekind zeta function has a pole.
Hence there are no zeros on \(\Re s=1\).
Finitely many modes in a fixed compact height range therefore have a
fixed positive zero gap from that line.

Set
\[
Z_{\rm low}=
 \sum_{|m|\le M}\sum_{\substack{\rho\ {\rm nontrivial}\\|\Im\rho|\le M}}
                 X^{\Re\rho-1}.
\]
The functional equation (7) pairs \(\rho\) with \(1-\rho\) in the
same \(L_m\), preserving multiplicity and absolute height.
Thus \(Z_{\rm low}\) is at most twice its part with \(\Re\rho\ge1/2\).

Outside bounded parameters, the zero-free input bounds the zeros by
\(\Re\rho\le1-\eta_M\), where
\[
\eta_M=\frac{c_0}{(\log M)^{2/3}(\log\log M)^{1/3}}
\]
for a sufficiently small fixed \(c_0>0\).
The finitely many bounded cases, including any fixed exceptional zero,
contribute \(O(X^{-\kappa})\) for a fixed \(\kappa>0\).

For \(\beta\ge1/2\), use the elementary identity
\[
X^{\beta-1}=X^{-1/2}
       +(\log X)\int_{1/2}^{\beta}X^{\sigma-1}\,d\sigma.
\]
After summation, (8) bounds the initial term by
\(O(X^{-1/2}M^{5/2}(\log M)^B)\), and the integral term by
\[
(\log X)(\log M)^B
 \int_{1/2}^{1-\eta_M}X^{\sigma-1}M^{5(1-\sigma)}\,d\sigma.
\tag{19}
\]
The integrand is at most \(X^{-(1-5\tau)(1-\sigma)}\).
Both \(1-5\tau>0\) and \(-1/2+5\tau/2<0\).
Also \(\eta_M\log X\) has order
\((\log X)^{1/3}/(\log\log X)^{1/3}\).
For each fixed \(0<\nu<1/3\), absorption of logarithmic factors gives
\[
Z_{\rm low}\ll e^{-c(\log X)^\nu}.
\tag{20}
\]
By (11)--(12), this contributes
\(O(rh e^{-c(\log X)^\nu})\) to the smoothed sums.

The summation identity above is derived explicitly; no displayed
partial-summation equality from [K, equation (14)] is needed.

### 6.2 High nontrivial zeros

For \(|\gamma|>M\), \(0<\beta<1\), (11) yields
\[
|G(\beta+i\gamma)|\ll_\ell h u^{-\ell}X^\ell|\gamma|^{-\ell}.
\]
Summing the per-mode bound (9) over \(O(M)\) modes and both signs
of the height gives
\[
\begin{aligned}
\sum_{|m|\le M}|c_m|\sum_{|\gamma|>M}|G(\beta+i\gamma)|
 &\ll_\ell rh\,u^{-\ell}X^\ell
     M\int_M^\infty t^{-\ell}\log(2+t+M)\,dt\\
 &\ll_\ell rh\,X^{2\tau-\ell(\tau-\tau')}\log X.
\end{aligned}
\tag{21}
\]
Choose an integer \(\ell>2\tau/(\tau-\tau')\).
This is a negative power of \(X\) relative to \(rh\).

### 6.3 Trivial zeros

The support bound gives directly
\[
|G(-\epsilon_m-2k\pm i\mu_m)|
 \ll h(X/2)^{-1-\epsilon_m-2k}.
\]
Summing in \(k\) proves \(|T_m(G)|\ll h/X\), uniformly for \(m\ne0\).
Equation (16) gives the same bound for \(m=0\).
Consequently
\[
\sum_{|m|\le M}|c_m T_m(G)|\ll rh\,M/X.
\tag{22}
\]
No real-axis assumption about the nonprincipal trivial zeros occurs.

### 6.4 Removing the approximations

All errors in (17), (21), (22) are fixed negative powers of \(X\)
relative to \(rh\). They are absorbed by (20) after reducing \(c\).
The sandwich (13) proves
\[
S(X,I_X(\theta_0))
 =2rh\left(1+O_{a,b,\nu}(e^{-c(\log X)^\nu})\right).
\tag{23}
\]
No inclusion--exclusion identifying conjugate ideals was performed.

## 7. Prime norms and polarization classes

Proper prime-ideal powers and prime ideals of residue degree two have
total logarithmic weight, even globally up to norm \(2X\), bounded by
\[
O(\sqrt X\log X).
\tag{24}
\]
There are at most two prime ideals over a rational prime.
Every excluded term has norm \(p^j\), \(j\ge2\), and weight at most
\(2\log p\). It suffices to bound
\[
\sum_{j=2}^{\lfloor\log_2(2X)\rfloor}
 \sum_{p\le(2X)^{1/j}}\log p\ll\sqrt X\log X.
\]
For \(j=2\), count integers; the terms \(j\ge3\) are
\(O(X^{1/3}(\log X)^2)\), which are absorbed for large \(X\).

Relative to \(rh=X^{1-a-b}\), (24) is
\(O(X^{a+b-1/2}\log X)\).
Since \(a+b<2/5\), it is negligible in (23).
The ramified prime ideal of norm five is outside the window for
large \(X\). This proves (2).

For \(X\le p<X+h\),
\[
\log X\le\log p\le\log X+O(X^{-b}).
\]
Positivity permits division between these bounds, yielding (3).
The extra relative error \(O(X^{-b}/\log X)\) is absorbed.

By [G], every such prime ideal gives one polarization class with
\(D^2/2=p\). For elementary divisors \(d_1\mid d_2\), their product
is \(p\), so \(d_1=1,d_2=p\). The classes are primitive.
Two ideals above a split prime give two distinct classes;
there is no additional division by two.

## 8. Centers, endpoints and units

Translation of the interval multiplies \(c_m\) by
\(e^{-2\pi i m\theta_0}\). All bounds use only \(|c_m|\) and its
unchanged constant coefficient. The radial cutoffs do not depend on
the center. This proves uniformity for arbitrary \(\theta_0(X)\),
including arcs crossing zero.
Using one interval avoids center-dependent polytope intersections
needed when deduplicating rational primes.

Two prime ideals of rational-prime norm can have equal \(\theta\)
only if they are equal. Adjust one positive generator by a positive
unit. Their quotient then has equal real embeddings, so lies in
\(\mathbb Q_{>0}\). The ratio of the two prime norms is its square.
A ratio of rational primes is a rational square only when the primes
are equal; the positive quotient is then one and the ideals coincide.
Each angular endpoint contains at most one such ideal.
Changing endpoint conventions alters (3) by at most two and (2) by
\(O(\log X)\), both negligible.

The radius \(X^{-a}\) is in \(\theta=t/(2L)\)-units, hence its
rapidity radius is \(2LX^{-a}\).
If the radius \(X^{-a}\) is instead measured directly in \(t\),
its normalized length is \(X^{-a}/L\) and the leading constant is
\(1/L\). Fixed multiples of the angular length are allowed by the
proof: normalized length \(c_I X^{-a}\) gives constant \(c_I\).

The theorem counts classes rather than distinct represented rational
primes. At the conjugation fixed centers \(0,1/2\), the symmetric arc
contains conjugate ideals together, so the rational-prime count is
half the class count for large \(X\).
Elsewhere a sufficiently small arc need not contain both.
The rational-prime constant in [K, Theorem 1.1] cannot replace the
ideal constant derived here without checking this overlap.

## 9. Consequences and limits

The main term tends to infinity. For all sufficiently large \(X\),
uniformity implies that every arc of the specified radius contains
prime-norm polarization classes in the specified short norm window.

This gives a literature-based theorem for individual arcs on the full
\(2L\) circle. It does not transfer Baier--Roy's stronger angular
exponent, prove a growing-mode reciprocal-\(L\) estimate, establish
relative-norm reachability, construct transition probabilities or
the native operator \(U\), or prove RH.

## References and immutable inputs

- **[K]** T. Khale, C. O'Kuhn, A. Panidapu, A. Sun, S. Zhang,
  *A Bombieri--Vinogradov Theorem for primes in short intervals and
  small sectors*, [arXiv:2008.09677v3](https://arxiv.org/pdf/2008.09677v3),
  12 January 2022. This version was examined; journal typesetting
  was not separately compared.
  [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records the admitted source identities and external theorem locations.

- **[N]** [Public normalization of Xi_m](https://github.com/mathorn1973/twist-j/blob/655e022d0ef95ee94681464d3325d2aa589df1d6/notes/C-RH-CM5-HECKE-DICTIONARY-N/HECKE_MAASS_BRIDGE.md).
  It supplies the completion, principal-mode exception and exact
  trivial-zero orders at the pinned public comparison revision.

- **[G]** [Public polarization/ideal correspondence](https://github.com/mathorn1973/twist-j/blob/655e022d0ef95ee94681464d3325d2aa589df1d6/notes/C-RH-CM5-HECKE-DICTIONARY-N/CM5_POLARIZATIONS.md).
  Only the fixed-model geometric dictionary and positive-unit/narrow-class
  facts are imported. Selection of this model from the original
  TWIST operator is not asserted.

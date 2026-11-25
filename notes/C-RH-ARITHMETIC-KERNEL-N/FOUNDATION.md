# Foundation for the one-sided rational window criterion

C-RH-ARITHMETIC-KERNEL-N. NON-CANONICAL, no authority. Candidate-D.
This retains the relevant analytic foundation from the same-session
C-RH-2D-SYNTHESIS-N packet, previously reviewed by root, Astra and Sol.
It is included to make the new tail criterion self-contained. General
oscillation methods and the classical RH/Mertens equivalence are not claimed
as novel. The new arithmetic cutoff is in KERNEL.md.

## 1. A signed power-window lemma


Let \(f:[0,\infty)\to\mathbb R\) be measurable and satisfy \(|f(u)|\le B e^{A u}\). Suppose its Laplace transform \(F(s)=\int_0^\infty f(u)e^{-su}\,du\), initially for \(\Re s>A\), extends meromorphically to \(\Re s>\theta\) and has no pole on the real axis there. We can increase \(A\) so that \(A>\theta\).

If \(F\) has any pole in \(\Re s>\theta\), then for every \(\lambda>1\) there are \(c_0,\eta>0\) and \(L_0\) such that, for both signs and all \(L\ge L_0\),
\[
 \int_L^{\lambda L}(\pm f(u))_+e^{-\theta u}\,du\ge c_0 e^{\eta L}.
\]
In particular, each sufficiently late interval \([L,\lambda L]\) contains points of both signs at which \(\pm f(u)> C e^{\theta u}\), for every fixed \(C\ge0\). The two points may differ.

**Proof.** Fix \(1<\alpha<\lambda\). Choose a real \(c>A\) sufficiently large, with the fixed choices specified below, and set \(a=c-\theta\), \(b=c-A\). The disk \(|s-c|<a\) is inside the half-plane of continuation. For a given pole \(\rho=\beta+i\gamma\) with \(\beta>\theta\), the inequality \(|c-\rho|<a\) holds for all sufficiently large \(c\), by squaring and using \(\beta>\theta\). Fix \(c\) so that this holds.

Let \(R<a\) be the minimum distance from \(c\) to a pole. There are finitely many nearest poles \(\rho_j\), and a radius \(R_1\) strictly between \(R\) and \(a\) such that the closed disk of radius \(R_1\) has no other poles. Let \(m\ge1\) be the largest order among these poles. In the Taylor expansion of \(F(c-z)\), denote the coefficient of \(z^k\) by \(A_k\). Differentiation under the absolutely convergent integral gives
\[
 A_k=\frac1{k!}\int_0^\infty f(u)u^k e^{-cu}\,du.
\]
Subtract the full principal parts at the nearest poles and apply Cauchy's coefficient estimate to the remainder in the \(z\)-disk of radius \(R_1\). A pole term \(b_{jh}(s-\rho_j)^{-h}\) contributes \(b_{jh}(c-\rho_j)^{-k-h}\binom{k+h-1}{h-1}\). It follows that
\[
 A_k=R^{-k}k^{m-1}\bigl(P(k)+O(k^{-1})\bigr),\qquad
 P(k)=\sum_{j:\,m_j=m}D_j z_j^k,\qquad z_j=R/(c-\rho_j).
\]
Here \(D_j=b_{jm}(c-\rho_j)^{-m}/(m-1)!\ne0\), the \(z_j\) are distinct unit complex numbers, and none is \(1\) because there is no real pole. Conjugation symmetry of \(F\) follows from reality of \(f\) in the original half-plane and uniqueness of continuation, so \(P(k)\) is real. The estimate includes \(m=1\), where Cauchy's remainder is exponentially smaller.

Write \(D=\sum_j|D_j|\), \(H=\sum_j|D_j|^2>0\). Averaging over any consecutive block of length \(K\), the geometric-sum formula gives \(|\operatorname{avg} P|=O(1/K)\) and \(\operatorname{avg} P^2=H+O(1/K)\), uniformly in the first index. The latter uses \(P^2=|P|^2\) and that \(z_i\overline{z_j}\ne1\) for \(i\ne j\). Fix \(K\) large enough that \(|\operatorname{avg}P|\le H/(4D)\) and \(\operatorname{avg}P^2\ge H/2\). Since \(|P|\le D\), \(\operatorname{avg}|P|\ge H/(2D)\), so both \(\operatorname{avg}(\pm P)_+\ge H/(8D)\). Consequently, every sufficiently late block of length \(K\) contains indices \(k_+,k_-\) with
\[
 \pm A_{k_\pm}\ge \frac{H}{16D}\,R^{-k_\pm}k_\pm^{m-1}.
\]

It remains to show that such a block can be tested using only the chosen interval for \(u\). Put
\[
 t_-=(1+1/\alpha)/2<1,\qquad t_+=(1+\lambda/\alpha)/2>1,
 \qquad \delta=\min_{t\in\{t_-,t_+\}}(t-1-\log t)>0 .
\]
Make the original choice of \(c\) large enough also that \(b\lambda/(a\alpha)>t_+\) and \(\log(a/b)<\delta/2\). This is possible because \(b/a\to1\). The block length \(K\) is fixed only after \(c\) has been fixed. For \(k=\lfloor\alpha aL\rfloor+j\), \(0\le j<K\), and \(n=k+1\), we have \(bL/n<t_-\) and \(b\lambda L/n>t_+\) uniformly for all sufficiently large \(L\).

For a Gamma variable \(U\) of integer shape \(n\) and rate \(1\), \(\mathbb E e^{vU}=(1-v)^{-n}\) for \(v<1\). Markov's inequality with \(v=1-1/t\) bounds the lower tail for \(t<1\) or the upper tail for \(t>1\) at \(nt\) by \(\exp[-n(t-1-\log t)]\). Substitution \(w=bu\) in the integral and normalization by \(k!\) therefore give
\[
 \frac{1}{k!}\int_{[0,\infty)\setminus[L,\lambda L]}
       |f(u)|u^k e^{-cu}\,du
 \le 2B b^{-n} e^{-\delta n}
 \le 2B a^{-n}e^{-\delta n/2}.
\]
Inside the interval, \(e^{-au}(au)^k/k!\le1\), by the exponential series. Thus for either sign and \(k=k_\pm\),
\[
 \frac{H}{16D}\,R^{-k}k^{m-1}
 \le \pm A_k
 \le a^{-k}\int_L^{\lambda L}(\pm f(u))_+e^{-\theta u}\,du
         +2B a^{-(k+1)}e^{-\delta(k+1)/2}.
\]
Multiplying by \(a^k\) and using \(k=\alpha aL+O(1)\), \(a/R>1\), proves the claim with \(\eta=\alpha a\log(a/R)>0\) and a reduced positive constant \(c_0\). If \(\pm f(u)\le C e^{\theta u}\) on the interval, the integral is at most \(C(\lambda-1)L\), contradicting the lower bound for large \(L\). This proof uses neither simple poles nor a unique nearest pole.

## 2. Exact coefficient unit and real-axis regularity


Set \(s_5(d)=(-2)^{\omega(d)}\) on squarefree split integers and zero elsewhere. Define the signed split-residue statistic
\[
 T(x)=\sum_{d\le x}s_5(d)S_\chi(x/d).
\]
It is the difference of the two **signed** sums selected by residues \(1\) and \(3\) of \(\lfloor x/d\rfloor\). Its Dirichlet coefficient series is \(L(s,\chi) S_5(s)\), with \(S_5(s)=\prod_{p\ {\rm split}}(1-2p^{-s})\), initially for \(\Re s>1\). The exact local factors of \(U\) in
\[
 \zeta(s)^{-1}=U(s)L(s,\chi)S_5(s)
\]
are, in the order split, inert, ramified,
\[
 \frac{(1-t)^2}{1-2t},\quad 1-t^2,\quad 1-t,\qquad t=p^{-s}.
\]
At split primes \(U_p=1+t^2/(1-2t)\), \(U_p^{-1}=1-t^2/(1-t)^2\), and \(p\ge11\). The other two factors are explicit. Both \(U,U^{-1}\) therefore have absolutely summable coefficients at every real \(\sigma>1/2\), since \(2p^{-\sigma}\le2/\sqrt{11}<1\) at split primes and their deviations in degree \(2\) are summable. They are reciprocal holomorphic nonvanishing functions on \(\Re s>1/2\). For \(\theta>1/2\), convolution in each direction transfers a bound \(O(x^\theta)\) from \(T\) to \(M\) and back, with a constant bounded by the appropriate absolute series at \(\theta\).

For the one-sided **window** criterion, use the common pole structure directly. Since \(|s_5(d)|\le(1*\chi)(d)\), \(|T(x)|\le x\). Its Laplace transform after \(x=e^u\) is \(1/(s\zeta(s)U(s))\), with all the same poles as \(1/(s\zeta(s))\) on \(\Re s>1/2\). The lemma thus applies to \(T\) too. It does not rely on convolution preserving individual windows. The split-residue weight is essential to this statement. Dropping \(L(s,\chi)\) from the coefficient series leaves the reciprocal of \(\zeta(s)L(s,\chi)U(s)\), sensitive to additional zeros of \(L(s,\chi)\), as in the public Dedekind route. The inert Euler factors alone constitute an absolutely summable unit above the critical line. The signed balance still needed lies among products of split primes after the residue weighting.


For completeness, the coefficients t=chi*s_5 have the exact local values
t(p^k)=-1 at split primes, t(p^k)=(-1)^k at inert primes, and t(5^k)=0,
for every k>=1. Consequently |t(n)|<=1. The transform of T(e^u) is
1/(s zeta(s) U(s)). It has no real poles for s>1/2: for 0<s<1 the
alternating series eta(s) is positive by pairing successive terms, and
zeta(s)=eta(s)/(1-2^(1-s)) is nonzero. At s=1 its reciprocal has a zero,
and for s>1 the Euler product is nonzero. U and U inverse are holomorphic
in the half-plane under consideration. A zero of zeta there is therefore
a pole of exactly the same multiplicity in this transform.

## 3. Exact rational criterion

For integer Y>=2 put

    Q_T(Y)=sum_{n=Y}^{Y^2-1} max(T(n),0)^2/[n(n+1)].

Then RH is equivalent to the following statement W(T): for every integer
r>=1 and every Y0>=1, some integer Y>=max(2,Y0) satisfies Q_T(Y)^r<=Y.
The negative part alone has the same equivalence.

Extend T by T(x)=T(floor x). Exact integration on each unit interval gives
Q_T(Y)=integral_Y^(Y^2) T(x)_+^2 x^-2 dx. If RH fails, the functional
equation gives a zero of real part beta>1/2. Choose theta between 1/2 and
beta, and apply section 1 with f(u)=T(e^u), lambda=2. On every sufficiently
late window, for some c,eta>0,

    I_theta(Y)=integral_Y^(Y^2) T(x)_+ x^(-1-theta) dx >= cY^eta.

Cauchy-Schwarz yields

    I_theta(Y)^2 <= Q_T(Y) integral_Y^(Y^2) x^(-2theta) dx
                  <= Q_T(Y)Y^(1-2theta)/(2theta-1).

Thus Q_T(Y)>=c^2(2theta-1)Y^delta, delta=2eta+2theta-1>0. One fixed
integer r>1/delta then excludes every sufficiently large Y, contrary to
W(T). This lower bound concerns the positive part, not just absolute value.

Conversely the classical RH/Mertens theorem gives M(x)=O_epsilon(x^(1/2+epsilon))
for every epsilon>0 under RH. The absolutely convergent coefficient series
of U inverse transfers it to T by convolution. Hence

    Q_T(Y) <<_epsilon integral_Y^(Y^2) x^(-1+2epsilon) dx
           <<_epsilon Y^(4epsilon).

For prescribed r choose epsilon=1/(8r). Then Q_T(Y)^r<=C_r Y^(1/2)<=Y
for every sufficiently large Y. This proves all stated quantifiers.
Convolution is used only for the all-argument converse. It is not assumed
to preserve an individual good window.

## Sources and boundaries

- Fujisawa and Minamide, Theorem 1.3 with number field Q, for the classical
  RH/Mertens equivalence: https://arxiv.org/pdf/1212.4348 .
- Kaczorowski and Pintz, Oscillatory properties of arithmetical functions I
  (1986), antecedent for power-window oscillation:
  https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf .
- Pintz, Oscillatory properties of M(x), I:
  https://matwbn.icm.edu.pl/ksiazki/aa/aa42/aa4214.pdf .

This is an equivalence and an analytic obstruction, not an arithmetic proof
of W(T). The independent arithmetic target is explicitly retained as O.

# Signed augmentation on the finite rapidity span

**NON-CANONICAL. Authority none.** The paper deductions below are **candidate-D**. The arithmetic estimate in the final section is **O**. This note uses the integral rapidity lift of Public Canon v117. It concerns a mathematical transfer, with action layer `NOT_APPLICABLE`.

## 1. The actual span and its sharp augmentation norm

Let \(P_N\) be the set of split primes at most \(N\). Let \(\mathcal D\) consist of squarefree products of split primes, including \(1\), and write \(\omega(d)\) for the number of prime factors. Define

\[
E_d=\prod_{p\mid d}(X_p+X_p^{-1}),\qquad
w(d)=\mathbf 1_{\mathcal D}(d)2^{\omega(d)},\qquad D(x)=\sum_{d\le x}w(d).
\]

Equip the Laurent polynomials in the formal independent \(X_p\) with the monomial coefficient inner product, linear in its first argument. Let \(\mathcal H_N\) be the span of the actual rows \(\boldsymbol\mu(n)\), \(1\le n\le N\). The canonical local factors give

\[
\boldsymbol\mu(d)=\prod_{p\mid d}(1-X_p-X_p^{-1})
=\sum_{e\mid d}(-1)^{\omega(e)}E_e
\qquad(d\in\mathcal D).
\]

This divisor change of basis is triangular with diagonal entries \(\pm1\). Every actual row with arbitrary \(n\le N\) belongs to the span of the \(E_d\) with \(d\mid n\), by the same local factors, including the split prime-power factors \(2-X_p-X_p^{-1}\). Therefore

\[
\mathcal H_N=\bigoplus_{d\in\mathcal D,\ d\le N}\mathbf C E_d.
\]

The norms and evaluations of the basis vectors satisfy \(\|E_d\|^2=w(d)\) and \(\operatorname{aug}(E_d)=w(d)\). Distinct \(d\) give disjoint monomial supports. The monomial support of the whole space consists of the exponent words \(e\in\{-1,0,1\}^{P_N}\) for which \(\prod_{e_p\ne0}p\le N\). Its size is \(D(N)\), while the dimension of the inversion-symmetric space \(\mathcal H_N\) is \(|\mathcal D\cap[1,N]|\). The vector representing augmentation is

\[
k_N=\sum_{d\in\mathcal D,\ d\le N}E_d,
\qquad \operatorname{aug}(f)=\langle f,k_N\rangle,
\qquad \|\operatorname{aug}\|_{\mathcal H_N\to\mathbf C}^2=\|k_N\|^2=D(N).
\]

The last equality is sharp by taking \(f=k_N\) inside the actual span.

### Growth of the squared norm

Let \(\chi=\chi_5\), \(H(m)=\sum_{j\le m}\chi(j)\) for nonnegative integers \(m\), and \(a_F=1*\chi\), the canonical ideal count. The sequence \(H\) has period five with values \((0,1,0,-1,0)\). For \(x\ge1\) and \(y=\lfloor\sqrt x\rfloor\), the exact divisor hyperbola gives

\[
\sum_{n\le x}a_F(n)
=\sum_{b\le y}\chi(b)\lfloor x/b\rfloor
+\sum_{a\le y}H(\lfloor x/a\rfloor)-yH(y).
\]

The bounded partial sums of \(\chi\) bound its reciprocal-series tail by \(O(1/y)\). The floor errors and the other two terms are \(O(y)\). Thus \(\sum_{n\le x}a_F(n)=L(1,\chi)x+O(\sqrt x)\). The value \(L(1,\chi)\) is positive because the sum over each successive five-term block is

\[
\frac1{(5j+1)(5j+2)}-\frac1{(5j+3)(5j+4)}>0.
\]

Compare the local coefficients of \(w\) and \(a_F\). Their quotient defines a multiplicative function \(h\) with local factors in the formal variable \(t\)

\[
h_p(t)=
\begin{cases}
(1+2t)(1-t)^2=1-3t^2+2t^3,&p\text{ split},\\
1-t^2,&p\text{ inert},\\
1-t,&p=5.
\end{cases}
\]

In particular \(w=a_F*h\). For \(\sigma>1/2\), the Euler product for \(\sum |h(d)|d^{-\sigma}\) converges since the unramified deviations start in degree two. Fix \(1/2<\sigma<1\). Substituting the ideal-count asymptotic in \(\sum_{d\le x}h(d)\sum_{m\le x/d}a_F(m)\) gives an error bounded by a constant times \(x^\sigma\sum |h(d)|d^{-\sigma}\). The same bound controls the omitted tail in the main term. Therefore for every \(\epsilon>0\),

\[
D(x)=\kappa_5 x+O_\epsilon(x^{1/2+\epsilon}),\qquad
\kappa_5=L(1,\chi)\prod_p h_p(1/p)>0.
\]

Each local factor at \(1/p\) is positive and the product of the unramified factors converges absolutely. This proves that the sharp evaluation norm grows as \(\sqrt{\kappa_5 N}\) in the actual span.

## 2. Where positive diagonal control loses the signs

Write \(B_N=\sum_{n\le N}\boldsymbol\mu(n)=\sum_{d\le N}\beta_N(d)E_d\), where basis sums run over \(\mathcal D\). Canonical augmentation gives \(\operatorname{aug}(B_N)=M(N)\). For \(N/2<d\le N\), only \(n=d\) can contribute to \(\beta_N(d)\), because a row with that direction support has \(d\mid n\). Thus

\[
\beta_N(d)=(-1)^{\omega(d)},\qquad
\sum_{N/2<d\le N}w(d)|\beta_N(d)|=D(N)-D(N/2)\asymp N.
\]

In particular \(\|B_N\|^2\ge D(N)-D(N/2)\). Let \(F_N\) be either \(B_N\) or any projection of \(B_N\) onto a set of directions retaining the full band \(d>N/2\), and let \(F_N=\sum_d f_N(d)E_d\). For any positive diagonal weights \(\xi_N(d)\) on the retained set, the direct Cauchy upper bound for its evaluation satisfies

\[
\left(\sum_d w(d)\xi_N(d)|f_N(d)|^2\right)^{1/2}
\left(\sum_d \frac{w(d)}{\xi_N(d)}\right)^{1/2}
\ge \sum_d w(d)|f_N(d)|\ge D(N)-D(N/2).
\]

The first inequality is Cauchy applied to the absolute sum, uniformly even when weights depend on \(N\) and the coefficients. The obstruction covers this diagonal bound after the true rapidity rows have already been summed. It also covers diagonal weights on individual monomials by the same argument. A pointwise absolute bound built only by this method is at least linear in \(N\), so its squared bound with weight \(1/[N(N+1)]\) has at least constant size per sufficiently late integer. It cannot certify a subpower window sum.

The coefficient Gram data have an exact phase ambiguity. The single simultaneous substitution \(X_p\mapsto-X_p\) is a coefficient isometry, multiplies each \(E_d\) by \((-1)^{\omega(d)}\), and commutes with every direction-support projection. It preserves the Gram matrix of any family of rows and their projections, the norms, the inversion symmetry and every neutral coefficient. The projected actual sum on \(N/2<d\le N\) has all its coefficients positive after this substitution. Its evaluation is then \(D(N)-D(N/2)\). For an explicit pair with unequal evaluations, take the sum of the actual rows over all subproducts of a nonempty finite split prime set \(P\). The sum and its rotated image are

\[
\prod_{p\in P}(2-E_p),\quad \prod_{p\in P}(2+E_p),\qquad
\text{with evaluations }0,\ 4^{|P|}.
\]

The rotated rows serve as an ambiguity witness for the listed data. The canonical local signs select the original rows. A comparison using the known overlaps with \(k_N\), or using other restrictions that fix those signs in the measured coordinates, can distinguish the pair. Neither obstruction covers a general non-diagonal signed kernel.

## 3. Exact anchored reconstruction from nontrivial characters

Assume \(P_N\ne\varnothing\), put \(r=|P_N|\) and \(q=4^r\), and take \(G=(\mathbf Z/4\mathbf Z)^{P_N}\). For \(t\in G\), evaluate a polynomial at \(X_p=i^{t_p}\) for every \(p\). Use the normalized sample \(q^{-1/2}f(i^t)\). Distinct exponent words in \(\{-1,0,1\}^{P_N}\) are distinct modulo four, so orthogonality of the finite characters makes the full analysis map an isometry on \(\mathcal H_N\). The normalization is the rational number \(2^{-r}\) and the evaluations of the integral polynomials use only Gaussian integers. These are formal product characters of the independent variables.

Delete the sample \(t=0\) and call the remaining analysis map \(A_N\). If \(k_N k_N^*\) denotes \(f\mapsto\langle f,k_N\rangle k_N\), then

\[
A_N^*A_N=I-q^{-1}k_N k_N^*,\qquad
\beta=D(N)/q\le (3/4)^r<1.
\]

It follows that the deleted trivial sample can be reconstructed exactly from the other samples using a vector anchored to the target,

\[
z_N=\frac{A_N k_N}{1-\beta},\qquad
A_N^*z_N=k_N,\qquad
\operatorname{aug}(f)=\langle A_N f,z_N\rangle.
\]

The vector \(z_N\) is in the range of \(A_N\), orthogonal to the kernel of \(A_N^*\), so it is the minimal-norm reconstruction among all solutions. Its squared norm is \(D(N)/(1-\beta)\). This is of order \(N\), with the factor \((1-\beta)^{-1}\) bounded by four. On the actual signal \(F_N\) from section 2, the lower frame bound gives \(\|A_NF_N\|\ge\sqrt{1-\beta}\|F_N\|\), so the product of the two norms in the plain frame Cauchy estimate is at least \(\sqrt{D(N)}\|F_N\|\gg N\). The signed scalar pairing remains the quantity to be estimated. The construction gives a finite formal reconstruction and makes no assignment of the product sample coordinates to the single integer rapidity modes of the Canon frontier.

More generally, for any finite sampling operator \(A_N\) and any proposed readout vector \(z_N\) in its sample space, set \(r_N=k_N-A_N^*z_N\). A uniform transfer for the actual signal must account for

\[
\left|\operatorname{aug}(F_N)-\langle A_NF_N,z_N\rangle\right|
\le \|r_N\|\|F_N\|.
\]

This identity fixes the target anchor, with an explicit error in the norm on the actual span. It can be used with a substitute frame if a definition of \(A_N\), the anchored reconstruction, and estimates of the signed pairing and its residual are supplied on the same windows. A matrix of pairwise norm data without the target overlap does not specify this readout.

## 4. Two different moving support cutoffs

Let \(\mathcal C_0(s)=\sum_{n\ge1}c_0(n)n^{-s}\) denote the canonical neutral coefficient series, and let \(C_0(x)=\sum_{n\le x}c_0(n)\) be its partial sum. Write \(a(d)=(-2)^{\omega(d)}\) for \(d\in\mathcal D\), and zero otherwise. The split local factor for a fixed nonzero orientation at a prime is \(-t/(1-t)\), while the neutral local factor is \((1+t^2)/(1-t)\). Therefore the coefficient series of the augmented sector supported at precisely \(d\in\mathcal D\) is

\[
\mathcal C_0(s)\,a(d)d^{-s}\prod_{p\mid d}(1+p^{-2s})^{-1}.
\]

This follows coefficientwise from the local factors and as a Dirichlet series in the absolutely convergent domain. Equivalently the contribution of the sector to \(M(N)\) is

\[
\gamma_d(N)=a(d)\sum_{\substack{m^2\le N/d\\\operatorname{rad}(m)\mid d}}
 (-1)^{\Omega(m)} C_0\!\left(\frac{N}{dm^2}\right),
\qquad V(N)=\sum_{d>N^{1/4}}\gamma_d(N),
\]

where \(\Omega(m)\) counts prime factors with multiplicity. This is the orientation cutoff described at Matematyka. It retains the top band used in section 2.

### Neutral bound and the discarded sectors

For \(x\ge1\) and \(y=\lfloor x^{1/3}\rfloor\), every pair of positive integers with \(ab^2\le x\) has \(a\le y\) or \(b\le y\). When both hold, the product is at most \(y^3\le x\). Splitting on these two sets and subtracting the overlap gives

\[
\left|\sum_{ab^2\le x}\chi(a)\chi(b)\right|\le 2y+1\le3x^{1/3},
\]

since the inner character sums are bounded by one, and the overlap is \(H(y)^2\). The canonical factorization of \(\mathcal C_0(s)\) is \(L(s,\chi)L(2s,\chi)\) times \((1-5^{-s})\prod_{p\ne5}(1-p^{-4s})\). This last factor has coefficients given by the ordinary Möbius function on fourth powers coprime to five, convolved with the sequence \(1\) at \(1\), \(-1\) at \(5\), and zero elsewhere. The preceding bound now gives

\[
|C_0(x)|\le3(1+5^{-1/3})\zeta(4/3)x^{1/3}.
\]

The cited web page reports a Lean formalization of its stated neutral bound \(6\zeta(4/3)^2 N^{1/3}\). It attributes the removal of the small direction-support band to a written proof. The deductions here use the displayed paper argument and no Lean result as a premise.

For the sectors, the bound just proved gives

\[
|\gamma_d(N)|\ll N^{1/3}d^{-1/3}g(d),\qquad
g(d)=w(d)\prod_{p\mid d}(1-p^{-2/3})^{-1}\quad(d\in\mathcal D),
\]

with \(g=0\) outside \(\mathcal D\). To see that \(\sum_{d\le x}g(d)\ll x\), define the nonnegative multiplicative function \(v\) supported on \(\mathcal D\) by \(v(p)=2p^{-2/3}/(1-p^{-2/3})\) at split primes. On \(\mathcal D\) the equality \(g=w*v\) holds from the prime factors, so \(w*v\) is a global majorant. The ideal count is nonnegative and pointwise at least \(w\), and its cumulative count is at most \(x\) by \(\sum_{m\le x}a_F(m)=\sum_{a\le x}H(\lfloor x/a\rfloor)\). Finally \(\sum v(d)/d<\infty\) by its absolutely convergent product. The stated majorant follows by convolution. Partial summation gives \(\sum_{d\le D} g(d)d^{-1/3}\ll D^{2/3}\). Hence

\[
M(N)-V(N)=\sum_{d\le N^{1/4}}\gamma_d(N)=O(N^{1/2}).
\]

### Exact comparison with the periodic kernel of issue #2087

The statistic of issue #2087 uses the same signed \(a(d)\), and has the definitions

\[
T(N)=\sum_{d\le N}a(d)H(\lfloor N/d\rfloor),\qquad
R(N)=\sum_{\substack{d\le N\\d^3>N^2}}a(d)H(\lfloor N/d\rfloor).
\]

Its moving cutoff is \(d\le N^{2/3}\) for the retained short component. The individual orientation sector instead uses

\[
\gamma_d(N)=a(d)\sum_{k\le N/d}u_d(k)H(\lfloor N/(dk)\rfloor),
\]

with the explicit coefficient series

\[
\sum_k u_d(k)k^{-s}=
\frac{L(2s,\chi)}{\zeta(4s)}\frac{1-5^{-s}}{1-5^{-4s}}
\prod_{p\mid d}(1+p^{-2s})^{-1}.
\]

The absolute coefficient sums of this series and its inverse at any fixed \(\sigma>1/2\) are uniformly bounded over \(d\), by absolute convergence of the common factors and the majorants \(\prod_p(1-p^{-2\sigma})^{-1}\) for the products over \(p\mid d\) and their inverses. The multiplier still depends on \(d\). The sector formula and periodic formula agree in the band \(N/2<d\le N\), where only \(k=1\) appears and \(H(1)=1\). For \(N>8\) this band occurs in both tails. Outside that band the cutoff and kernel formulas differ.

For the full sequences the separate common Euler unit of #2087 gives \(M(N)=\sum_{k\le N}u(k)T(N/k)\) with inverse convolution. The local factors of its Dirichlet series are \((1-t)^2/(1-2t)\) at split primes, \(1-t^2\) at inert primes, and \(1-t\) at \(5\). The reciprocal and the unit have absolutely summable coefficients with weight \(n^{-\sigma}\) for each \(\sigma>1/2\). The split factors start their deviations in degree two and \(2p^{-\sigma}<1\) at all split primes. This gives equivalence of all-argument estimates \(T(x)=O_\epsilon(x^{1/2+\epsilon})\) and \(M(x)=O_\epsilon(x^{1/2+\epsilon})\), and thus also of the corresponding estimate for \(V\) by the discarded band bound. The inputs of a dilation convolution for \(N\) in a single window can lie below its lower endpoint. The same-window statements below instead use direct comparisons on that window.

## 5. Signed window criterion and the remaining estimate

Fix \(1<\lambda\le2\). The external prime-power proof uses \(\lambda=3/2\). Let \(I_\lambda(Y)=\{n\in\mathbf Z:Y\le n<Y^\lambda\}\) for integers \(Y\ge2\), and put

\[
Q_F(Y)=\sum_{n\in I_\lambda(Y)}\frac{F(n)_+^2}{n(n+1)},\qquad
W_\lambda(F)\ \Longleftrightarrow\
\forall r\in\mathbf Z_{\ge1}\ \forall Y_0\in\mathbf Z_{\ge1}\ \exists Y\ge\max(2,Y_0)\ \ Q_F(Y)^r\le Y.
\]

Here \(F(n)_+=\max(F(n),0)\). Membership for \(\lambda=3/2\) uses \(n^2<Y^3\). The Lipschitz property of the positive part and the triangle inequality for this weighted Euclidean norm give

\[
|\sqrt{Q_M(Y)}-\sqrt{Q_V(Y)}|\ll_\lambda\sqrt{\log Y}.
\]

Indeed \((M(n)-V(n))^2\ll n\) on this exact interval. The logarithmic short-support estimate of #2087 bounds the weighted square of \(T-R\) on \([Y,Y^2)\) by \(O((1+\log Y)^4)\). Its restriction gives \(|\sqrt{Q_T(Y)}-\sqrt{Q_R(Y)}|\ll(1+\log Y)^2\). These imply \(W_\lambda(M)\Longleftrightarrow W_\lambda(V)\) and \(W_\lambda(T)\Longleftrightarrow W_\lambda(R)\). For a prescribed exponent \(r\), take sufficiently late windows supplied for exponent \(2r\), square the comparison bound, and absorb the fixed logarithmic loss in \(Y^{1/r}\).

The signed power-window lemma proved in the #2087 foundation applies separately to \(M(e^u)\) and \(T(e^u)\) for any fixed \(\lambda>1\). The respective Laplace transforms start as \(1/(s\zeta(s))\) and \(1/(s\zeta(s)U(s))\), where \(U\) is the common Euler unit above. Both have the same poles in \(\Re s>1/2\), and neither has real poles there. For \(1/2<s<1\) on the real axis, nonvanishing of \(\zeta\) follows from the positive alternating eta series and the eta factor, and for \(s>1\) from the Euler product. At \(s=1\) the reciprocal has a zero. If there were an off-line zero to the right of \(1/2\), there would be \(\theta>1/2\) and \(\eta>0\) such that all sufficiently large \(Y\) satisfy

\[
\int_Y^{Y^\lambda}F(\lfloor x\rfloor)_+ x^{-1-\theta}\,dx\gg Y^\eta
\qquad(F=M,T).
\]

The integral of \(F(\lfloor x\rfloor)_+^2/x^2\) over this real interval is bounded by \(Q_F(Y)\), with a possible shortened last cell. Cauchy and \(\int_Y^\infty x^{-2\theta}\,dx=Y^{1-2\theta}/(2\theta-1)\) imply \(Q_F(Y)\gg Y^{2\eta+2\theta-1}\) on every sufficiently late window. The condition \(W_\lambda(F)\) excludes this, and symmetry then gives RH. The converse is the classical RH/Mertens estimate and absolute convolution with the common unit inverse, applied as all-argument statements before taking windows. This comparison preserves the individual-window implications in each pair and supplies a common analytic criterion for the two tails.

**O.** For a direct rapidity proof on arbitrarily late \([Y,Y^{3/2})\) windows, take \(F_N\) to be the orientation projection defining \(V(N)\). A sufficient anchored estimate is that for each \(r\ge1\) and every lower scale there exists a common later window on which

\[
\left(\sum_{N\in I_{3/2}(Y)}\frac{(\Re\langle A_NF_N,z_N\rangle)_+^2}{N(N+1)}\right)^{1/2}
+\left(\sum_{N\in I_{3/2}(Y)}\frac{\|r_N\|^2\|F_N\|^2}{N(N+1)}\right)^{1/2}
\le Y^{1/(2r)}.
\]

The first term is a signed pairing followed by a positive part. The exact product-character reconstruction makes the second term zero and still leaves the first term open. The external argument supplies a long-window estimate for a different smoothed prime-power observable, derived from its matched arithmetic inputs. Transferring that method would require identifying a source that fixes the orientation of this pairing and proving the stated bounds without assuming RH or an equivalent cancellation estimate. Issue #2087 retains ownership of its periodic kernel and its own tail estimate.

## Sources

- Public Canon v117, section 10 and `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE` [O], with evidence in `P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1` and `P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1`.
- Issue [#2087](https://github.com/mathorn1973/twist-j/issues/2087), with the pinned [kernel](https://github.com/mathorn1973/twist-j/blob/59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd/notes/C-RH-ARITHMETIC-KERNEL-N/KERNEL.md), [window tail](https://github.com/mathorn1973/twist-j/blob/59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd/notes/C-RH-ARITHMETIC-KERNEL-N/WINDOW-TAIL.md) and [foundation](https://github.com/mathorn1973/twist-j/blob/59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd/notes/C-RH-ARITHMETIC-KERNEL-N/FOUNDATION.md).
- Matematyka, [Divisibility and the road to the Riemann hypothesis](https://matematyka.cz/en/rh), section on the Möbius function.
- [The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf), version 2, Parts I–II, with the corresponding [Lean source pin](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005).
- Fujisawa and Minamide, [On partial sums of the Möbius and Liouville functions for number fields](https://arxiv.org/pdf/1212.4348), Theorem 1.3 for the rational field.

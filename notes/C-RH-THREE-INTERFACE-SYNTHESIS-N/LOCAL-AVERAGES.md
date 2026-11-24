# Conditional averages in the signed fourth-root pairing

**NON-CANONICAL. Authority none.** The identities and deductions below are
**candidate-D**. The final signed window estimate is **O**. The objects
are the actual rapidity rows and the fourth-root operator of
[MOBIUS.md](MOBIUS.md). The action layer is `NOT_APPLICABLE`. This is
a paper calculation. The sampled formulas use \(P_N\ne\varnothing\).

## Exact conditional readouts

For a split prime \(p\in P_N\), let \(C_p\) average the coordinate \(X_p\)
over the four fourth roots of unity. Thus \(C_p E_d=E_d\) if \(p\nmid d\)
and \(C_pE_d=0\) otherwise. The \(C_p\) are commuting orthogonal
projections on \(\mathcal H_N\). For \(S\subseteq P_N\), averaging outside
\(S\) gives

\[
 P_S=\prod_{p\notin S} C_p,\qquad
 \operatorname{aug}P_S B_N=\sum_{\substack{d\le N\;p\mid d\Rightarrow p\in S}}\gamma_d(N).
\]

Order the split primes \(p_1<\cdots<p_r\) and put
\(Q_j=(I-C_{p_j})\prod_{i>j}C_{p_i}\). Its supports have greatest
prime \(p_j\). The exact hierarchical partition is

\[
 I=P_{\varnothing}+\sum_{j=1}^r Q_j,
 \qquad
 \langle A_N B_N,z_N\rangle
 =C_0(N)+\sum_{j=1}^r\operatorname{aug}Q_j B_N.
\]

Every block can be read from the same nontrivial fourth-root samples.
For a family \(\mathcal F\) of retained supports put
\(k_{\mathcal F}=\sum_{d\in\mathcal F}E_d\) and
\(D_{\mathcal F}=\sum_{d\in\mathcal F}w(d)\). Write
\(q=4^r\), \(D=D(N)\), and assume \(r\ge1\). The minimum squared
readout norm for extracting the block from the **unprojected** samples
\(A_N f\), uniformly over \(f\in\mathcal H_N\), is

\[
 \begin{aligned}
 z_{\mathcal F}
 &=A_N\left(k_{\mathcal F}+\frac{D_{\mathcal F}}{q-D}k_N\right),\\
 \operatorname{aug}(\operatorname{proj}_{\mathcal F}f)
 &=\langle A_N f,z_{\mathcal F}\rangle,\\
 \|z_{\mathcal F}\|^2
 &=D_{\mathcal F}+\frac{D_{\mathcal F}^2}{q-D}.
 \end{aligned}
\]

Indeed \((A_N^*A_N)^{-1}=I+k_N k_N^*/(q-D)\). Applying this
inverse to \(k_{\mathcal F}\), then applying \(A_N\), gives a solution
orthogonal to \(\ker A_N^*\). Its squared norm is
\(\langle (A_N^*A_N)^{-1}k_{\mathcal F},k_{\mathcal F}\rangle\).
The readers add over disjoint blocks. For disjoint \(\mathcal F,\mathcal G\)
their inner product is \(D_{\mathcal F}D_{\mathcal G}/(q-D)\).
For the full partition the readout cost is again \(D/(1-D/q)\).

There is also a reader using only two faces of the sample cube for a
single \(Q_j\). Fix \(X_{p_i}=1\) for \(i<j\) and average all
\(i>j\) coordinates. Let \(F_j(\xi)\) be the resulting function of
\(X_{p_j}=\xi\) for a given input \(f\). As \(F_j\) is affine in
\(\xi+\xi^{-1}\),

\[
 \operatorname{aug}Q_j f=F_j(i)-F_j(-1).
\]

Neither face contains the deleted sample. Their squared readout norm
in the normalization of \(A_N\) is \(2\cdot 4^j\), since each
average uses \(4^{r-j}\) samples with coefficient of absolute value
\(q^{1/2}/4^{r-j}\). The minimum cost above uses the full sample
space and the actual support condition.

## A character-controlled set beyond the short orientation cutoff

The neutral bound \(|C_0(x)|\ll x^{1/3}\) and the exact sector
formula in [MOBIUS.md](MOBIUS.md) give, for any \(S\subseteq P_N\),

\[
 \sum_{\substack{d\le N\;p\mid d\Rightarrow p\in S}}|\gamma_d(N)|
 \ll N^{1/3}\prod_{p\in S}
 \left(1+\frac{2p^{-1/3}}{1-p^{-2/3}}\right).
\]

To see the product, bound the sum over square powers in each sector
by \(\prod_{p\mid d}(1-p^{-2/3})^{-1}\), then sum the resulting
positive weights over all squarefree products from \(S\). The bound
also applies to every subfamily of those supports. Hence the
product condition \(\prod_{p\in S_N}(1+2p^{-1/3}/(1-p^{-2/3}))
\le N^{1/6}\) permits deletion with \(O(\sqrt N)\) absolute error.
This cut concerns the prime factors of the orientation support
\(d\) inside each row, with the row index still running through \(N\).
The basis mass of this family is at most
\(N^{1/3}\prod_{p\in S_N}(1+2p^{-1/3})\), by inserting
\((N/d)^{1/3}\ge1\) in its defining sum. Thus under the product
condition its minimum squared readout norm is \(O(\sqrt N)\).

The range can be made explicit. If \(S_N\) consists of split
primes at most \(z\ge1\), then \(p\ge11\) for each such prime,
so the log of the displayed product is at most
\(3\sum_{n\le z}n^{-1/3}\le (9/2)z^{2/3}\). Thus
\(z=(\log N/27)^{3/2}\) satisfies the product condition
when \(z\ge1\). For \(z<1\) the prime set is empty and its product
is one. More generally, for fixed \(0<A<3/2\) and
\(z=(\log N)^A\), the bound is \(N^{1/3+o(1)}\) without an
estimate on the distribution of primes.

The fixed-modulus prime number theorem sharpens this range.
This refinement was proposed in the internal Astra review.
Let \(P(z)\) denote the product in the deletion condition over
split primes up to \(z\). The logarithm of its factor at \(p\)
is \(2p^{-1/3}+O(p^{-2/3})\). The total error is \(O(z^{1/3})\)
by summing over all integers. The split prime count satisfies
\(\Pi(z)\sim z/(2\log z)\). Partial summation gives

\[
 \sum_{\substack{p\le z\\p\ {\rm split}}}p^{-1/3}
 =z^{-1/3}\Pi(z)+\frac13\int_2^z\Pi(t)t^{-4/3}\,dt
 \sim\left(\frac12+\frac14\right)\frac{z^{2/3}}{\log z}.
\]

Here \(\int_2^z t^{-1/3}/\log t\,dt\sim(3/2)z^{2/3}/\log z\),
as follows by differentiating the proposed main term. Thus
\(\log P(z)\sim(3/2)z^{2/3}/\log z\). For every fixed \(0<c<1/6\),
the moving cutoff \(z=(c\log N\log\log N)^{3/2}\) tends to infinity,
is less than \(N\) eventually, and satisfies
\(\log P(z)=(c+o(1))\log N\). The strict inequality on \(c\)
gives \(P(z)\le N^{1/6}\) on all sufficiently large integers \(N\).
The \(O(\sqrt N)\) deletion bound therefore holds throughout
every sufficiently late window.

Keeping the condition \(d\le N\) longer gives a further refinement
from the same review. Insert \((N/d)^{\sigma-1/3}\ge1\) in the
positive sector bound, for \(1/3\le\sigma\le1/2\), and then extend
over all products of the selected primes. This yields the uniform
bound

\[
 \sum_{\substack{d\le N\\ p\mid d\Rightarrow p\in S_N}}
 |\gamma_d(N)|
 \ll N^\sigma
 \prod_{p\in S_N}\left(1+\frac{2p^{-\sigma}}{1-p^{-2/3}}\right).
\]

For \(z=(\log N)^A\) and fixed \(0<A<2\), choose a fixed
\(\max(1/3,1-1/A)<\sigma<1/2\). The logarithm of the product for
all split \(p\le z\) is \(O_\sigma(z^{1-\sigma})=o(\log N)\)
by the integer sum. The right side is \(O(\sqrt N)\).
For \(z=c(\log N)^2\) with fixed \(0<c<1/(4e^2)\), use
\(\sigma=1/2-1/\log z\) for sufficiently large \(N\).
Then \(p^{-\sigma}\le e p^{-1/2}\) for \(p\le z\). The contribution
to the logarithmic upper bound from replacing
\((1-p^{-2/3})^{-1}\) by \(1\) is \(O(\sum_p p^{-7/6})=O(1)\).
Partial summation gives
\(\sum_{p\le z,\ p\ {\rm split}}p^{-1/2}\sim\sqrt z/\log z\).
Consequently the logarithm of the product is at most
\((2e+o(1))\sqrt z/\log z\). The factor
\(N^\sigma=\sqrt N\exp(-\log N/\log z)\) absorbs this allowance
because \(2e\sqrt c<1\). These two ranges also give
\(D_{\mathcal F}=O(\sqrt N)\) for the deleted family by the same
insertion into its basis mass sum, which has the smaller local
factors \(1+2p^{-\sigma}\).

The converse, including failure at \(c=1/(4e^2)\), is proved for the
actual absolute sector sum in [ROUND2-REVIEW.md](ROUND2-REVIEW.md).
The combined exact Dirichlet readout after these deletions is specified
in [DIRICHLET-READOUT.md](DIRICHLET-READOUT.md), Sections 4 and 5.

For example, take \(S_N=\{p\in P_N:p\le \log N\}\). The logarithm
of the product is \(O((\log N)^{2/3})\). The fixed-modulus prime
number theorem gives
\(\sum_{p\in S_N}\log p=(1/2+o(1))\log N\), so the support
\(\prod_{p\in S_N}p=N^{1/2+o(1)}\) lies above \(N^{1/4}\) and
at most \(N\) for all sufficiently large \(N\).

Let \(V_S(N)\) retain the supports with \(d>N^{1/4}\) and with at
least one prime outside \(S_N\). In each \(O(\sqrt N)\) deletion range,
\(M(N)-V_S(N)=O(\sqrt N)\), since the short orientation cutoff
has the same bound and the two deleted families can be made
disjoint. On every exact \(I_\lambda(Y)\) of [MOBIUS.md](MOBIUS.md),

\[
 \left|\sqrt{Q_M(Y)}-\sqrt{Q_{V_S}(Y)}\right|\ll_\lambda\sqrt{\log Y}.
\]

The triangle inequality and the Lipschitz property of the positive
part give the comparison on each window. Taking exponent \(2r\) in
the source condition absorbs the logarithm for any prescribed
exponent \(r\) on sufficiently late windows. Thus
\(W_\lambda(M)\) and \(W_\lambda(V_S)\) are equivalent.

## Complete large-prime orientation blocks

For \(p>\sqrt N\), every row that depends on \(X_p\) has the form
\((1-E_p)\boldsymbol\mu(m)\) with \(m\le N/p\). No row can involve
two such primes. The complete support block and its evaluation are
therefore

\[
 Q_p B_N=-E_p B_{\lfloor N/p\rfloor},\qquad
 \operatorname{aug} Q_p B_N=-2M(\lfloor N/p\rfloor),
\]

where \(Q_p\) is the \(Q_j\) for that prime. In particular for
\(1/2\le a<1\) the projection \(Q_{>N^a}=\sum_{p>N^a}Q_p\) has
the signed readout

\[
 L_a(N):=\operatorname{aug}Q_{>N^a}B_N
       =-2\sum_{\substack{N^a<p\le N\\p\ {\rm split}}}M(\lfloor N/p\rfloor).
\]

It is contained in the orientation tail \(d>N^{1/4}\). The
actual-row mask selects the whole \((1-E_p)B_{\lfloor N/p\rfloor}\)
and reads \(-M(\lfloor N/p\rfloor)\). Averaging that row mask in the
coordinate \(p\) reads \(+M(\lfloor N/p\rfloor)\). Their difference
gives the orientation block.

Its squared basis mass is
\(D_{>N^a}=2\sum_{N^a<p\le N,\ p\ {\rm split}}D(N/p)\),
because each retained support is uniquely \(pe\) with \(e\le N/p<p\).
In particular

\[
 D_{>N^a}=\kappa_5N\log(1/a)+O_a(N/\log N).
\]

For this estimate use \(D(x)=\kappa_5x+O(x^{3/4})\) from
[MOBIUS.md](MOBIUS.md). Partial summation of the fixed-modulus prime
number theorem yields
\(\sum_{N^a<p\le N,\ p\ {\rm split}}1/p=(1/2)\log(1/a)
+O_a(1/\log N)\) and
\(\sum_{p\le N}p^{-3/4}\ll N^{1/4}/\log N\).
Thus the minimum squared readout cost in the first section is still
of order \(N\) for every fixed \(a\).

Equation (7) of the pinned
[large-prime analysis for #2087](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/round3/LARGE-PRIME-TAIL.md)
already evaluates this Mertens prime average by the fixed-modulus
prime number theorem and the classical unconditional Mertens bound.
The exact block identity supplies the matching projection of the
fourth-root pairing. For \(\ell=\log N\), the resulting estimate is

\[
 L_a(N)=\frac{N}{\ell^2}+O_a(N/\ell^3).
\]

The moments there come from \(G_M(s)=1/(s\zeta(s))\), with
\(G_M(1)=0\) and \(G_M'(1)=1\). The pinned periodic statistic
\(T\) uses \(T(N/p)\) in place of \(M(N/p)\), with matched range
\(a\ge2/3\) for its own tail. Its derivative is \(1/U(1)\) by
its coefficient unit. These are distinct inner sums with exact
normalizations on the same arguments.

There is also a cancellation at first logarithmic order within
\(L_a(N)\) itself. Let \(J_a(N)\) be the contribution from the
single-prime supports. For such a support the cofactor evaluation
is neutral, so

\[
 J_a(N)=-2\sum_{\substack{N^a<p\le N\\p\ {\rm split}}}C_0(N/p).
\]

The coefficients of \(C_0\) satisfy \(|c_0(m)|\le\tau(m)\) by
the local factors, where \(\tau\) counts positive divisors. Thus
\(\sum_{m\le Z}|c_0(m)|/m\le (1+\log Z)^2\). On interchanging
the prime and coefficient sums, the prime count for each
\(m\le N^{1-a}\) is \(\Pi(N/m)-\Pi(N^a)\), where \(\Pi\) counts
split primes. Substituting
\(\Pi(t)=\operatorname{Li}(t)/2+O_A(t/(\log t)^A)\) in both
counts gives total error \(O_{A,a}(N\ell^{2-A})\), using
\(N^a\le N/m\). Interchange the main-term integrals with
the finite sum and substitute \(u=N/t\). This gives
\(-N\int_1^{N^{1-a}} C_0(u)u^{-2}(\ell-\log u)^{-1}\,du\).
Expanding the last factor through its first two terms gives error
\(O_a(N/\ell^3)\), since \(|C_0(u)|\ll u^{1/3}\) is integrable
against \(u^{-2}(\log u)^2\). Extending the first two moments
to infinity costs less than this error.

Write \(G_0(s)=\mathcal C_0(s)/s\). The neutral Euler
factorization gives
\(b_0=G_0(1)=L(1,\chi)L(2,\chi)(1-5^{-1})
\prod_{p\ne 5}(1-p^{-4})>0\). Integrating the neutral
step sum gives moments \(G_0(1)\) and \(-G_0'(1)\). Hence

\[
 \begin{aligned}
 J_a(N)&=-b_0\frac{N}{\ell}+G_0'(1)\frac{N}{\ell^2}+O_a(N/\ell^3),\\
 L_a(N)-J_a(N)&=b_0\frac{N}{\ell}
    +(1-G_0'(1))\frac{N}{\ell^2}+O_a(N/\ell^3).
 \end{aligned}
\]

The opposite first terms cancel within the same large-prime mask.
The corresponding coefficient for single-prime supports in the
periodic statistic of #2087 is \(-L(1,\chi)\).
The remaining positive second term gives
\(Q_{L_a}(Y)\gg_{a,\lambda}Y^\lambda/(\log Y)^4\), by restricting
to \(Y^\lambda/2\le N<Y^\lambda\) in every sufficiently late
window. If \(S_N\subseteq\{p:p\le N^a\}\) is in an \(O(\sqrt N)\)
deletion range, the remaining orientation block \(V_S(N)-L_a(N)\)
has the opposite leading second term.
Indeed \(V_S=M+O(\sqrt N)\) and the classical Mertens bound
gives \(M(N)=o(N/\ell^2)\). A square-root bound still requires
joint control after this cancellation.

For comparison the exact upper slice \(p>N/3\) has nonpositive
evaluation for \(N\ge9\), because \(M(1)=1\) and \(M(2)=0\).
Its value is \(-2[\Pi(N)-\Pi(N/2)]\). Dropping this slice raises
the remaining pairing to
\(M(N)+2[\Pi(N)-\Pi(N/2)]\), or to that value plus \(O(\sqrt N)\)
after the controlled support deletions. The latter bound also
covers any overlap, since the bound on absolute contributions
applies to every subfamily of the controlled supports.
This quantity is positive
of order \(N/\log N\) by the same classical estimates.

## Finite coordinate changes

Fix a finite set \(S\) of split primes independently of \(N\).
At each \(p\in S\), fix a value \(\eta_p\in[-2,2]\) for \(E_p\).
The value \(0\) gives the average \(C_p\) in this coordinate.
Evaluate at augmentation elsewhere. The resulting signed sequence
\(F_\eta(N)\) has coefficient series

\[
 \frac{V_\eta(s)}{\zeta(s)},\qquad
 V_\eta(s)=\prod_{p\in S}
 \frac{1-\eta_p p^{-s}+p^{-2s}}{(1-p^{-s})^2}.
\]

The local numerator follows by summing coefficients \(1-\eta_p\)
at \(p\) and \(2-\eta_p\) at higher powers. Its roots in
\(p^{-s}\) have modulus one, so \(V_\eta\) and its reciprocal
are holomorphic in \(\Re s>0\), with absolutely convergent
coefficient series at every real \(\sigma>0\).
The full fourth-root readout cost for this functional is
\(\sum_{d\le N} w(d)u(d)^2 + (\sum_{d\le N}w(d)u(d))^2/(q-D)\),
where \(u(d)=\prod_{p\mid d,\ p\in S}(\eta_p/2)\). This follows from
the same inverse applied to \(\sum_{d\le N}u(d)E_d\).

Convolution gives all-argument equivalence of the
\(O_\epsilon(N^{1/2+\epsilon})\) bounds for \(F_\eta\) and \(M\).
For \(W_\lambda\), the Laplace transform of \(F_\eta(e^u)\)
is \(V_\eta(s)/(s\zeta(s))\). It has the same poles as the
Mertens transform in \(\Re s>1/2\) and no real poles there.
The signed power-window lemma in the
[pinned foundation](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/FOUNDATION.md)
and the weighted Cauchy argument of [MOBIUS.md](MOBIUS.md) give
the forward implication from \(W_\lambda(F_\eta)\) to RH. The
classical Mertens estimate under RH gives the converse through
all-argument convolution. The window equivalence follows by
applying the pole criterion separately to both sequences.

**O.** The remaining estimate is \(W_{3/2}(V_S)\) for the
original signed pairing with the controlled support families
removed. The same-window comparison above fixes its cutoff and
quantifiers. The large-prime block and its complement must
enter with their signs in that estimate.

### Analytic inputs

- [Thorner and Zaman, Refinements to the prime number theorem for arithmetic progressions, Corollary 1.4](https://arxiv.org/pdf/2108.10878), at the fixed modulus five.
- [Fujisawa and Minamide, On partial sums of the Möbius and Liouville functions for number fields, Theorems 1.2 and 1.3](https://arxiv.org/pdf/1212.4348), at the rational field.

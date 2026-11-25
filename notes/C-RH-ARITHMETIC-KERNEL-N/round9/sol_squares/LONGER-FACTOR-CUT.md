# A longer factor cut with the two negative squares

C-RH-ARITHMETIC-KERNEL-N, owner [#2087](https://github.com/mathorn1973/twist-j/issues/2087), draft [#2089](https://github.com/mathorn1973/twist-j/pull/2089), round 9. **NON-CANONICAL. No authority. Candidate-D paper deductions.** Action layer NOT_APPLICABLE. The full signed estimate remains **O**. Scope fixed in [PREREG.md](PREREG.md).

## 1. An inverse-weight mean with a resolved cubic-scale term

Use the actual \(t=\chi_5*s\), \(T(y)=\sum_{m\le y}t(m)\), and \(f=t^{-1}=\mathbf1*u\) from round eight. Here \(u\) is the coefficient sequence of \(U\), and the inverse and products of sequences are for Dirichlet convolution. Via the inherited factorization \(U(s)=L(2s,\chi_5)\zeta(3s)L(3s,\chi_5)W_4(s)\), the actual mean now satisfies
\[
 \boxed{\quad F(y):=\sum_{k\le y}f(k)
     =U(1)y+C_U\zeta(1/3)y^{1/3}+O(y^{7/22}),\quad y\ge1. \quad}      \tag{1}
\]
Here \(C_U=L(1,\chi_5)L(2/3,\chi_5)W_4(1/3)>0\), as in round six. The error exponent is below \(1/3\).

Let \(\chi=\chi_5\), \(c(m)=\sum_{d^2\mid m}\chi(d)\), and \(g=\mathbf1*\chi\). Both sequences are nonnegative by their prime-power coefficients. For \(c\), at inert primes the alternating sum through \(\lfloor v_p(m)/2\rfloor\) is zero or one, and elsewhere its local sum is nonnegative directly. Write \(C(y)=\sum_{m\le y}c(m)\), \(G(y)=\sum_{m\le y}g(m)\). The fixed-character hyperbola bound \(G(y)=L(1,\chi)y+O(\sqrt y)\) follows by splitting \(\sum_{d k\le y}\chi(d)\) at \(d=\lfloor\sqrt y\rfloor\), bounding the shifted character intervals by periodicity, and completing \(\sum\chi(d)/d\) by partial summation.

To estimate \(C(y)\), set \(B=\lfloor y^{3/8}\rfloor\) and split \(\sum_{d^2 m\le y}\chi(d)\) at \(d=B\). For \(d>B\) regroup by \(m\le y/B^2\). The inner character sum is over \(B<d\le\sqrt{y/m}\), and bounded periodic partial sums give total \(O(y/B^2)\). In the shorter part the main term from replacing the floor is \(y\sum_{d\le B}\chi(d)d^{-2}\). Completion to \(L(2,\chi)y\) also costs \(O(y/B^2)\) by the same character partial sums. After centering the fractional parts, the constant one-half costs \(O(1)\) using \(\sum_{d\le B}\chi(d)=O(1)\).

For the centered floor error split \(d\) into its four nonzero residue classes modulo five. The part \(d\le y^{1/4}\) costs \(O(y^{1/4})\). On one class in a dyadic interval \(D<d\le2D\) with \(y^{1/4}\le D\le B\), possibly truncated, use Erdős–Turán discrepancy for the fractional parts of \(y/d^2\). Its bound also bounds the centered fractional-part sum, by integrating the counts in \([0,u)\) over \(0\le u\le1\) and using \(\int_0^1\mathbf1_{\{v<u\}}du=1-v\) for \(v\in[0,1)\). This identity handles integer arguments. For an integer cutoff \(H\ge1\) the resulting bound is
\[
  \ll D/H+\sum_{h\le H}\frac1h
             \left|\sum_{\substack{D<d\le \min(2D,B)\\d\equiv j\ (5)}}
                  e(hy/d^2)\right|,\qquad e(v)=e^{2\pi i v}.
\]
Write \(d=5m+j\); the magnitude of the phase's second derivative in \(m\) is between constant positive multiples of \(hy/D^4\). Van der Corput's second-derivative estimate therefore bounds the inner sum by
\(\ll \sqrt{hy}/D+D^2/\sqrt{hy}\), also on the truncated interval. Summing \(h\) gives
\[
       \ll D/H+\sqrt{yH}/D+D^2/\sqrt y .
\]
Take \(H=\lfloor(D^4/y)^{1/3}\rfloor\), at least one. The first two terms are \(O(y^{1/3}D^{-1/3})\). As the dyadic intervals run from \(y^{1/4}\) to \(y^{3/8}\), the sums of \(y^{1/3}D^{-1/3}\) and \(D^2/\sqrt y\) are each \(O(y^{1/4})\) by geometric summation from their dominating ends. With the short and long cutoff errors this proves
\[
                  C(y)=L(2,\chi)y+O(y^{1/4}).                       \tag{2}
\]

Write \(c_1=L(2,\chi)\), \(g_1=L(1,\chi)\). For \(\Re s>1\), the series of \(c\) is \(\zeta(s)L(2s,\chi)\). Partial summation with \(C(y)=c_1y+E(y)\), \(E(y)=O(y^{1/4})\), gives the continuation
\[
 \zeta(s)L(2s,\chi)=\frac{c_1 s}{s-1}
                      +s\int_1^\infty E(y)y^{-s-1}\,dy
 \qquad (\Re s>1/4,\ s\ne1).
\]
All functions agree first on \(\Re s>1\), so this gives the actual value at \(s=1/3\). In particular, for real \(K\ge1\),
\[
 \sum_{m\le K}c(m)m^{-1/3}
    =\tfrac32 c_1 K^{2/3}
           +\zeta(1/3)L(2/3,\chi)+O(K^{-1/12}).                    \tag{3}
\]

Now consider \(P(y)=\sum_{m d^3\le y}c(m)g(d)\). Let \(J=\lfloor y^{3/11}\rfloor\) and \(K=\lfloor y/J^3\rfloor\). Keeping the strict tail \(d>J\) gives exactly
\[
 P(y)=\sum_{d\le J}g(d)C(y/d^3)
        +\sum_{m\le K}c(m)\bigl[G((y/m)^{1/3})-G(J)\bigr].
\]
In the first part, (2) gives error \(O(y^{1/4}J^{1/4})\) by \(G(u)\ll u\), positivity of \(g\), and partial summation. Completing the main term uses the tail
\(\sum_{d>J}g(d)d^{-3}=(g_1/2)J^{-2}+O(J^{-5/2})\), obtained by partial summation. Thus the first part is
\[
 c_1\zeta(3)L(3,\chi)y-\tfrac12c_1g_1 yJ^{-2}
      +O(y^{1/4}J^{1/4}+yJ^{-5/2}).
\]
For the second part use \(G(u)=g_1u+O(\sqrt u)\), with error
\[
 O\!\left(y^{1/6}\sum_{m\le K}c(m)m^{-1/6}+J^{1/2}C(K)\right)
     =O(yJ^{-5/2}),
\]
by \(C(u)\ll u\) and \(c\ge0\). Its main term is \(g_1[y^{1/3}\sum_{m\le K}c(m)m^{-1/3}-JC(K)]\). Equations (2) and (3) expand this as
\[
 c_1g_1\big[\tfrac32 y^{1/3}K^{2/3}-JK\big]
       +g_1\zeta(1/3)L(2/3,\chi)y^{1/3}
       +O(y^{1/4}J^{1/4}).
\]
The two terms in brackets can be evaluated at \(K=y/J^3\) at cost \(O(J)\), and then equal \(\tfrac12 yJ^{-2}\). This cancels the first-part term at that scale. Both \(y^{1/4}J^{1/4}\) and \(yJ^{-5/2}\) have order \(y^{7/22}\), while \(J\) is smaller. Finally convolve \(P\) with the actual coefficient sequence of \(W_4\). Its absolute Dirichlet series converges at \(7/22\) since \(11^7>2^{22}\), and the inherited deviations start at degree four away from five. Summation of the errors and completion of both main coefficients cost \(O(y^{7/22})\). The coefficient of \(y\) is \(U(1)\), and that of \(y^{1/3}\) is \(C_U\zeta(1/3)\). This proves (1).

## 2. Transfer with both negative squares and complete upper arguments

Freeze any cutoff and short coefficients \(a\) on a block, set \(b=t-a\), and let \(B_b(v)=\sum_{m\le v}b(m)\) with integer-floor convention. Assume \(a=t\) on \(1\le m\le A\), \(a=0\) for \(m>2A\), and \(|a(m)|\ll1\). Then \(b=0\) through \(A\). Put \(h(a)=\sum_m a(m)/m\), \(c(a)=\sum_m a(m)m^{-1/3}\). Since
\[
 t=2a-f*a*a+f*b*b,
\]
the long rectangle, with its two orientations and common overlap subtracted, is \(\mathcal L_b(n)-\mathcal S_b(n)\), where
\[
 \begin{split}
 r_k&=\lfloor\sqrt{n/k}\rfloor,\\
 \mathcal L_b(n)&=2\sum_{1\le k\le n/(A+1)^2}f(k)
                    \sum_{A<m\le r_k}b(m)B_b(n/(km)),\\
 \mathcal S_b(n)&=\sum_{1\le k\le n/(A+1)^2}f(k)B_b(r_k)^2\ge0.
 \end{split}
\]
The strict lower support and upper endpoints follow from \(km m'\le n\), and every admissible pair has at least one coordinate at most \(r_k\). The overlap is the full square \(A<m,m'\le r_k\). All linear states, including those beyond \(\sqrt n\), enter with exactly the same \(b\) as the overlap. In particular the largest possible linear state is \(n/(A+1)\).

As long as \((2A)^2\le7X/8\), insert (1) on the entire short rectangle. The main term is \(nU(1)h(a)^2\) and the cubic term is \(C_U\zeta(1/3)n^{1/3}c(a)^2\). Because each \(|a(m)|\ll1\), the error on the taper is
\[
  O\big(X^{7/22} A^{15/11}\big).
\]
The separate linear short sum \(2\sum_{m\le n}a(m)\) is \(O(A)\). Hence, uniformly on the taper,
\[
 T(n)=\mathcal L_b(n)-nU(1)h(a)^2-\mathcal S_b(n)
        -C_U\zeta(1/3)n^{1/3}c(a)^2
        +O\big(A+X^{7/22} A^{15/11}\big).                          \tag{4}
\]
The cubic contribution in (4) is nonnegative since \(\zeta(1/3)<0\). Two choices preserve the \(O(\sqrt X)\) comparison in the genuine two-negative-square profile.

- With \(A=\lfloor X^{1/8}\rfloor\) take the strict cut \(a=t_{\le A}\). The cubic contribution is \(O(X^{1/3}A^{4/3})=O(\sqrt X)\) and the remaining power is \(X^{43/88}\). Thus (4) gives a two-negative-square profile with every linear argument at most \(O(X^{7/8})\).
- With \(A=\lfloor X^{2/15}\rfloor\) take \(a(m)=t(m)\) for \(m\le A\), \(a(m)=\lambda_X\) for \(A<m\le2A\), and zero above \(2A\), where
  \[
      \lambda_X=-\frac{\sum_{m\le A}t(m)m^{-1/3}}
                         {\sum_{A<m\le2A}m^{-1/3}} .
  \]
  The denominator is \(\asymp A^{2/3}\), so \(|\lambda_X|\ll1\) and \(c(a)=0\) exactly. The explicit prefix for \(v>A\) is
  \[
      B_b(v)=T(v)-T(A)-\lambda_X(\min(\lfloor v\rfloor,2A)-A).
  \]
  For \(v\le A\) it is zero. This reallocation is fixed from actual \(t\) and affects both the two-factor profile and its compensating square. The error in (4) is \(O(\sqrt X)\), and every linear argument is at most \(O(X^{13/15})\).

Each profile therefore differs from \(T\) by \(O(X)\) in the taper norm. By the original norm comparisons it transfers the full all-epsilon \(Q_7\) and \(Q_8\) criteria, and the one-sided criterion still uses the same complete windows and positive-part norm comparison. This is a longer exact transfer with bounded error. It gives no upper bound for the signed profile itself. At the strict original round-eight cutoff the actual positive energy of the linear term after omitting the overlap penalty is already too large, as proved in [SQUARE-RETENTION.md](SQUARE-RETENTION.md).

## 3. Joint approximation of the large inverse-factor range

There is also a uniform approximation of the combined long-rectangle contribution from \(k>K\), keeping the two orientations together. Let \(K\ge1\) be an integer, fixed on the block, and \(\mathcal L_{b,>K},\mathcal S_{b,>K}\) be the above sums restricted to \(k>K\). For \(s>0\) put
\[
 J_s(n,K)=\sum_{\substack{m,m'>A\\mm'\le n/K}}
             b(m)b(m')\big[(n/(mm'))^s-K^s\big].
\]
An equality at \(mm'=n/K\) contributes zero. The exact unsmoothed predecessor is
\[
 \mathcal L_{b,>K}(n)-\mathcal S_{b,>K}(n)
     =\sum_{\substack{m,m'>A\\mm'\le n/K}}b(m)b(m')
                      \big[F(n/(mm'))-F(K)\big].
\]
This follows by counting the strict lower endpoint \(K<k\) for each pair. Substituting (1) controls the two terms jointly:
\[
 \mathcal L_{b,>K}-\mathcal S_{b,>K}
    = U(1)J_1(n,K)+C_U\zeta(1/3)J_{1/3}(n,K)
       +O\big(X K^{-15/22}\log(2X)\big).                            \tag{5}
\]
Indeed the total absolute error is at most a constant times
\(X^{7/22}\sum_{mm'\le n/K}(mm')^{-7/22}\). Summing first in \(m'\) gives \(O(XK^{-15/22}\log(2X))\). This applies to the strict and reallocated cuts. For the strict \(A=\lfloor X^{1/8}\rfloor\) and \(K=\lfloor X^{11/15+\delta}\rfloor\) with fixed \(0<\delta<1/60\), the error is \(O(X^{1/2-(15/22)\delta}\log(2X))\), and all arguments in this large-\(k\) sector lie at \(O(X^{17/120-\delta})\). Its geometric region remains nonempty since \(11/15+\delta<3/4\). The two real signed forms in (5) must stay with the original negative affine square, and the entire \(k\le K\) contribution remains in (4). No bound for the energies of the replaced joint profiles is implied by their approximation errors.

## Scope and evidence

**Candidate-D.** Equations (1) and (4)–(5) give a resolved actual inverse-weight mean, square-root-precision comparison with two retained negative squares at a longer factor cutoff, and a uniform polynomially smaller error for the combined large inverse-factor range. **O.** The full signed bound remains open.

- [Arithmetic-kernel baseline 6a91ef48f6454743797614503aa5863dde54befb](https://github.com/mathorn1973/twist-j/tree/6a91ef48f6454743797614503aa5863dde54befb/notes/C-RH-ARITHMETIC-KERNEL-N). Read FOUNDATION, round 6 BALANCED-UNIT-TAIL, and round 8 COUPLED-CUTS and REPORT. Their exact unit factorization, signs, norms, and complete-window transfer are inherited.
- [P. Erdős and P. Turán, On a problem in the theory of uniform distribution, I](https://users.renyi.hu/~p_erdos/1948-02.pdf) and [II](https://users.renyi.hu/~p_erdos/1948-03.pdf). Use their classical discrepancy inequality for a finite list of fractional parts, with the \(D/H\) and harmonic exponential-sum terms.
- [S. W. Graham and G. Kolesnik, Van der Corput's Method of Exponential Sums, Theorem 2.2](https://assets.cambridge.org/97805213/39278/excerpt/9780521339278_excerpt.pdf). Use the second-derivative estimate on fixed residue classes in (2). No distribution estimate for \(t\) in short intervals is required here.
- Read [the neighboring full coupled-energy proof at ceb77e3632ec4617c54d8e1fd504d3b1c99dd106](https://github.com/mathorn1973/twist-j/tree/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N) and [the Huang prime-scale reallocation at fd6232aa10da26a374e421d6d46538b36b41aafb](https://github.com/mathorn1973/twist-j/tree/fd6232aa10da26a374e421d6d46538b36b41aafb/notes/C-HUANG-ARITHMETIC-BRIDGE-N). Their Möbius coefficients and compensation schemes have different carriers. Here the additional constant weight enforces precisely one cubic moment of the actual \(t\) short factor, while the harmonic square and the true overlap remain.

Paper algebra and estimates only. No numerical or symbolic scientific execution, formal runner, or repository modification was performed in this lane. The authority and scope readbacks were completed by the session owner before delegation.

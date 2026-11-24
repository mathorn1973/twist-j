# Signed character estimates on the complete window

**NON-CANONICAL. Authority none.** The finite identities, bounds and
stated implications are **candidate-D**. The direct signed estimate at
the required scale is **O**. Action layer `NOT_APPLICABLE`. This is a
paper calculation on the family in [DIRICHLET-READOUT.md](DIRICHLET-READOUT.md),
with the cutoff constant fixed at \(1/36\).

## A fixed reader on the complete window

Take an integer \(Y\ge11\), \(X=\lceil Y^{3/2}\rceil\), and the least
power of two \(m>X^2\). The number of dyadic characters is \(h=m/2\).
Throughout this note \(\mathbb E_\chi\) means \(h^{-1}\sum_{\chi\bmod m}\)
and \(\psi=\theta\chi\), with the fixed cubic component modulo seven.
All intervals of integer arguments in the target are exactly \(Y\le N<X\).
Write \(R(N)=R_{1/36}(N)\) and \(K_{R,N}=K_{1/36,N}\) for the original
residual and its reader. Define the fixed reader

\[
\mathcal U_Y=\{d\in\mathcal D:Y^{1/4}<d\le X,
                     \ P^+(d)>(\log Y)^2/36\},\qquad
K_Y=\sum_{d\in\mathcal U_Y}E_d,
\qquad S_Y(N)=\mathbb E_\chi B_N(\psi)\overline{K_Y(\psi)}
\quad (1\le N\le X).
\]

By orthogonality on \(\mathcal H_X\), only \(d\le N\) contribute to this
pairing. For \(N\ge Y\), its summands include all the directions of
\(R(N)\). The additional directions have \(d\le N^{1/4}\) or
\(P^+(d)\le(\log N)^2/36\). Both are covered by the absolute deletion
bounds of [DIRICHLET-READOUT.md, Section 4](DIRICHLET-READOUT.md).
Consequently, uniformly on the same complete window,

\[
|S_Y(N)-R(N)|\ll\sqrt N,\qquad |S_Y(N)-M(N)|\ll\sqrt N,\qquad
\left|\sqrt{Q_R(Y)}-\sqrt{Q_{S_Y}(Y)}\right|\ll\sqrt{\log Y}.
\]

Here \(Q_{S_Y}\) uses the positive part after the signed average, and
the last bound follows by the positive-part Lipschitz inequality and
\(\sum_{Y\le N<X}(N+1)^{-1}=O(\log Y)\). The squared norm of the full
\(K_Y\) is of order \(X\). In pairings with \(B_N\), its orthogonal
projection to \(\mathcal H_N\) has squared norm \(D(N)-O(\sqrt N)\), by
the same deleted mass bounds. The switch of reader preserves all the
window quantifiers by using the source exponent \(2r\) and absorbing
the square-root logarithmic term.

## Fourth moments with all congruences retained

Every oriented direction of height at most \(D\) is a reduced ratio
\(u/v\) of odd integers with \(uv\le D\). Consider the fourth moment of
a polynomial in such directions with monomial coefficients at most
\(A_0\) in absolute value, where \(1\le D\le X\). Expanding the moment
and using dyadic character orthogonality leaves the congruences

\[
A=u_1u_2v_3v_4\equiv B=v_1v_2u_3u_4\pmod m,
\qquad AB\le D^4.
\]

The weights from \(\theta\) have absolute value one. For \(A=B\) there
are at most \(D^2\) choices of \(A\). For \(A>B\) we have \(B\le D^2\)
and \(A=B+km\) for some \(1\le k\le D^4/(mB)\le D^2/B\).
Summing over \(B\), and exchanging \(A,B\) for the other strict
ordering, gives \(O(D^2\log(2D))\) pairs including all congruence
aliases. Each pair has at most \(d_4(A)d_4(B)\) decompositions into
the eight ordered factors. The fixed-order divisor estimate
\(d_4(a)\ll_\epsilon a^\epsilon\) follows by bounding its prime-power
polynomial by \(p^{j\epsilon}\) for large primes uniformly in the
exponent \(j\), then taking the finite product of the bounds at small
primes. Thus the fourth moment is \(O_\epsilon(A_0^4D^{2+\epsilon})\).
The product directions have height up to \(D^2\), and their pairwise
determinants can be as large as \(D^4\). The use of \(m>X^2\) here is
through the congruence count.

Apply this to \(K_{R,N}\), whose nonzero monomial coefficients are
one, to get \(\|K_{R,N}\|_4\ll_\epsilon N^{1/2+\epsilon}\) in the
probability measure \(\mathbb E_\chi\). For \(B_N\), use dyadic bands
\(D/2<d\le D\), with upper endpoints \(D=N,N/2,\ldots\) down to the
band containing \(1\). The sector estimate of [MOBIUS.md](MOBIUS.md)
gives the bound for the individual monomials in such a band,

\[
|\beta_N(d)|\ll (N/d)^{1/3}\prod_{p\mid d}(1-p^{-2/3})^{-1}
                  \ll_\epsilon (N/D)^{1/3}D^\epsilon.
\]

For the second inequality, each sufficiently large prime factor
satisfies \((1-p^{-2/3})^{-1}\le p^\epsilon\). The finitely many
remaining factors contribute a fixed constant. The fourth norm of
each band is \(O_\epsilon(N^{1/3}D^{1/6+\epsilon})\), after adjusting
\(\epsilon\) in the congruence estimate. The triangle inequality for
the fourth norm and the geometric sum in \(D\) give

\[
\|B_N\|_4,\ \|K_{R,N}\|_4\ll_\epsilon N^{1/2+\epsilon},
\qquad
\mathbb E_\chi|B_N\overline{K_{R,N}}|^2\ll_\epsilon N^{2+\epsilon}.
\]

The same fourth norm bound for the reader holds for the projection of
\(K_Y\) to \(\mathcal H_N\), since its coefficients also belong to
\(\{0,1\}\). Everything uses the one sample family on the full
window.

The exact second norms of \(B_N\) and \(K_{R,N}\) are of order
\(\sqrt N\), by [MIXING.md](MIXING.md) and [DIRICHLET-READOUT.md](DIRICHLET-READOUT.md).
The interpolation inequality \(\|f\|_2^3\le\|f\|_1\|f\|_4^2\) now
shows that both first norms are \(\gg_\epsilon N^{1/2-\epsilon}\).
Therefore every separately evaluated Hölder product on the character
space, including exponents depending on \(N\), satisfies

\[
\|B_N\|_p\,\|K_{R,N}\|_q\gg_\epsilon N^{1-\epsilon}
\qquad(1/p+1/q=1,\ \ 1\le p,q\le\infty).
\]

This is a lower bound on that allowance. The signed average itself
may be much smaller. The fourth moment estimates include aliases
and establish the scale of the separate norms, while the estimate
for the product moment is only an upper bound.

## The weighted Dirichlet series and its distant aliases

Put \(b_\psi(n)=\boldsymbol\mu(n)(\psi)\) and
\(a_Y(n)=\mathbb E_\chi b_\psi(n)\overline{K_Y(\psi)}\), allowing all
\(n\ge1\). In the domain of absolute convergence,

\[
\mathcal F_Y(s)=\sum_{n\ge1}a_Y(n)n^{-s}
  =\mathbb E_\chi\overline{K_Y(\psi)}\left[
       U_\psi(s)\frac{L(s,\chi_5)^2}{L(s,\psi)L(s,\bar\psi)
                              L(s,\psi\chi_5)L(s,\bar\psi\chi_5)}
                                     \right]^{1/2}_{\mathrm{Euler}}.
\]

The branch indicated here is the product specifying \(F_\psi(s)\)
for \(\Re s>1\). The Dirichlet coefficient of the contribution with
direction support \(d\) comes from
\(\mathcal C_0(s)(-1)^{\omega(d)}d^{-s}\prod_{p\mid d}(1+p^{-2s})^{-1}E_d\).
Orthogonality compares its oriented ratios of height \(d\) with ratios
of height at most \(X\) in \(K_Y\). If \(dX\le m\), congruence implies
equality of the reduced ratios, since their positive cross products
are at most \(dX\) and their difference has absolute value less than
\(m\). It follows that

\[
\mathcal F_Y(s)=\mathcal C_0(s)
  \sum_{d\in\mathcal U_Y}\frac{(-2)^{\omega(d)}d^{-s}}
                                      {\prod_{p\mid d}(1+p^{-2s})}
  +\mathcal A_Y(s),\qquad \Re s>1,
\]

where the Dirichlet coefficients of \(\mathcal A_Y\) vanish for
\(n\le m/X\). Indeed, every direction at row index \(n\) has \(d\mid n\),
so an alias must have \(n\ge d>m/X>X\). Thus all coefficients of the
needed truncation at \(X\) come exactly from the displayed finite
direction sum. The separation concerns support in the coefficient
index. It supplies no bound for the weighted Dirichlet series outside
its domain of absolute convergence.

Half the dyadic characters have odd index \(b\) in the parametrization
of [DIRICHLET-READOUT.md](DIRICHLET-READOUT.md). Their value at \(5\)
has order \(2^{k-2}\) with \(m=2^k\), so they do not descend to modulus
\(m/2\). For these indices the primitive conductors of \(\psi\) and
\(\psi\chi_5\) are exactly \(7m\) and \(35m\), by coprimality of the
components. Their orders of magnitude are \(X^2\asymp Y^3\). An
estimate at a fixed conductor gives no uniform constant for these
indices. Even a uniform bound of the form
\(|B_N(\psi)|\ll_\epsilon N^{1/2+\epsilon}\), applied with the first
norm of the reader, gives an allowance of size \(N^{1+o(1)}\) in the
power scale. The Euler formula keeps the phases in \(\mathcal F_Y\)
and supplies no estimate of their signed joint contribution.

## A precise mixed moment at finite height

Let \(s=1/2+it\) and set

\[
\mathcal T_Y(s)=\mathbb E_\chi\!\left[
  \overline{K_Y(\psi)}\left(Y^{-s}B_Y(\psi)
    +\sum_{Y<n\le X}b_\psi(n)n^{-s}-X^{-s}B_X(\psi)\right)\right].
\]

The expression within the scalar average is obtained by truncating
the weighted series with all indices through \(Y\) pooled and all
indices after \(X\) excluded. Direct integration of the finite step
sum gives

\[
\int_Y^X S_Y(\lfloor x\rfloor)x^{-s-1}\,dx=\mathcal T_Y(s)/s.
\]

This identity follows by integrating each \(a_Y(n)\) from
\(\max(Y,n)\) to \(X\). All indices through \(Y\), including \(n=Y\),
are in \(B_Y\). The term for \(n=X\) cancels between the sum and
\(X^{-s}B_X\), so one may equivalently end the sum at \(X-1\) and
replace \(B_X\) by \(B_{X-1}\). With \(u=\log x\), the integral is the
Fourier transform of
\(e^{-u/2}S_Y(\lfloor e^u\rfloor)\mathbf1_{[\log Y,\log X)}(u)\).
Fourier Plancherel yields the exact equality

\[
\sum_{N=Y}^{X-1}\frac{S_Y(N)^2}{N(N+1)}
 =\frac1{2\pi}\int_{\mathbb R}\frac{|\mathcal T_Y(1/2+it)|^2}{1/4+t^2}\,dt.
\]

The factor \(1/[N(N+1)]\) is the integral of \(x^{-2}\) over
\([N,N+1)\). Both endpoints of the integer window are accounted for.
For \(n\le X\), the exact coefficient readout and the prime-power
rules imply \(|a_Y(n)|\le d_3(n)\). At a split prime the absolute sum
of the local monomial coefficients is \(3\) at exponent one and \(4\)
at higher exponents. Other prime powers have absolute sum at most one.
Combining these local bounds gives the divisor majorant at \(n\).
Counting the ordered factorizations shows
\(\sum_{n\le u}d_3(n)\le u(1+\log u)^2\). Thus

\[
|\mathcal T_Y(1/2+it)|
 \le\sum_{n\le X}|a_Y(n)|\bigl(\max(Y,n)^{-1/2}+X^{-1/2}\bigr)
 \ll \sqrt X(\log(2X))^2.
\]

The part of the weighted integral with \(|t|>X\) is
\(O((\log(2X))^4)\), uniformly in \(Y\). Consequently, a sufficient
analytic estimate is that for each \(\eta>0\), arbitrarily late
complete windows satisfy

\[
\int_{-X}^{X}\frac{|\mathcal T_Y(1/2+it)|^2}{1/4+t^2}\,dt
                       \ll_\eta Y^\eta.                         \tag{1}
\]

For exponent \(r\) in the target, use any \(\eta<1/r\) and absorb the
fixed constants and logarithms. The estimate (1) controls the
two-sided square. Its character average is taken before squaring.

There is also an exact one-sided requirement. For \(f_N\ge0\) with
\(\sum_{N=Y}^{X-1}f_N^2/[N(N+1)]\le1\), put

\[
H_f(n)=\sum_{\substack{Y\le N<X\\N\ge n}}\frac{f_N}{N(N+1)}.
\]

The supremum over these \(f\) of

\[
\Re\,\mathbb E_\chi\overline{K_Y(\psi)}
                    \sum_{n<X} b_\psi(n)H_f(n)
\]

is \(\sqrt{Q_{S_Y}(Y)}\). Interchanging the finite sums gives the
weighted pairing with \(S_Y(N)\). Its maximum is attained by the
normalized positive part when that part is nonzero, and by zero
otherwise. A subpower bound on this supremum on arbitrarily late
windows is equivalent to the target for \(R\), by the same-window
comparison. The exact one-sided formulation and (1) are estimates
to be proved. Neither the fourth moments nor the squared Euler
identity proves either estimate.

## Bounds imported through the scalar comparison

The unconditional Mertens bound in Lee and Leong, [version 4,
Theorem 1.2](https://arxiv.org/pdf/2208.06141v4), has the form

\[
|M(x)|\ll x\exp(-c\Phi(x)),\qquad
\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5},\qquad c>0.
\]

Together with \(R(N)=M(N)+O(\sqrt N)\) it gives, on every sufficiently
late whole window,

\[
Q_R(Y)\ll Y^{3/2}\exp(-2c\Phi(Y))+\log Y.
\]

Here \(\Phi\) is increasing at large arguments. This is a quantitative
subexponential saving over the separate norm estimate. Its leading
allowance has power \(Y^{3/2-o(1)}\).

Importing the Riemann hypothesis from the externally checked proof
gives a stronger bound through the rational-field case of Fujisawa
and Minamide, [Theorem 1.3](https://arxiv.org/pdf/1212.4348).
The [joint Lean FRO and Mathlib statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
identifies the externally checked theorem with Mathlib's statement
of the Riemann hypothesis. With that input, for each \(\epsilon>0\),

\[
|R(N)|\ll_\epsilon N^{1/2+\epsilon},\qquad
Q_R(Y)\ll_\epsilon X^{2\epsilon}\ll_\epsilon Y^{3\epsilon}.
\]

The same bound holds for the two-sided weighted square of \(S_Y\).
For each \(r\ge1\), choosing \(\epsilon=1/(6r)\) gives \(Q_R(Y)^r\le Y\)
for every sufficiently late \(Y\). This closes the numerical inequality
with the external RH input. The direct signed estimate in the fixed
Dirichlet family remains **O**.

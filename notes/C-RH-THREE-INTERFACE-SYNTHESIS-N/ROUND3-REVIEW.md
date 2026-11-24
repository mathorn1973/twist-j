# Whole-window opposition and a summable critical block

**NON-CANONICAL. Authority none.** The deductions and cross-checks in this
note are **candidate-D**. The direct estimate of the positive part of the
complete signed residual is **O**. Action layer `NOT_APPLICABLE`. The
opponent examined the three authors' paper arguments. Section 2 is an
additional derivation by the opponent. This is an open paper review under
the same candidate owner. No blind two-agent or computation-grade
confirmation is claimed.

Use the fixed residual at \(c=1/36\), the integer interval
\(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\), and the weights \(1/[N(N+1)]\) in
[DIRICHLET-READOUT.md](DIRICHLET-READOUT.md). Write \(Q_F\) for the
weighted squared norm of \(F_+\) on this interval. Every comparison below
takes the positive part after the complete signed sum.

## 1. Checks on the neutral and smooth bounds

**Candidate-D.** The exact neutral series has the finite-prime factor
\((1-5^{-s})/(1-5^{-4s})\). The pole of \(\zeta(4s)\) gives a zero of
its reciprocal on the real point of the boundary. On a vertical
dyadic block at height \(T\), the square of \(1/s\) contributes
\(O(T^{-2})\), and the square of the first Dirichlet factor contributes
\(O_\epsilon(T^{3/4+2\epsilon})\) by convexity at fixed conductor five.
The mean square of the second factor contributes \(O(T\log T)\) at
height \(2T\). The reciprocal zeta factor costs \(O((\log T)^2)\)
after squaring. Thus the block costs
\(O_\epsilon(T^{-1/4+2\epsilon}(\log T)^3)\), summable over dyadic
heights for \(0<\epsilon<1/8\). The mean-square input applies to a
primitive character of prime modulus. It is independent of the
growing conductors in the third section of this review.
[Katsurada and Matsumoto, Theorem 1](https://www.math.nagoya-u.ac.jp/~kohjimat/L-functions5.pdf).
[Lee and Leong, Theorem 3.1](https://arxiv.org/html/2208.06141v4).

Shifting an *unsmoothed* Perron integral would require separate
justification. In [WINDOW-BOUND.md](WINDOW-BOUND.md) the transform of a
compactly supported smooth test function decreases faster than every
power, uniformly across the entire strip. The horizontal edges vanish
against the polynomial growth there. Equality with the inverse Fourier
transform at \(1/4\) therefore holds in distributions. Plancherel gives
the finite number
\[
 B^2=\int_0^\infty |C_0(u)|^2u^{-3/2}\,du,
 \qquad C_0(u)=0\quad(0<u<1).
\]

For the smooth block, with \(L=\log N\), \(z=L^2/36\),
\(\ell=\log z\), and \(t=\log3\), the exponent from \(N^\sigma\) below
\(L/2\) equals \(-tL/\ell\). The product upper bound contributes
\(L/\ell+2(1-t)L/\ell^2+O(L/\ell^3)\) to its logarithm.
In particular the second-order term has the saving sign, and the
coefficient \(\delta=t-1>0\) survives in the pointwise exponent
\(-\delta L/\ell\). The passage to energy uses the strict
\(-\log36\) in \(\ell=2\log\log N-\log36\), which absorbs the harmonic
factor while retaining the coefficient in equation (4) of the window
note. The fixed value \(1/36\) is essential to these constants.

## 2. Global absolute energy at the critical support exponent

**Candidate-D.** Put
\[
 A_{1/3}(N)=\sum_{d\in\mathcal D,\ d\le N^{1/3}} |\gamma_d(N)|.
\]
The following strengthens the whole-window logarithmic allowance:
\[
 \sum_{N\ge1}\frac{A_{1/3}(N)^2}{N(N+1)}<\infty.             \tag{1}
\]
Cancellations within a neutral partial sum \(C_0\) enter through its
mean square. Absolute values may be taken over both the supports
and their square-power corrections in the remaining argument.

Write \(V=2^j\) for \(j\ge0\) and take the integer slab \([V,2V)\).
For \(i\ge0\) set \(D=2^{-i}(2V)^{1/3}\) and consider
\(D/2<d\le D\). Every short support is in one such band, and
the additional condition \(d\le N^{1/3}\) is a pointwise mask.
Keep the square-power index \(m\) fixed, put \(q=\operatorname{rad}(m)\),
and take only \(m\) composed of split primes, including \(m=1\).
At nonzero terms \(q\mid d\). For \(U=V/(Dm^2)\) define
\[
 B(U)^2=\int_U^{4U}|C_0(u)|^2u^{-3/2}\,du .
\]
The weighted slab norm of \(C_0(N/(dm^2))\) equals the norm obtained
by integrating over real \(x\in[V,2V)\) against \(dx/x^2\). Indeed
\(dm^2\) is an integer and all jumps occur at integer endpoints.
Set \(k=dm^2\). After the substitution \(x=ku\), the integration
interval in \(u\) is contained in \([U,4U]\), and its lower
endpoint is \(V/k\). The squared norm is at most
\(V^{-1/2}k^{-1/2}B(U)^2\).

For \(q\in\mathcal D\), squarefreeness gives
\[
 \sum_{d\le D,\ q\mid d}w(d)
 \le w(q)\sum_{e\le D/q}w(e)\ll w(q)D/q .
\]
For \(D<q\) the left side vanishes. Apply the norm triangle inequality
in the band to the enlarged absolute sector formula from [MOBIUS.md](MOBIUS.md).
Since \(d>D/2\), the cost of this \((i,m)\) on slab \(j\) is at most
\[
 C V^{-1/4}D^{3/4}\frac{w(q)}{q\sqrt m}B(U)
 =C'2^{-3i/4}\frac{w(q)}{q\sqrt m}B(U).                    \tag{2}
\]
This retains the divisibility restriction tying each square correction
to its own support.

At fixed \((i,m)\), the successive values of \(U\) as \(j\) increases
have ratio \(2^{2/3}\). Each \(u>0\) belongs to at most four of the
intervals \([U,4U]\). Thus the square sum in \(j\) of the localized
neutral norms is at most \(4B^2\). Take the triangle inequality again,
this time in the space of square-summable sequences indexed by \(j\).
The sum of \(2^{-3i/4}\) converges. The remaining sum is
\[
 \sum_{m}\frac{w(\operatorname{rad} m)}
                  {\operatorname{rad}(m)\sqrt m}
 =\prod_{p\ {\rm split}}\left(1+\frac{2}{p(\sqrt p-1)}\right)<\infty
\]
because its prime deviations are \(O(p^{-3/2})\). The estimates apply
first to finite subsums of the nonnegative majorant. Monotone convergence
proves (1) for all indices.

The total absolute smooth block at \(z_N=(\log N)^2/36\) also has
finite global weighted energy. In fact its squared summand is
\(\ll N^{-1}\exp(-2\delta\log N/\log z_N)\) eventually. This series
converges by comparison to \(1/[N(\log N)^2]\). Hence removing the
union of the smooth and critical short blocks leaves a separate residual
\[
 R^{(1/3)}(N)=\sum_{d\in\mathcal D,\ N^{1/3}<d\le N,\ P^+(d)>z_N}\gamma_d(N)
\]
with \(\|M-R^{(1/3)}\|_{[Y,\infty)}=o(1)\). Its square-root positive
energy differs from that of \(M\) by \(o(1)\) on every late window.
The original \(R\) retains its \(N^{1/4}\) cutoff and the quantitative
bound in equation (5) of [WINDOW-BOUND.md](WINDOW-BOUND.md). Equation
(1) gives no rate for the critical tail.

## 3. Frozen reader, aliases, conductor and finite height

**Candidate-D.** On \(Y\le N<X=\lceil Y^{3/2}\rceil\), the frozen
reader of [CHARACTER-WINDOW.md](CHARACTER-WINDOW.md) contains every
retained direction, and its projection is contained in the full
reader. Each difference of signed readouts among \(S_Y,R,M\) is
therefore bounded by the same *absolute* short and smooth deletions.
For any pair \(F,G\) in this triple one has the stronger comparison
\[
 |\sqrt{Q_F}-\sqrt{Q_G}|^2
 \le\|F-G\|_{I(Y)}^2
 \ll Y^{-1/8}+\exp(-\delta\log Y/\log\log Y).
\]
This uses the mask-uniform bound at \(1/4\) before summing the
neutral samples. A small *signed* difference for \(M-R\) alone would
not justify arbitrary intermediate subfamilies.

In the fourth moment, equality of the dyadic residues can occur
without rational equality. With \(AB\le D^4\) and \(m>D^2\), the
strict case \(A>B\) gives at most \(D^2/B\) positive multiples of
\(m\) to test at a fixed \(B\le D^2\). Counting all such pairs, including
the reverse ordering and equality, gives \(O(D^2\log(2D))\).
The fixed-order divisor bounds cost \(D^\epsilon\) after choosing the
individual exponents smaller. Interpolation in the *probability*
measure on the characters then gives the stated lower bound on every
product of separate Hölder norms. It yields no lower bound for the
absolute value of the signed average. Distant coefficient aliases
start beyond \(m/X\), since every contributing direction divides its
row index. Half of the dyadic characters are primitive at the full
power of two. Their fixed cubic and quadratic components have coprime
conductors, so the corresponding conductor growth is real.

For the finite Mellin transform the lower endpoint contributes \(Y^{-s}B_Y\).
The upper endpoint contributes \(-X^{-s}B_X\), with the coefficient
at \(n=X\) canceling against the finite sum. Plancherel gives the
two-sided energy. The coefficient bound by \(d_3(n)\) through \(X\)
bounds the contribution of \(|t|>X\) by \(O(\log^4(2X))\), using
\(\int_X^\infty t^{-2}\,dt=X^{-1}\). The resulting two-sided finite
moment is a sufficient estimate. The positive-test supremum in the
character note is the exact one-sided condition.

## 4. Centering, denominator removal and the surviving signed sum

**Candidate-D.** In [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md) the
removed large split-prime square divides \(m^2\), and the same prime
must divide \(d\). Its first possible total exponent is three.
The summatory estimate at each exponent \(2j+1\) gives
\(O(N/p^{2j+1})\), so summing over \(p>N^{1/4}\) gives
\(O(\sqrt N/\log N)\) with its asserted square-summable late tail.

Take \(X\) as the lower endpoint of a dyadic slab in this section.
The padding coefficients used there satisfy both \(\sum c_a=0\) and
\(c_a=\mu(a)\) through \(A\). The error convolution starts beyond
\(A^2\), including at the endpoint. The first identity makes the
constant term in the centered floor sum vanish exactly. The coefficient
of \(N+1/2\) in the resulting formula for \(M(N)\) is
\(-(\sum c_a/a)^2\). Extending the centered sum to products \(d>N\)
is required to keep this sign and exactness.

For \(g=(d,e)\), conditioning on the common residue gives covariance
\(\operatorname{Var}(r)/(de)=(g^2-1)/(12de)\). It is a complete-period
identity. An incomplete slab uses the separated-frequency bound, with
squared coefficient mass \(O(D(1+\log D)^3)\) and the factor
\(O(X+D^2)\). At \(D=\lfloor X^{2/3}\rfloor\), division by the local
\(X^2\) bounds weighted energy by \(O((1+\log X)^3)\) per slab.
Summing over the slabs meeting the whole window costs one logarithm
in the squared norm. The cutoff depends on the local \(X\), including
at the first partially used slab. The periodic covariance and generic
separated-frequency method for the earlier carrier are recorded in
[issue 2087](https://github.com/mathorn1973/twist-j/issues/2087).

There is also an endpoint version of the short-average multiplier test.
For \(H=\lceil\sqrt X\rceil\) and \(J=\lceil\log_2 X\rceil\), on
\(\|\theta\|\ge1/H\) the individual multiplier is at most \(1/2\),
so its \(J\)-th power is at most \(1/X\). The total absolute long-mode
coefficient mass is \(O(X(1+\log X)^2)\). Thus the discarded
high-frequency contribution costs \(O((1+\log X)^2)\) pointwise
after averaging. The price of replacing \(M(N)\) by its averaged
value is \(J(H-1)\), with squared weighted slab cost
\(O((1+\log X)^2)\). All translates are inside the identity's range
for sufficiently large \(X\). Jensen's inequality preserves the
short-denominator estimate for the iterated averages since these are
convex combinations of translates with a uniform bound. This proves
the logarithmic whole-window comparison of the prime note with the
retention \(0<\|\theta\|<1/H\). Even \(H=\lceil\sqrt{X\log X}\rceil\)
has weighted smoothing cost \(O((1+\log X)^3)\) per slab.
In both versions, the affine negative drift must be averaged as well.

For a primitive frequency of denominator \(q\), all contributing raw
denominators are multiples of \(q\). Combining them costs at most
\(\tau(q)(1+\log X)^2/q\) before the common geometric denominator.
The sum of the squared geometric reciprocals over the numerators is
\(O(q^2)\). Thus all primitive denominators through \(D_1\) together
cost \(O(D_1(1+\log X)^7)\) in squared Fourier mass. Applying the
separated-frequency bound with spacing \(D_1^{-2}\) confirms the
removal through \(D_1=\lfloor X^{2/3}/(\log X)^2\rfloor\) in the
final version of the prime note. If only equivalence of the subpower
criterion is wanted, one can even put \(D_1=\lfloor X^{2/3}\rfloor\):
the weighted cost is \(O((1+\log X)^7)\) per slab and the square-root
whole-window error is \(O((\log Y)^4)\). This version removes every
reduced denominator through the same cutoff as the raw denominators,
under the indicated larger logarithmic allowance.

In the lower-argument recurrence the endpoint terms are
\((\lfloor N/D\rfloor+1/2)B(D)\) and \(-(N+1/2)I(D)\).
When \(D\mid N\), the last floor-index pair contributes
\(B(D)-B(D)=0\), as required. For \(k,a\) fixed, changing
\(x=kat\) in the square norm gives the factor \((ka)^{-1/2}\).
Summing separate norms costs at most
\(O(X^{3/4}D^{-1/2})=O(X^{5/12})\) times the lower-energy supremum.
This is an allowance of that inference. It gives no necessary lower
bound on the size of the coupled recurrence.

## 5. Verdict on the requested positive energy

**Candidate-D from classical inputs.** For \(X=Y^{3/2}\), and
\(\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}\), the full positive energy
has the unconditional bound
\[
 Q_R(Y)\le (C^2+o(1))X\exp(-2c\Phi(X)).
\]
The endpoint \(X\) in the exponential is admissible because the
exponential weight is slowly varying on fixed proportional subintervals.
Its small-argument remainder is dominated by the summable integral
of \(v^{-1/2}\) in \(v=N/X\). The theorem's stated example gives
\(C=70179/12500\), \(c=319/100000\). These constants refer to
all sufficiently large arguments in the cited range and do not give
a numerical effective cutoff for the comparison's \(o(1)\).
[Lee and Leong, Theorem 1.2](https://arxiv.org/html/2208.06141v4).

**Candidate-D with external RH as premise.** The rational-field case of
the classical equivalence gives \(|M(N)|\ll_\epsilon N^{1/2+\epsilon}\).
Then \(Q_R(Y)\ll_\epsilon Y^{3\epsilon}\) for each \(\epsilon>0\), on every
sufficiently late window. Taking \(\epsilon=1/(6r)\) absorbs the fixed
constant in \(Q_R(Y)^r\le Y\). The cited joint Lean FRO and Mathlib
statement reports external verification of RH. This calculation imports
that theorem explicitly and performs no local rerun of the verification.
[Fujisawa and Minamide, Theorem 1.3](https://arxiv.org/pdf/1212.4348).
[Lean FRO and Mathlib joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/).

**O.** With RH excluded as an input, the deductions leave the original
late-window quantifiers open for the positive part of the full retained
pairing. A small mixed moment or a one-sided estimate on its surviving
coupled terms would address them. The absolute deletion estimates,
the separate character norms, and the short-denominator estimates
control designated errors on each same window.

# The signed sample kernel and its large-prime contribution

**NON-CANONICAL. Authority none.** The identities and restricted
asymptotic transfers are **candidate-D**. The full signed window estimate
is **O**. The argument uses the actual rows and coefficient inner product
of [MOBIUS.md](MOBIUS.md). Its analytic inputs are unconditional.

## 1. The kernel after conjugate samples are combined

Let \(P_N\) be the split primes up to \(N\), let \(r=|P_N|\ge1\), and
put \(q=4^r\). Write \(u_p=E_p/2\) at a fourth-root sample and
\(u_d=\prod_{p\mid d}u_p\). The two conjugate fourth roots \(i,-i\) both
give \(u_p=0\). The pushforward of the uniform fourth-root law is
\[
 \rho(u)=\prod_{p\in P_N}\rho_1(u_p),\qquad
 \rho_1(1)=\rho_1(-1)=\tfrac14,\quad \rho_1(0)=\tfrac12.
\]
Here \(E_d(u)=w(d)u_d\) for the admissible squarefree directions
\(d\le N\). Write \(u_+=(1,\ldots,1)\) and \(D=D(N)\). The fiber of
\(u_+\) has size one, so deletion removes its entire mass \(1/q\).
The isometric identification of sample vectors constant on the remaining
fibers sends their entry \(q^{-1/2}f(u)\) to
\(\rho(u)^{1/2}f(u)\).

In the \(3^r-1\) resulting Euclidean coordinates, the sample-space
operator \(AA^*\) has entries
\[
 (AA^*)_{u,v}=\sqrt{\rho(u)\rho(v)}\,K_N(u,v),\qquad
 K_N(u,v)=\sum_{d\le N}w(d)u_dv_d,\qquad u,v\ne u_+ .
\]
This follows by applying the analysis map to the orthonormal basis
\(E_d/\sqrt{w(d)}\). In the original fourth-root coordinates the entry
is \(q^{-1}K_N(u(t),u(t'))\). The normalization changes with the orbit
size in the combined coordinates. The kernel at the anchor is
\(K_N(u,u_+)=k_N(u)\). Thus with \(\beta=D/q\),
\[
 z(u)=\frac{\sqrt{\rho(u)}\,k_N(u)}{1-\beta},\qquad
 \langle AB_N,z\rangle
   =\frac{1}{1-\beta}\sum_{u\ne u_+}\rho(u) B_N(u)\,k_N(u).
\]
Since the compression is an isometry on the relevant image,
\(\|z\|^2=D/(1-\beta)\) is still minimal. The deleted term in the
numerator is \((D/q)\operatorname{aug}(B_N)\). A simultaneous change
\(u\mapsto-u\), \(v\mapsto-v\) leaves the undeleted kernel formula
fixed. Changing only the sample changes each summand of \(k_N\) by
\((-1)^{\omega(d)}\), with the coefficient norm invariant. A
one-prime check has \(k_N=1+E_p\), \(D=3\), \(q=4\),
and, in the order \(u_p=0,-1\), \(z=(2\sqrt2,-2)\). Its squared
norm is \(12\), and its readout on \(1-E_p\) is \(-1\).

## 2. Combining large split primes at the same quotient

Fix \(1/2\le a<1\) and set \(z_0=N^a\). A direction or a row with
argument at most \(N\) involves at most one prime \(p>z_0\), with
exponent one. Write \(P_{\le z_0}\) for the split primes at most \(z_0\),
and let
\[
 P_m=\{p\text{ split}:z_0<p\le N,\ \lfloor N/p\rfloor=m\},
 \qquad b_m=|P_m|,\qquad S_m=\sum_{p\in P_m}E_p.
\]
All sums over \(m\) below use the nonempty \(P_m\). For \(p\in P_m\) the
cofactor \(j\le m\) has all prime factors at most \(z_0\). The actual
rows with \(p\mid n\) therefore sum to \((1-E_p)B_m\). Let \(G_N\)
be the part of \(B_N\) with no directions involving any \(p>z_0\),
and define \(k_{\le z_0,N}\) by the analogous projection of \(k_N\).
The exact polynomials are
\[
 \begin{aligned}
 B_N &=G_N-\sum_m S_m B_m,\\
 k_N &=k_{\le z_0,N}+\sum_m S_m k_m,\\
 G_N &=\sum_{\substack{n\le N\\
               p\mid n,\ p\ \mathrm{split}\ \Rightarrow\ p\le z_0}}
                  \boldsymbol\mu(n)+\sum_m b_m B_m .
 \end{aligned}
\]
The last equality separates the actual-row mask from the
direction-support projection. The complete split-prime group at \(m=2\)
contributes zero even before sampling, since
\(B_2=\boldsymbol\mu(1)+\boldsymbol\mu(2)=1-1=0\).

In the ternary law \(S_m/2\) has the distribution
\[
 {\mathbb P}(S_m=2j)=4^{-b_m}\binom{2b_m}{b_m+j},
 \qquad -b_m\le j\le b_m .
\]
The probability generating Laurent polynomial per prime is
\((x^{-1}+2+x)/4\). Different groups are independent, with
\({\mathbb E}S_m=0\) and \({\mathbb E}S_m^2=2b_m\).
The \(P_{\le z_0}\) coordinates and these independent sums preserve both
actual polynomials. The all-positive corner requires the maximum in
each group and all the remaining coordinates to be \(1\). Its mass is
\(1/q\). The resulting number of undeleted coordinates is
\(3^{|P_{\le z_0}|}\prod_m(2b_m+1)-1\), strictly smaller than
\(3^r-1\) if any \(b_m\ge2\).

For \(f=f_0+\sum_m S_m f_m\) with \(f_0,f_m\) depending only on the
small coordinates, the squared norm of the grouped weighted analysis
after deletion is exactly
\[
 \|f_0\|^2+2\sum_m b_m\|f_m\|^2-\frac{|\operatorname{aug}(f)|^2}{q}.
\]
Here \(f\) is in the invariant subspace of \(\mathcal H_N\) under
permutations within every \(P_m\). This subspace contains \(B_N\)
and \(k_N\). For arbitrary \(f\in\mathcal H_N\), averaging these
permutations projects to it and preserves the target evaluation.
For grouped nodes \((u,S)\), \((v,S')\), the weighted sample-space
matrix uses the kernel
\[
 K_{\le z_0,N}(u,v)+\sum_m\frac{S_m S_m'}{2b_m}K_m(u,v)
\]
times the square roots of the two grouped node weights. Here
\(K_{\le z_0,N}\) restricts the sum defining \(K_N\) to directions
using only the small primes, and \(K_m\) uses the cofactor cutoff
\(d\le m\). The divisor \(2b_m\) is the squared norm of \(S_m\).
Evaluating the second node at \(S_m'=2b_m\) and \(v_p=1\) for
every small prime recovers \(k_N\). In particular,
\(D=\|k_{\le z_0,N}\|^2+2\sum_m b_mD(m)\) gives its exact squared
norm before deletion.
The grouped readout has the same minimal squared norm
\(D/(1-\beta)\) on the invariant subspace by the single removed
sample argument. With \(\mathbb E_{\le z_0}\) denoting the expectation
in the small coordinates, the numerator of the grouped pairing is
\[
 \mathbb E_{\le z_0}\!\left[
    G_N k_{\le z_0,N}-2\sum_m b_m B_m k_m\right]
    -\frac{D}{q}\operatorname{aug}(B_N).
\]
The first term inside the expectation retains all small-coordinate
products. Pairings between different large groups vanish by centering.
The retained same-group terms depend on the signed \(B_m\). Under the
independent two-point law with \(E_p=-2,1\) of respective weights
\(1/3,2/3\), the same conditional product gives these coefficients
\(-2b_m\) with no corner removed. It uses just the common first and
second moments. Changing the law preserves this identity and leaves
its signed cofactor arithmetic to be estimated.

An alternative grouped readout uses only \(1+\#\{m:b_m>0\}\) nodes
when at least one group is present. Fix all the small coordinates at
\(1\). Use the node \(\nu_0\) with all \(S_m=0\) and the node \(\nu_m\)
with \(S_m=-2\) and all other group sums zero. These nodes are
available and lie outside the deleted corner. Writing
\(b=\sum_m b_m\), the affine dependence on the group sums gives
\[
 \operatorname{aug}(f)
    =(1+b)f(\nu_0)-\sum_m b_m f(\nu_m).
\]
With \(\bar\rho\) the grouped probability, its squared Euclidean
reconstruction cost is
\[
 \frac{(1+b)^2}{\bar\rho(\nu_0)}
   +\sum_m\frac{b_m^2}{\bar\rho(\nu_m)}
   \ \ge\ (1+b)^2\,4^{|P_{\le z_0}|}.
\]
This bound follows from the weight of the fixed small coordinates.
The reduction in the number of sampled coordinates comes with this
explicit cost.

## 3. What is cancelled by the prime classes

The orientation projection onto directions containing a split
prime above \(z_0\) is
\[
 L_{N,a}=-\sum_m S_m B_m,\qquad
 \operatorname{aug}(L_{N,a})=-2\sum_m b_m M(m).
\]
The actual-row mask selecting \(n\) divisible by a split prime above
\(z_0\) has polynomial \(\sum_m(b_m-S_m)B_m\) and augmentation
\(-\sum_m b_m M(m)\). This mask retains the term \(b_mB_m\) in the
small-direction subspace. Every direction of \(L_{N,a}\) is also in
the orientation tail \(d>N^{1/4}\) of [MOBIUS.md](MOBIUS.md).

The pinned large-prime calculation in #2089, Section 4, equation (7),
gives the signed asymptotic for the scalar in the orientation
projection. The polynomial identity above identifies the prime
average with the orientation statistic at the same \(N\) and fixed cutoff.
[LOCAL-AVERAGES.md](LOCAL-AVERAGES.md) records the analytic derivation.
\[
 \operatorname{aug}(L_{N,a})
 =\frac{N}{(\log N)^2}
   +O_a\!\left(\frac{N}{(\log N)^3}\right).
\]
The actual-row mask for the split primes has half this value.

For \(N^a\ge5\), the large inert primes contribute
\(-\boldsymbol\mu(j)\) at \(n=pj\), while the contribution in the
neutral coordinate of a large split prime is \(+\boldsymbol\mu(j)\).
No large ramified prime occurs. Let
\[
 C_{N,a}=\sum_{z_0<p\le N}\chi_5(p) B_{\lfloor N/p\rfloor},
 \qquad
 B_{N,a}^{\mathrm{sm}}=
 \sum_{\substack{n\le N\\p\mid n\,\Rightarrow\, p\le z_0}}
       \boldsymbol\mu(n).
\]
Grouping the rows by all primes above \(z_0\), including the inert
ones, gives
\[
 B_N=B_{N,a}^{\mathrm{sm}}+C_{N,a}+L_{N,a},\qquad
 G_N=B_{N,a}^{\mathrm{sm}}+C_{N,a}.
\]
In the full product law the second polynomial is the conditional mean
of \(B_N\) over the large split coordinates. The deleted pairing uses
the explicit corner correction of Section 2.

For any fixed \(A>0\), the fixed-modulus prime number theorem bounds
\(\Pi_\chi(x)=\sum_{p\le x}\chi_5(p)\) by
\(O_A(x/(\log x)^A)\). The two residue classes for each sign have the
same density. The exact finite sum exchange is
\[
 C_{N,a}=
 \sum_{j\le N^{1-a}}\boldsymbol\mu(j)
          \big[\Pi_\chi(N/j)-\Pi_\chi(z_0)\big].
\]
Both prime arguments are at least \(N^a\), and \(z_0\le N/j\) in
every retained term. The bracket is thus
\(O_{A,a}((N/j)(\log N)^{-A})\).
In the Laurent monomial coefficient \(\ell^1\) norm,
\(\|\boldsymbol\mu(j)\|_1\le d_3(j)\), where \(d_3(j)\) counts
ordered factorizations into three positive integers. The local norms
are \(3\) at a split \(p\), \(4\) at a split \(p^e\) for \(e\ge2\),
and at most \(1\) at other prime powers. They are dominated by the
local values \(\binom{e+2}{2}\) of \(d_3\), and the coordinate
sets at distinct primes are disjoint.
The bound \(\sum_{j\le Z}d_3(j)/j\le(1+\log Z)^3\) follows by
dropping the product cutoff in the three harmonic sums. Taking the
prime estimate with exponent \(A+3\) gives, for every fixed \(A>0\),
\[
 \|C_{N,a}\|_1\ll_{A,a}\frac{N}{(\log N)^A}.
\]
This dominates the coefficient \(\ell^2\) norm and the evaluation
at every point with \(|X_p|=1\), including the anchor and both
sample families. It bounds the exact signed readout of \(C_{N,a}\)
without an extra factor for the reconstruction cost.

The surviving contribution from all rows with a prime greater than
\(z_0\) is positive to leading order \(N/(\log N)^2\), because it is
\(L_{N,a}+C_{N,a}\). The unconditional bound
\(M(N)=O_A(N/(\log N)^A)\) then forces
\[
 \operatorname{aug}(B_{N,a}^{\mathrm{sm}})
 =-\frac{N}{(\log N)^2}
   +O_a\!\left(\frac{N}{(\log N)^3}\right).
\]
This places the opposing term in the rows whose every prime factor
is at most \(z_0\), at the same argument as the positive orientation
term. Both estimates are on a logarithmic scale.
For the tail \(V(N)\) of [MOBIUS.md](MOBIUS.md), the complementary
term is the augmentation of \(B_{N,a}^{\mathrm{sm}}+C_{N,a}\) after
projection onto \(d>N^{1/4}\). Its value differs from the unprojected
complement by \(O(N^{1/2})\), because \(L_{N,a}\) lies in that
projection and the removed directions have the bound in that note.
It has the same leading negative term.

## 4. The whole-window requirement

On \([Y,Y^{3/2})\) the positive orientation contribution by itself
has energy
\[
 \sum_{Y\le N<Y^{3/2}}\frac{(\operatorname{aug}(L_{N,a})_+)^2}
                            {N(N+1)}
 \ \sim\ \frac{16}{81}\frac{Y^{3/2}}{(\log Y)^4}.
\]
For fixed \(0<\delta<1\), the summands on
\([\delta Y^{3/2},Y^{3/2})\) are uniformly
\((1+o(1))/((3/2)\log Y)^4\). The remaining terms are bounded by
\(O_a((\log Y)^{-4})\) each and number at most \(\delta Y^{3/2}\).
Taking the large-\(Y\) limit and then \(\delta\) to zero gives the
constant. A proof taking the positive part of this orientation
block before recombining the signed contributions cannot yield the
requested subpower window bound.

**O.** The scalar still to be controlled inside the positive part at
each \(N\) is
\[
 \operatorname{aug}(B_{N,a}^{\mathrm{sm}})
 +\operatorname{aug}(C_{N,a})
 -2\sum_{N^a<p\le N,\,\chi_5(p)=1}M(N/p).
\]
The signed joint residual on arbitrarily late whole windows is open
after aggregation has preserved the exact kernel and reconstruction cost.

## Sources

- [Pinned #2089 large-prime averaging, especially Section 4, equation (7)](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/round3/LARGE-PRIME-TAIL.md)
  provides the Mertens prime average at the fixed cutoff. The statistic
  using \(T\) in the same source is a separate residue-weighted average.
- [Thorner and Zaman, *Refinements to the prime number theorem for arithmetic progressions*, Corollary 1.4 and Remark 1.5](https://arxiv.org/pdf/2108.10878v2).
  At modulus five the possible secondary term has a fixed exponent below
  one. Partial summation gives the asserted arbitrary fixed inverse
  logarithmic orders for the prime counts.
- [Lee and Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, Theorem 1.1, equation (9)](https://arxiv.org/pdf/2208.06141v4).
  The unconditional exponential-in-square-root-logarithm bound implies
  the fixed inverse logarithmic orders used here.

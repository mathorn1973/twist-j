# Opposition on the signed pairing

**NON-CANONICAL. Authority none.** This is an internal paper review by a
separate Astra agent in the same session. The deductions retained here are
**candidate-D**. The arithmetic window estimate is **O**. The review used
no new scientific executable, enumeration or Lean build.

## Support, signs and size

For a fixed \(1/2\le a<1\), a row has at most one prime exceeding
\(N^a\). If that prime is split and \(m=\lfloor N/p\rfloor\), its row
contribution is \((1-E_p)B_m\). Its nonconstant direction contributes
\(-E_p B_m\). At the target these give \(-M(m)\) and \(-2M(m)\),
respectively. An inert prime contributes \(-B_m\) before evaluation.
Together with the neutral split term this gives the signed carrier
\(\sum_{N^a<p\le N}\chi_5(p) B_{\lfloor N/p\rfloor}\) for \(N^a\ge5\).
The exchange with the row sum uses both endpoints of the same prime
count. Bounding the row coefficient norm by \(d_3(j)\) costs at most
three fixed logarithmic powers. The fixed-modulus error absorbs them,
also after evaluating any unit-circle sample. This last estimate has no
factor from Cauchy with the readout vector.

The grouping by \(m\) preserves the two actual polynomials because each
large prime in a group has exactly the same permitted cofactors. A
generic input need not have this symmetry. The grouped minimal cost
refers to the permutation-invariant span. The grouped kernel divisor is
\(2b_m\), the variance of the group sum. Multiplication of the two signed
expansions therefore produces \(-2b_m B_m k_m\) in its conditional
mean. The omitted fourth-root sample has mass \(4^{-|P_N|}\), also in
the grouped coordinates. Only one corner has that mass removed.

The pinned Mertens prime average has leading term \(+N/(\log N)^2\)
for the orientation projection. The cofactor Mellin transform
\(1/(s\zeta(s))\) vanishes at one and its derivative there is one.
For the single-prime sector, the transform \(\mathcal C_0(s)/s\) has
positive value \(b_0\) there. The orientation terms at order
\(N/\log N\) consequently have coefficients \(-b_0,+b_0\). At order
\(N/(\log N)^2\) they sum to one. The total positive orientation
energy on \([Y,Y^{3/2})\) has leading constant \((3/2)^{-4}=16/81\).
The opposite term for the rows with all prime factors at most \(N^a\)
uses the classical unconditional bound for \(M(N)\). It determines a
logarithmic main term. Any fixed logarithmic accuracy still permits an
error larger than the square-root scale. All these asymptotics hold for
fixed \(a\), with no conclusion uniform as \(a\) approaches one.

## Deletions and moving windows

With \(p\ge11\) split, \(2/(1-p^{-2/3})\le3\). Replacing split primes
by all positive integers bounds the logarithm of the product in the
sector estimate by \((9/2)z^{2/3}\). At
\(z=(\log N/27)^{3/2}\) this is \((\log N)/6\). The argument bounds the
sum of absolute sector contributions, hence every subfamily. It does
not place a smoothness condition on row indices. The separate small
support cutoff can be subtracted first to avoid double counting. The
resulting \(O(\sqrt N)\) pointwise error gives a difference of at most
\(O_\lambda(\sqrt{\log Y})\) between square roots of positive-part
energies on each complete window. Passing from exponent \(2r\) to \(r\)
absorbs this error on arbitrarily late good windows for either sequence.

For a fixed finite set of modified split coordinates, a unit-circle
value of each root of \(1-\eta t+t^2\) follows from real
\(-2\le\eta\le2\), including its double-root endpoints. The denominator
has roots on the same circle. Both the modification and its inverse are
absolutely convergent for every positive real part. Poles and their
multiplicities in the open right critical half-plane are consequently
preserved. The one-sided criterion follows separately for each real
sequence by the pinned signed power-window lemma. Dilation convolution
is used for all-argument bounds only. No such fixed Euler modification
argument provides uniform estimates for a growing set of coordinates.

## Metric and raw-data tests

Compressing a positive form to the span of signal and target decreases
the inverse quadratic form by its variational formula. Conversely an
optimal plane form extends without increasing its condition number.
After determinant normalization, minimizing over the real bisector
entry gives \(\rho^2+\max(0,Cs-S)^2\) for the squared normalized
product. The imaginary off-diagonal entry cannot lower this value.
At \(\rho=0\) the result is \(1/K\), at \(\rho=1\) it is one, and
the two branches agree at \(s=S/C\). Optimizing a form for the actual
pair uses its unknown overlap. A rank-one form fixed from the target
alone realizes the displayed minimax alternative. Its measured
component along the target still contains the whole overlap.

The actual coefficient energy has order \(N\). The lower bound uses
the untouched top band. The upper bound squares the sector estimate
before the positive convolution, giving the squared factor
\((1-p^{-2/3})^{-2}\) and the integrable exponent \(2/3\) in partial
summation. For \(K\asymp N\), the raw mixed squared norm product is
exactly \(M(N)^2\) plus a nonnegative \(O(N)\) term. Thus a bounded
readout norm at this choice of metric does not estimate the signal
component pointing at the target. For a removed block of squared mass
\(D_T\), the minimum readout costs on projected and unprojected data
are \(D_T/(1-D_T/q)\) and \(D_T+D_T^2/(q-D)\), respectively. The
different denominators correspond to different data available to the
readout.

For block-preserving positive forms, the within-block Cauchy bounds and
one more Cauchy across blocks give the absolute mass obstruction.
For any fixed prime set \(R\) the top-band obstruction survives with
positive density. For a moving \(R_N\) the exact coprime top-band sum
can shrink or vanish, so the fixed-set lower bound supplies no uniform
linear obstruction. The stronger two-sided block-energy criterion is
sufficient on arbitrarily late complete windows. Its endpoint with
one block is the weighted square of the actual Mertens sum. No bound
for an intermediate moving partition has been obtained here.

## The sharp constant for absolute removal of smooth directions

**Candidate-D.** Define the actual absolute sector sum
\[
 S(N,z)=\sum_{\substack{d\le N,\ d\in\mathcal D\\p\mid d\Rightarrow p\le z}}
              |\gamma_d(N)|.
\]
For fixed \(c>0\), a uniform pointwise bound
\(S(N,c(\log N)^2)=O_c(\sqrt N)\) holds exactly when
\(c<1/(4e^2)\). The obstruction at and above the endpoint occurs
on an unbounded sequence of integer arguments. It concerns an absolute
sum. There is no resulting obstruction to the signed subpower test on
arbitrarily late complete windows.

For the upper bound, retaining \(d\le N\) in the old sector estimate gives
for \(1/3\le\sigma<1/2\)
\[
 S(N,z)\ll N^\sigma\prod_{p\le z,\ p\ {\rm split}}
 \left(1+\frac{2p^{-\sigma}}{1-p^{-2/3}}\right)
\]
by inserting \((N/d)^{\sigma-1/3}\ge1\). Set
\(\sigma=1/2-1/\log z\). For large \(z\) this is admissible and
\(p^{-\sigma}\le e\,p^{-1/2}\) for all the indicated primes.
The logarithm of the product is at most
\((2e+o(1))\sqrt z/\log z\), since partial summation of the
fixed-modulus prime count gives
\(\sum_{p\le z,\ p\ {\rm split}}p^{-1/2}\sim\sqrt z/\log z\).
The correction from the denominator is bounded by a convergent
multiple of \(\sum_p p^{-7/6}\). For \(z=c(\log N)^2\) the saving
\((\log N)/\log z\) in the log of the prefactor absorbs this bound
whenever \(2e\sqrt c<1\).

It suffices for the converse to treat \(c=1/(4e^2)\), by monotonicity
of the absolute sum. Take real \(T\to\infty\), \(l=\log T\), and put
\[
 \sigma=\tfrac12-l^{-1}-2l^{-2}-3l^{-3},\qquad
 a=1-\sigma,\qquad H=T^a/a.
\]
Select a squarefree subset of the split primes up to \(T\) by giving its
product \(d\) probability \(w(d)d^{-\sigma}/Z\), where
\(Z=\prod_{p\le T,\ p\ {\rm split}}(1+2p^{-\sigma})\).
The individual prime selections are independent. For
\(\mu=\mathbb E\log d\) one has
\[
 \mu=H+O(H/l^5),\qquad
 \log Z=\operatorname{Li}(T^a)+O(H/l^5),\qquad
 \operatorname{Var}(\log d)\le l\mu.
\]
Indeed the inclusion probability is \(2p^{-\sigma}/(1+2p^{-\sigma})\).
Replacing it by \(2p^{-\sigma}\) and expanding the log of each Euler
factor give errors bounded by
\(O(\sum_{n\le T} n^{-2\sigma}\log(2n))=O(l^2)\), uniformly here
because \(n^{-2\sigma}\ll n^{-1}\) for \(n\le T\).
Partial summation of the fixed-modulus prime count to arbitrary fixed
inverse logarithmic precision leaves the integrals
\(\int_2^T u^{-\sigma}\,du\) and
\(\int_2^T u^{-\sigma}\,du/\log u\), respectively.
Their values differ from \(H\) and \(\operatorname{Li}(T^a)\) by
bounded quantities. Splitting the integrals at \(\sqrt T\) and choosing
the prime-count error exponent above seven bounds those errors uniformly,
since \(a\) stays in a fixed compact subinterval of \((0,1)\).
For the variance, each Bernoulli variance is at most its mean
and \((\log p)^2\le l\log p\).

At this precision, three terms of the logarithmic integral give
\[
 H=2e\sqrt T\bigl(1+l^{-2}+O(l^{-3})\bigr),\qquad
 \log Z+(\sigma-\tfrac12)H
      =\frac{H}{l^3}\bigl(1+O(l^{-1})\bigr).
\]
For the first identity take logs in \(H/(2e\sqrt T)\).
For the second put \(r=al\). Integration by parts gives
\(\operatorname{Li}(T^a)/H=l^{-1}(1+r^{-1}+2r^{-2}+O(l^{-3}))\),
where \(r^{-1}=2/l-4/l^2+O(l^{-3})\).
The coefficient of \(l^{-3}\) after adding \(\sigma-1/2\) is
\(-3-4+8=1\).

Chebyshev's inequality places probability \(1-o(1)\) on
\(|\log d-H|\le H/l^4\). At most \(O(H)\) intervals of the form
\((N/2,N]\) with \(N\) a power of two meet this range. One of them
has probability \(\gg1/H\), and \(\log N=H+O(H/l^4)\). Hence
\(T<(\log N)^2/(4e^2)\) for all sufficiently large \(T\). Every
selected product in the interval is a permitted smooth support and
lies in the top band of the actual sum at this \(N\), so
\(|\gamma_d(N)|=w(d)\). The total weight in the band is at least
\(Z(N/2)^\sigma\) times its probability. After dividing the total by
\(\sqrt N\), its logarithm is bounded below by
\[
 \log Z+(\sigma-\tfrac12)\log N-O(\log H)
       =(1+o(1))H/l^3\longrightarrow\infty.
\]
In particular a bound for the full absolute sum cannot extend to the
endpoint. Additional cancellation between signed sectors remains possible.

## Arithmetic sampling and the missing corner

**Candidate-D.** In the preliminary prime-modulus proposal, deletion
of the principal character removes only one index. Other characters can
restrict trivially to the subgroup generated by the sampled primes.
The reviewer contributed the dyadic family with a fixed cubic twist
and the squared Dirichlet-series identity. The Sol author developed
the full proof in [DIRICHLET-READOUT.md](DIRICHLET-READOUT.md). This
part is joint work within the session.

Readback confirms that every dyadic character takes a value of
two-power order at \(11\), while the twist takes a primitive cubic
value there. Consequently every evaluation differs from augmentation
on \(E_{11}\) when \(N\ge11\). The fixed phases preserve orthogonality
of the separated fractions in the entire common window. The norm
\(D(N)\) is the minimum squared readout norm in the stated uniform
scalar product. The independent two-point product law attains the
same cost on the symmetric span.

For the squared Euler factorization, the split local identity is
exact. At \(2,7\) all four denominator characters vanish and the
unit contributes \((1-t^2)^2\). At five only the two untwisted
denominator factors survive. All other corrections start in degree
two, so absolute convergence of the unit and its inverse at each
fixed \(\sigma>1/2\) is uniform in the sample conductor. This
continues the square. A conclusion about individual square roots
needs local parity of zeros and poles. A bound for the signed
character readout also requires its actual weights and cutoff on
the same windows.

The root's combined residual in DIRICHLET-READOUT.md, Sections 4 and 5,
was checked separately after the component deductions. The common
isometry reads its retained coefficients directly from the unprojected
data, with minimum squared norm D_c(N) on the full input space. The
absolute bounds apply to both deleted families and their possible
overlap; the smaller Euler factors bound the deleted basis mass as
well. Thus M(N)-R_c(N)=O(sqrt(N)) and D(N)-D_c(N)=O(sqrt(N)).
The square-root energy comparison on each same window, with the
source accuracy 2r for the target accuracy r, proves both directions
of the stated window equivalence. The simple choice c=1/36 lies
strictly inside the allowed range because e<3. No residual-window
bound is supplied by that equivalence.

## Disposition

**Candidate-D.** The compressed samples, block readers and metric
computations retain the original signed scalar and their respective
reconstruction costs. The positive complete large-prime block rules out
bounding its energy separately at the requested scale. **O.** An
arithmetic estimate of the joint residual on the same complete windows
remains open. This is a review of paper derivations within the present
candidate. It carries no external referee or architecture confirmation.

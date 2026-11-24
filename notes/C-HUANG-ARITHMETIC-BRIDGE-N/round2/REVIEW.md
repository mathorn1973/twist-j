# Astra review of the two signs across time

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
The paper deductions below have candidate-D status. The original
complete-window positive-energy estimate is O. This is a same-session
review of the proofs. No scientific executable, enumeration, numerical
test or formal proof assistant was used.

| Reviewed input | Commit |
| --- | --- |
| Round-two scope | `51c7bc9024ca601d4d21511a2b88ffcacc9f84fe` |
| SIGNED-INTERVALS.md | `bd2eae68aebeebd5d7a16d113a367b6693699cfa` |
| MIXED-BOUNDARIES.md | `652b068179d5c277022fdb6d05ac4f4cb8617ddc` |
| PRIME-SCALE-CANCELLATION.md | `4bd0bd8442ae2a95dd32cd9f06d10419f18829a7` |
| Prior complete-window arithmetic | `ceb77e3632ec4617c54d8e1fd504d3b1c99dd106` |
| Neighboring coupled cuts | `6a91ef48f6454743797614503aa5863dde54befb` |

## Interval endpoints and the compensated sum

**Candidate-D.** Pairing a squarefree \(p\)-free base \(a\) with \(pa\)
puts coefficient \(+\mu(a)\mu(b)\) at the threshold \(kab\) when
\(a>T\), and \(-\mu(a)\mu(b)\) at \(kpab\) when \(pa>T\). Thus if
\(T/p<a\le T\), only the second jump occurs and it persists to the
end of the range. On a slab-window intersection the half-open interval
Gram kernel uses the integer endpoints
\(A=\max(X,Y)\), \(B=\min(2X,\lceil Y^{3/2}\rceil)\) for integer
\(Y\). For a nonempty intersection \([l,u)\) the exact weight is
\(1/l-1/u\). A shift that makes an interval start below one changes
neither this rule nor the actual positive lower endpoint \(l\).
Two separately averaged intervals require a double sum over shifts.
The squared norm has both mixed signs, the cross term with the
negative affine square, and the squared affine term. The positive
dual uses a single nonnegative test normalized over the entire
window, including its two outer fragments.

The factorization \(\mu=(\delta_1-\delta_p)*\nu_p\) holds at all
prime powers. The \(p\)-free core supplies the original sign, inserting
one \(p\) reverses it, and greater powers give zero. In
\(u'=(\delta_1-\delta_p)*(\nu_p\mathbf1_{d\le T})\) the two summands
have disjoint support and opposite total mass. Thus \(\sum u'=0\)
and the support ends at \(pT\). For \(g=\mu-u'\) the identity
\((g*g-u'*u')*\mathbf1=\mu-2u'\) permits the reallocation.
At \(n\ge pT\), summing the short linear term gives zero. The intercept
from the small rectangle also vanishes because it equals
\((\sum u')^2/2\). Its harmonic sum still gives the negative term
\(-(n+1/2)(\sum_d u'(d)/d)^2\). The long corner contains the actual
floor combination \(\lfloor x\rfloor-2\lfloor x/p\rfloor+
\lfloor x/p^2\rfloor\) at \(x=n/(ab)\), with \(p\)-free \(a,b>T\).
These identities remove a known intercept exactly. They leave a
signed two-factor sum to estimate.

**Candidate-D. Quantitative cost.** For several selected primes put
\(P=\prod_{p\in S}p\), with nonempty \(S\) fixed throughout a slab.
The unique decomposition into a selected-prime divisor and a coprime
core gives \(|u'|\le1\), support \(d\le PT\), and zero total mass.
For \(T=\lfloor X^{1/4}\rfloor\), the inherited small-rectangle
estimate gives, uniformly in such selections with \(PT\le X^{1/3}\),
\[
 \|U_H^J M-Z'_X\|_X
 \ll P^3 X^{-1/4}(1+\log X)^{3/2}.
\]
Indeed the square of the norm is bounded by a constant times
\((X+(PT)^4)(PT)^2(1+\log X)^3/X^2\). This proves power saving
when \(P\le X^{1/12-\delta}\) with fixed \(\delta>0\). This includes
the selection \(p\le\kappa\log X\) with fixed \(0<\kappa<1/12\)
by the prime number theorem. Since the slab errors sum in square
and decrease geometrically in the dyadic scale up to logarithms,
the inherited full comparison with \(R_{1/36}\) saves every fixed
inverse power of \(\log Y\) on each sufficiently late complete window.
This saving bounds the difference of the two carriers. The positive
energy of either carrier still needs its own estimate.

## Mixed paths, persistent classes and readout cost

**Candidate-D.** In a nested pair of product cutoffs an off-diagonal
mixed term survives exactly when one intermediate vertex is inside the
smaller cutoff and the other is outside the larger, for nonzero weights
in both changing directions. Both occurrences of the signed path then
have the same sign. For the coefficient of \(c_p^2c_q^2\) with
\(p<q\), a face occupied at both times only by its base contributes
\(2\mu(d)\). Extending the larger cutoff to the first edge contributes \(\mu(d)\).
When both cuts contain three vertices the rank-one defect on the two
upper vertices contributes \(-2\mu(d)\). The other pairs of initial
segments give zero mixed coefficient. In particular equal pairs of
individual indices need not determine a mixed trace.

For the one-factor filtration, the paired subcomplex contracts by
\(c_p^{-1}\varepsilon_p\). For an unpaired \(d\), each term of
\(\partial e_d\) removes a prime of nonzero weight at least \(p\),
so that its \(p\)-extension is already present when \(d\) enters.
This proves that \(z_d=e_d-c_p^{-1}\varepsilon_p\partial e_d\)
is a cycle at birth \(d\). It projects to its own unpaired basis label
throughout \([d,pd)\). Upon inclusion at \(pd\) it becomes
\(c_p^{-1}\partial\varepsilon_p e_d\). The rank from \(N\) to
\(M\ge N\) therefore counts the \(p\)-free labels \(M/p<d\le N\)
in each degree. This proof uses the least prime of nonzero weight.
If smaller primes have zero weight, deleting them contributes no
term to the differential. The ambient list and the weights must
remain fixed across both cuts.

The cycles above represent homology. They need not themselves be
harmonic. Orthogonally projecting a cycle to the harmonic space
changes it by a boundary. Inclusion preserves boundaries, which
identifies the rank of harmonic projection from one cut to the
other with the rank just proved. The argument does not specify the
nonzero singular values. At \(p=2,N=1,M=3\) on the ordinary divisor
cutoffs the map is zero and the product of indices equals \(-1\).
Thus even zero overlap can coexist with a nonzero scalar product
of traces. The barcode concerns the one-factor divisor complex.
The nested path formula applies more generally to the two-copy cut.

There is an exact comparison between the two time formulas.
For this same \(p\), the coefficient of \(c_p^4\) in the mixed graded
trace is the even rank minus the odd rank of harmonic inclusion.
Both are the sum of \(\mu(d)\) over the labels present at both cuts.
In the product \(I_N I_M\) of the scalar indices, expanding both
as signed interval sums gives one term for each pair of labels.
The diagonal terms add up to the *sum* of the two harmonic ranks,
since \(\mu(d)^2=1\) on these labels. All pairs of distinct labels
remain in the scalar product, including their signs. This describes
the exact part of the two-time pairing recovered by ranks.

The grading functional on the full tensor space has representing
matrix \(\Gamma_x\otimes\Gamma_y\). Its singular values are ones in
dimension \(d_xd_y\). This proves the respective dual costs
\(\sqrt{d_xd_y}\) and \(d_xd_y\) for Hilbert-Schmidt and operator
norms. These costs describe unrestricted tests. The real square of
the summed scalar readout uses the tensor, all pairs of shifts and
floor layers, the affine cross term and its square. The positive
energy additionally requires the sign of that scalar.

## The diagonal on a complete time window

**Candidate-D.** Let \(A=Y\), \(B=\lceil Y^{3/2}\rceil\) for integer
\(Y\ge11\), and use \(w(N)=1/[N(N+1)]\). Specialize the one-prime
formula to \(p=2\) and the actual Möbius sum. Each odd squarefree
label \(d\) contributes \(\mu(d)\) on \([d,2d)\). For two odd labels
\(a<b\), their window overlap has weight
\[
 K(a,b)=
 \begin{cases}
 l^{-1}-u^{-1},&l<u,\\
 0,&l\ge u,
 \end{cases}
 \qquad l=\max(A,b),\quad u=\min(B,2a).
\]
In particular, a nonzero overlap requires \(a<b<2a\). Expanding the
two-sided squared norm gives \(E_M=D+C\), where
\[
 C=2\sum_{\substack{a<b<B\\a,b\ {\rm odd}}}\mu(a)\mu(b)K(a,b),
 \qquad D=\sum_{A\le N<B}w(N)r_N.
\]
Here \(r_N\) is the number of odd squarefree labels in \((N/2,N]\),
which is the total harmonic dimension at that cut with unit weights.
All terms with a nonsquarefree label vanish. Counting the odd
integers already gives \(r_N\le N/4+1\). Consequently
\[
 0\le D\le\tfrac14\log(B/A)+1/A,
\]
since \(\sum_{A\le N<B}(N+1)^{-1}\le\log(B/A)\) and
\(\sum_{A\le N<B}w(N)=1/A-1/B\). Thus the actual diagonal fits
a logarithmic bound on every such window by elementarily counting
labels.

The remaining \(C\) is signed and satisfies \(C\ge-D\) by \(E_M\ge0\).
Since \(Q_M\le E_M\le D+C_+\), a bound \(C_+\le Y^\epsilon\) on
arbitrarily late original windows for every \(\epsilon>0\) would
suffice for the positive-energy target. Choose a smaller exponent
to absorb the logarithm and the inherited weighted norm error in
passing to \(R_{1/36}\). For exact one-sided energy, insert
\(g_N=\mathbf1_{M(N)>0}\) in every overlap sum and the diagonal,
giving \(Q_M=D_g+C_g\) and \(0\le D_g\le D\). This gate is determined
by the same coefficients as the pair products. The reduction gives
no bound on their signed correlations. Their shifts \(b-a\) are even
and may grow with the window.

## Prime filters across scales

**Candidate-D.** The two-prime kernel for \(2,3\) puts opposite signs
on two pulses of equal logarithmic length. At prime cores the prime
number theorem gives filtered contribution \(-x/(3\log x)\) to leading
order. The unit and composite cores consequently contribute
\(+x/(3\log x)\) to leading order by the inherited classical estimate
for \(M\). This is cancellation of actual coefficients. The positive
energy of the latter sector already exceeds a constant times
\(Y^{3/2}/(\log Y)^2\) on every sufficiently late complete window.
An upper bound obtained by keeping this sector alone is too large.

On the full critical log line the inverse multiplier has norm
\(\prod_{p\in S}(1-p^{-1/2})^{-1}\), since the minimum modulus of
the forward multiplier occurs at frequency zero. For finite windows
the inverse expansion uses translations of the test interval. For a single
prime a nonnegative input on \((J-\log p)\setminus J\) can give a
positive inverse output on \(J\) even when the input there vanishes.
A negative input in the same place can give positive forward output.
These examples test an operator assertion for general inputs. They
put no lower bound on actual Möbius energy.

For the unreallocated two-factor expression the lower core bounds
are \(T/s,T/t\) and the coefficient of the affine term is
\((n+1/2)/(st)\) on a term with selected divisors \(s,t\). Replacing
this by \(n/(st)+1/2\) before summing would change the intercept.
The alternative common core cutoff becomes valid with the reallocated
coefficients and their own negative square. The neighboring split-prime
contraction uses different coefficients.

**O.** The open obligation is a sufficiently small positive dual
supremum for the joint signed expression, for every required exponent
on arbitrarily late original windows. Opposite leading terms in the
prime and composite sectors, the persistent ranks, and a small
reconstruction error each leave this supremum undetermined.

## Final synthesis check

**Candidate-D.** For the synthesis at
`3f41fc8938ff2246a36c724e766e1f4dfc276dfd`, set
\(V_Y=(\mathcal C_{Y,g})_+\) with the actual gate
\(g_N=\mathbf1_{M(N)>0}\). If the gated correlation is nonnegative,
\(Q_M-V_Y=D_{Y,g}\). If it is negative, \(V_Y=0\) and
\(0\le Q_M\le D_{Y,g}\). Thus equation (7) gives
\(0\le Q_M-V_Y\le D_Y\). Combining this with the inherited full
comparison gives on every sufficiently late complete window
\[
 \big|\sqrt{Q_R(Y)}-\sqrt{V_Y}\big|
 \le \|R-M\|_{I(Y)}+\sqrt{D_Y}
 \ll 1+\sqrt{\log Y}.
\]
For fixed integer \(q\ge1\), arbitrarily late witnesses at exponent
\(2q\) on either side have square root at most \(Y^{1/(4q)}\).
Adding the displayed error still gives at most \(Y^{1/(2q)}\)
eventually. This establishes the two directions with the original
starting-cutoff quantifier. It gives no bound on the gate or on the
correlation itself.

The arithmetic rank comparison requires the fixed list to contain all
primes through the cutoffs being identified with actual Möbius sums.
The one-prime short support is bounded above by \(pT\). Its multi-prime
identity uses \(n\ge P_XT_X\). The uniform growing-product estimate
above is proved for \(P_XT_X\le X^{1/3}\), as guaranteed on late slabs
by budget (12). The positive-energy estimate remains **O**.

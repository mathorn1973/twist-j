# Astra review of the Huang arithmetic bridge

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.** Same-session
internal paper review of three author arguments. The deductions have
candidate-D status. The complete-window energy bound remains O. The reviewer
read the proofs. This review provides neither blind nor external confirmation.

## Reviewed texts

| Text | Commit |
| --- | --- |
| Public basis | `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed` |
| Prospective scope | `7ea2295831f8444be5a64dcb8da618b911972ab6` |
| PRIME-RULES.md, corrected | `8b3cccecf4f92b5161f343cde0939242161b95d9` |
| GALOIS.md | `5a73fc1b568062f7ba5f5234213a38c820ba79ce` |
| BOUNDARY.md | `00d5e406526309271498c793d1be9a6ea65b7976` |
| Prior FULL-COUPLED-ENERGY.md and WINDOW-BOUND.md | `ceb77e3632ec4617c54d8e1fd504d3b1c99dd106` |

## What the majority gives

**Candidate-D.** With \(m=M_P(N)\ne0\), splicing the parity classes at
the cutoff changes the size of the selected class from half the cube to
half plus \(k=|m|\). Every induced edge joins a retained lower divisor of
Möbius sign \(\operatorname{sgn}m\) to an upper divisor outside the
cutoff. Deleting fewer than \(k\) vertices preserves strict majority.
If \(L^2=\sum_i w_i^2>0\), the absolute adjacency on the remainder has
spectral radius at least \(L\). The row sums of its square are bounded
by the largest product of weighted degrees across a positive-weight
edge. Thus any cover of the original edges with degree product at least
\(L^2\) has size at least \(k\). The cube is bipartite, so König's theorem
gives \(k\) disjoint qualifying edges. The deletion argument uses original
degrees only after proving a product bound in the remainder. It works
also when some coordinate weights vanish.

At \(N=1\) with unit weights, the only edges are \(1\leftrightarrow p_i\).
Their degree products equal \(r\), while each upper endpoint has degree
one. The matching need not supply a square-root degree on each side.
The prime vertices alone have size at most half in both direct encodings.
Huang on the odd bit subcube requires the separate strict-majority
premise for primes in that subcube.

**Candidate-D. Localization to the original cutoff.** Take all primes
through \(N\ge2\) and \(r=\pi(N)\), with unit weights. At any crossing
edge write \(d_+=pd_-\), with \(d_-\le N\). As \(d_-\) is squarefree,
\(2^{\omega(d_-)}\le d_-\), and an upper vertex can return through at most
\(\omega(d_+)=1+\omega(d_-)\le1+\lfloor\log_2 N\rfloor\) directions.
Whenever \(M(N)\ne0\), the matching therefore supplies at least \(|M(N)|\)
distinct lower divisors, each admitting at least
\[
 \left\lceil\frac{\pi(N)}{1+\lfloor\log_2 N\rfloor}\right\rceil
\]
distinct prime multipliers crossing the cutoff. These divisors can be
composite. The count gives neither the weighted signs on the two-factor
region nor cancellation across complete windows.

**Candidate-D. Prime-semiprime specialization.** If all selected primes
lie below or at the cutoff, every triple lies above it and \(t<r-1\)
pairs lie below or at it, then \(m=1-r+t<0\). Every nonisolated upper
vertex is a semiprime of degree two. The qualification “nonisolated”
matters because upper vertices with at least four factors can be
present. The corrected author text supplies it.

The prime conclusion, including distinct upper products, also has an
elementary proof. In the graph of prime pairs with product above \(N\),
a vertex of degree below \(\lceil r/2\rceil\) misses at least
\(\lfloor r/2\rfloor\) neighbors. The sum of the missing degrees is
\(2t\). For \(r\ge4\) there are at most \(t\) such vertices. For \(r=3\)
there are either three qualifying vertices when \(t=0\), or one when
\(t=1\). Hence for \(r\ge3\) at least \(r-1-t\) vertices qualify.
Every subset of qualifying vertices is incident to at least as many
distinct upper products as its cardinality. Each vertex supplies at
least two incidences, and an upper product receives at most two.
Hall's theorem assigns distinct products to all qualifying vertices.
For \(r=2\) the hypothesis forces \(t=0\) and a single pair suffices.
For \(r=1\) the hypothesis is empty. This finite graph argument uses
the given product count and gives no estimate for how often it occurs.

## Size of the positive matching majorant

**Candidate-D.** Fix exactly the primes through \(N\ge2\). Use the
even-inside, odd-outside set \(H_+\) for both signs of \(M(N)\). Write
\(\nu_+(N)\) for the maximum matching size after retaining its edges
whose endpoint degrees in the original \(H_+\) have product at least
\(r=\pi(N)\). The majority argument gives \(M(N)_+\le\nu_+(N)\).

For every prime \(q>3\) in \((N/6,N/3]\), the even vertex \(3q\)
lies in \((N/2,N]\). Every one of its \(r-2\) possible prime additions
crosses the cutoff. The odd vertex \(6q>N\) has the three lower
neighbors \(3q,2q,6\), all at most \(N\). Hence the edge joining
\(3q\) and \(6q\) has degree product \(3(r-2)\ge r\). Distinct \(q\)
give disjoint edges because their lower vertices are distinct and
their upper vertices are distinct, on opposite sides of the cutoff.
Consequently
\[
 \nu_+(N)\ge\pi(N/3)-\pi(N/6)-2.
\]
For \(N\ge18\) the subtraction of two is unnecessary. By the prime
number theorem the resulting lower bound is asymptotic to
\(N/(6\log N)\). On the integers in \([Y^{3/2}/2,Y^{3/2})\), contained
in the full window for late \(Y\), each summand below is then
\(\gg 1/(\log Y)^2\). Thus
\[
 \sum_{N\in I(Y)}\frac{\nu_+(N)^2}{N(N+1)}
       \gg \frac{Y^{3/2}}{(\log Y)^2}.
\]
The majorant's energy eventually exceeds \(Y\) on every such window
and therefore fails even the required exponent one. The proved lower
bound concerns the size of the qualifying matching. Inferring any
lower bound for \(M(N)_+\) or the energy of \(R_{1/36}\) would reverse
the comparison. This rules out proving the target simply by substituting
that unsigned matching size for the positive Möbius sum.

## What the boundary trace sees

**Candidate-D.** The positive spectra of \(G^*G\) and \(GG^*\) pair
with multiplicity for the two parity blocks of the compressed odd
operator. The dimension imbalance \(E-O\) occurs at zero for its square,
hence at \(s\) for the defect \(B\). This proves
\(\operatorname{str}f(B)=f(s)(E-O)\) even when one parity has no zero
mode. At distance two the off-diagonal defect entry can survive when
exactly one intermediate vertex exits, with magnitude \(|c_i c_j|\).
Two outside paths cancel by anticommutation. A general matrix element
can therefore retain information lost in every scalar graded moment.

In the two-copy region the lower cut is imposed on each factor,
\(a,b>T\), and the upper cut on their product, \(ab\le n/k\). An upper
exit from a \(p\)-free base \(a\) carries \(\mu(a)\mu(b)\). A lower exit
from the retained vertex \(pa\) carries the opposite sign. A common
prime in \(a\) and \(b\) still yields two coordinates. Summing the
graded defects divided by \(s\) over the floor multiplicity \(k\)
recovers the ordered two-factor sum exactly. The coordinatewise
diagonal trace already follows by pairing opposite parities. It
gains no sign cancellation from the orientation of the cube edges.

## What the first coordinate reads

**Candidate-D.** Quadratic conjugation and multiplication by \(\tau\)
anticommute with respect to the stated action. Both are self-adjoint
in the trace metric. On the real plane an additional symmetric
generator anticommuting with both normalized generators must vanish.
In the basis for \(Z,X\) it would be off-diagonal symmetric and hence
a multiple of \(X\). This argument concerns that fixed real plane.
Frobenius gives \(\chi_5(p)\) for \(p\ne5\), while negating the
coefficient at each prime toggle supplies Möbius parity. The prime
\(5\) uses the stated bookkeeping convention.

The encoding \((x,y)\mapsto x+\tau y\) is linear for the two parallel
coefficient records. Field multiplication introduces cross terms.
Its trace norm squared is \(2x^2+10y^2\), giving \(12 b_d^2\) on one
encoded coefficient and first-coordinate functional norm \(1/\sqrt2\).
The first coordinate of the complete averaged record is exactly
\(Z_X=U_H^J C_T-L_Xh_T^2\) before taking the positive part.
The twisted companion has its own square. The written construction
makes no comparison of that companion with the original residual.
The identity \(2T_pT_q D=0\) forces \(D=0\) only in the stated
real, linear, stepwise transport to commuting invertible target
operators. Compression and endpoint readouts require separate analysis.

**Candidate-D (inherited).** On the original complete integer windows
\(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\), with weights \(1/[N(N+1)]\), the
pinned input gives \(\|Z-R_{1/36}\|_{I(Y)}\ll_K(\log Y)^{-K}\) for
each fixed \(K>0\). It includes the outer slab fragments and has stronger
content than a comparison only of the square roots of the positive
energies. The new descriptions preserve the forward average and the
negative affine square. The hyperbola split retains its negative overlap
squares.

**O.** Bounding the positive energy of the complete signed sum still
requires an arithmetic estimate. No scientific code, enumeration,
numerical test or formal proof assistant was used for this review.

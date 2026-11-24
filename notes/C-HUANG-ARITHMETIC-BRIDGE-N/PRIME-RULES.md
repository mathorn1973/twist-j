# Prime vertices and product cutoffs in Huang's theorem

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
Paper deductions are candidate-D. The complete-window energy estimate retains O.
The scope and owner are recorded in [SCOPE.md](SCOPE.md).

Hao Huang's Theorem 1.1 gives an induced degree of at least
\(\lceil\sqrt r\rceil\) somewhere in a subset of more than \(2^{r-1}\)
vertices of the binary \(r\)-cube. Larger subsets follow from the stated
\(2^{r-1}+1\) case by restriction. The cube vertices are subsets of
\(\{1,\ldots,r\}\), with an edge for each one-coordinate change.
[Huang, Annals of Mathematics, 2019](https://annals.math.princeton.edu/2019/190-3/p06).

## Direct encodings of primes

**Candidate-D. Divisor cube.** Let \(r\ge1\), let \(p_1,\ldots,p_r\) be
distinct primes, and put \(P=\prod_i p_i\). The cube vertex \(I\)
represents \(d(I)=\prod_{i\in I}p_i\). Edges join \(d\) to \(dp_i\)
when \(p_i\nmid d\). In particular this applies to the primorial of the
first \(r\) primes. Unique factorization makes the encoding bijective
onto the positive divisors of \(P\).

The prime vertices are the singletons. Every pair of distinct singletons
differs in two coordinates, so the induced degree of every prime vertex
is zero. Their count \(r\) is at most \(2^{r-1}\), by \(r=1\) and
\(r+1\le 2r\). Also, \(\mu(d(I))=(-1)^{|I|}\), and toggling any fixed
coordinate exchanges the two parity classes bijectively. Each class
has exactly \(2^{r-1}\) vertices and induces degree zero.

**Candidate-D. Divisor cutoff.** Write \(D_N=\{d\mid P:d\le N\}\) for
real \(N\ge0\). If a prime \(p_i\) is missing from \(D_N\), then every
member of \(D_N\) omits coordinate \(i\) and \(|D_N|\le2^{r-1}\).
Consequently whenever Huang's premise holds, \(1\) has all \(r\) neighbors
in \(D_N\) by this elementary argument.

Since \(P\) is squarefree and greater than \(1\), the map \(d\mapsto P/d\)
has no fixed divisor. Exactly one divisor in each pair lies below
\(\sqrt P\), giving \(|D_{\sqrt P}|=2^{r-1}\). If \(d_+\) is the smallest
divisor above \(\sqrt P\), strict majority begins at \(N=d_+\), including
equality there.

**Candidate-D. Binary integer cube.** For the ordinary \(r\)-bit
encoding of \(0,\ldots,2^r-1\), \(2^{r-1}\) vertices are odd, and the odd
vertex \(1\) is a unit. At most one even prime, \(2\), can compensate
for its absence from the prime set. Thus the prime set has at most \(2^{r-1}\) vertices. The
one-bit cube has no prime vertices.

There is a conditional prime rule on an odd subcube. Let
\(i_1,\ldots,i_s\) be distinct positive bit positions and let \(b\) be
an odd integer \(b\ge1\) with these bits zero. Put
\(n(I)=b+\sum_{j\in I}2^{i_j}\) for \(I\subseteq\{1,\ldots,s\}\)
and \(s\ge1\). If more than half these integers are prime, one of
those primes has at least \(\lceil\sqrt s\rceil\) prime neighbors of
the form \(n(I)+2^{i_j}\) with \(j\notin I\), or \(n(I)-2^{i_j}\)
with \(j\in I\). This is an induced degree rule for that specified
subcube. Its density premise needs arithmetic input for each chosen
subcube.

## Parity selection on the product cutoff

**Candidate-D.** Put \(m=M_P(N)=\sum_{d\in D_N}\mu(d)\). Let \(H_+\)
consist of the even-coordinate vertices in \(D_N\) and the odd-coordinate
vertices outside \(D_N\). Let \(H_-\) be the complementary set. Then
\[
 |H_+|=2^{r-1}+m,\qquad |H_-|=2^{r-1}-m.
\]
Indeed \(|H_+|\) is the size of the whole odd class plus the number of
included even vertices minus the number of included odd vertices.

Suppose \(m\ne0\). Put \(k=|m|\), \(\epsilon=\operatorname{sgn}(m)\),
and \(H=H_\epsilon\). Because the cutoff is downward closed and any
edge changes parity, the edges induced on \(H\) are exactly
\[
 d\longleftrightarrow dp_i,\qquad
 d\mid P/p_i,\qquad d\le N<dp_i,\qquad \mu(d)=\epsilon. \tag{1}
\]
Huang gives one vertex of degree at least \(\lceil\sqrt r\rceil\)
in this selected boundary graph. Explicitly, the qualifying neighbors
of a vertex \(d\in H\) are indexed by
\[
 \mathcal I(d)=
 \begin{cases}
 \{i:p_i\nmid d,\ dp_i>N\},& d\le N,\\
 \{i:p_i\mid d,\ d/p_i\le N\},& d>N .
 \end{cases} \tag{2}
\]
The edges below-to-above come from adjoining distinct selected primes.
The edges above-to-below come from removing distinct selected prime
factors. A witness from the upper side alone can be composite.

The construction also works for any nonempty coordinate set \(U\).
Write \(P_U=\prod_{i\in U}p_i\). For \(a\mid P/P_U\), fix the other
coordinates to the prime factors of \(a\). In this fiber the cutoff
is \(d'\le N/a\), where \(d'\mid P_U\), and its signed contribution to
the full sum is \(\mu(a)M_{P_U}(N/a)\). These contributions sum to \(m\).
If \(m\ne0\), at least one contribution has sign \(\epsilon\). Huang
within that fiber gives an original selected witness with at least
\(\lceil\sqrt{|U|}\rceil\) crossing neighbors in directions \(U\).
For a fixed sign \(\epsilon\), if no fiber of \(H_\epsilon\)
permits such a degree, then \(\epsilon M_P(N)\le0\). Excluding
the degree for both signs forces \(M_P(N)=0\).

There is a midpoint check. When \(r\) is even and \(N=\sqrt P\),
complementary divisors have the same Möbius sign and exactly one of
each pair enters \(D_N\). Their full sum is zero, giving \(m=0\).
For odd \(r\) the complementary signs are opposite, so the same
pairing leaves the partial sum undetermined.

## Weighted witnesses, disjoint edges, and trace

**Candidate-D.** Let \(w_i\ge0\) be real weights, with
\(L^2=\sum_i w_i^2>0\). The weighted degree at \(d\in H\) is
\(b(d)=\sum_{i\in\mathcal I(d)}w_i\). Squaring avoids square roots when
\(w_i\) are integers or ratios. For \(k=|m|>0\), there are at least
\(k\) vertex-disjoint edges of positive weight in (1)
whose endpoint weighted degrees satisfy \(b(d)b(dp_i)\ge L^2\).
For unit weights this guarantees \(k\) disjoint crossing pairs with
degree product at least \(r\).

To see the spectral input, on cube basis vectors \(e_I\) define
\[
 C_i e_I=(-1)^{|\{j\in I:j<i\}|}e_{I\triangle\{i\}},
 \qquad C=\sum_i w_i C_i .
\]
Each \(C_i\) is symmetric and squares to the identity. Toggling a
smaller coordinate reverses the sign of the larger coordinate,
so \(C_iC_j+C_jC_i=0\) for \(i\ne j\). Thus \(C^2=L^2I\).
It has zero diagonal, so each of its two eigenspaces has dimension
\(2^{r-1}\). On any vertex set \(S\) of size \(2^{r-1}+h\) with
\(h>0\), the subspace supported on \(S\) meets each eigenspace in
dimension at least \(h\). Compression to \(S\) therefore retains at
least \(h\) eigenvalues \(L\) and at least \(h\) eigenvalues \(-L\).
This is Huang's signed-cube argument with coordinate weights. The
weighted bound was proved with Clifford algebras by Mathews and also
appears in Theorem 24 of Laplante, Naserasr, and Sunny.
[Huang, 2019](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p06-s.pdf).
[Mathews](https://arxiv.org/abs/1907.12357).
[Laplante, Naserasr, and Sunny, MFCS 2020](https://doi.org/10.4230/LIPIcs.MFCS.2020.62).

For any \(S\subseteq H\) with \(|S|>2^{r-1}\), let \(B\) be the
entrywise absolute value of the compression to \(S\). It is the
weighted graph adjacency. The Rayleigh quotient on the entrywise
absolute value of an eigenvector for \(L\) shows that the largest
eigenvalue of \(B\) is at least \(L\).

For the product bound, the row sum of \(B^2\) at \(u\) equals
\(\sum_v B_{uv}b_S(v)\), where \(b_S\) uses only retained edges.
If \(b_S(u)>0\), this sum is at most
\(\max_{v:B_{uv}>0} b_S(u)b_S(v)\), by dividing each summand by
\(b_S(u)=\sum_v B_{uv}\). A vertex of degree zero has row sum zero.
The largest eigenvalue of \(B^2\) is at least \(L^2\), so there is
an edge in \(S\) with product at least \(L^2\).

Delete any set of \(k-1\) vertices from \(H\). The remainder still
has more than half the cube vertices, and the bound supplies a
qualifying edge. Its original degrees in \(H\) are at least its
remaining degrees. Thus the bipartite graph of qualifying original
edges has minimum vertex-cover size at least \(k\). König's matching
theorem gives at least \(k\) pairwise vertex-disjoint qualifying edges.

In particular at least one endpoint of each qualifying edge has
weighted degree at least \(L\). If one side has weighted degrees
bounded above by \(U>0\), then the other side has at least \(k\)
vertices with degree at least \(L^2/U\). For example, at \(N=1\)
and with unit weights, the selected graph has a star centered at \(1\), with the \(r\) primes
as its leaves. Every vertex on the upper side has degree at most one,
and every star edge attains degree product \(r\).

**Candidate-D. A prime-anchored case.** Suppose every selected prime
is at most \(N\) and every product of three distinct selected primes
exceeds \(N\). Let \(t\) count selected pairs with product at most
\(N\). Then \(m=1-r+t\). If \(t<r-1\), every selected crossing edge
has a prime \(p_i\) below the cutoff and a semiprime \(p_ip_j\) above
it. Each upper vertex has degree exactly two, since both its prime
factors lie below the cutoff. Thus the matching gives at least
\(r-1-t\) distinct primes \(p_i\), each admitting at least
\(\lceil r/2\rceil\) distinct selected prime multipliers \(p_j\)
with \(p_ip_j>N\). The selected pairs can be chosen with distinct
upper products as well. The input is a count of prime products in
a finite, specified range.

## Coordinate counts and the squared trace

**Candidate-D.** Put
\[
 B_i=\#\{d\mid P/p_i:N/p_i<d\le N\}.
\]
Splitting \(M_P(N)\) according to whether \(p_i\) divides the summand
gives the exact identity
\[
 m=\sum_{\substack{d\mid P/p_i\\N/p_i<d\le N}}\mu(d). \tag{3}
\]
Each \(B_i\) therefore gives the elementary bound \(k\le B_i\).
The majority graph has \((B_i+k)/2\) edges of direction \(i\), since
(3) is the difference of the counts for the two signs of the lower
endpoint. The trace of the squared signed compression is
\(\sum_i w_i^2(B_i+k)\). Its \(k\) eigenvalues \(L\) and \(k\)
eigenvalues \(-L\) yield
\[
 k\le \frac{\sum_i w_i^2 B_i}{\sum_i w_i^2}.
\]
This average already follows from (3) in each direction. Its
infimum over weights equals \(\min_iB_i\).

## Scope of the arithmetic conclusion

**Candidate-D.** For \(N\ge2\), taking \(P\) to be the product of all
primes at most \(N\) identifies \(M_P(N)\) with the usual \(M(N)\).
Every squarefree integer up to \(N\) then divides \(P\), and the other
integers contribute zero to \(M(N)\). The dimension in the degree bound
is \(r=\pi(N)\). The ambient cube now includes divisors as large as
\(P\), and its selected boundary is drawn from all cutoff-crossing
multiplications of those divisors. Any bound confined to a restricted
factor range needs a separate localization argument. A full-window
estimate of \(R_{1/36}\) remains O.

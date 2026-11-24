# Huang's majority threshold on arithmetic cutoffs

**NON-CANONICAL. Authority none. Action layer NOT_APPLICABLE.**
New paper deductions are **candidate-D**. The required complete-window
positive-energy estimate remains **O**. This package makes no novelty claim.
Its prospective scope is [SCOPE.md](SCOPE.md), owned by
[issue #2094](https://github.com/mathorn1973/twist-j/issues/2094).

The question is whether Huang's theorem about more than half the vertices
of a cube can yield a rule for primes and help the existing signed-energy
problem. The exact connection uses a parity selection across a product
cutoff. It yields a conditional matching rule for prime multiplications.
The Galois and graded-boundary descriptions preserve the original arithmetic
readout. Neither description yet supplies a new bound on its positive energy.

## 1. An exact rule for prime multiplications

Choose distinct primes \(p_1,\ldots,p_r\), with \(r\ge1\), and put
\(P=\prod_i p_i\). The \(2^r\) vertices of the divisor cube are
\(d\mid P\). An edge adjoins or removes one selected prime. In particular,
the dimension is the number of selected primes, not the integer cutoff.
Let
\[
 D_N=\{d\mid P:d\le N\},\qquad
 m=M_P(N)=\sum_{d\in D_N}\mu(d).
\]
The even and odd classes mean an even or odd number of prime factors.
Select the even vertices inside \(D_N\) and the odd vertices outside it.
This set has exactly \(2^{r-1}+m\) vertices. Its complement has
\(2^{r-1}-m\). If \(m\ne0\), select the larger set \(H\), whose excess
over half is \(k=|m|\). Its induced edges are exactly
\[
 d\longleftrightarrow dp_i,\qquad
 d\mid P/p_i,\quad d\le N<dp_i,\quad
 \mu(d)=\operatorname{sgn}(m).                              \tag{1}
\]

**Candidate-D. Matching rule.** Write \(b(v)\) for the degree of \(v\)
in this selected crossing graph. There are at least \(k\) pairwise
vertex-disjoint edges in (1) such that
\[
 b(d)b(dp_i)\ge r.                                         \tag{2}
\]
For nonnegative coordinate weights \(w_i\), not all zero, the weighted
degrees satisfy the same statement with right side \(\sum_i w_i^2\).

The proof in [PRIME-RULES.md](PRIME-RULES.md) combines Huang's signed-cube
matrix with a degree-product estimate and König's matching theorem.
Deleting fewer than \(k\) vertices leaves a strict majority. The surviving
graph must contain an edge satisfying (2) with its surviving degrees;
its original degrees can only be larger. Thus fewer than \(k\) vertices
cannot cover all qualifying edges. Bipartite matching gives (2).

This rule does not require both ends of an edge to have degree at least
\(\sqrt r\). At \(N=1\), the selected nonisolated graph is a star
centered at \(1\), with the selected primes as leaves. Its edge degree
products are \(r\), with leaf degree one.

**Candidate-D. Localization.** If \(N\ge2\) and the prime list contains
all primes at most \(N\), then \(m=M(N)\) and \(r=\pi(N)\).
At an upper endpoint \(d_+=pd_-\), with \(d_-\le N\),
\[
 b(d_+)\le\omega(d_+)\le1+\lfloor\log_2N\rfloor.
\]
Consequently, when \(M(N)\ne0\), at least \(|M(N)|\) distinct squarefree
integers \(d\le N\), all of sign \(\mu(d)=\operatorname{sgn}M(N)\),
each have at least
\[
 \left\lceil\frac{\pi(N)}{1+\lfloor\log_2N\rfloor}\right\rceil
\]
distinct prime multipliers \(p\le N\), with \(p\nmid d\), for which
\(pd>N\). Their matching partners can be chosen distinct. The integers
\(d\) need not be prime. The proof and its scope are in
[REVIEW.md](REVIEW.md).

### Direct prime sets and a prime-only conditional example

**Candidate-D.** Prime vertices in a divisor cube are singletons, have
no edges between them, and number \(r\le2^{r-1}\). A full binary cube of
integers also has at most half its vertices prime, since its odd vertices
include \(1\) and \(2\) is the only possible even prime. Neither direct
encoding meets the strict-majority premise. On a specified odd binary
subcube, a strict majority of prime vertices would give a conditional
prime-neighbor statement; that premise needs separate arithmetic input.

For a divisor cutoff itself, strict majority already implies that all
selected primes are included, and \(1\) then has all \(r\) neighbors.
The useful signed translation is therefore the parity selection (1).

If all selected primes are at most \(N\), all distinct triple products
exceed \(N\), and exactly \(t<r-1\) pair products are at most \(N\),
then \(m=1-r+t<0\). The selected edges join primes to semiprimes above
the cutoff. Their upper endpoints have degree two. Formula (2) yields
at least \(r-1-t\) distinct selected primes, each having at least
\(\lceil r/2\rceil\) selected prime multipliers taking the product above
\(N\), with distinct chosen upper products. The review gives an
elementary degree-count and Hall proof of this specialization. It is a
conditional rule about a dense graph of given prime pairs; it gives no
new estimate for the distribution of primes.

## 2. The Galois connection and its exact reconstruction cost

**Candidate-D, with registered identities attributed.** In the real
quadratic field \(F=\mathbb Q(\sqrt5)\), let
\(\alpha=j+j^{-1}=\varphi^{-1}\) and \(\tau=2\alpha+1\).
Multiplication and conjugation in the integral basis \((1,\alpha)\) give
\[
 L=\begin{pmatrix}0&1\\1&-1\end{pmatrix},\quad
 K=2L+I=\begin{pmatrix}1&2\\2&-1\end{pmatrix},\quad
 S=\begin{pmatrix}1&-1\\0&-1\end{pmatrix},
 \qquad K^2=5I,\quad S^2=I,\quad SK=-KS.
\]
Both \(K\) and \(S\) are self-adjoint in the positive trace metric,
whose Gram matrix is \(\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\).
This locates an actual anticommuting pair in the named field action.
Two multiplication operators still commute; conjugation is essential.
The identities for \(L,K\) and the Gauss sum already have registered
public predecessors, identified in [GALOIS.md](GALOIS.md).

For \(p\ne5\), Frobenius changes \(\tau\) by the quadratic character
\(\chi_5(p)\). This character differs from Möbius parity. Writing
\(\eta(d)=\chi_5(d/5^{v_5(d)})\) gives a completely multiplicative
\(\pm1\) companion, with \(\eta(5)=1\) only a bookkeeping convention.
An original coefficient \(b_d\) has exact record
\(\mathbf b_d=b_d(1+\eta(d)\tau)\). First-coordinate readout
\(\ell_0=\operatorname{Tr}_{F/\mathbb Q}/2\) returns \(b_d\) with zero
algebraic reconstruction error. The exact costs are
\[
 \|x+\tau y\|_{\rm tr}^2=2x^2+10y^2,\qquad
 \|\ell_0\|=1/\sqrt2,\qquad \|\mathbf b_d\|_{\rm tr}^2=12b_d^2.
\]
The record uses coordinatewise convolution transported by a linear map;
field multiplication would introduce different cross terms. It extends
to the full averaged two-large-factor expression and preserves its
negative affine square before the positive part is taken. The added
character coordinate has not been proved to control the original one.

## 3. What the graded boundary can and cannot estimate

**Candidate-D.** Let \(A\) be the signed weighted cube operator, with
\(A^2=sI\), and let \(P_V\) project onto a selected arithmetic vertex
set. Its compression and exit defect are
\[
 D=P_VAP_V,\qquad B=P_VA(I-P_V)AP_V,\qquad D^2=sI-B.
\]
The defect \(B\) is positive semidefinite. Nevertheless its signed trace
is a difference of two parity contributions. If \(E,O\) count retained
even and odd vertices, the positive spectra of the two parity blocks
of \(D^2\) pair exactly. Hence for every scalar function on the spectrum,
\[
 \operatorname{str}f(B)=f(s)(E-O).                           \tag{3}
\]
In particular every scalar graded power or spectral projection of this
one defect returns the same index. It supplies no separate upper bound
on the parity imbalance. Off-diagonal entries can retain additional
arithmetic boundary information, so (3) does not exclude all operator
methods.

For the actual two-factor sum
\[
 C_T(n)=\sum_{a,b>T}\mu(a)\mu(b)\left\lfloor\frac n{ab}\right\rfloor,
\]
use two distinct copies of the prime coordinates and the finite regions
\(a,b>T,\ ab\le n/k\). Then
\[
 C_T(n)=\frac1s\sum_{1\le k\le n/(T+1)^2}
             \operatorname{str}B_{T,n/k}.
\]
Both the upper product exits and the lower factor exits are present,
with opposite signs as written in [BOUNDARY.md](BOUNDARY.md). Shared
prime factors in \(a,b\) do not identify the two coordinates. Forward
averaging and the subtraction of \(L_Xh_T^2\) preserve this exact readout.

## 4. Remaining quantitative obligation

The inherited target fixes \(R=R_{1/36}\), integer windows
\(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\), and
\[
 Q_R(Y)=\sum_{N\in I(Y)}\frac{(R(N)_+)^2}{N(N+1)}.
\]
**O.** For every integer \(q\ge1\) and every starting cutoff \(Y_0\),
find an integer \(Y\ge\max(11,Y_0)\) such that \(Q_R(Y)^q\le Y\).
No restriction to a selected subwindow is admitted.

For \(Z_X=U_H^JC_{T_X}-L_Xh_{T_X}^2\), with
\(T_X=\lfloor X^{1/4}\rfloor\), the pinned prior note proves
\(\|Z-R\|_{I(Y)}\ll_K(\log Y)^{-K}\) for each fixed \(K>0\).
This full weighted norm comparison is inherited. It is not a new saving
from Huang or the Galois representation. The same bound holds for the
difference of square roots of positive energies. The target therefore
transfers between \(R\) and \(Z\) with its original quantifiers, by
using exponent \(2q\) and absorbing the error.

One exact next test is the positive dual form
\[
 \sqrt{Q_Z(Y)}=
 \sup_{\substack{h_N\ge0\\\sum_{N\in I(Y)}h_N^2/[N(N+1)]\le1}}
       \sum_{N\in I(Y)}\frac{h_NZ(N)}{N(N+1)}.              \tag{4}
\]
Cauchy--Schwarz gives the upper bound, and \(h=Z_+/\|Z_+\|\)
attains it when the norm is nonzero. A useful boundary argument must
control this signed readout on the required windows, including the
affine square, or give a quantitatively equivalent estimate. Scalar
graded moments (3) do not do so. Information about particular boundary
matrix elements or the relation between cutoffs at different arguments
remains a possible subject of further work; no such estimate is claimed
here.

## Evidence and scope

Three Sol author lanes were read by the coordinating Astra and a separate
Astra opponent. [REVIEW.md](REVIEW.md) records the same-session paper
review and elementary comparisons. No scientific executable, numerical
search, enumeration or formal verifier was run for these deductions.
Repository checks only validate the package's repository conformance.
The primary sources and existing scopes are mapped in
[SOURCES.md](SOURCES.md); the bounded handoff is
[PROMO-C-HUANG-ARITHMETIC-BRIDGE-N.md](PROMO-C-HUANG-ARITHMETIC-BRIDGE-N.md).

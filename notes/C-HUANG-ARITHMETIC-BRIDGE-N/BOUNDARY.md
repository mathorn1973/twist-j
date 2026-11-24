# Graded boundary of the arithmetic cutoff

**NON-CANONICAL. Authority none.** The finite algebra and readout
deductions below are **candidate-D**. The full signed energy estimate
is **O**. Action layer NOT_APPLICABLE. This is a paper argument for
C-HUANG-ARITHMETIC-BRIDGE-N under [SCOPE.md](SCOPE.md).

## Cube, grading, and compressed operator

Fix an ordered list of \(m\ge1\) distinct primes. The orthonormal
basis of the real exterior algebra on \(m\) generators is indexed by
their subsets \(S\). Let \(\varepsilon_i\) be exterior multiplication
on the left by generator \(i\), let \(\iota_i=\varepsilon_i^*\), and
put \(\gamma_i=\varepsilon_i+\iota_i\). In the subset basis, \(\gamma_i\)
toggles coordinate \(i\) with sign \((-1)^{|\{j\in S:j<i\}|}\).
In particular it is symmetric, \(\gamma_i^2=I\), and
\(\gamma_i\gamma_j=-\gamma_j\gamma_i\) for \(i\ne j\). This is the
exterior-algebra description of the signed cube used in Huang's
argument. [Huang](https://annals.math.princeton.edu/2019/190-3/p06).
[Karasev](https://arxiv.org/pdf/1907.11175).

Let \(\Gamma e_S=(-1)^{|S|}e_S\) be the grading. For an operator on
a graded space define \(\operatorname{str}F=\operatorname{tr}(\Gamma F)\).
For real coordinate weights \(c_i\), set
\[
 A=\sum_i c_i\gamma_i,\qquad s=\sum_i c_i^2>0.
\]
Then \(A^2=sI\) and \(A\Gamma=-\Gamma A\). For any vertex set
\(V\) use \(P\) for its orthogonal coordinate projection and \(Q=I-P\).
On \(\operatorname{ran}P\), write
\[
 D=PAP,\qquad B=PAQAP=(QAP)^*(QAP),\qquad D^2=sI-B.             \tag{1}
\]
Here \(I\) on the right acts on the retained space. The operator \(D\)
is odd and \(B\) preserves the grading. Write \(E,O\) for the dimensions
of the even and odd retained spaces. The even-to-odd block \(G\) of
\(D\) has adjoint as its odd-to-even block. The even and odd blocks
of \(D^2\) are \(G^*G\) and \(GG^*\), respectively. Their positive
spectra coincide with multiplicities, since \(G\) and \(G^*\) give
inverse isomorphisms up to a scalar on each positive eigenspace.
Consequently
\[
 \dim\ker G-\dim\ker G^*=E-O,\qquad
 \operatorname{str}f(B)=f(s)(E-O)                             \tag{2}
\]
for every scalar function \(f\) on the finite spectrum of \(B\),
extending \(f\) arbitrarily to \(s\) if needed. In the second formula
nonzero singular values of \(G\) contribute equally in both gradings.
This includes every positive power of the defect and every spectral
projection of \(B\). The only possible difference of the graded
spectral multiplicities is at \(s\), corresponding to the zero
eigenvalues of \(D^2\). Thus these scalar graded moments return the
index and supply no separate signed boundary estimate.

For a retained vertex \(S\), the outside one-step neighbors in
different coordinates are orthogonal. This gives
\[
 B_{S,S}=\sum_{i:\,S\mathbin{\triangle}\{i\}\notin V}c_i^2,
 \qquad
 \operatorname{str}B
   =\sum_{S\in V}(-1)^{|S|}
       \sum_{i:\,S\mathbin{\triangle}\{i\}\notin V}c_i^2
   =s(E-O).                                                  \tag{3}
\]
In any one coordinate, full pairs in \(V\) cancel by opposite
parities, while a pair with exactly one retained vertex contributes
the parity sign of that vertex. This proves the last equality
without the edge signs, and proves it separately for each coordinate.
Choosing the \(c_i\) therefore only weights identities already
available from the individual coordinate pairings.

The off-diagonal matrix entries have a further exact description.
For distinct retained \(S,S'\), the entry of \(B\) vanishes unless
they differ in two coordinates. In that case there are exactly two
possible two-step paths between them, and the signed products for
the two paths have opposite signs by anticommutation. If both
intermediate vertices are outside \(V\), the two terms cancel.
If neither is outside \(V\), both terms are absent. If exactly one
intermediate vertex is outside, its term survives and has magnitude
\(|c_ic_j|\) for the two changing coordinates. Formula (2) shows that
even graded trace powers involving these two-step entries reduce to
the same index. This leaves open an estimate using other observables
or independent arithmetic control of the unmatched eigenspaces.

## A single product cutoff

Take the prime list to contain all primes at most \(N\), with
\(N\ge2\). Identify \(S\) with \(d=\prod_{i\in S}p_i\).
The retained vertices \(d\le N\) are precisely the squarefree
positive integers through \(N\), including \(1\). Their grading
sign is \(\mu(d)\), so \(E-O=M(N)\). Equivalently they form
Björner's simplicial complex \(\Delta_N\), in which a subset of size
\(j\) has simplicial degree \(j-1\), including the empty subset in
degree \(-1\). Thus \(\widetilde\chi(\Delta_N)=-M(N)\).
[Björner, Section 1, equations (1.1)–(1.2)](https://arxiv.org/pdf/1101.5704).

For \(c_i=1\), the operator \(\partial=\sum_i\iota_i\) preserves
the retained span by divisor closure and has \(\partial^2=0\).
The operator \(D\) on this span is the sum of that restricted
differential and its adjoint. In this convention the Euler count
uses exterior degree, whereas reduced homology uses simplicial
degree, accounting for the minus sign. Every lower neighbor of a
retained vertex is retained. Formula (3) has only upper exits and
gives for each listed prime \(p\)
\[
 M(N)=\sum_{\substack{d\le N\\p\nmid d\\pd>N}}\mu(d).           \tag{4}
\]
The sum may run over all integers because nonsquarefree \(d\) have
zero weight. For two retained vertices that differ in two
coordinates, divisor closure keeps the lower intermediate vertex
in the mixed add-remove case. The upper intermediate vertex can
be outside if the least common multiple exceeds \(N\). When the
two toggles are both additions or both deletions from one retained
vertex, both intermediates are retained.

For perspective on the majority threshold, the two extreme
eigenspaces of \(A\) have dimension \(2^{m-1}\), by oddness and
\(A^2=sI\). If \(|V|>2^{m-1}\), each meets the retained space in
dimension at least \(|V|-2^{m-1}\); vectors in these intersections
give eigenvalues \(+\sqrt{s}\) and \(-\sqrt{s}\) of \(D\).
Thus \(\operatorname{tr}(D^2)\ge s(2|V|-2^m)\).
The same trace inequality follows by counting ordered weighted
edges: the full squared mass is \(2^m s\), and removal of one
vertex costs at most \(2s\). The trace inequality therefore
supplies no signed improvement over that edge count. The operator
norm gives Huang's stronger degree conclusion for unit weights
when the strict majority holds, because a symmetric signed
adjacency has norm at most its largest absolute row sum.
For the single product cutoff the vertex \(1\) is adjacent to all
\(m\) prime vertices, so a degree lower bound there supplies no
further information on \(M(N)\).

## The full two-factor region and both boundary signs

Use the arithmetic notation of
[FULL-COUPLED-ENERGY.md](https://github.com/mathorn1973/twist-j/blob/ceb77e3632ec4617c54d8e1fd504d3b1c99dd106/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N/FULL-COUPLED-ENERGY.md).
For integers \(T\ge1\), \(n\ge T\) write
\[
 C_T(n)=\sum_{\substack{a,b>T\\ab\le n}}
                \mu(a)\mu(b)\lfloor n/(ab)\rfloor .
\]
On a slab \(X\le N<2X\), use \(B_X=2X+J(H-1)\) and freeze
the prime list through \(B_X-1\) in each of two separate copies.
A vertex is an ordered pair of subsets, with products \(a,b\);
even the same prime in the two positions is two distinct
coordinates. Its sign is \(\mu(a)\mu(b)\). For any integer
\(n<B_X\), and each integer \(1\le k\le n/(T+1)^2\), retain
\[
 V_{T,n/k}=\{(a,b):\ a,b\text{ squarefree},\
                         a,b>T,\ ab\le n/k\}.
\]
In the ambient span, the larger region \(ab\le n/k\) and the
subregion in it with \(a\le T\) or \(b\le T\) are both closed
under deletions. The retained span identifies with the quotient
of their chain spaces for \(\partial=\sum_i\iota_i\).
In particular \(P\partial P\) squares to zero: once a deletion
enters the removed subregion further deletions cannot leave it.
For unit weights \(D\) is this quotient differential plus its
adjoint. Formulae (1)–(3) also apply here directly as compression
to a vertex set.

Write \(B_{T,n/k}\) for the defect of that set, keeping the same
positive \(s\) for every \(n,k\) in the slab. Expanding the floor
as a count of the positive integers \(k\) gives the exact readout
\[
 C_T(n)=\frac1s
   \sum_{1\le k\le n/(T+1)^2}\operatorname{str} B_{T,n/k}.
                                                               \tag{5}
\]
There are no multiplicity corrections for primes shared by \(a,b\)
because a pair has distinct coordinate copies. For one prime \(p\)
in the first copy, fix a squarefree \(b>T\), put \(u=n/(kb)\)
and pair a squarefree \(p\)-free base \(a\) with \(pa\).
The contribution of that pair to the exit trace, divided by
the coordinate weight squared when nonzero, is
\[
 \mu(a)\mu(b)
  \left(\mathbf1_{\{T<a\le u<pa\}}
          -\mathbf1_{\{a\le T<pa\le u\}}\right).               \tag{6}
\]
Both indicators give zero if \(u<T+1\). The first term is the
upper exit from \(a\) to \(pa\), and the second is the lower exit
from \(pa\) to \(a\). In the second term the retained vertex has
sign \(-\mu(a)\mu(b)\). If both endpoints are retained they
contribute zero to the signed pairing, and if neither endpoint is
retained there is no exit. Fixing \(a\) and pairing in \(b\) gives
the second copy. Equation (6) is unchanged if the signed toggle
in this coordinate is replaced by its unsigned swap. This is a
finite test of what the diagonal boundary trace uses: it retains
the product comparison and parity and discards the Clifford
orientation signs. Equation (2) also holds for the direct sum
over \(k\), with the same \(s\). It supplies no new scalar graded
moment on that sum.

## Coupled readout on complete windows

On the slab put \(T=\lfloor X^{1/4}\rfloor\), let \(U_H^J\) denote
the given positive forward average, and keep
\[
 L_X(N)=N+1/2+J(H-1)/2,\qquad
 h_T=\sum_{a\le T}\mu(a)/a,\qquad
 Z_X=U_H^J C_T-L_Xh_T^2 .
\]
Substituting (5) at every averaged argument is an equality. The
prime list contains every prime needed there, since each averaged
argument is in \([X,B_X)\). The affine term is external to the
defect trace and keeps its negative square. The prior convolution
identity additionally gives the exact intercept
\(M(T)^2/2+2M(T)\) and a centered small-rectangle correction when
reconstructing \(U_H^J M\). The intercept costs \(O(1)\) in
weighted slab norm, and the small-rectangle correction costs
\(O(X^{-1/4}(1+\log X)^{3/2})\) in that norm. No such terms are
discarded inside (5). The cited paper's vanishing comparison uses the
classical Mertens envelope for the intercept, the maximal Möbius
short-sum bound for the difference between the forward average and
\(M\), and the direct comparison of \(M\) with \(R_{1/36}\). It gives,
for every fixed \(K>0\),
\[
 \|Z-R_{1/36}\|_{I(Y)}\ll_K(\log Y)^{-K},\qquad
 \left|\sqrt{Q_Z(Y)}-\sqrt{Q_{R_{1/36}}(Y)}\right|
       \ll_K (\log Y)^{-K} .
\]
Here \(\|\cdot\|_{I(Y)}\) uses weights \(1/[N(N+1)]\) and
\(Q_Z(Y)=\sum_{N\in I(Y)}Z_X(N)_+^2/[N(N+1)]\), with \(X\) the dyadic
slab of \(N\). The second inequality follows by the Lipschitz bound for
the positive part. Both bounds are inherited from the previous analytic
inputs. The boundary representation supplies no stronger estimate.
The positive part follows the complete signed sum, including
the affine term. The comparison holds on each sufficiently late
complete window, with the two outer slab fragments included.
Using exponent \(2r\) in the source bound absorbs the norm error
when transferring the target for exponent \(r\) in either direction.

The prior hyperbola splitting also writes \(C_T(n)\) as a signed
linear term in \(M(\lfloor n/j\rfloor)-M(T)\) minus the exact
sum of squares \(\sum_{k\le n/(T+1)^2}(M(\lfloor\sqrt{n/k}\rfloor)
-M(T))^2\). Equation (5) represents their total. It supplies no
separate replacement for those squares and no reason to discard
them when estimating that split expression.

**O.** The remaining estimate requires cancellation of the actual
signed boundary readout after summing over \(k\) and taking the
forward averages jointly with the affine term. Its scalar graded
spectral moments restate the parity count. The majority-degree
statement and the ordinary edge trace yield no bound here for
the positive energy on arbitrarily late complete windows.

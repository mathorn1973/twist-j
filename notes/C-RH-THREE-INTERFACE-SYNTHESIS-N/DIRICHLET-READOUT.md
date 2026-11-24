# Exact augmentation from nontrivial Dirichlet samples

**NON-CANONICAL. Authority none.** The finite isometry, anchored
reconstruction and Euler factor identities are **candidate-D**. The
signed window estimate is **O**. The finite character calculation uses
classical orthogonality on the rapidity span of [MOBIUS.md](MOBIUS.md).

## 1. A common modulus with no augmentation sample

For an integer \(N\ge11\), take \(m=2^k\) to be the least power of two
strictly greater than \(N^2\). Then
\[
 N^2<m\le 2N^2,\qquad
 G=(\mathbf Z/m\mathbf Z)^\times,\qquad
 h=|G|=2^{k-1}\le N^2 .
\]
Each element of \(G\) has a unique representation \((-1)^\epsilon5^j\)
with \(\epsilon\in\{0,1\}\), \(0\le j<2^{k-2}\). In fact
\(v_2(5^{2^j}-1)=j+2\) for \(j\ge0\), by induction using
\(5^{2^j}+1\equiv2\bmod4\). Consequently \(5\) has order \(2^{k-2}\).
Its powers fill the residues \(1\bmod4\), and multiplication by \(-1\)
gives the other odd residues. The full set of characters of \(G\) is
therefore
\[
 \chi_{\eta,b}((-1)^\epsilon5^j)
    =(-1)^{\eta\epsilon}\zeta_{2^{k-2}}^{\,bj},
 \qquad \eta\in\{0,1\},\quad 0\le b<2^{k-2}.
\]
Extend each character to integers by zero on even integers.

Let \(\theta\) be the cubic character modulo seven taking
\(\theta(3)=\zeta_3\). The residue \(3\) has order six modulo seven,
since its square is \(2\) and its cube is \(-1\). The assignment
determines \(\theta\), with \(\theta(11)=\theta(3^4)=\zeta_3\).
For every \(\chi\) modulo \(m\), set \(\psi=\theta\chi\), a Dirichlet
character modulo \(7m\). Every split prime \(p\equiv1,4\bmod5\) is
coprime to \(7m\), since \(2\) and \(7\) are inert. We use the
substitution \(X_p=\psi(p)\) on these variables. The values are exact
roots of unity in \(\mathbf Z[\zeta_{3\cdot2^{k-2}}]\). Since
\(\chi(11)\) has order a power of two,
\(\psi(11)\ne1\). In particular, the sample has
\(E_{11}(\psi)\ne2\) and differs from augmentation as a functional
on the actual span, even for the principal \(\chi\). All \(h\) indices
are retained, and their modulus satisfies \(7m\le14N^2\).

## 2. Injection of the oriented monomials and exact readout

An oriented Laurent monomial in the support of \(\mathcal H_N\)
corresponds to a reduced positive rational \(u/v\). Here \(u\) is the
product of the split primes with exponent \(+1\), and \(v\) is the
product of those with exponent \(-1\). The integers \(u,v\) are
coprime, \(uv\le N\), and both are units modulo \(7m\).

Distinct oriented monomials give distinct residues \(uv^{-1}\) in
\(G\). To see this, equality of residues for \(u/v\) and \(u'/v'\)
gives \(m\mid uv'-u'v\). Both products are positive and at most
\(N^2\), so \(|uv'-u'v|<N^2<m\). They are equal as integers, and
reduced fractions then give the same oriented monomial.

Evaluation of that monomial at a sample is
\(\theta(u)\overline{\theta(v)}\chi(uv^{-1})\).
The fixed \(\theta\) factors have modulus one. By character
orthogonality in \(G\), the average over \(\chi\) of one monomial
times the complex conjugate of another is zero for different
residues and one for equal monomials. Equivalently one can sum the
two geometric sums in the preceding description of the characters.
This proves the exact isometry
\[
 \frac1h\sum_{\chi\bmod m} f(\theta\chi)\overline{g(\theta\chi)}
        =\langle f,g\rangle
 \qquad(f,g\in\mathcal H_N)
\]
in the Laurent monomial coefficient inner product. It also applies
to the full span of the oriented monomials with the same cutoff.

For a sample indexed by \(\psi=\theta\chi\), put
\[
 K_N(\psi)=k_N(\psi)
      =\sum_{\substack{d\le N\\d\in\mathcal D}}
        \prod_{p\mid d}\bigl(\psi(p)+\overline{\psi(p)}\bigr).
\]
The isometry applied to \(k_N\) and to \(B_N,k_N\) gives
\[
 \frac1h\sum_{\chi\bmod m}|K_N(\theta\chi)|^2=D(N),\qquad
 M(N)=\frac1h\sum_{\chi\bmod m}
          B_N(\theta\chi)\,\overline{K_N(\theta\chi)} .
\]
Each summand is real, since both polynomials have real coefficients
in the basis \(E_d\) and every \(E_d(\psi)\) is real.
The same readout reconstructs \(\operatorname{aug}(f)\) for every
\(f\in\mathcal H_N\). With the sample-space norm from the average
\(h^{-1}\sum\), \(K_N\) is the minimum-norm vector giving this
readout. It is the image of \(k_N\) under the isometry, and any other
reconstruction differs by a vector orthogonal to the image. Its
squared norm is exactly \(D(N)\).

The family can be held fixed across a full window
\([Y,Y^{3/2})\). Take \(X=\lceil Y^{3/2}\rceil\), \(X\ge11\), and
choose the modulus by the same rule \(m>X^2\). The proof on
\(\mathcal H_X\) restricts to each \(\mathcal H_N\) with \(N\le X\).
At each \(N\) the readout uses \(K_N\) with the cutoff at \(N\) and
cost \(D(N)\), in the same \(h\) sample coordinates. Every sample
still differs from augmentation on each \(\mathcal H_N\) with
\(N\ge11\). The common modulus is at most \(14X^2\). The sample
family depends on the cutoff \(X\) and the fixed cubic character.

## 3. Ordinary Dirichlet Euler factors for the sample series

Fix one \(\psi=\theta\chi\). The substitution extends to all split
primes, so it defines the full Dirichlet series
\[
 F_\psi(s)=\sum_{n\ge1}\boldsymbol\mu(n)(\psi)n^{-s}.
\]
The prime-power rules and independent prime variables give
multiplicativity of its coefficients. Their absolute values are
bounded by \(d_3(n)\), the number of ordered factorizations into
three positive integers. At split prime powers the bounds are \(3\)
at exponent one and \(4\) at higher exponents, and other primes
give a bound of one. This proves absolute convergence for
\(\Re s>1\).

Put \(t=p^{-s}\). At a split prime set \(e=\psi(p)+\overline{\psi(p)}\).
The local series is
\[
 1+(1-e)t+\frac{(2-e)t^2}{1-t}
   =\frac{1-et+t^2}{1-t}
   =\frac{(1-\psi(p)t)(1-\overline{\psi(p)}t)}{1-t}.
\]
At an inert prime and at \(5\) the local series is \(1-t\).
Let \(\chi_5\) be the quadratic character modulo five. Comparing
with the ordinary Dirichlet \(L\) functions yields, for \(\Re s>1\),
\[
 F_\psi(s)^2=
 U_\psi(s)\,
 \frac{L(s,\chi_5)^2}
 {L(s,\psi)L(s,\overline\psi)
  L(s,\psi\chi_5)L(s,\overline\psi\chi_5)}.
\]
The \(L\) functions of \(\psi,\overline\psi\) use the indicated
characters modulo \(7m\), and the products with \(\chi_5\) use
modulo \(35m\). In particular, those four functions omit primes
\(2\) and \(7\), and the two products with \(\chi_5\) additionally
omit \(5\). The numerator uses the original character modulo five.

The local factors \(U_{\psi,p}(t)\) of \(U_\psi(s)\) are as follows.

| Prime | \(U_{\psi,p}(t)\) |
|---|---|
| Split \(p\) | \(1\) |
| Inert \(p\notin\{2,7\}\) | \(\displaystyle\frac{(1-t^2)^2}{(1-\psi(p)^2t^2)(1-\overline{\psi(p)}^{\,2}t^2)}\) |
| \(p=2,7\) | \((1-t^2)^2\) |
| \(p=5\) | \(\displaystyle\frac{(1-t)^2}{(1-\psi(5)t)(1-\overline{\psi(5)}t)}\) |

At split primes the two \(\chi_5\) twists reproduce the original
characters, so the reciprocal of the four local \(L\) factors gives
the square of the displayed split numerator. At ordinary inert
primes the sign of each twist is reversed, so its two linear
factors combine with the untwisted ones into the two quadratic
factors shown in the table. The local \(L(s,\chi_5)^2\) factor
\((1+t)^{-2}\), multiplied by \((1-t^2)^2\), supplies the inert
local square \((1-t)^2\). At \(2,7\) all four reciprocal factors are
one. At \(5\) exactly the two untwisted reciprocal factors survive.

For every fixed \(\sigma>1/2\), both \(U_\psi\) and its reciprocal
have absolutely summable Dirichlet coefficients with weight
\(n^{-\sigma}\), with bounds uniform in \(m,\chi\). At an ordinary
inert prime, with \(x=p^{-2\sigma}\), the sum of absolute weighted
local coefficients of either factor is bounded by
\((1+x)^2/(1-x)^2=1+O_\sigma(p^{-2\sigma})\), using
\(|\psi(p)|=1\) and the geometric series. The primes \(2,7\)
give convergent coefficient bounds for the polynomial
\((1-t^2)^2\) and its inverse. At \(5\) the same bound with
\(x=5^{-\sigma}\) applies. The product over primes of the absolute
local bounds converges. The two resulting analytic products multiply
to one, so \(U_\psi\) is nonzero for \(\Re s>1/2\).

The four denominator characters have a nontrivial cubic component
modulo seven, and \(\chi_5\) is nonprincipal. Bounded partial sums
of each character give holomorphic \(L\) functions for \(\Re s>0\)
by summation by parts. Thus the displayed ratio gives a meromorphic
continuation of \(F_\psi^2\) to \(\Re s>1/2\). Continuation of
\(F_\psi\) as a single-valued function across possible zeros and poles
requires further information about the ratio.

## 4. A controlled residual with its exact readout cost

**Candidate-D.** Write \(B_N=\sum_d\beta_N(d)E_d\) and
\(\gamma_d(N)=w(d)\beta_N(d)\), as in [MOBIUS.md](MOBIUS.md).
Let \(P^+(d)\) be the largest prime factor, with \(P^+(1)=1\).
Fix
\[
 0<c<\frac1{4e^2},\qquad
 \mathcal R_c(N)=\{d\in\mathcal D:N^{1/4}<d\le N,
                         \ P^+(d)>c(\log N)^2\}.
\]
All logarithms here are natural. One concrete choice is \(c=1/36\),
since \(e<3\). On the common sample family of Section 2 define
\[
 K_{c,N}(\psi)=\sum_{d\in\mathcal R_c(N)}E_d(\psi),\qquad
 R_c(N)=\frac1h\sum_{\chi\bmod m}
           B_N(\theta\chi)\overline{K_{c,N}(\theta\chi)}.
\]
The isometry gives, directly from the unprojected samples,
\[
 R_c(N)=\sum_{d\in\mathcal R_c(N)}\gamma_d(N),\qquad
 \frac1h\sum_{\chi\bmod m}|K_{c,N}(\theta\chi)|^2
       =D_c(N):=\sum_{d\in\mathcal R_c(N)}w(d).
\]
This is an exact reconstruction with zero sampling residual. As in
Section 2, \(D_c(N)\) is the minimum squared readout norm when the
block functional must be reconstructed for every input in
\(\mathcal H_N\). It is not a norm obtained by fitting this one signal.

The short-support estimate of [MOBIUS.md](MOBIUS.md) and the
smooth-support estimate of [LOCAL-AVERAGES.md](LOCAL-AVERAGES.md) imply
\[
 |M(N)-R_c(N)|
 \le\sum_{d\le N^{1/4}}|\gamma_d(N)|
     +\sum_{\substack{d\le N\\P^+(d)\le c(\log N)^2}}
                  |\gamma_d(N)|
 \ll_c\sqrt N.
\]
Every support sum is over \(\mathcal D\). The possible overlap
between the two deleted families only enlarges this upper bound.
The sharp converse in [ROUND2-REVIEW.md](ROUND2-REVIEW.md) shows that
the absolute smooth-support estimate cannot include
\(c=1/(4e^2)\): its ratio to \(\sqrt N\) is unbounded along an
unbounded sequence of integers. This is a statement about absolute
deletion, with no conclusion about cancellation in the signed residual.

The same Rankin product bound, now with the smaller local factors
\(1+2p^{-\sigma}\), bounds the deleted smooth basis mass by
\(O_c(\sqrt N)\). Also \(D(N^{1/4})=O(N^{1/4})\). Hence
\[
 0\le D(N)-D_c(N)\ll_c\sqrt N,\qquad
 D_c(N)=\kappa_5N+O_{c,\epsilon}(N^{1/2+\epsilon}).
\]
The retained squared norm still grows linearly. The reduction supplies
a smaller, explicitly specified arithmetic sum whose discarded part
already has the required square-root bound.

## 5. The remaining whole-window estimate

**O.** For integer \(Y\ge11\), use one family from Section 2 with
\(X=\lceil Y^{3/2}\rceil\). The kernel changes with the specified
cutoff \(N\); the samples and their modulus remain fixed throughout
that window. Put
\[
 Q_{R_c}(Y)=\sum_{\substack{N\in\mathbf Z\\Y\le N<Y^{3/2}}}
              \frac{R_c(N)_+^2}{N(N+1)}.
\]
The scalar \(R_c(N)\) is real. The still required assertion is
\[
 \forall r\in\mathbf Z_{\ge1}\quad
 \forall Y_0\in\mathbf Z_{\ge1}\quad
 \exists Y\in\mathbf Z_{\ge\max(11,Y_0)}:
                  Q_{R_c}(Y)^r\le Y.
\]
Taking the positive part follows the complete signed character average.
This assertion is exactly equivalent to the original
\(W_{3/2}(M)\) of [MOBIUS.md](MOBIUS.md). In fact the pointwise
comparison in Section 4 gives on each sufficiently late complete window
\[
 |\sqrt{Q_M(Y)}-\sqrt{Q_{R_c}(Y)}|\ll_c\sqrt{\log Y}.
\]
For any required exponent \(r\), choose the windows supplied for
\(2r\) and a sufficiently high lower endpoint. Their square-root
energy is at most \(Y^{1/(4r)}\), and adding the displayed logarithmic
term is at most \(Y^{1/(2r)}\) eventually. This works in both
directions. It uses a comparison on each same window, not dilation
convolution or a separate choice of a good window for each summand.

The full readout's ordinary Cauchy allowance is
\(\|B_N\|\sqrt{D(N)}\asymp N\), using the exact coefficient-energy
order in [MIXING.md](MIXING.md). Replacing \(D(N)\) by \(D_c(N)\)
leaves that order unchanged. The sample modulus grows with the window
scale, and the squared Euler factor identity alone gives no estimate
for the weighted, signed character average above. The number \(h\le X^2\)
counts evaluations, not total bit operations or the work of computing
each evaluation. No fast algorithm or zero-free estimate is asserted.

## Appendix. A two-point product cubature

An independent local law on \(E_p\) giving weights \(1/3,2/3\) to
\(-2,1\) has mean zero and second moment two. Its product is an
isometry on \(\mathcal H_N\): the squarefree basis vectors \(E_d\)
are orthogonal with squared norm \(2^{\omega(d)}\) by those two
moments. The law can be realized with \(X_p=-1\) or a primitive
sixth root of unity. It has \(2^r\) samples for \(r=|P_N|\ge1\),
none with all \(E_p=2\), and gives the readout \(k_N\) evaluated
on these samples with squared norm \(D(N)\).

Among two distinct integer nodes in \([-2,2]\) excluding \(2\),
this is the unique positive law with those moments. For nodes \(a,b\),
\(\mathbb E[(E_p-a)(E_p-b)]=0\) forces \(ab=-2\), so the nodes are
\(-2,1\). Their probabilities follow from the mean. For any
isometric sample map the minimal reconstruction norm is
\(\|k_N\|=\sqrt{D(N)}\). The formal product law realizes that norm,
and the Dirichlet construction gives the polynomial sample count and
ordinary Dirichlet series above.

The general orthogonality identity is recorded in
[NIST DLMF §27.8, equation 27.8.6](https://dlmf.nist.gov/27.8.E6).

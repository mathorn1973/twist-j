# The quadratic character of conductor five on primes and squarefree integers

**NON-CANONICAL. No authority. Candidate C-RH-SEMISTABLE-FRAME-N, round 18.**
The paper deductions below have status **candidate-D**. The fixed-character
Möbius estimate has status **O**. The calculation treats the owner's prime
pattern as an arithmetic question in its own right.

## 1. A finite bound for the parity of inert factors

Let \(\chi=\chi_5\) be the primitive real character with values
\((0,1,-1,-1,1)\) on \(0,1,2,3,4\bmod5\). For \(t\ge0\) write
\(C(t)=\sum_{1\le m\le t}\chi(m)\). One complete period sums to zero.
For \(\lfloor t\rfloor\equiv1,3\bmod5\) the respective values are \(1,-1\).
For the other residues \(C(t)=0\). This is also the prefix law in the
registered [ideal Mertens two-sum](../../../canon/CANON.md#ideal-count-rational-descent-and-exact-mertens-two-sum).

**Candidate-D.** For real \(x\ge1\), set \(D=\lfloor\sqrt{x}\rfloor\) and
\(S_{\rm sf}(x)=\sum_{n\le x}\mu^2(n)\chi(n)\). Square-divisor inversion gives

\[
 S_{\rm sf}(x)=\sum_{\substack{d\le D\\5\nmid d}}\mu(d)\,C(x/d^2).
\]

Indeed \(\mu^2(n)=\sum_{d^2\mid n}\mu(d)\) by its factors at each prime.
Writing \(n=d^2m\) leaves \(\chi(d)^2\chi(m)\), and
\(\chi(d)^2=\mathbf 1_{5\nmid d}\). Consequently

\[
 |S_{\rm sf}(x)|\le
 \#\{d\le D:\ \mu^2(d)=1,\ 5\nmid d,\
             \lfloor x/d^2\rfloor\bmod5\in\{1,3\}\}
 \le D-\lfloor D/5\rfloor .
\]

The final bound holds for each cutoff. It uses only the period and integer
divisor identities.

**Candidate-D, with external input.** The ordinary prime number theorem
strengthens this to \(S_{\rm sf}(x)=o(\sqrt{x})\). Use its classical form
\(M(y)=\sum_{d\le y}\mu(d)=o(y)\). Put \(M_5(y)=\sum_{d\le y,\,5\nmid d}\mu(d)\).
Separating multiples of \(5\) gives \(M(y)=M_5(y)-M_5(y/5)\), hence
\(M_5(y)=\sum_{j\ge0}M(y/5^j)=o(y)\). To justify the last limit, divide
by \(y\) and use \(|M(y/5^j)|/y\le5^{-j}\) for dominated convergence.
[Soundararajan, §1, equivalence of PNT and Möbius cancellation](https://math.stanford.edu/~ksound/Math155W10/Notes1.pdf)

Fix \(0<\delta<1\). The part \(d\le\delta\sqrt{x}\) of the inversion sum
has absolute value at most \(\delta\sqrt{x}\). On the remaining range,
\(\lfloor x/d^2\rfloor\) takes finitely many values bounded by \(\delta^{-2}\).
The portion with value \(k\) has
\(\max(\delta\sqrt{x},\sqrt{x/(k+1)})<d\le\sqrt{x/k}\) when nonempty.
There \(C(x/d^2)=C(k)\), and the sum is \(C(k)\) times a difference of
two values of \(M_5\) at fixed positive multiples of \(\sqrt{x}\).
Each difference is \(o_\delta(\sqrt{x})\). Taking the upper limit after
division by \(\sqrt{x}\) gives at most \(\delta\). Let \(\delta\downarrow0\).

**Candidate-D, existing polynomial.** The registered golden-ladder
polynomial \(Q_x(z)\) sums \((-1)^{b_{\rm all}(n)}z^{a(n)}\) over squarefree
\(n\le x\), where \(a(n)\) counts split prime divisors and
\(b_{\rm all}(n)\) counts inert prime divisors together with \(5\).
Separating \(5\nmid n\) from \(n=5m\) gives
\[
 Q_x(1)=S_{\rm sf}(x)-S_{\rm sf}(x/5)=o(\sqrt{x}).
\]
Take \(S_{\rm sf}(y)=0\) for \(y<1\). The finite bound also yields
\(|Q_x(1)|\le\lfloor\sqrt{x}\rfloor+\lfloor\sqrt{x/5}\rfloor\).
This evaluation is at \(z=1\),
corresponding to the formal parameter \(\tau=0\), outside the golden
unit rungs. The registered target \(Q_x(-1)=M(x)\) evaluates the same
polynomial at a different point. [Registered polynomial and target](../../../canon/CANON.md#rapidity-target-reconstruction-t)

**Candidate-D, first derivative.** For this same polynomial and every
\(\theta<1\), the bound \(Q'_x(1)=O(x^\theta)\) is false. To see why, form
the Dirichlet series of the squarefree polynomial coefficients. For real
\(\sigma>1\), its Euler product is
\[
 D(z,\sigma)=(1-5^{-\sigma})
 \prod_{p\ {\rm split}}(1+zp^{-\sigma})
 \prod_{p\ {\rm inert}}(1-p^{-\sigma}).
\]
The product converges locally uniformly in \(z\), and differentiation at
\(z=1\) marks one split prime factor. Its derivative series therefore has
partial sums \(Q'_x(1)\). Euler factors give
\[
 D(1,\sigma)=\frac{L(\sigma,\chi)}{(1+5^{-\sigma})\zeta(2\sigma)},\qquad
 D_z(1,\sigma)=D(1,\sigma)\sum_{p\ {\rm split}}\frac{p^{-\sigma}}{1+p^{-\sigma}}.
\]
The first factor tends to \(5L(1,\chi)/(6\zeta(2))>0\). In the logarithm
of \(\zeta(\sigma)L(\sigma,\chi)\), the terms of prime degree one are twice
the split prime sum \(\sum_{p\ {\rm split}}p^{-\sigma}\) plus \(5^{-\sigma}\).
All higher degrees are bounded in total as \(\sigma\downarrow1\).
Replacing \(p^{-\sigma}\) by \(p^{-\sigma}/(1+p^{-\sigma})\) also costs
\(O(1)\). Hence the sum in \(D_z\) equals
\(\tfrac12\log(1/(\sigma-1))+O(1)\), and \(D_z(1,\sigma)\to+\infty\).
The hypothetical power bound would instead keep
\(\sigma\int_1^\infty Q'_x(1)x^{-\sigma-1}\,dx=D_z(1,\sigma)\)
bounded as \(\sigma\downarrow1\). Thus the square-root cancellation at
this single evaluation fails already for its first split-factor moment.

**Candidate-D, one-sided lower bound.** More precisely, set
\[
 c=\frac{5L(1,\chi)}{12\zeta(2)}
   =\frac{\sqrt5\log\phi}{\pi^2}.
 \qquad
 \limsup_{x\to\infty}\frac{\log x}{x}Q'_x(1)\ \ge\ c.
\]
Indeed \(D_z(1,\sigma)/\log(1/(\sigma-1))\to c\) by the product above
and [the exact \(L(1,\chi)\) value](OPPOSITION.md). Write \(u=\sigma-1\).
The substitution \(v=u\log x\) gives
\(\int_2^\infty x^{-\sigma}\,dx/\log x=\int_{u\log2}^\infty e^{-v}\,dv/v
=\log(1/u)+O(1)\), by splitting the integral at one. If the displayed
upper limit were below \(c\), some \(\eta>0\) would give
\(Q'_x(1)\le(c-\eta)x/\log x\) for all sufficiently large \(x\).
Inserting this in the partial summation integral and dividing by
\(\log(1/u)\) would bound its upper limit by \(c-\eta\), a contradiction.
Using the prime number theorem in progressions modulo five as an additional
input, [the hyperbola argument](OPPOSITION.md) proves the full asymptotic
\(Q'_x(1)\sim c x/\log x\). The evaluation at \(z=-1\) remains open
at the conjectured square-root scale.

## 2. The sign in the fixed-character Möbius estimate

**Candidate-D.** On squarefree \(n\) prime to \(5\), write \(a(n)\) and
\(b(n)\) for the numbers of split and inert prime divisors in
\(\mathbb Q(\sqrt5)\). Then

\[
 \chi(n)=(-1)^{b(n)},\qquad
 \mu(n)\chi(n)=(-1)^{a(n)}.
\]

Both summatory functions vanish termwise outside this support when the first
is weighted by \(\mu^2\). The finite estimate in §1 controls the discrepancy
of the two parities of \(b(n)\). The Möbius target measures the parity of
\(a(n)\) on exactly the same integers. The Dirichlet series make the roles
of a zero of \(L(s,\chi)\) explicit. For \(\Re s>1\),

\[
 \sum_{n\ge1}\frac{\mu^2(n)\chi(n)}{n^s}
 =\prod_{p\ne5}(1+\chi(p)p^{-s})
 =\frac{L(s,\chi)}{(1-5^{-2s})\zeta(2s)},\qquad
 \sum_{n\ge1}\frac{\mu(n)\chi(n)}{n^s}=\frac1{L(s,\chi)} .
\]

**O.** The assertion \(\sum_{n\le x}\mu(n)\chi(n)=O_\varepsilon(x^{1/2+\varepsilon})\)
for every \(\varepsilon>0\) is equivalent to the critical-line hypothesis
for this particular \(L(s,\chi)\). The implication from the bound follows
by partial summation and the functional equation. The converse is the
classical fixed-character estimate. This target concerns conductor five.
The ordinary Riemann hypothesis concerns \(\zeta(s)\).
[Garg and Maji, proof of Theorem 2.2, equation (4.22)](https://arxiv.org/abs/2208.07596)

## 3. One conductor-five sign in several exact forms

**Candidate-D, with registered overlap.** In the complex embedding
\(j=e^{2\pi i/5}\), set \(J=1+j^2,\ \phi=-j^2-j^3\),
\(A_0(X)=(1-X)(1-X^2)\), and \(\tau=jA_0(j)\).
Then \(J\phi=j\) and

\[
 \tau=j+j^{-1}-j^2-j^{-2}=2\phi-1=\sqrt5
 =\frac jJ+\frac Jj,\qquad h=J\overline J=\phi^{-2}.
\]

Here \(\phi^2=\phi+1\). The four automorphisms \(j\mapsto j^u\) send
\(\tau\mapsto\chi(u)\tau\), as one sees by permuting its four monomials.
In particular \(h=(3-\tau)/2\), and conjugation of the real quadratic
field sends \(h\) to \(h^{-1}\).

Let \(g\) be the cyclic shift in dimension five, \(N=\mathbf1\mathbf1^t\),
\(B=I+g^2\), and \(\Gamma=g+g^{-1}-g^2-g^{-2}\).
On the Fourier line indexed by \(u\ne0\bmod5\), \(\Gamma\) has eigenvalue
\(\chi(u)\tau\), with two lines for each sign. The constant line has eigenvalue
zero. Thus \(\Gamma^2=5I-N\). Expanding gives
\(\Gamma=3I-2B^t B+N\), so the final term vanishes on the zero-sum subspace.
Also \(\sum_{r\bmod5}\chi(r)j^{ur}=\chi(u)\tau\) at every \(u\), including
zero. Division by \(\sqrt5\) fixes the vector \(\chi\) under the normalized
discrete Fourier transform. The same Gauss sum gives root number \(+1\)
in the standard functional equation for this even primitive character.
Thus \(\Lambda(s)=(5/\pi)^{s/2}\Gamma_{\rm Euler}(s/2)L(s,\chi)\) satisfies
\(\Lambda(s)=\Lambda(1-s)\).
The same scalar polynomial \(A_0\) supplies a positive Mellin kernel on
the real axis. The separate [opposition note](OPPOSITION.md) gives that argument.

The registered [polar orbit result](../../../canon/CANON.md#j-plenum-polar-orbit-separation-t)
already contains \(\Gamma^2=5I-N\) and the polar decomposition. The
[ideal-count and Möbius results](../../../canon/CANON.md#ideal-count-rational-descent-and-exact-mertens-two-sum)
already identify the finite fixed-line character with \(\chi_5\), the ideal
count with \(1*\chi_5\), the descent \(\mu=b*\chi_5\), and its exact Mertens
two-sum. Here \(b\) in the descent denotes the registered ideal Möbius
coefficient. Its notation is independent of the factor count \(b(n)\) above.
The [golden ladder](../../../canon/CANON.md#rapidity-golden-ladder-t)
already uses \(\mathbb Z[\phi]\), its units and the split-prime character.

## 4. Which torus element gives the Fibonacci rank?

**Candidate-D.** For any prime \(p\) use the full quadratic algebra
\(R_p=\mathbb F_p[T]/(T^2-T-1)\). Write \(\alpha=T,\ \beta=1-T\), so
\(\alpha\beta=-1\). Set \(h=\alpha^{-2}\) and \(t=\beta/\alpha=-h\).
For \(F_0=0,\ F_1=1,\ F_{n+2}=F_{n+1}+F_n\), the recurrence gives

\[
 (\alpha-\beta)F_n=\alpha^n-\beta^n=\alpha^n(1-t^n).
\]

The element \(\alpha-\beta=2T-1\) is nonzero at every prime, including
\(2\) and \(5\), by the basis \(1,T\). Multiplication by it on the scalar
copy of \(\mathbb F_p\) is injective. Therefore \(p\mid F_n\) exactly when
\(t^n=1\) in \(R_p\). The least positive such \(n\) is
\(z(p)=\operatorname{ord}(t)=\operatorname{ord}(-h)\).

For \(p\ne5\), the two roots are distinct. If \(\chi(p)=1\), the algebra
splits as \(\mathbb F_p\times\mathbb F_p\). Frobenius fixes both components,
and the norm-one group consists of \((u,u^{-1})\). If \(\chi(p)=-1\),
the algebra is \(\mathbb F_{p^2}\) and Frobenius exchanges \(\alpha,\beta\).
For odd primes this dichotomy follows from discriminant five and quadratic
reciprocity. At \(2\), the polynomial \(T^2+T+1\) is irreducible.
Consequently \(h^p=h^{\chi(p)}\), and the norm-one group containing \(t\)
is cyclic of size \(N_p=p-\chi(p)\). In the field case it is the kernel
of \(u\mapsto u^{p+1}\). Thus \(z(p)\mid N_p\), which gives
\(p\mid F_{p-\chi(p)}\). At \(2\), \(\alpha\) has order three and
\(t=\alpha^{-2}=\alpha\) has order three as well.

**Candidate-D.** For odd \(p\ne5\), the exact half-power identities are

\[
 h^{N_p/2}=\chi(p),\qquad t^{N_p/2}
 =(-1)^{N_p/2}\chi(p)=(-1)^{(p-1)/2}.
\]

In the split case \(\alpha^{p-1}=1\). In the inert case
\(\alpha^{p+1}=\alpha\beta=-1\). This proves the first identity, and
\(t=-h\) gives the second. Hence \(z(p)\mid N_p/2\) exactly when
\(p\equiv1\bmod4\). For \(p\equiv3\bmod4\), \(z(p)\) contains the full
power of two dividing \(N_p\). The modulus-four sign is a separate character.
The Chinese remainder theorem permits either sign for either value of
\(\chi_5\), and Dirichlet's theorem realizes all four pairs on primes.
The group order and this square-class test still leave the exact order
as an element-order question.

**Candidate-D.** At \(5\) write \(\varepsilon=2T-1\). Then
\(R_5=\mathbb F_5[\varepsilon]/(\varepsilon^2)\), and
\(t=(1-\varepsilon)/(1+\varepsilon)=1-2\varepsilon\).
Since \(t^n=1-2n\varepsilon\), its order is five and \(z(5)=5\).
The residue-field image is \(t=1\), so passing to that field loses the rank.
Conjugation sends \(\varepsilon\) to \(-\varepsilon\), so the norm-one
units are \(\pm(1+t\varepsilon)\), \(t\in\mathbb F_5\), a group of order ten.
This is the ramified algebra, outside the two unramified torus cases.
The Fibonacci entry point and the order of a point on the quadratic torus
are classical. Cubre and Rouse use the point \(\phi^2=h^{-1}\) and explicitly
account for its sign in comparing orders. [Cubre and Rouse, §3, Lemmas 8–10](https://arxiv.org/abs/1212.6221)

The historical Möbius work in issues 978, 1033 and 1193 retains its existing
custody. The statements here are paper deductions within the R18 handoff.

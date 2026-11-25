# Adversarial review of the large-prime tail

C-RH-ARITHMETIC-KERNEL-N, issue #2087. NON-CANONICAL. Candidate-D paper review. Reviewed [LARGE-PRIME-TAIL.md](LARGE-PRIME-TAIL.md) against the pinned candidate's FOUNDATION.md, WINDOW-TAIL.md and ROUGH-TAIL.md. No scientific execution or change to the reviewed source.

**Verdict.** The exact identities, fixed-order expansion, reciprocal-unit coefficient, complement cancellation and energy obstruction follow at the stated scope. No mathematical gap found. The parameter \(2/3\le a<1\) and number of expansion terms are fixed before the limit.

## 1. Exact slice and cube-root rough membership

For each \(X>1\), a support element \(d\le X\) has at most one prime \(p>X^a\), since \(2a>1\). In \(d=pe\) the cofactor satisfies \(e\le X/p<X^{1/3}\le X^a<p\), so it cannot repeat \(p\). Conversely any supported \(e\le X/p\) pairs with this \(p\) to make a supported \(d>X^{2/3}\) with the required greatest prime. Multiplicativity gives \(w(pe)=-2w(e)\). If \(e>1\), its least prime is at most \(e<X^{1/3}\), so the term lies in \(H\), the complement of the cube-root rough part. The case \(e=1\) lies in \(B\). This remains valid at \(a=2/3\) and when an endpoint \(X^a\) is prime, because the lower inequality is strict. Equation (1) is exact for the three quantities it defines. It does not identify \(C_a^B\) with all of \(B\) or \(C_a^H\) with all of \(H\).

## 2. Endpoint replacement accounts for every jump

The finite sum \(F(X/p)=\sum_{m\le X/p}c(m)\) gives equation (3) with the exact prime interval \((D,X/m]\), including a zero contribution when its endpoints coincide. When replacing each endpoint by the fixed-modulus prime approximation, \(D\le X/m\) and \(\log D=a\log X\). Thus each prime-count difference has error \(O_{A,a}(X/(m(\log X)^A))\). Summing after multiplication by \(|c(m)|\) gives the stated \(O_{A,a}(X(\log X)^{2-A})\) by (2). No additional total variation estimate for \(F(X/p)\) is required.

Optional sharpening. On split prime powers the local convolution coefficient is \(1-2=-1\), on inert ones it is \((-1)^k\), and on powers of 5 it is zero. Therefore \(|(w*\chi)(m)|\le1\), and \(\sum_{m\le Z}|c(m)|/m\le1+\log Z\) holds in both cases. This can save one logarithm in the replacement error but is unnecessary for the stated expansion.

The factor \(1/2\) from the prime density cancels the outer \(2\) after multiplying by \(-2\). Finite interchange gives \(-\int_D^X F(X/t)\,dt/\log t\). The substitution \(u=X/t\) reverses the limits and has absolute Jacobian \(X/u^2\), giving the negative sign in (4).

## 3. Moment and complement signs

Write \(L=\log X\) and \(W=(1-a)L\). The finite geometric remainder is
\[
 \frac{(\log u)^m}{L^m(L-\log u)}
       \le \frac{(\log u)^m}{aL^{m+1}}
       \qquad(1\le u\le X^{1-a}).
\]
The absolute logarithmic moments are finite by the unconditional bounds in (2). With \(t=\log u\), the tail above \(W\) is bounded by a constant times \(\int_W^\infty t^j e^{-c_0\sqrt t}\,dt\). For fixed \(a<1\) and \(j\) this is smaller than all inverse powers of \(L\), by the substitution \(r=\sqrt t\). Choose \(A\ge m+3\) in the prime remainder. Both Mellin germs agree with the defining integrals for \(\Re s>1\). Differentiating there and taking \(s\downarrow1\) by dominated convergence gives moment \(j\) equal to \((-1)^jG_F^{(j)}(1)\). This argument does not need integral convergence to the left of one.

The exact unit orientation is \(D_T(s)=1/(\zeta(s)U(s))\). Its factors at \(s=1\) are positive and the product converges to a nonzero value. Since \(\zeta\) has residue one,
\[
 G_T(1)=0,\qquad G_T'(1)=1/U(1)>0.
\]
The sign of the prime transform in moment \(j\) is \(-(-1)^j\). Thus the \(j=1\) term for \(C_a\) is positive. For \(S_\chi\), \(G_{S_\chi}(1)=L(1,\chi)\) and \(G_{S_\chi}'(1)=L'(1,\chi)-L(1,\chi)\). Subtraction gives exactly the three displays in (6). The global \(R(X)\) bound at all inverse-logarithmic orders follows from the unconditional \(T\) estimate and the \(O(X^{2/3})\) short part. By taking that bound past the chosen expansion order, \(R-C_a\) indeed has the termwise opposite finite expansion. This is a fixed-order result with constants allowed to depend on \(a\) and the order.

## 4. Energy, evidence, and scope

Since \(C_a(n)\sim\kappa n/(\log n)^2\) for \(\kappa=1/U(1)>0\), the positive part equals \(C_a(n)\) eventually. Restricting to \(Y^2/2\le n<Y^2\) gives the stated lower bound \(Q_{C_a}(Y)\gg_a Y^2/(\log Y)^4\). The argument even gives the leading coefficient \(\kappa^2/16\) in front of \(Y^2/(\log Y)^4\). For fixed \(0<\delta<1\), \(\log n/(2\log Y)\to1\) uniformly on \(\delta Y^2\le n<Y^2\), while the contribution of \(Y\le n<\delta Y^2\) is \(O(\delta Y^2/(\log Y)^4)\). Let \(\delta\downarrow0\) after taking the limit in \(Y\). The lower bound in the source suffices. It concerns the slice alone. Its complement carries the opposite expansion and must remain in the signed bound at the same \(n\).

Yamada's [pinned HTML §1](https://arxiv.org/html/1306.5322v4#S1) was accessible and supplies a super-logarithmic fixed-modulus prime error. Put \(q=5\), discard prime powers, then partially sum for the two prime-counting classes. This yields the all-fixed-order estimate used in (3). The introductory classical theorem is sufficient independently of the explicit table restriction in Theorem 1.2. The borrowed Mertens bound is [Lee–Leong, Theorem 1.1](https://arxiv.org/html/2208.06141v4#Thmtheorem1.1). No explicit constants, zero tables or scientific runs are used in this review.

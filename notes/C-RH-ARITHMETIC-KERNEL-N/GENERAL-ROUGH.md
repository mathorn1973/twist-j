# Every fixed roughness cutoff leaves a Dickman main term

C-RH-ARITHMETIC-KERNEL-N, paper-only result-exposed extension. NON-CANONICAL, no authority. Candidate-D. This extends the cube-root calculation within the authorized arithmetic continuation. The earlier preregistration, cutoff, and checker remain as frozen. This extension uses no numerical computation and makes no historical priority claim.

Let \(\mathcal P\) be the split primes (classes \(1,4\) modulo five), \(\chi=\chi_5\), and \(S_\chi(v)=\sum_{j\le v}\chi(j)\). Let \(w(d)=(-2)^{\omega(d)}\) on squarefree \(d\) supported on \(\mathcal P\), zero otherwise. Fix a real \(u>1\), and put \(z=X^{1/u}\), \(D=X^{2/3}\). Define
\[
 B_u(X)=\sum_{\substack{D<d\le X\\P^-(d)>z}}
     w(d)S_\chi(X/d),\qquad
 H_u(X)=R(X)-B_u(X),\qquad R(X)=\sum_{D<d\le X}w(d)S_\chi(X/d).
\]
The cutoff is strict, with \(P^-(1)=+\infty\).

**Theorem.** For each fixed \(u>1\),
\[
 B_u(X)\sim -\rho(u-1)L(1,\chi)\frac{X}{\log X},\qquad
 H_u(X)\sim +\rho(u-1)L(1,\chi)\frac{X}{\log X},
\]
where \(\rho\) is the Dickman function defined by \(\rho(v)=1\) on \([0,1]\) and \(v\rho'(v)=-\rho(v-1)\) for \(v>1\). The constant \(\rho(u-1)L(1,\chi)\) is strictly positive. In particular, the obstruction to estimating the two positive parts separately holds at every fixed power cutoff. For \(u=3\) the constant is \((1-\log 2)L(1,\chi)\).

## 1. Fixed quotient prime census

Write \(a=1/u\), \(L=\log X\), and \(\delta=1/2\) for the prime density of \(\mathcal P\). In what follows \(j\ge1\) is fixed and \(y=X/j\). The classical prime number theorem modulo five gives \(\pi_{\mathcal P}(v)\sim\delta v/\log v\). We use its uniform relative error on \(v\ge z=X^a\), valid since \(z\to\infty\), and its corresponding uniform big-O bound. Partial summation gives, for fixed \(0<b<c\le1\),
\[
 \sum_{X^b<p\le X^c,\ p\in\mathcal P}\frac1p
  \longrightarrow\delta\log(c/b).
 \tag{1}
\]
In particular, \(\sum_{z<p\le X,p\in\mathcal P}1/p=O_u(1)\).

There are finitely many possible numbers of prime factors: a product of \(k\) primes all strictly greater than \(z\) exceeds \(X\) whenever \(k\ge u\). For a positive integer \(k\), let \(C_k(y;z)\) count the ordered \(k\)-tuples of distinct primes in \(\mathcal P\), each greater than \(z\), with product at most \(y\). An upper bound for the count, even allowing repeats, holds for every \(y\le X\) and \(1\le k<u\):
\[
 C_k(y;z)\ll_u \frac{y}{\log X}.
 \tag{2}
\]
To see this, for \(k\ge2\) fix the first \(k-1\) primes with product \(P\le y/z\). Their final prime has argument \(y/P\ge z\), so its count is \(O_u(y/(P\log X))\). Sum the resulting products of reciprocal primes using (1). The same bound for \(k=1\) is immediate when \(y\ge z\), and the count is zero for \(y<z\).

For \(k=1\), \(C_1(y;z)=\pi_{\mathcal P}(y)-\pi_{\mathcal P}(z)\) for all large \(X\), and \(\pi_{\mathcal P}(z)=o(y/L)\). For \(2\le k<u\) allow repeats at first and fix the first \(k-1\) primes with \(P\le y/z\). The count is the sum of \(\pi_{\mathcal P}(y/P)-\pi_{\mathcal P}(z)\). By (2) for \(k-1\) the subtracted sum is \(O_u(y/L^2)\). The count of tuples with any repeated prime is \(o(y/L)\): fix a repeated pair of positions with prime \(p>z\). The remaining \(k-2\) factors have product at most \(y/p^2\), and even as arbitrary positive integers their number is
\[
 O_k\bigl((y/p^2)(1+\log X)^{k-2}\bigr)
 \quad\text{when }p^2\le y.
\]
For positive tuple length this follows by fixing all but the last factor and bounding harmonic sums by \(1+\log X\). For length zero the bound holds because \(y/p^2\ge1\). Sum over the finitely many pairs of positions and use \(\sum_{m>z}m^{-2}\ll z^{-1}\). The resulting bound \(O_k(y(1+\log X)^{k-2}/z)\) is \(o(y/L)\) for fixed \(u\).

It follows that the leading term comes from replacing the last prime count by \(\delta y/(P\log(y/P))\). For \(k\ge2\), put \(\alpha_i=\log p_i/L\) for the first \(k-1\) primes. Their reciprocal-prime measure on the compact interval \([a,1]\) tends by (1) to \(\delta\,d\alpha_i/\alpha_i\). Products of these measures converge on rectangles by factorization. Approximation by finite rectangles extends the convergence to the integrand with the cutoff \(\sum_i\alpha_i\le1-a-\log j/L\): the limiting boundary hyperplane has measure zero, and the moving endpoint stays inside any fixed-width neighborhood of that hyperplane for large \(X\). The factor \(1/(1-\sum_i\alpha_i-\log j/L)\) is bounded by \(1/a\) on the allowed region and tends uniformly to its limiting expression away from that hyperplane. Thus
\[
 \lim_{X\to\infty}\frac{L}{X}C_k(X/j;z)=\frac{\delta^k}{j}I_k(u),
 \qquad
 I_k(u)=\int_{\substack{\alpha_i\ge1/u\ (1\le i<k)\\\sum_{i<k}\alpha_i\le1-1/u}}
     \frac{d\alpha_1\cdots d\alpha_{k-1}}
      {\alpha_1\cdots\alpha_{k-1}(1-\sum_{i<k}\alpha_i)}.
 \tag{3}
\]
Set \(I_1(u)=1\). The above arguments prove (3) for \(1\le k<u\). For \(k\ge u\) both sides are zero, with the integral at \(k=u\) supported on a set of measure zero. The set boundary where a prime equals the strict cutoff changes neither the measure limit nor the exact exclusion of a product with \(k=u\).

Each unordered squarefree product has \(k!\) ordered distinct representations. Its weight is \((-2)^k\). Thus the leading weighted coefficient in (3) is \((-1)^k I_k(u)/k!\), because \((-2)^k\delta^k=(-1)^k\). The extra lower cutoff \(d>D\) changes the fixed-quotient weighted sum by \(O(D)\), from the preceding estimate \(\sum_{d\le D}|w(d)|\le D\). This argument handles every fixed \(u>1\) without comparing \(z\) and \(D\).

## 2. Summation in the quotient

Fix an integer \(J\ge1\) and replace \(S_\chi(X/d)\) by \(\sum_{j\le\min(J,X/d)}\chi(j)\). The error before multiplying by \(w(d)\) is at most two and occurs only for \(d\le X/(J+1)\), since \(|S_\chi|\le1\). The count weighted by \(|w(d)|\) in this range is \(O_u(X/(J\log X))\) by (2), summing only the finitely many \(k<u\). The excluded product \(d=1\) contributes nothing here. The estimate is uniform in \(J\) and does not bound the character tail by an unsigned harmonic sum.

Now (3) applies to each of the finitely many \(j\le J\). Taking \(X\to\infty\) first and then \(J\to\infty\), we get
\[
 \lim_{X\to\infty}\frac{\log X}{X}B_u(X)
  = L(1,\chi) K(u),\qquad
 K(u)=\sum_{k\ge1}\frac{(-1)^k}{k!}I_k(u).
 \tag{4}
\]
The convergence of the character Dirichlet series at one follows from bounded partial sums. Its value is positive by pairing the terms in each five-term block, as in the preceding note.

## 3. Identification of the coefficient

Let \(h(t)=\mathbf1_{t\ge1}/t\), extended by zero below one, and define the locally finite sum
\[
 g(v)=\sum_{k\ge1}\frac{(-1)^k}{k!}h^{*k}(v),
 \qquad F(v)=1+\int_0^v g(t)\,dt\quad(v\ge0).
\]
Each convolution power is supported on \([k,\infty)\). In (3), the substitution \(t_i=u\alpha_i\) gives \(I_k(u)=u h^{*k}(u)\): the Jacobian contributes \(u^{-(k-1)}\) and the \(k\) denominator factors contribute \(u^k\). The identity also holds for \(k=1\) since \(u>1\). Thus \(K(u)=u g(u)\).

On the convolution simplex, multiply the integrand by \(v=t_1+\cdots+t_k\). Symmetry makes the \(k\) resulting terms equal, and \(t h(t)=\mathbf1_{t\ge1}\). Hence
\[
 v h^{*k}(v)=k\,[\mathbf1_{[1,\infty)}*h^{*(k-1)}](v).
\]
For \(k=1\) interpret convolution with \(h^{*0}\) as the identity. Multiply by \((-1)^k/k!\) and sum. For every \(v>1\), this gives \(v g(v)=-F(v-1)\). The right side is continuous there, and \(F\) is locally absolutely continuous, so \(vF'(v)=-F(v-1)\). The support of \(h\) gives \(F=1\) on \([0,1]\). The differential equation determines a continuous solution one unit interval at a time. Therefore \(F=\rho\) and \(K(u)=-\rho(u-1)\).

The differential equation also gives \(v\rho(v)=\int_{v-1}^v\rho(t)\,dt\) for \(v\ge1\), since both sides agree at one and have the same derivative. A first zero at any finite \(v>1\) would make its left side zero and its right side strictly positive. Since \(\rho=1\) on \([0,1]\), no such zero exists. Finally \(\rho(2)=1-\log 2\) by integration on \([1,2]\).

## 4. Consequence for the signed target

The prior arithmetic argument gives \(R(X)=o(X/\log X)\) from the unconditional Mertens bound, absolute summability of the Dirichlet unit, and the elementary low-support bound \(O(X^{2/3})\). Thus the complementary asymptotic follows by \(H_u=R-B_u\). For every fixed \(u>1\) the positive-part energy of \(H_u\) on \([Y,Y^2]\) is \(\gg_u Y^2/(\log Y)^2\) on every sufficiently late window, by retaining the integers \([Y^2/2,Y^2)\). The positive part of \(B_u\) vanishes eventually. This rules out removing the opposing main term by a choice of a fixed power cutoff. The estimate is pointwise in the fixed parameter \(u\). It gives neither a uniform estimate for \(u=u(X)\to\infty\) nor cancellation at square-root strength in their signed sum.

## Primary sources

- [Bennett, Martin, O’Bryant and Rechnitzer, Explicit bounds for primes in arithmetic progressions](https://arxiv.org/abs/1802.00085), the fixed-modulus prime number theorem used in (1)–(3).
- [Hildebrand and Tenenbaum, On a class of differential–difference equations arising in number theory](https://tenenb.perso.math.cnrs.fr/PPP/Diff-diff_eqns.pdf), §1 for the classical Dickman normalization and unique continuous solution. The coefficient identification here is proved directly.
- [de Bruijn, On the number of positive integers at most x and free of prime factors greater than y](https://research.tue.nl/en/publications/on-the-number-of-positive-integers-leq-x-and-free-of-prime-factor/), original asymptotic study of the function in the complementary small-prime setting.
- [Previous rough-tail proof](ROUGH-TAIL.md), exact support weights, character signs, and unconditional bound giving the complementary asymptotic.

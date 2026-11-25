# Further conductor deletion and a joint estimate at low frequencies

**NON-CANONICAL. No authority. Candidate-D paper deductions. The full
square-root-scale estimate remains O.** Same owner, issue
[#2087](https://github.com/mathorn1973/twist-j/issues/2087), draft
[#2089](https://github.com/mathorn1973/twist-j/pull/2089).
Action layer NOT_APPLICABLE.

This continuation gives a new deletion at the required error scale, an
improved unconditional estimate for a specified slow observation of the
actual joint core and prime correction, and two quantitative obstructions
to stronger claims from absolute values or generic smaller-argument norms.
The paper does not assume the target estimate or a zeta-zero statement.

## 1. The inherited joint quantity

Let \(X\) be a sufficiently late dyadic integer, \(D=4X\), and \(z=D^{1/3}\).
The quadratic character \(\chi_5\) has values \(0,1,-1,-1,1\) on residues
\(0,1,2,3,4\). Write \(H(q)=\sum_{m\le q}\chi_5(m)\) and let \(s(d)\)
equal \((-2)^{\omega(d)}\) on squarefree products of split primes
\(p\equiv1,4\pmod5\), with \(s(1)=1\), and zero elsewhere. The actual sequence is
\[
 T(n)=\sum_{d\le n}s(d)H(\lfloor n/d\rfloor),\qquad t(n)=T(n)-T(n-1).
\]
Its coefficient series is \(1/(\zeta(s)U(s))\); the fixed unit \(U\) is
defined in [FOUNDATION](../FOUNDATION.md). The inherited positive rational
taper \(w\) is one on \([X,2X)\), supported in \([7X/8,17X/8]\), and
\(\|F\|_w^2=\sum_n w(n)|F(n)|^2\).

Keep the exact round-six core, with all original numerator, height,
smoothing and cofactor data. Its conductors satisfy
\[
 D^{2/3}<r\le D,\qquad (\log X)^2<P^+(r)\le D^{1/3}.
\]
Each is squarefree and has at least three distinct split primes. The
same-argument replacement is
\[
 C_z(n)=-2\sum_{z<p\le n}T(\lfloor n/p\rfloor)
        -4\sum_{\substack{z<p\le q\\pq\le n}}
                      T(\lfloor n/(pq)\rfloor).
\]
All primes here are split. The repeated case \(p=q\) stays in the sum.
The input arguments are at most \(O(X^{2/3})\).

The [round-six comparison](../round6/CUBE-ROOT-TRANSFER.md) proves
\(\|T-(G_{\rm core}+C_z)\|_w^2\ll_\varepsilon X^{2+\varepsilon}\).
The signed criterion retains the mixed term:
\[
 Q_{\rm core}=P_{\rm core}
       +2\operatorname{Re}\langle G_{\rm core},C_z\rangle_w
       +\|C_z\|_w^2.
\]
Here \(P_{\rm core}\) is the original ordered unequal-conductor
determinant-strip sum after the inherited large-gcd removal.

## 2. A new family can be removed at the target scale

**Candidate-D.** On an inherited shell \(R<r\le\min(2R,D)\), let
\[
 u_y(r)=\prod_{\substack{p\mid r\\p\le y}}p,\qquad H_R=R^2/X.
\]
For every fixed \(B\ge1\), set \(y=(\log X)^B\). If \(V\) is any subset
of the actual core modes with \(u_y(r)\ge U\), \(1\le U\le R\), then
\[
 \boxed{\quad
 \|V\|_w^2\ll_{B,\varepsilon}
       X^\varepsilon\frac{R^3}
       {[U\min(U,H_R)]^{1/B}} .
 \quad}                                                        \tag{1}
\]
This includes all retained numerators, with their original coefficients.
The [full proof](SMOOTH-DIVISOR-AND-TRANSFER.md) counts eligible
conductors globally and inside one close-frequency row, then sums the
norms over numerators. It needs no assumed cancellation in \(s(r)\).

For one completely fixed successor, delete the union of these two
conductor classes:

| Shell range | Class deleted |
|---|---|
| Every inherited core shell | \(u_{\log X}(r)\ge R^{3/2}/X\) |
| Inherited core shells with \(R\le X\) | \(u_{(\log X)^2}(r)\ge R^3/X^2\) |

The general theorem also gives other fixed \(B\)-families. Only the two
classes displayed above define the successor in this report. Assign
overlapping conductors to the first class; the subset form of (1) controls
the remainder of the second class. Summing over the shells gives
\[
 \|G_{\rm core}-G_7\|_w^2\ll_\varepsilon X^{2+\varepsilon}.       \tag{2}
\]

These are families of actual nonzero coefficients. In a shell
\(R\asymp X^{3/4}\), the first class contains at least
\(X^{5/8-o(1)}\) distinct conductors with nonzero numerator-one modes.
In a shell \(R\asymp X^{7/10}\), the second class contains at least
\(X^{3/5-o(1)}\) further conductors with \(u_{\log X}(r)=1\);
the first class keeps all of these. The constructions use a product
of small split primes and two larger split primes. The odd-denominator
parity of the exact cofactor sum proves its nonvanishing. These counts
are not lower bounds for a signed energy.

Let \(P_7\) use exactly the same pair conditions as \(P_{\rm core}\),
restricted to the conductors of \(G_7\). All cross products in the
successor are retained:
\[
 Q_7=P_7+2\operatorname{Re}\langle G_7,C_z\rangle_w+\|C_z\|_w^2 .
                                                                  \tag{3}
\]
Equations (1) and (2), with the inherited absolute pair errors, give
\[
 \|T-(G_7+C_z)\|_w^2\ll_\varepsilon X^{2+\varepsilon},\qquad
 Q_7=\|G_7+C_z\|_w^2+O_\varepsilon(X^{2+\varepsilon}).             \tag{4}
\]
Consequently the inherited equivalence is preserved:
\[
 {\rm RH}\ \Longleftrightarrow\
 (Q_7)_+\ll_\varepsilon X^{2+\varepsilon}
 \quad\hbox{for every fixed }\varepsilon>0
 \hbox{ on all sufficiently late dyadic blocks}.                 \tag{5}
\]
The proof compares amplitudes in norm. It does not claim an unconditional
target-scale bound for \(Q_{\rm core}-Q_7\).

## 3. The actual signs at the cube-root cutoff

**Candidate-D.** Put \(\kappa=1/U(1)>0\) and
\[
 c_*=\kappa(\log2-1/2)>0,\qquad
 M_X=\sum_n w(n)\frac{n^2}{(\log n)^4}\asymp\frac{X^3}{(\log X)^4}.
\]
The [prime-pushforward proof](PRIME-PUSHFORWARD.md) gives, uniformly
on the taper,
\[
 C_z(n)=c_*\frac{n}{(\log n)^2}
              +O\!\left(\frac{X}{(\log X)^3}\right).             \tag{6}
\]
This is the uniform block and cube-root form of the earlier
two-prime integral, with its repeated-prime correction explicit.
The exact signed core therefore has
\[
 \begin{aligned}
 P_{\rm core}&=c_*^2M_X+O(X^3/(\log X)^5),\\
 2\operatorname{Re}\langle G_{\rm core},C_z\rangle_w
             &=-2c_*^2M_X+O(X^3/(\log X)^5),\\
 \|C_z\|_w^2&=c_*^2M_X+O(X^3/(\log X)^5).
 \end{aligned}                                                   \tag{7}
\]
The coefficients \(1,-2,1\) persist when the core is restricted to
heights \(X|a|/r\le(\log X)^{14}\) and \(C_z\) is kept whole.
For the full core, the joint cancellation holds to every fixed
inverse-logarithmic order, using the inherited unconditional estimate
for \(T\). The unchanged \(C_z\) retains (6), and (2) transfers (7)
to \(G_7,P_7\); the same height statement follows by the uniform
conductor-mask estimate.
These leading and fixed-order results leave the power-scale gap in (5).

The exact smaller-argument expression can be written
\(C_z(n)=-\sum_m W_{nm}T(m)\), with nonnegative integer \(W_{nm}\)
counting the single primes with weight two and unordered pairs with
weight four. Its energy is a positive Gram form, but its coupling to the
core is the signed linear functional
\[
 -2\sum_m T(m)\sum_n w(n)G_{\rm core}(n)W_{nm}.
 \]
Discarding that functional would remove the negative leading term in (7).

## 4. A compact balanced carrier and a stronger joint slow observation

**Candidate-D.** A second proof uses the actual balanced convolution
of \(t\), retaining the signed unit \(u\). The
[compact balanced note](COMPACT-BALANCED-BAND.md) allocates both affine
terms to the same smooth raw-denominator mask. Raw denominators above
the valid time range have zero floor, so this allocation is exact.

In particular take the separately specified longer unit cutoff
\[
 L_+=\left\lceil X^{3/4}\exp(\sqrt{\log X})\right\rceil.
\]
The entire omitted unit tail is
\(O(\sqrt X\exp[-(2/3)\sqrt{\log X}])\) pointwise on the required
time interval. A finite balanced carrier \(F_{X,+}=G_{{\rm b},+}+
\mathcal B_+\) can therefore omit that tail while retaining both its
masked affine terms. Every reduced Fourier denominator is at most \(4X\),
independently of the longer unit cutoff, and
\[
 \|T-F_{X,+}\|_w\ll_A X(\log X)^{-A}
                  \quad\hbox{for every fixed }A>0.              \tag{8}
\]
The same-window positive-energy norm difference on every sufficiently
late complete integer window \([Y,Y^2)\) is smaller than every fixed
inverse power of \(\log Y\). This is a proved comparison between
distinct carriers.

Write
\[
 \Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}.
\]
Let \(\gamma>0\) be the fixed constant retained in the previously
attributed unconditional estimate
\(T(x)\ll x\log x\exp[-\gamma\Phi(x)]\).
Choose fixed
\[
 0<\lambda<\gamma(1-2^{-2/5}),\qquad
 K=\exp(\lambda\Phi(\sqrt X)).
\]
Use a fixed smooth even cutoff \(\chi\), one on \([-1,1]\) and zero
outside \([-2,2]\). Let \(\mathscr P_{X,K}\) be the integer-time
convolution whose circle multiplier is \(\chi(X\theta/K)\).
Let \(I^+=[X-kh,2X-1+kh]\cap\mathbb Z\) be the buffered interval
from the original taper. On all of \(I^+\), \(w\ge1/2\), and each
point of \([X,2X)\) is at distance at least \(kh\ge X/32\) from
its complement.

The proved joint estimate is
\[
 \boxed{\quad
 \max_{X\le n<2X}
 \left|\mathscr P_{X,K}
       [1_{I^+}(G_{\rm core}+C_z)](n)\right|
 \ll X\exp[-(2\gamma-2\lambda-o(1))\Phi(\sqrt X)] .
 \quad}                                                        \tag{9}
\]
It includes the block endpoints. It also holds with \(G_7\), because
(2) changes this convolved observation by at most
\(O_\varepsilon(X^{1/2+\varepsilon}\sqrt K)\), using
\(\|p\|_2\ll\sqrt{K/X}\). This is smaller than the right side of
(9) for any fixed \(0<\varepsilon<1/2\).

Two partial summations supply two factors of cancellation in the
balanced \(t\) coefficients. Summing the larger unit factors with their
sign gives a cutoff error proportional to \(k_0^{-2/3}\); taking their
absolute values by the same method would give \(k_0^{-1/2}\).
The full affine term is estimated separately with its exact mask and
then included. The finite-time comparison to the core uses (8) and the
original buffer; it is not an identification of Fourier coefficient
families.

Since \(\Phi(\sqrt X)=(2^{-3/5}+o(1))\Phi(X)\), the saving constant
in the scale \(\Phi(X)\) is
\[
 (2\gamma-2\lambda)2^{-3/5}>\gamma .
 \]
This is a strict improvement over applying the inherited pointwise
envelope directly to this specified slow observation. Its squared
energy bound still has scale \(X^{3-o(1)}\). The complementary
frequencies and their mixed products remain part of the full target.

## 5. Two quantified limitations

**Candidate-D, actual coefficients.** At any fixed
\(z=D^\beta\), \(0<\beta<1/3\), the exact primitive-versus-raw
discrepancy has a positive pair subtotal of order at least
\[
 \frac{(D/z)^3}{(\log X)^{2l+2}},
 \qquad l>(1-\beta)/\beta.
 \]
For \(1/4<\beta<1/3\), take \(l=3\), giving denominator
\((\log X)^8\). These are actual numerator-one coefficients with the
original cuts and even the small-gcd restriction. The proof counts
primes on a fixed relative interval and only then bins their products;
it assumes no prime asymptotic inside the small bins.
This blocks the target-scale bound on absolute pair contributions below
the cube root. The signed discrepancy can still cancel against its
other pairs. [Proof](SMOOTH-DIVISOR-AND-TRANSFER.md)

**Candidate-D, a generic-method obstruction.** For every fixed number
\(k\) of prescribed vanishing Mellin moments, there are integer
sequences \(F_X\), supported on \(m\asymp X^{1/2}\), such that
\[
 |F_X(m)|\le\sqrt m,\quad
 \Delta F_X(m)\in\{-1,0,1\},\quad
 \sum_m\frac{|F_X(m)|^2}{m(m+1)}\ll_k1,
 \quad
 \int_1^\infty F_X(u)(\log u)^j\frac{du}{u^2}=0\ (j<k),
 \]
but
\[
 \|\mathcal C_z[F_X]\|_w^2
       \asymp_k \frac{X^{5/2}}{(\log X)^{2k+2}}.                \tag{10}
\]
The integer construction uses disjoint dilated ramps and
\(1/(r+1)+1/[r(r+1)]=1/r\). More generally it yields the power
\(X^{3-\delta}\) for every fixed \(0<\delta<2/3\), with the stated
derivative-zero qualification on the logarithmic exponent.
These probes do not have the multiplicative coefficients of \(T\).
They exclude an isolated prime-operator induction from those generic
norm and finitely many moment conditions alone. They are not
counterexamples to (5). [Proof](PRIME-PUSHFORWARD.md)

## 6. Remaining estimate and evidence status

**O.** Prove (5) for the complete jointly signed quantity (3). The two
fixed divisor removals are paid at its required scale. The slow joint
observation has the stronger bound (9). Neither result estimates the
whole remaining amplitude at square-root scale. No parameter in a
fixed-order asymptotic is allowed to grow without a new uniform proof.

The latest neighboring balanced work was read at
[eac05e3cde56d0fb3e429b91aa7129087e5da4db](https://github.com/mathorn1973/twist-j/tree/eac05e3cde56d0fb3e429b91aa7129087e5da4db/notes/C-RH-THREE-INTERFACE-SYNTHESIS-N).
Its affine allocation and double partial summation are credited.
The present proofs supply the signed-unit transfer and the finite-time
comparison to this candidate's actual core. The classical prime-count,
Mertens and maximal short-sum inputs retain their primary attribution in
the proof files and [SOURCES](../SOURCES.md).

Three bounded paper lanes and root, comprising two Astra and two Sol
participants, performed this work. The retained reviews cover
[divisor deletion](REVIEW-SMOOTH-DIVISOR.md),
[prime pushforward](REVIEW-PRIME-PUSHFORWARD.md), and
[balanced transfer](REVIEW-COMPACT-BALANCED.md), and the
[final synthesis](REVIEW-SYNTHESIS.md).
This is same-session opposition, not external or blind confirmation.
No scientific executable, finite enumeration, external computation or
formal proof build was run. Earlier proof and finite-audit files are
unchanged. The package remains a draft with no Canon, registry, formal
probe, workflow, merge, release or physical-layer change.

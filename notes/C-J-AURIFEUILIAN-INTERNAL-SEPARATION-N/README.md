# Inside one Aurifeuilian return factor

**NON-CANONICAL. NO AUTHORITY. L1 arithmetic only.** Paper results below are
candidate-D; the prospectively pinned finite audit is candidate-C on one
architecture. No Canon, physical, RH or primality-algorithm status changes.

Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261124-Internal-Separation.
[Claim #2090](https://github.com/mathorn1973/twist-j/issues/2090).
Public basis: main `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, Public Canon v117.
All authority files, declared immutable basis and required successful
checks were verified on that unchanged public basis. Uploaded snapshots
are references, not authority.

## Round two: four units are insufficient at the next index

**Paper results: candidate-D. Finite obstruction: candidate-C.** The
continuation proves that the complete Lucas menu already detects every
separation possible with four signed units, including arbitrary exponents
and fifth-root phases, with full prime-power multiplicities.

The newly frozen menu at m=125 returns no proper gcd on either side:
781246 unit gcds and four whole-input gcds on each side. Both independently
authored programs agree on all 1562500 tests. Separate exposed product and
Bezout certificates prove that each side contains at least two distinct
prime divisors. Thus four units, optimal for the earlier index-25 pair,
are insufficient for internal separation at index 125. Whether five units
attain separation there remains open.

A second paper theorem bounds the entire proper gcd for every fixed weight
even with unrestricted exponents. Its exact integer threshold grows
subexponentially in m at fixed weight. Large-prime flags remain locked
under any such menu; a universal bound on weight remains unresolved.

[Round-two results and sources](round2/README.md),
[complete four-unit proof](round2/FOUR_UNIT_COMPLETENESS.md),
[unrestricted-exponent bound](round2/GROWING_WEIGHT.md),
[exact audit record](round2/RUN.md), [internal opposition](round2/OPPOSITION.md).
The original frozen index-25 source and output files below are unchanged.

## What this continues

Write $j=\zeta_5$, $\mathcal O=\mathbb Z[j]$, $J=1+j^2$,
$\phi=-j^2-j^3$, and $\alpha=\phi^2$. Since $J\phi=j$, the signed
units $\pm j^a\phi^b$ are exactly the same units written using $J$ and
the fifth-root phase. Content means the nonnegative gcd of the four
integral coordinates, with content zero for the zero element.

For $m=5^k$, $k\ge1$, put
\[
 A_\pm(m)=5F_m^2\pm5F_m+1,\qquad
 M(m)=A_-(m)A_+(m)=L_{5m}/L_m.
\]
The classical factorization and the six-unit prescription in
[PR #2088](https://github.com/mathorn1973/twist-j/pull/2088) separate the
two sides. Every prime in either side has whole-ideal order $5m$ for
$\alpha$. The remaining question is separation of different primes
**within one side**, without using the factors to choose the tests.

## 1. An actual internal split of minimum unit weight four [candidate-D]

The prescribed search at $m=25$ derives its input from $F_{25}$ and visits
all comparisons $L_a\pm L_b$ with $a$ even in $[0,248]$ and $b$ odd in
$[1,249]$, in a fixed lexicographic order. Its first proper divisor is
\[
 \gcd(28144128251,L_{103}+L_2)=251,
 \qquad 28144128251=251\cdot112128001.
\]
The value $L_{103}+L_2$ is $3355265920593054081632$. Its unit expression is
\[
 \phi^{103}-\phi^{-103}+\phi^2+\phi^{-2}.
\]
The two factors are used only in the auxiliary audit, after defining the
main search; they do not choose its test family or traversal order.

A separate paper proof establishes the lower bound throughout this tower:
for every sum $S$ of at most three signed units, including arbitrary
fifth-root phases,
\[
       \gcd(M(m),\operatorname{cont}S)\in\{1,M(m)\}.
\]
This includes every prime-power multiplicity. Thus three terms cannot
separate any two primes at a fixed index, and the displayed internal
four-term witness is optimal in unit weight for its pair. The bound on
weight says nothing by itself about how many tests are needed.

The proof reduces a real three-unit relation to $x+y=1$, with norms
$s,t\in\{\pm1\}$, and then to
\[
                 x^2+(t-s-1)x+s=0.
\]
There are six universal ordered solutions. The only other case would
require an element of order six, excluded by the power-of-five return
order. The decomposition $\mathcal O=\mathbb Z[\phi]\oplus j\mathbb Z[\phi]$
transfers the result to phased units without increasing the term count.
[Full lower-bound proof](THREE_UNIT_OBSTRUCTION.md).

## 2. Why this new four-term prescription is not universal [candidate-D]

After the finite search, extend $103=4\cdot25+3$ to the fixed prescription
$L_{4m+3}+3$. Its behavior can be classified completely:
\[
 \gcd(A_\sigma(m),L_{4m+3}+3)=
 \begin{cases}251,&m=25,\ \sigma=+1,\\1,&\text{otherwise}.\end{cases}
\]
At the relevant cyclotomic roots the comparison reduces to
$P_a=3+\phi^3j^{-a}-\phi^{-3}j^a$. Pairing opposite phases gives
$P_aP_{-a}=28+13t$, where $t^2+t-1=0$. Therefore
\[
                  N_{\mathbb Q(j)/\mathbb Q}(P_1)
                  =28^2-28\cdot13-13^2=251.
\]
The whole gcd divides this one norm. A short hand calculation modulo
251 proves the positive case and the return order excludes all other
indices. This classifies the prescription without depending on the
search output or the primality of its cofactor.
[Full witness and all-index proof](FOUR_UNIT_WITNESS.md).

## 3. Explicit four-coordinate readout without factoring [candidate-D]

For either side set $f=F_m$ and $A=A_\sigma(m)$. The integers
\[
       \rho=3+5\sigma f,\qquad
       \lambda=1+\sigma(2f-F_{m-1})
\]
give $\rho^2-\rho-1=0$ and $\Phi_5(\lambda)=0$ modulo $A$.
Moreover $1+\lambda+\lambda^{-1}=\rho$. They provide the isomorphism
\[
 \mathcal O/A\mathcal O\ \cong\ (\mathbb Z/A\mathbb Z)^4,
 \quad P(j)\longmapsto(P(\lambda),P(\lambda^2),P(\lambda^3),P(\lambda^4)).
\]
No factorization of $A$ enters these coordinates. Pairwise differences of
the four roots are units modulo $A$, so the description preserves repeated
prime factors. Whole-ideal divisibility is simultaneous zero in all four
coordinates; selecting one zero coordinate is insufficient.

This decomposes the algebraic branches. It does not factor the scalar ring
$\mathbb Z/A\mathbb Z$: every one of the four coordinates still contains
the entire integer $A$. It is an explicit decoder, not an unproved shortcut
from algebraic conjugates to the prime factors.
[Coordinate proof and exact orders](SPLIT_COORDINATES.md).

## 4. A fixed family of affine prescriptions eventually stops reading

**candidate-D.** Let $P(Z)\in\mathcal O[Z,Z^{-1}]$ be fixed. Define
\[
 Q_\sigma(Z)=Z^4+\sigma\sqrt5 Z^3+3Z^2+\sigma\sqrt5 Z+1.
\]
If $Q_\sigma$ divides $P$, the gcd of $A_\sigma(m)$ with the content of
$P(\phi^m)$ is the whole side at every index. Otherwise that gcd divides
one fixed nonzero integer and equals one at every sufficiently large index.
Thus finitely many prescriptions with exponents $a_i m+b_i$, with all
coefficients fixed, eventually have identical prime-divisibility flags
within each side. Constant polynomials in $F_m,F_{m-1}$ are included after
clearing an invertible power of $\sqrt5$.

The precise all-pairs equivalence is stated in
[Affine dichotomy](AFFINE_DICHOTOMY.md). It does not assume that infinitely
many individual sides contain two distinct primes. That infinitude remains
open in this work; composite prime powers would not by themselves supply
distinct-prime pairs.

## 5. Quantitative obstruction even for adaptive slopes [candidate-D]

Let a test have $w$ signed-unit terms and integer exponents
\[
 e_i=(a_i m+b_i)/D,\qquad D\ge1,\qquad 5^{v_5(D)}\mid m.
\]
Allow all parameters and slopes to depend on $m$. Put
\[
 H=(\max b_i-\min b_i)/D,\qquad
 C_H=\frac w2(\phi^{H/2}+\phi^{-H/2}),\qquad
 g=\gcd(A_\sigma(m),\operatorname{cont}S).
\]
Then
\[
                  g=A_\sigma(m)\quad\hbox{or}\quad g\le C_H^{4D}.
\]
This bounds the full gcd including valuations. It is independent of the
sizes and signs of the slopes $a_i$. Since every prime factor is at least
$10m+1$, the strict inequality $C_H^{4D}<10m+1$ allows only gcd 1 or the
whole side, for any number of tests in the stated resource box.

For example, at $m=5^k\ge625$, no test with at most six terms, integer
slopes and shifts $b_i\in[-1,1]$ can split either side: here
$C_H^4\le2025<10m+1$. Bounded denominators and rounded slopes are covered
as well. A bounded $w,H$ requires $D$ to grow at least on the scale of
$\log m$ for this obstruction even to cease applying. That condition is
necessary, not sufficient, for obtaining an internal split.
[Full proof, including an integer-only sufficient inequality](DENOMINATOR_RIGIDITY.md).

## Finite evidence [candidate-C]

The public source pin is
[`dab860c8c51ecc76da24a6960051340ad2e5d2cb`](https://github.com/mathorn1973/twist-j/commit/dab860c8c51ecc76da24a6960051340ad2e5d2cb).
The exact preregistration and both independently written programs were
read back before execution. Both programs produced identical 965-byte
output. No frozen input or domain was changed.

| Audit | Result |
| --- | --- |
| Prescribed trace comparisons | 31250 |
| gcd 1 | 31126 |
| gcd 251 | 120 |
| gcd equal to the whole input | 4 |
| Exact order of phi at each prime | 250 |
| Exact order of alpha at each prime | 125 |
| Distinct signed labels at each prime | 500 |
| Normalized three-unit relations | Same six ordered pairs |
| Separating relation of weight at most three | None |
| Implementation output mismatch | None |

The primary verifier uses sequence recurrences and quadratic coefficient
pairs. The breaker uses separate matrix powers, quartic coefficient
arithmetic and a full ordered-pair loop. [Preregistration](PREREG.md),
[execution receipt](RUN.md), [verifier output](EXPECTED.txt),
[breaker output](BREAK_EXPECTED.txt), [review scope](REVIEW.md).
The later paper lower bound and all-index witness proof are self-contained;
the finite audit remains one-architecture candidate-C.

## Remaining question

For arbitrary two distinct primes within the same side, does some universal
constant unit weight suffice if the exponents can be chosen without the
factorization, and how large a prescribed menu is needed? The first round settles
one optimal four-unit instance and rules out specified broad classes of
eventual fixed prescriptions. Round two excludes universal weight four
by the actual composite index-125 sides and gives a bound for all
unrestricted-exponent proper outputs at each fixed weight. It does not
settle the universal constant-weight question.
The next useful scope must allow exponent offsets or denominator resolution
to grow beyond the quantitative obstruction, and separately control the
number and cost of tests. It must be prospectively specified before a new
search, not obtained by extending the completed audit bounds.

## Prior work and sources

* John Brillhart, Peter L. Montgomery and Robert D. Silverman,
  *Tables of Fibonacci and Lucas Factorizations*, Mathematics of Computation
  50 (1988), 251-260, equation (2.9).
  [DOI 10.1090/S0025-5718-1988-0917832-6](https://doi.org/10.1090/S0025-5718-1988-0917832-6).
  The underlying Aurifeuilian factorization is classical, not claimed new.
* Marie-Nicole Gras, *Non monogeneite de l'anneau des entiers de certaines
  extensions abeliennes de Q*, Seminaire de theorie des nombres de Besancon,
  1983-1984. Remark 5 gives the factorization; the table on PDF page 17 and
  Example 2 on PDF page 19 list the relevant prime factors.
  [Primary PDF](https://www.numdam.org/item/10.5802/pmb.a-41.pdf).
* The supplied C-J-UNIT-RELATION-DEPTH-1 and C-J-UNIT-ARITY-BOUND-1 notes
  retain their separate ownership. Their sparse-unit and phase-projection
  questions were read in the previous work; unrelated finite minima are
  not adopted as new verification here. See the scoped review in
  [#2084](https://github.com/mathorn1973/twist-j/issues/2084) and
  [#2088](https://github.com/mathorn1973/twist-j/pull/2088).

All proofs and code in this directory are original to this scoped write-up;
the list above attributes inherited identities and problem context. The
existence of this write-up is not a priority claim for the derived theorems.

# What the inert-prime comparison supplies

**NON-CANONICAL. No authority. No Canon status change.**

**Candidate-D for the derivations and source applications below.** The cited
classical statements retain their original scope. This note checks the
inert-prime comparison supplied for round 15; it does not take ownership of
the separate augmentation problem. No scientific program was executed.

## 1. Three operators, with different coefficient spaces

Let $K=\mathbb Q(j)$, $j=\zeta_5$, and let $q$ be an odd prime congruent to
$2$ or $3$ modulo $5$. For $C:y^2=x^5-1$ and its reduced Jacobian $A_q$,
point counting over $\mathbb F_q$ and $\mathbb F_{q^2}$ gives $q+1$ and
$q^2+1$. Indeed fifth powering is bijective in both fields. Newton's identities
and the reciprocal form of the genus-two Frobenius polynomial give

$$
P_q(X)=X^4+q^2,\qquad \pi_q^4=[-q^2],\qquad
\pi_qj=j^q\pi_q.
$$

The point-count argument and the full rational geometric endomorphism algebra
are in Galbraith and Pujolas, *Distortion maps for genus two curves*, Section 3,
especially Lemma 3.1 and Proposition 3.5/Corollary 3.6. The algebra statement
concerns $\operatorname{End}(A_{\overline{\mathbb F}_q})\otimes\mathbb Q$,
not an asserted action on the characteristic-zero period space $HH$.
[Primary paper](https://www.math.auckland.ac.nz/~sgal018/jordi-paper.pdf#page=3).

The following distinctions are load-bearing.

| Operator | Space and coefficients | Fourth power |
| --- | --- | --- |
| $x\mapsto x^q$ | the residue field $\mathbb F_{q^4}$ over $\mathbb F_q$ | $I$ |
| $q$-power Frobenius endomorphism $\pi_q$ | prime-to-$q$ rational Tate module of $A_q$ | $-q^2I$ |
| reduction of a $q$-integral matrix model satisfying that relation | its residue module, when such a model exists | $0$ |

They cannot be substituted for one another. In particular, the elementary
quartic orbit theorem in [the main proof](PROOF.md) uses multiplication by
$j$, not an identification of these three Frobenius operations.

There is also an exact obstruction to a proposed four-dimensional rational
model. Over $K_q=\mathbb Q_q(j)$, let $\sigma(j)=j^q$ and suppose $V=K_q^m$
has a $\sigma$-semilinear operator $\pi$ with $\pi^4=-q^2I$. Write
$\pi=C\sigma$, with $C\in\mathrm{GL}_m(K_q)$. Taking determinants in
$C\sigma(C)\sigma^2(C)\sigma^3(C)=-q^2I$ gives

$$
N_{K_q/\mathbb Q_q}(\det C)=(-q^2)^m.
$$

The extension is unramified of degree four, so normalized valuations give
$4v(\det C)=2m$. Thus $m$ is even and $\dim_{\mathbb Q_q}V$ is divisible by
eight. A single regular four-dimensional $J$ register cannot carry this
particular $\pi$. This says nothing against the prime-to-$q$ Tate module,
whose coefficient field is different. The opposition gives the corresponding
residue-module argument in [REVIEW.md](REVIEW.md).

## 2. The genus-two derivative has nilpotence depth two

The author announcement records $D^q=0$ for an invariant derivation on a CM
curve at an inert prime, followed by divisibility of normalized theta
derivatives. That statement does not specify the present genus-two carrier.
[Alpoge, announcement, timeline item 2](https://alpo.ge/remark.pdf#page=3).

For the present Jacobian, a direct calculation makes the limitation precise.
Put $h=(q-1)/2$ and

$$
(x^5-1)^h=\sum_n c_nx^n,\qquad
c_{5a}=(-1)^{h-a}\binom ha,
$$

with other coefficients zero. Use the ordered differential basis
$\omega_1=dx/y$, $\omega_2=x\,dx/y$ and **column-vector, left-action**
conventions. The Cartier operator has matrix

$$
M_{ij}=c_{qi-j}^{1/q},\qquad 1\le i,j\le2.
$$

For completeness, write
$\omega_j=y^{-q}\sum_n c_nx^{n+j-1}dx$. Cartier selects exponents
$n+j-1=qi-1$ and sends $x^{qi-1}dx$ to $x^{i-1}dx$. This proves the formula
and fixes its transpose convention. Here all coefficients lie in
$\mathbb F_q$, so the displayed $q$th roots do not change their values.

It follows that

$$
M=\begin{cases}
\begin{pmatrix}0&c_{q-2}\\0&0\end{pmatrix},&q\equiv2\pmod5,\\[4pt]
\begin{pmatrix}0&0\\c_{2q-1}&0\end{pmatrix},&q\equiv3\pmod5.
\end{cases}
$$

The indicated coefficient is nonzero: its index divided by five is an integer
between zero and $h<q$, so the binomial coefficient has no factor $q$.
Consequently $M\ne0$ but $M^2=0$. Over an algebraic closure the operator is
inverse-Frobenius semilinear; since its matrix is over $\mathbb F_q$, its
second iterate is still represented by $M^2=0$.

This agrees, up to action/transposition convention, with the nonzero
rank-one Cartier matrix for the $q\equiv3\pmod5$ family in Boix, Noordman
and Top, Example 2.3. Our calculation also covers $q\equiv2\pmod5$ and the
small good primes $3,7$. We use the matrix rank and nilpotence, not an
unstated choice of its kernel basis. Achter and Howe explain why Cartier
and Hasse-Witt matrices and their semilinear iteration must be distinguished.
[Boix et al., Example 2.3](https://www.math.rug.nl/~top/Alberto.pdf#page=4) ·
[Achter and Howe, Sections 1-3](https://www.math.colostate.edu/~achter/math/hwcm1017.pdf).

Let $D$ now denote a translation-invariant derivation on $A_q$, extended to
an algebraic closure if desired. Cartier's pairing identity is

$$
\langle\mathcal C\omega,D\rangle^q
=\langle\omega,D^{[q]}\rangle
 -D^{q-1}\langle\omega,D\rangle.
$$

For invariant forms and vector fields the last term is zero because the
pairing is constant. Abel-Jacobi pullback identifies invariant forms on
$A_q$ with regular differentials on $C$. Thus the restricted power map on
the two-dimensional invariant Lie algebra has rank one and square zero.
Equivalently,

$$
D^{[q^2]}=0\quad\text{for every invariant }D,
\qquad D^{[q]}\ne0\quad\text{for some invariant }D.
$$

Exactly one line of invariant directions is killed after the first restricted
power. Here brackets denote restricted powers, which are compositions of
derivations in characteristic $q$. This is distinct from the fourth-power
identity on a prime-to-$q$ Tate module.
[Cartier, original 1957 note, formula (6) and the Jacobian corollary](https://www.ihes.fr/wp-content/uploads/2024/09/CartierCRAS57.pdf).

No theta-divisibility bound is inferred by replacing $q$ with $q^2$ in the
announcement. Such a bound needs a specific integral theta construction,
chosen derivative directions and control of its normalizations.

## 3. The inert-only cancellation obstruction is valid at its stated scope

Let $\mathcal I$ be the rational primes $2,3\pmod5$, and put
$F_{\mathcal I}(s)=\prod_{q\in\mathcal I}(1-q^{-s})$ for $\Re s>1$.
For the quadratic character $\chi_5$ and
$\zeta^*(s)=(1-5^{-s})\zeta(s)$, comparison of Euler factors gives

$$
F_{\mathcal I}(s)^2
=\frac{L(s,\chi_5)}{\zeta^*(s)}F_{\mathcal I}(2s).
$$

At a split prime the ratio factor is one. At an inert prime it is
$(1-t)/(1+t)$, and multiplication by $1-t^2$ gives $(1-t)^2$.
The ramified prime has been removed from both sides of that ratio.

The classical facts that $\zeta$ has a simple pole at one and
$L(1,\chi_5)\ne0$ make the right side holomorphic with a simple zero near
one; $F_{\mathcal I}(2s)$ is holomorphic and nonzero there. If the inert-only
Mobius summatory function were $O(x^\theta)$ for any fixed $\theta<1$,
partial summation would continue $F_{\mathcal I}$ holomorphically to
$\Re s>\theta$. Its square could not have a zero of odd order. The proposed
power bound is therefore impossible for this restricted summatory function.
This uses no RH. A finite nonzero Euler factor at one, including the factor
for five, does not alter the obstruction.

This is a rechecked scalar comparison, not a period-rank estimate. In the
registered rapidity lift an inert prime acts at zero rapidity with factor
$1-T$, while the split factors retain the nontrivial directions. The
coefficientwise inert/split convolution follows, but no uniform cancellation
bound on that convolution has been supplied. The public augmentation owner
remains open with its existing non-circular transfer requirement.
[Public registry, fixed authority revision](https://github.com/mathorn1973/twist-j/blob/ed3b1878d95825ab9473c16416c8db76cc152079/canon/REGISTRY.tsv) ·
[Public frontier](https://github.com/mathorn1973/twist-j/blob/ed3b1878d95825ab9473c16416c8db76cc152079/canon/FRONTIER.md#enrichment-enrichment).

## 4. What can actually be used for the period problem

The genuine RH source already has inert-prime local valuation input. Its
route is through a changed algebraic column lattice and the integral pairing
$B_k$, not an asserted CM5 endomorphism of $HH$. The exact source links and
the passage back to the full period space are recorded in [SOURCE.md](SOURCE.md).

The modular and filtration criteria in [PROOF.md](PROOF.md) can be applied
to the genuine algebraic $B_k$ without asserting a number-field model of all
uncut analytic periods. A useful small residual/graded defect is still an
additional mathematical obligation. Neither the CM5 Frobenius polynomial,
the scalar norm valuation identity, nor the inert-only Euler product supplies
it automatically.

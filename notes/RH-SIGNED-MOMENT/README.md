# Signed prime correlations and a finite moment problem

A. M. Thorn — 6 September 2026

**NON-CANONICAL research note.** The results stated as proved below are
unconditional mathematical derivations for the fixed quadratic character
modulo 5. The target moment is open. This note does not establish RH or
change any claim in the TWIST-J Canon.

## Abstract

We study cancellation in a signed squarefree-support decomposition of an
integral refinement of the Möbius function. A controlled functional-equation
and truncation argument turns a specified analytic-tail estimate into a
finite rational-frequency moment. Its coalesced diagonal and the complete
signed sector with one squarefree numerator core are smaller than the target
by a power. Fixed-core short correlations have an explicit Euler-product
main term. Actual prime-frequency families nevertheless contribute much
more than the target when estimated separately. We construct their signed
companions, including a strictly negative second-difference quartet, and
prove that discarding this large negative family prevents a target-sized
bound for its complement. Classical exponent-pair inputs give a bound for
the whole Fejér moment and imply power-accurate compensation between actual
terms with different cores. The stronger joint estimate needed to reach
the target is isolated with all cutoffs and weights retained.

The mathematical point is that small total energy need not come from small
individual sectors. Here explicitly identified positive and negative
contributions are larger than the comparison budget, while their full
signed balance has a better bound.

## Reading the note

This document gives the arithmetic origin, main statements, and remaining
question. The three proof appendices are part of the same note:

| Appendix | Content |
|---|---|
| [Arithmetic](ARITHMETIC.md) | Exact coefficients, parity masks, short correlations, rational diagonal, Fejér identity, and complete same-core estimate |
| [Analysis](ANALYTIC.md) | Uniform character-polynomial moments, finite approximation, whole Fejér bound, analytic-tail transfer, and the reduced sufficient input |
| [Prime cancellation](PRIME-CANCELLATION.md) | Actual prime families, singleton determinant sums, negative companions, second differences, and forced compensation |

All necessary local definitions and proofs are included in this package;
external analytic inputs are attributed to specific primary theorems in
the appendices. No numerical experiment is used to support an unbounded
claim. No priority claim over the literature is made.

## 1. Arithmetic origin: prime factors, coefficient channels, and Z

Let $\chi=\chi_5$, with values $(0,1,-1,-1,1)$ on residues
$(0,1,2,3,4)$ modulo 5. A split prime means a rational prime
$p\equiv1,4\pmod5$. Write $\mathcal R$ for the squarefree
positive integers supported on split primes, including 1, and

$$
f(r)=(-2)^{\omega(r)}\quad(r\in\mathcal R),\qquad f(r)=0
\quad(r\notin\mathcal R).
\tag{M1}
$$

The integral refinement used in the repository can be specified here
without any geometric interpretation. Introduce independent invertible
symbols $X_p$ for split primes, and define a multiplicative
Laurent-polynomial-valued sequence with $\boldsymbol\mu(1)=1$ by

$$
\begin{array}{c|cc}
&\boldsymbol\mu(p)&\boldsymbol\mu(p^e),\ e\ge2\\ \hline
p\text{ split}&1-X_p-X_p^{-1}&2-X_p-X_p^{-1}\\
p\text{ not split, including }5&-1&0.
\end{array}
\tag{M2}
$$

Set $U_r=\prod_{p\mid r}(X_p+X_p^{-1})$, $U_1=1$.
Independent inversion of the symbols leaves every coefficient invariant,
so the accumulated polynomial has a unique expansion

$$
\sum_{n\le N}\boldsymbol\mu(n)
=\sum_{\substack{r\le N\\r\in\mathcal R}}A_r(N)U_r.
\tag{M3}
$$

The supports are squarefree because each symbol has exponent at most one
in absolute value at its own prime. An oriented monomial supported on r
can occur only at an integer divisible by r. Different $U_r$ have
disjoint monomials, proving uniqueness and the bound r≤N in (M3).

Augmentation is the substitution $X_p=1$. Each local coefficient
in (M2) then becomes the ordinary Möbius coefficient. Therefore

$$
M(N):=\sum_{n\le N}\mu(n)
=\sum_{\substack{r\le N\\r\in\mathcal R}}2^{\omega(r)}A_r(N).
\tag{M4}
$$

This is an identity, not a cancellation estimate. The formal construction
is also recorded in the public
[integral-lift proof](../../probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1/PREREG.md).
The existing [full-shell transfer note](../RH-FULL-SHELL-FOURIER-CONTRACT-2026-09-05.md)
studies reconstruction from the larger shell. The present note examines
the signed arithmetic after the support decomposition.

### The central coefficient has structured signs

Put $Z(x)=A_1(x)=\sum_{n\le x}c_0(n)$, with all summatory
functions zero below 1. Taking constant coefficients in (M2) gives

$$
c_0(p^e)=
\begin{cases}
1,&p\text{ split},\ e=1,\\
2,&p\text{ split},\ e\ge2,\\
-1,&p\text{ not split},\ e=1,\\
0,&p\text{ not split},\ e\ge2.
\end{cases}
\tag{M5}
$$

For $5\nmid n$, the coefficient vanishes if an inert prime square
divides n; otherwise
$c_0(n)=\chi(n)2^{\#\{p\text{ split}:p^2\mid n\}}$.
At 5, $c_0(5m)=-c_0(m)$ when $5\nmid m$, and
$c_0(25m)=0$. Thus the exact sign-amplitude identity is

$$
c_0(n)=\varepsilon_{25}(n)|c_0(n)|,\qquad
\varepsilon_{25}(n)=\chi(n)-\mathbf1_{5\mid n}\chi(n/5).
\tag{M6}
$$

The quotient in the second term is evaluated only when 5 divides n.
The sign function is periodic modulo 25; its period has twelve positive,
twelve negative, and one zero entries. Prime squares determine the
remaining amplitude and can also force it to vanish. For example,
$c_0(11^2)=2$, $c_0(7^2)=0$, and $c_0(5\cdot11^2)=-2$,
directly from (M5). Values of Z are consequently constrained by arithmetic;
they are not independent choices of signs.

### The support cutoff leads to the analytic object

For $\Re s>1$, define $C(s)=\sum_nc_0(n)n^{-s}$. Its local
factors from (M5) are $(1+p^{-2s})/(1-p^{-s})$ at a split
prime and $1-p^{-s}$ at every other prime. Equivalently,

$$
C(s)=\frac{(1-5^{-s})L(s,\chi)L(2s,\chi)}{\zeta_5(4s)},
\qquad \zeta_5(w)=(1-5^{-w})\zeta(w).
\tag{M7}
$$

Indeed the Euler factor of $L(2s,\chi)/\zeta_5(4s)$ at
$p\ne5$ is $1+\chi(p)p^{-2s}$, which gives the factors
just listed after multiplication by $L(s,\chi)$.

At a prime included in an oriented support, its coefficient series is
$-p^{-s}/(1-p^{-s})$. Dividing this local series by the central
one proves the formal coefficient identity

$$
A_r(N)=(-1)^{\omega(r)}
\sum_{\substack{\operatorname{rad}(v)\mid r\\rv^2\le N}}
(-1)^{\Omega(v)}Z\!\left(\frac{N}{rv^2}\right).
\tag{M8}
$$

Every sum in (M8) is finite. Here $\Omega$ counts prime factors
with multiplicity, and $\operatorname{rad}(1)=1$.
The corresponding restricted augmentation

$$
R_Y(N)=\sum_{\substack{r\le\min(Y,N)\\r\in\mathcal R}}
2^{\omega(r)}A_r(N)
\tag{M9}
$$

is the partial sum of the coefficient sequence whose Dirichlet series
is $C(s)T_Y(s)$, where

$$
T_Y(s)=\sum_{\substack{r\le Y\\r\in\mathcal R}}
f(r)r^{-s}\prod_{p\mid r}(1+p^{-2s})^{-1}.
\tag{M10}
$$

This support bound is on the product of the distinct primes, not on each
prime separately. For Y=N, (M9) equals M(N); smaller Y retains only
part of that sum. Establishing a bound for one of its analytic factors
does not by itself estimate the full unrestricted augmentation.

## 2. A precisely normalized intermediate target

Fix $1/4<\sigma<1/2$, put $T=\sqrt Y\ge2$, and normalize
$\|Q\|_{2,T}^2=T^{-1}\int_T^{2T}|Q(t)|^2dt$.
Define

$$
H(s)=\frac{(1-5^{-s})L(2s,\chi)}{\zeta_5(4s)},\qquad
G_Y(s)=L(s,\chi)T_Y(s),\qquad C=HL.
\tag{M11}
$$

Let $g_Y(n)$ be the coefficient of $G_Y$ in its absolutely
convergent half-plane and
$P_Y(s)=\sum_{n\le Y}g_Y(n)n^{-s}$. Local coefficient
cancellation gives $|g_Y(n)|\le1$ for $n\le Y$; the
complete formula and proof are in [Analysis](ANALYTIC.md).
The analytic-tail norm studied here is

$$
r_Y(T)=\|H(\sigma+it)(G_Y(\sigma+it)-P_Y(\sigma+it))\|_{2,T}.
\tag{M12}
$$

This is an analytic remainder after removing a finite prefix. It must not
be replaced by an unproved convergent Dirichlet-series tail on the line
$\Re s=\sigma$. Its target scale and the reflected finite scale are

$$
\mathcal B=Y^{1-\sigma}T^{-\sigma},\qquad
\mathcal N=Y^{1-\sigma}T^{-1/2},\qquad
T^{1/2-\sigma}\mathcal N=\mathcal B.
\tag{M13}
$$

Set $M=\lceil40T\rceil$, choose fixed
$0<\beta<2\sigma$, $0<\gamma<\min(1/2-\sigma,2\sigma-1/2)$,
and put $K=\lceil T^{(1/2+\gamma)/\beta}\rceil$. The actual
finite polynomial is

$$
\begin{split}
A_M(t)&=\sum_{a\le M}\chi(a)a^{\sigma-1+it},\\
B_M(t)&=\sum_{b\le M}\chi(b)b^{-2\sigma-2it},\\
S_{Y,K}(s)&=\sum_{\substack{r\le Y,\ r\in\mathcal R\\
v\le K,\ \operatorname{rad}(v)\mid r}}
f(r)(-1)^{\Omega(v)}r^{-s}v^{-2s},\\
\mathcal P(t)&=A_M(t)B_M(t)S_{Y,K}(\sigma+it).
\end{split}
\tag{M14}
$$

**Finite-reduction theorem.** With these choices, the two all-epsilon
estimates

$$
r_Y(T)\ll_{\sigma,\epsilon}\mathcal B T^\epsilon
\quad\Longleftrightarrow\quad
\|\mathcal P\|_{2,T}^2\ll_{\sigma,\epsilon}\mathcal N^2T^\epsilon
\tag{M15}
$$

are equivalent. Fixed auxiliary choices may enter the constants.
The proof reflects only the first L-factor by its functional equation,
uses literal finite cutoffs for both remaining L-factors, controls the
geometric v-tail with its radical weight, and bounds the prefix. Every
error is below its target by a fixed positive power. The multiplier in
the functional equation is bounded above and below by fixed multiples
of $T^{1/2-\sigma}$; no L-function is divided out. Both directions
and the error estimates are proved in [Analysis](ANALYTIC.md).

For a local pair expansion define the nonnegative Fejér form

$$
\mathscr F_T(Q)=\frac1{2\pi T}\int_{\mathbb R}
\operatorname{sinc}^2\!\left(\frac{t-3T/2}{2T}\right)|Q(t)|^2dt,
\qquad \operatorname{sinc}(x)=\frac{\sin x}{x},
\tag{M16}
$$

with value 1 at zero. Its measure has mass 1. For finite polynomials
with real coefficients the exact pair kernel is

$$
\mathcal L_T(u)=(1-T|u|)_+\cos(3Tu/2),\qquad
\|\mathcal P\|_{2,T}^2<7\mathscr F_T(\mathcal P).
\tag{M17}
$$

The kernel is strictly positive for $|u|<1/T$ and zero outside.
Thus the stronger local estimate

$$
\mathscr F_T(\mathcal P)
\ \stackrel{?}{\ll}_{\sigma,\epsilon}\mathcal N^2T^\epsilon
\tag{M18}
$$

is sufficient for (M15). No reverse implication from the sharp time
moment to (M18) is asserted. In particular, a global pair-cancellation
claim below is deduced from a bound for the entire integral (M16),
not just its restriction to $[T,2T]$.

## 3. Exact arithmetic and the parts already controlled

### Coefficients and short correlations

Coalescing integer numerators gives
$B_MS_{Y,K}=\sum_Nd_NN^{-\sigma-it}$. For the unique decomposition
$N=rn^2$, with $r\le Y$, $r\in\mathcal R$,

$$
d_{rn^2}=f(r)\chi(n)
\sum_{\substack{v\mid n,\ n/M\le v\le K\\
\operatorname{rad}(v)\mid r}}(-1)^{\Omega(v)}.
\tag{M19}
$$

Other squarefree parts have zero coefficient. If $n\le M$ and
$\prod_{p\mid r}p^{v_p(n)}\le K$, every relevant divisor is
included. The divisor sum then equals the parity indicator

$$
\psi_r(n)=\mathbf1_{\{v_p(n)\text{ even for all }p\mid r\}}.
\tag{M20}
$$

This is literal cancellation of a finite divisor sum. The surviving
exponents at primes dividing r in the numerator $rn^2$ are 1
modulo 4. The cutoff formula (M19), rather than (M20), applies outside
the complete region.

For positive n in an interval $I=(x,x+H]$, $Z_*=\max(2,x+H)$,
the masked character satisfies

$$
\left|\sum_{n\in I}\chi(n)\psi_r(n)\right|
\le2^{\omega(r)+1}
\prod_{p\mid r}\left(1+\frac{\log Z_*}{2\log p}\right).
\tag{M21}
$$

For fixed $r,r'\in\mathcal R$ and nonzero integer h there is
also the explicit correlation

$$
\sum_{x<n\le x+H}\chi(n)\chi(n+h)\psi_r(n)\psi_{r'}(n+h)
=\frac{Hc_5(h)}5\kappa(r,r';h)
+O_{r,r',h}((1+\log Z_*)^{\omega(r)+\omega(r')}),
\tag{M22}
$$

where $x\ge\max(0,-h)$, $H\ge0$, now
$Z_*=\max(2,x+H,x+H+h)$, and

$$
c_5(h)=\begin{cases}4,&5\mid h,\\-1,&5\nmid h,\end{cases}
\qquad
\kappa(r,r';h)=
\prod_{\substack{p\mid rr'\\p\nmid(r,r')}}\frac p{p+1}
\prod_{p\mid(r,r')}\frac{p-p^{-v_p(h)}}{p+1}>0.
\tag{M23}
$$

The proof uses divisor expansion and compatible congruences, with
complete control of the convergent main series. In complete regions,
multiplication by $f(r)f(r')$ gives the corresponding correlation
of actual numerator coefficients. The error is not uniform as r,r',h
grow with Y. Such fixed-parameter correlations cannot simply be summed
to establish the full moment.

### The full same-core sector

Write $\mathcal P=\sum_r\mathcal P_r$ according to the squarefree
numerator core r. The following bounds are uniform in all finite M,K:

$$
\begin{split}
E_J&:=\sum_\lambda c_\lambda^2
\ll_{\sigma,\eta}Y^{1-2\sigma}(1+\log Y)^{1+\eta},
\qquad \mathcal P(t)=\sum_\lambda c_\lambda\lambda^{-it},\\
0\le\sum_r\mathscr F_T(\mathcal P_r)
&\ll_{\sigma,\epsilon}Y^{1-2\sigma}(1+\log Y)T^\epsilon.
\end{split}
\tag{M24}
$$

Here equal rational frequencies are combined before squaring in $E_J$,
and $\eta>0$ is arbitrary. The second line includes all signed pairs
with the same core, not merely identical integer numerators. It is not
an absolute estimate for each of those pairs separately.

Let $E_r$ be the coalesced frequency diagonal inside $\mathcal P_r$.
The disjoint decomposition is exactly

$$
\mathscr F_T(\mathcal P)
=E_J+\sum_r[\mathscr F_T(\mathcal P_r)-E_r]
+\mathcal C_{\ne r,\ne\lambda}.
\tag{M25}
$$

Every equal-frequency collision, including collisions between different
cores, belongs to $E_J$. The remaining ordered pair sum
$\mathcal C_{\ne r,\ne\lambda}$ contains both different cores
and different rational frequencies. The arithmetic appendix proves (M24),
the corresponding bound for $\sum_rE_r$, and therefore

$$
\mathscr F_T(\mathcal P)
=\mathcal C_{\ne r,\ne\lambda}
+O_{\sigma,\epsilon}(Y^{1-2\sigma}T^\epsilon),\qquad Y=T^2.
\tag{M26}
$$

The error is below $\mathcal N^2$ by a factor T apart from small
power losses. This is a reduction to different cores, with the diagonal
intersection subtracted exactly.

## 4. Actual large prime families and their signed balance

For $Y\ge10^{12}$, take split primes $Y/2<p\le Y$ and
denominators $M/2+2<a<M-2$ with $\chi(a)=1$. Since p>M,
and any nontrivial multiple of a exceeds M, the full coalesced
coefficient at p/a is exactly

$$
c_{p/a}=-2p^{-\sigma}a^{\sigma-1}.
\tag{M27}
$$

There are no hidden representations in this coefficient. Pair frequencies
with distinct primes in the same logarithmic bin of length $1/(20T)$,
including both orientations. Their positive contribution obeys

$$
\mathcal P_+\ge
\frac{Y^{2-2\sigma}M^{2\sigma}}{37120\,T\log^2Y}
\gg_\sigma\mathcal N^2\frac{T^{2\sigma}}{\log^2Y}.
\tag{M28}
$$

The count uses a published explicit prime bound on $(Y/2,Y]$, not
a prime estimate on the much shorter frequency intervals. Cauchy–Schwarz
counts occupied bins and removes all same-prime pairs. For fixed p,p'
and determinant $h=pa'-p'a$, each remaining sum has at most one
point, because its integer steps p,p' exceed M. An absolute estimate of
all these individual short sums already exceeds the target.

### An explicit negative quartet

Restrict the base denominators further to $a,a'\equiv1\pmod5$
with $M/2+4<a,a'<M-4$, and orient p<p'. Replacing the second
denominator by $a',a'+1,a'+2,a'+3$ yields four disjoint actual
families with signs $+,-,-,+$. If $P_0>0$ denotes the base
contribution and Q the signed sum of all four, then

$$
P_0\ge\frac{Y^{2-2\sigma}M^{2\sigma}}{148480\,T\log^2Y},
\qquad Q\le-\frac{T^2}{10M^2}P_0<0.
\tag{M29}
$$

The proof retains the full amplitude, not only the character signs.
For $C=p'a/p$, $\alpha=\sigma-1$, define
$F(x)=x^\alpha\mathcal L_T(\log(C/x))$. Throughout the quartet
$T|\log(C/x)|<1/5$, and its contribution is a positive factor
times $F(a')-F(a'+1)-F(a'+2)+F(a'+3)$. The function is strictly
concave there. Its derivative also has a negative jump at x=C, so the
sign remains valid when the quartet crosses the central cusp. The
appendix proves the measure inequality
$dF'\le-(T^2/10)x^{\alpha-2}dx$, from which (M29) follows.

### Why this negative family cannot simply be discarded

At the fixed cutoff $M=\lceil40T\rceil$, (M29) implies
$-Q\gg\mathcal N^2T^{2\sigma}/\log^2Y$. Let
$R_Q=\mathscr F_T(\mathcal P)-Q$ be its complete complementary
pair sum, including the diagonal. Positivity of the full integral gives

$$
R_Q=\mathscr F_T(\mathcal P)+|Q|
\ge|Q|\gg_\sigma\mathcal N^2\frac{T^{2\sigma}}{\log^2Y}.
\tag{M30}
$$

Thus the valid inequality $\mathscr F_T(\mathcal P)\le R_Q$
cannot yield the target through a target-sized bound for $R_Q$:
that proposed bound is false for every fixed epsilon smaller than
$2\sigma$. The negative family must remain coupled to compensating
positive terms. This does not disprove the target for the complete form.

## 5. The proved whole-moment bound and the quantitative gap

For the following improved bound restrict to fixed
$1/4<\sigma<0.26$, and put

$$
\nu_\sigma=
\frac{2860\sigma-169}{9578}
+\frac{1261-2860\sigma}{3528}.
\tag{M31}
$$

Then $0<\nu_\sigma<\sigma$, $2\nu_\sigma<1$, and

$$
\boxed{
\mathscr F_T(\mathcal P)\ll_{\sigma,\epsilon}
\mathcal N^2T^{2\nu_\sigma+\epsilon},\qquad
r_Y(\sqrt Y)\ll_{\sigma,\epsilon}
Y^{1-3\sigma/2+\nu_\sigma/2+\epsilon}.}
\tag{M32}
$$

The argument processes Bourgain's exponent pair by the A-process and
convexity, checks the actual logarithmic phases in each residue class,
and combines the resulting uniform pointwise bounds for A,B with the
unweighted second moment of S. The proof integrates the entire Fejér
weight; its distant-time annuli converge because $2\nu_\sigma<1$.
It does not identify a time mean with a torus mean. The precise primary
inputs, parameter restrictions, and all finite-cutoff estimates are in
[Analysis](ANALYTIC.md).

Combining (M26), (M28), and (M32) gives actual compensation within the
different-core sector:

$$
\frac{\mathcal C_{\ne r,\ne\lambda}-\mathcal P_+}{\mathcal P_+}
=-1+O_{\sigma,\epsilon}
\left(T^{-2(\sigma-\nu_\sigma)+\epsilon}\log^2Y\right).
\tag{M33}
$$

This is unconditional. The complement is an exact set of terms from the
same finite expansion; it is not a random-sign model. The estimate
does not identify one adjacent-denominator companion as responsible
for all the compensation. For the negative quartet, similarly,

$$
0\le\frac{R_Q}{-Q}-1
\ll_{\sigma,\epsilon}T^{-2(\sigma-\nu_\sigma)+\epsilon}\log^2Y.
\tag{M34}
$$

The positive complement almost balances that large negative sum, with
a proved relative power saving. Both statements retain more cancellation
than an absolute estimate of separate families would permit.

At $\sigma=51/200=0.255$,
$\nu_\sigma=7069361/33791184$. The exponents below are decimal
representations of these exact rational expressions, not measured values:

| Quantity | Proved upper scale | Target or consequence of the Fejér target |
|---|---|---|
| Analytic tail $r_Y(\sqrt Y)$ | $Y^{0.722103629\ldots+\epsilon}$ | $Y^{0.6175+\epsilon}$ |
| $\mathscr F_T(\mathcal P)/\mathcal N^2$ | $T^{0.418414516\ldots+\epsilon}$ | $T^\epsilon$ |
| Relative error in (M33) | $T^{-0.091585484\ldots+\epsilon}\log^2Y$ | the Fejér target would imply $T^{-0.51+\epsilon}\log^2Y$ |

The remaining excess in the analytic norm is
$Y^{\nu_\sigma/2}=Y^{0.104603629\ldots}$. The final row concerns
the stronger Fejér target (M18); it is not inferred merely from the
sharp-time condition in (M15).

## 6. The remaining joint estimate

The long auxiliary v-sum can be removed from a sufficient formulation.
For squarefree split k set

$$
F_U^{(k)}(s)=\sum_{\substack{r\le U,\ r\in\mathcal R\\(r,k)=1}}
f(r)r^{-s}.
\tag{M35}
$$

Grouping the absolutely convergent geometric expansion in (M10) by
$k=\operatorname{rad}(v)$ gives the finite identity

$$
T_Y(s)=\sum_{\substack{k\le Y\\k\in\mathcal R}}
\frac{2^{\omega(k)}k^{-3s}}{\prod_{p\mid k}(1+p^{-2s})}
F_{Y/k}^{(k)}(s),\qquad \Re s>0.
\tag{M36}
$$

For a fixed $1/(4\sigma)<\kappa<1$, the part with
$k>T^\kappa$ contributes less than $\mathcal N$ in the
relevant second norm. The proof chooses $\beta<2\sigma$ with
$\kappa\beta>1/2$, retains the convergent radical weight, and
uses the uniform fourth moments of A,B. Consequently the following
uniform family of estimates would suffice for the analytic target:

$$
\boxed{
\|A_MB_MF_{Y/k}^{(k)}\|_{2,T}
\ \stackrel{?}{\ll}_{\sigma,\epsilon}
(Y/k)^{1-\sigma}T^{-1/2+\epsilon},
\qquad k\in\mathcal R,\quad k\le T^\kappa.}
\tag{M37}
$$

Its constant must be independent of k. The surviving lengths satisfy
$Y/k\ge T^{2-\kappa}>T$, and the coprime condition and the
time weight $|A_MB_M|^2$ remain essential. This is a sufficient
reduction, not a proof or an asserted equivalence of (M37).

There is a quantified limit to combining the existing separate inputs.
On the improved strip write $a_\sigma=(2860\sigma-169)/9578$,
$b_\sigma=(1261-2860\sigma)/3528$. Interpolating the fourth
moments and pointwise estimates of A,B, and the second and supremum
bounds of S, gives a norm loss

$$
\nu_\sigma+
\frac{1-4a_\sigma}{p_A}+
\frac{1-4b_\sigma}{p_B}\ge\nu_\sigma,
\qquad p_A,p_B\ge4.
\tag{M38}
$$

Thus retuning Hölder exponents in this specified family does not improve
the bound already used. This is a limit of these inputs, not a lower
bound for the actual moment or an exclusion of other methods.

The outstanding question is joint cancellation between the squarefree
support coefficients and both character factors. It can be addressed by
(M37), or by a direct upper bound for the complete signed form in (M26).
The fixed-core asymptotic (M22), the negative quartet alone, and unweighted
energy estimates do not supply that missing uniform estimate.

## 7. Scope relative to RH and TWIST-J

The connection to the integers is exact: augmentation of the refined
prime coefficients gives Möbius coefficients, and the support cutoff
gives (M9)–(M10). The new estimates nevertheless concern specified
finite forms and an intermediate analytic-tail norm. They do not prove
square-root cancellation of the unrestricted sum M(N), an RH-strength
augmentation transfer, or a zero-free statement for $L(s,\chi_5)$.
Neither ordinary RH nor character RH is a premise of the results proved
in this package.

The scope is one mathematical route inside the wider research program.
Earlier exploratory source statistics and other RH approaches are not
used as unstated premises. There is no physical interpretation, numerical
measurement, or promotion of the repository's open augmentation claim.
The useful outcome is a precise map of which signed sectors are already
controlled, which large families must remain coupled, and which joint
moment is still required.

# Exact carry moments for two integer digit alphabets

Date: 2026-10-29. **NON-CANONICAL. Analytical continuation prepared for review.**
This document assigns no Canon status and changes no registered claim.

The previously supplied carry calculation and its stored numerical outputs
were known before this argument was written. The new content is the complete
small-depth residue argument, an explicit finite-length formula that does not
take mixed moments from a dynamic program, and an exact rational bound on its
limit error. No mathematical experiment was executed while preparing this
proof. Any subsequent execution record belongs to its own frozen audit.

## 1. Objects and scope

Fix a primitive fifth root of unity `zeta`, put

\[
K=\mathbb Q(\zeta),\qquad O=\mathbb Z[\zeta],\qquad
\lambda=1-\zeta,
\]

and let the bar denote complex conjugation. Write

\[
\phi=1+\zeta+\zeta^{-1},\qquad
J=1+\zeta^2=\zeta\phi^{-1}.
\]

In the principal embedding `zeta = exp(2 pi i/5)`, `phi` is the positive root
of `phi^2 = phi + 1`. Both `phi` and `J` are units. In particular,

\[
J^{-1}=-\zeta-\zeta^2.
\]

The residue map `res: O -> F_5` sends `zeta` to 1. Thus
`res(c_0 + c_1 zeta + c_2 zeta^2 + c_3 zeta^3)` is the sum of the four
coefficients modulo 5. The ideal `(lambda)` has residue field `F_5`, and

\[
5O=\lambda^4 O.
\tag{1}
\]

For the arguments below it suffices that `5` belongs to `(lambda^4)` and
has exact lambda-adic valuation 4. One direct proof is
`5 = product_{k=1}^4 (1-zeta^k)`. Each factor is `lambda` times an integral
element with nonzero residue `k`. The factor and lambda both have norm 5,
so their integral quotient has norm one and is a unit. Each factor has
valuation one and the remaining product is a unit. All divisions by powers
of lambda used below are in `K`, with
integrality justified at the point of use.

We use exactly two digit alphabets:

| Alphabet | Digits | Mean `mu` | Variance |
| --- | --- | ---: | ---: |
| counting | `D_0 = {0,1,2,3,4}` | 2 | 2 |
| balanced | `D_2 = {-2,-1,0,1,2}` | 0 | 2 |

For either alphabet `D`, let `rep_D(r)` be its unique representative of
`r in F_5`. Fix a unit `u in O`, supply independent uniform input digits
`b_i in D`, and define

\[
C_0=0,\qquad
a_i=\operatorname{rep}_D(\operatorname{res}(C_i+u b_i)),\qquad
C_{i+1}=\frac{C_i+u b_i-a_i}{\lambda}.
\tag{2}
\]

Equation (2) defines integral carries. It gives the exact identity

\[
u\sum_{i=0}^{N-1}b_i\lambda^i
=\sum_{i=0}^{N-1}a_i\lambda^i+\lambda^N C_N.
\tag{3}
\]

Here `N` is the length of the supplied word. No identification with physical
time or the native checkpoint counter is made.

Define the nonnegative rational quadratic reading

\[
Q(x)=\operatorname{Tr}_{K/\mathbb Q}(x\bar x)
=\sum_{\sigma:K\hookrightarrow\mathbb C}|\sigma(x)|^2.
\tag{4}
\]

For integral `x`, `Q(x)` is a nonnegative integer. The word measure in (2)
is an explicit premise. `Q(C_N)` is a quadratic reading of carry memory;
no physical energy, work, dissipation or gate-cost identification is assumed.

## 2. Prefix permutations and mixed moments

Let `s` be any integer representative of `res(u)`. Since `u` is a unit,
`s` is nonzero modulo 5. At every step, after the input prefix before `i`
has fixed `C_i`, the map

\[
b_i\longmapsto
\operatorname{rep}_D(\operatorname{res}C_i+s b_i)
\]

is a permutation of `D`. Therefore the input-to-output map is a bijection
on every finite prefix `D^N`. Every output prefix is consequently uniform,
and the output digits, considered as a sequence, are independent uniform
digits of the same alphabet.

The inverse map is also causal. Given the output prefix through `i`, one
recovers the input digits sequentially using the inverse residue slope
`s^{-1}`. More explicitly, rearranging a step as

\[
u b_i+C_i=a_i+\lambda C_{i+1}
\]

shows that multiplication by `u^{-1}`, with input and output letters
interchanged, has carries

\[
\widetilde C_i=-u^{-1}C_i.
\tag{5}
\]

The starting carry is again zero. This proves the carry mirror identity for
each word and hence, under the supplied uniform word measure, for carry
distributions at each length.

Set

\[
d_i=u b_i-a_i,\qquad m_i=\mathbb E[b_i a_i].
\]

Both digits have mean `mu`, so `E[d_i] = mu(u-1)`. If `i > j`, the fresh
input `b_i` is independent of `a_j`, which is a function of an earlier input
prefix. If `i < j`, causal inversion makes `b_i` a function of the output
prefix through `i`; it is therefore independent of the later output digit
`a_j`. Consequently,

\[
\mathbb E[b_i a_j]=\mu^2\qquad(i\ne j).
\tag{6}
\]

Together with the independence of distinct digits within each word, (6)
implies the exact field-valued covariance identity

\[
\mathbb E\big[(d_i-\mu(u-1))
\overline{(d_j-\mu(u-1))}\big]=0
\qquad(i\ne j).
\tag{7}
\]

The same statement holds after every embedding of `K`. The diagonal
centered second moment is

\[
\mathbb E\big[(d_i-\mu(u-1))
\overline{(d_i-\mu(u-1))}\big]
=2(u\bar u+1)+(\mu^2-m_i)(u+\bar u).
\tag{8}
\]

Indeed, `E[b_i^2] = E[a_i^2] = mu^2+2`; expanding the product and subtracting
the squared mean gives (8). The prefix argument, rather than an assumption
that input and output words are jointly independent, is what proves (7).

## 3. Small-depth residue theorem

Choose `s = rep_D(res(u))` and suppose

\[
u=s+\lambda^h T,\qquad
h\in\{1,2,3\},\qquad
t=\operatorname{res}T\ne0.
\tag{9}
\]

Equivalently, `h = v_lambda(u-s)` lies between 1 and 3. Choosing a different
integer representative of `res(u)` changes `u-s` by a multiple of 5. By (1),
this does not alter an `h` in this range. Membership in the class (9), and
its `h`, are thus the same for the two alphabets.

**Theorem.** For a transducer (2) satisfying (9):

1. `a_i = rep_D(s b_i)` for `0 <= i < h`.
2. `res(C_i)` is uniform on `F_5` for every `i >= h`.
3. If

   \[
   M_D(s)=\frac15\sum_{b\in D}b\,\operatorname{rep}_D(s b),
   \tag{10}
   \]

   then

   \[
   m_i=\begin{cases}
   M_D(s),&0\le i<h,\\
   \mu^2,&i\ge h.
   \end{cases}
   \tag{11}
   \]

**Proof.** Start a block at any index `n` and expand its starting carry modulo
`lambda^h` in integer digits of `D`:

\[
C_n=\sum_{j=0}^{h-1}c_j\lambda^j+\lambda^h E,
\qquad c_j\in D,\quad E\in O.
\tag{12}
\]

These digits are fixed by the input before the block. At each of its `h`
positions the output is

\[
a_{n+j}=\operatorname{rep}_D(c_j+s b_{n+j})
\qquad(0\le j<h).
\tag{13}
\]

To verify (13), proceed through the block. The difference between
`c_j+s b_{n+j}` and its representative is an integer multiple of 5. A
rounding error created at position `j` can be divided by at most `h-j`
powers of lambda within the block. Its remaining valuation is at least
`4-(h-j) >= 1`, so it cannot affect the residues used at any later position
of this block. Likewise, the term `lambda^h T b_{n+j}` first reaches residue
order after `h` divisions, after every output position in the block. The
fixed lower coefficients in (12) are therefore exactly the residues
appearing in (13).

Using (13) in the `h`-step form of (2) gives

\[
\begin{split}
C_{n+h}
={}&E+T\sum_{j=0}^{h-1}b_{n+j}\lambda^j\\
&+\sum_{j=0}^{h-1}
 (c_j+s b_{n+j}-a_{n+j})\lambda^{j-h}.
\end{split}
\tag{14}
\]

Every summand on the last line belongs to `lambda O`: its integer numerator
is a multiple of 5, and its valuation is at least `4+j-h >= 1`. Reducing
(14) modulo lambda therefore yields the simple identity

\[
\operatorname{res}C_{n+h}=\operatorname{res}E+t b_n.
\tag{15}
\]

Conditionally on the entire input before `n`, and even on the other `h-1`
input digits of this block, `b_n` is still uniform. Since `t != 0`, (15) is
uniform on `F_5`. Taking `n=i-h` proves the second statement for every
`i >= h`. At `n=0`, all digits `c_j` in (12) are zero, which proves the first
statement. Finally, `b_i` is fresh and independent of `C_i`. For `i >= h`,
the pair `(res(C_i),b_i)` is uniform on `F_5^2`, so the pair `(a_i,b_i)` is
uniform on `D^2`. Hence `m_i=mu^2`. The first statement gives (10) for the
earlier positions. This proves (11). QED.

The restriction `h < 4` is essential to this proof: at four divisions a
multiple of 5 can contribute to the residue. No version of (11) for
`h >= 4` is inferred here.

The values in (10) depend only on the residue of `s`:

| `s mod 5` | 1 | 2 | 3 | 4 |
| --- | ---: | ---: | ---: | ---: |
| `M_D0(s)` | 6 | 5 | 5 | 4 |
| `M_D2(s)` | 2 | 0 | 0 | -2 |

Each entry is the displayed sum of five integer products divided by five.

## 4. Which members of the stated unit family are admitted

Consider the explicit family

\[
u=\epsilon\zeta^k\phi^m,
\qquad\epsilon\in\{-1,1\},\quad0\le k<5,\quad m\in\mathbb Z.
\tag{16}
\]

The argument in this section classifies this stated family and does not
require a separate assertion that it exhausts every unit of `O`.

Expanding `phi = -zeta^2-zeta^3` at `zeta=1-lambda` gives the exact identity

\[
\phi=-2+5\lambda-4\lambda^2+\lambda^3.
\tag{17}
\]

Modulo `lambda^3`, the constant and quadratic coefficients of `phi^m` are,
in `F_5`, respectively

\[
3^m,\qquad m3^{m-1}.
\tag{18}
\]

For negative `m`, the same expansion is valid in the finite quotient:
the constant `-2` is invertible there, and the binomial identity with a
nilpotent quadratic term is valid for every integer power. Integer lifts
of coefficients in `F_5` give the same congruence, because a change by 5 has
valuation at least 4.

Also `zeta^k = (1-lambda)^k`. Thus the coefficient of lambda in `u` is
`-epsilon k 3^m modulo 5`. It is nonzero for `k != 0`, and in that case
`h=1`. If `k=0` and `5` does not divide `m`, the linear coefficient is zero
and the quadratic coefficient is `epsilon m3^{m-1} != 0`; then `h=2`.

If `k=0` and `5` divides `m`, expand (17) modulo `lambda^4`. Both the
quadratic and cubic coefficients of its power are proportional to `m`
modulo 5. They vanish, so `u` is congruent to an integer modulo `lambda^4`.
It is outside (9). The choices `u=1` and `u=-1` are included among these
excluded cases. Values of `v_lambda(u-s)` at or above four can depend on
which integer representative `s` was chosen; the exclusion itself cannot.

In particular, the real units `phi`, `phi^{-1}`, `-phi` and `-phi^{-1}`
all have `h=2`. Formula (11) for them is proved after two positions; their
mixed moments no longer need to be supplied by a dynamic program. The
explicit test unit `phi^5 = 3 + 5 phi` has `h=4` in either alphabet and is
a useful negative control for admission into (9).

## 5. Exact finite-length second moment

Put

\[
L=\lambda\bar\lambda,
\qquad S_N=\sum_{k=1}^{N}\lambda^{-k},
\qquad T_N=\sum_{k=1}^{N}L^{-k},
\]

and, for the `h` in (9), put

\[
W_{N,h}=\sum_{i=0}^{\min(h,N)-1}L^{-(N-i)}.
\]

All three sums are zero when `N=0`. For every unit satisfying (9), every
`N >= 0`, and either one of the stated alphabets,

\[
\begin{split}
\mathbb E[Q(C_N)]
={}&\mu^2\operatorname{Tr}
 \big((u-1)(\bar u-1)S_N\bar S_N\big)\\
&+2\operatorname{Tr}\big((u\bar u+1)T_N\big)\\
&+(\mu^2-M_D(s))
 \operatorname{Tr}\big((u+\bar u)W_{N,h}\big).
\end{split}
\tag{19}
\]

To prove it, unroll (2):

\[
C_N=\sum_{i=0}^{N-1}\lambda^{-(N-i)}d_i.
\tag{20}
\]

Its mean is `mu(u-1) S_N`. Identity (7) removes all distinct-position
covariances. Substitute (8) in the remaining diagonal terms, take the trace,
and use (11). This is exactly (19).

Every input on the right side is specified algebraically: `u`, the chosen
alphabet, its mean, `s`, `h`, and the five-term sum (10). No empirical or
dynamic-program value of `m_i` occurs in (19). The identity is therefore
suited to a comparison with an independently enumerated finite distribution.

## 6. Limit of the mean quadratic reading

The elementary field identities needed for the limit are

\[
\lambda-1=-\zeta,
\qquad L=3-\phi=1+J\bar J,
\qquad Q(J^{-1})=6.
\tag{21}
\]

Indeed, `L = 2-zeta-zeta^{-1} = 3-phi`, while
`J conj(J) = phi^{-2} = 2-phi`. Also
`J^{-1} conj(J^{-1}) = phi^2 = 1+phi` and `Tr(phi)=2`, giving
`Q(J^{-1})=6`.

The four embeddings occur in two conjugate pairs. The squared moduli of
their values of lambda are

\[
\frac{5-\sqrt5}{2},\qquad \frac{5+\sqrt5}{2},
\]

both greater than one. Thus

\[
S_N\longrightarrow\frac1{\lambda-1},\qquad
T_N\longrightarrow\frac1{L-1},\qquad W_{N,h}\longrightarrow0
\]

at every embedding. Since `lambda-1` has modulus one at every embedding,
(19) gives

\[
\begin{split}
Q_{\infty,D}(u)
&:=\lim_{N\to\infty}\mathbb E[Q(C_N)]\\
&=\mu^2 Q(u-1)+2\operatorname{Tr}
 \frac{u\bar u+1}{J\bar J}\\
&=\mu^2 Q(u-1)+2Q(u/J)+12.
\end{split}
\tag{22}
\]

This proves convergence of the stated mean. It does not require, and does
not by itself prove, convergence of the entire carry distribution. The
sampling of words remains the stipulated independent uniform measure.

## 7. Exact rational bound on the finite-length error

Let `r=40/47`. At every embedding,

\[
|\sigma(\lambda)|>47/40,
\qquad |\sigma(\lambda)|^{-1}<r.
\tag{23}
\]

There is no decimal approximation in this bound. For the smaller squared
modulus, `(5-sqrt(5))/2 > (47/40)^2` is equivalent to
`1791 > 800 sqrt(5)`; squaring the positive sides gives
`3207681 > 3200000`.

For every `N >= h`, define the nonnegative rational number

\[
\begin{split}
B_{D,N}(u)={}&
\mu^2 Q(u-1)(2r^N+r^{2N})\\
&+(2Q(u/J)+12)r^{2N}\\
&+|\mu^2-M_D(s)|(Q(u)+4)
 \sum_{i=0}^{h-1}r^{2(N-i)}.
\end{split}
\tag{24}
\]

Then

\[
\left|\mathbb E[Q(C_N)]-Q_{\infty,D}(u)\right|
\le B_{D,N}(u).
\tag{25}
\]

For the first line of (19), use
`S_N=(1-lambda^{-N})/(lambda-1)` and
`abs(|1-z|^2-1) <= 2|z|+|z|^2`. At each embedding this bounds its deviation
from the first term in (22) by the corresponding summand of the first line
of (24).

For the second line, the exact remainder is
`T_N - 1/(L-1) = -L^{-N}/(L-1)`. Each embedded coefficient
`(|sigma(u)|^2+1)/(sigma(L)-1)` is positive. Bound `sigma(L)^{-N}` by
`r^{2N}` and sum, obtaining the second line of (24) by (21).

Finally,

\[
|\sigma(u+\bar u)|\le2|\sigma(u)|
\le|\sigma(u)|^2+1.
\]

Apply this to every summand of `W_{N,h}`, bound its power of `sigma(L)^{-1}`
using (23), and sum over the four embeddings. This gives the last line of
(24). The triangle inequality completes (25). Each term tends to zero.
The same reasoning supplies a bound for `N<h` if the upper index `h-1` in
(24) is replaced by `min(h,N)-1`; the stated audit bound needs only `N>=h`.

## 8. A trace inequality and its equality cases

For every nonzero algebraic integer `v in O`,

\[
Q(v)\ge4.
\tag{26}
\]

Indeed, AM-GM applied to the four positive numbers `|sigma(v)|^2` gives

\[
Q(v)\ge4|N_{K/\mathbb Q}(v)|^{1/2}\ge4,
\]

because the nonzero norm is an integer. Equality holds exactly when all four
embedded moduli are one. An algebraic integer with this property is a root
of unity: the monic integer polynomials whose roots are the conjugates of
its positive powers have bounded degree and bounded coefficients. There
are finitely many such polynomials and finitely many roots among them. Two
positive powers must therefore be equal.

The roots of unity in `K` are precisely

\[
\mu_{10}=\{\epsilon\zeta^k:
 \epsilon\in\{-1,1\},\ 0\le k<5\}.
\tag{27}
\]

For completeness, `K` is cyclic of degree four, with automorphisms
`zeta -> zeta^a`, `a in F_5^*`, and its unique quadratic subfield is the
real field `Q(sqrt(5))`. If a primitive root of order `m` belongs to `K`,
its degree `varphi(m)` divides four. The possible orders are
`1,2,3,4,5,6,8,10,12`; orders `3,4,6,8,12` contain the imaginary quadratic
field `Q(sqrt(-3))` or `Q(i)` and are excluded. The remaining orders give
exactly (27).

## 9. Sharp minima in the proved class

Let `H` denote the class of units satisfying (9), for either alphabet. It
excludes `u=1` and `u=-1`.

### Counting alphabet

For every `u in H`, (22) and (26) give

\[
Q_{\infty,D_0}(u)=4Q(u-1)+2Q(u/J)+12\ge36.
\tag{28}
\]

Both terms to which (26) is applied are nonzero algebraic integers: `u-1`
is nonzero, and `u/J` is a unit. Equality in (28) forces, at the principal
embedding,

\[
|u|^2=|J|^2=2-\phi,\qquad |u-1|^2=1.
\tag{29}
\]

These two circles have exactly two intersections. They are `J` and
`bar(J)`, since `J-1=zeta^2` and `bar(J)-1=zeta^3`. Both lie in `H`, both
have `Q(u-1)=4` and `Q(u/J)=4`, and both attain 36. Thus the equality set
is exactly

\[
u\in\{J,\bar J\}.
\tag{30}
\]

### Balanced alphabet

For every `u in H`, the mean term vanishes and

\[
Q_{\infty,D_2}(u)=2Q(u/J)+12\ge20.
\tag{31}
\]

By (26)-(27), equality is equivalent to `u/J in mu_10`. Thus all and only
the ten minimizers are

\[
u=\epsilon\zeta^k\phi^{-1},
\qquad\epsilon\in\{-1,1\},\quad0\le k<5.
\tag{32}
\]

Every unit in (32) lies in `H`. The eight with `k != 0` have `h=1`; the
two real units `phi^{-1}` and `-phi^{-1}` have `h=2`, as proved in section 4.
This additional two-position argument is what permits the two real members
to be included in the theorem about the actual carry process. A proof
restricted to the earlier first-order condition `res((u-s)/lambda) != 0`
would include only the eight nonreal members.

### Why the scope cannot be omitted

For the balanced alphabet and `u=1` or `u=-1`, every output `a_i=u b_i`
already belongs to the alphabet. Induction in (2) gives

\[
C_i=0\quad\hbox{for every }i.
\tag{33}
\]

Consequently the unrestricted assertion that all units have actual balanced
limiting mean at least 20 is false. These excluded units have limiting mean
zero. The algebraic functional `2Q(u/J)+12` equals 24 at either of them;
it is not their actual limiting mean. Equations (22), (28) and (31) are
claims about the process on `H`. A finite comparison over a list of units
does not enlarge that class.

## 10. Relation to word statistics and reversible implementation

Equation (3) and the prefix permutation show that every unit maps the same
uniform input-word law to the same uniform output-word law. Therefore a
statistic depending only on the output word, including a zero sum of fifth
roots assigned to its letters, retains its uniform-word distribution. The
carry distribution and its reading (4) can nevertheless depend on `u` and
on the selected integer representatives.

The mathematical selection in (28) is therefore a minimum of the specified
internal carry moment, conditional on the digit convention and supplied
uniform measure. The comparison of the two alphabets is exact for these two
alphabets, which have the same variance 2. It establishes no invariance under
arbitrary systems of residue representatives.

The carry mirror (5) is preserved. Under that mirror, an embedded squared
modulus is multiplied by `|sigma(u)|^{-2}`. Different forward and inverse
quadratic readings are compatible with a reversible algorithm. They do not
by themselves quantify work or dissipation, and two algorithms separately
initialized with zero carry are not a comparison of a complete physical
history with its temporal reverse.

A reversible circuit can compute the carry and subsequently uncompute its
temporary storage. This document neither derives the physical word source
nor identifies (4) with a Hamiltonian, a conserved account, or pulse cost.
Those are separate carrier, preparation and reading questions. The stated
word measure, digit convention, unit class and quadratic reading remain
explicit throughout this result.

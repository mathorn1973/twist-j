# A complete Lucas menu for four signed units

**NON-CANONICAL. NO AUTHORITY. L1 arithmetic. Candidate-D.**

This is a paper deduction under the continuation of claim #2090. It uses the
signed-label kernel and full-multiplicity return identity in
`THREE_UNIT_OBSTRUCTION.md` of PR #2092, at source commit
`0b81796c01d4bee47eceb6e451670ea0d233610b`. No new finite search enters the proof.

## Domain and statement

Let $m=5^k$, $k\ge1$, $h=5m$, and
\[
 A_\pm=5F_m^2\pm5F_m+1,\qquad M=A_-A_+.
\]
Put $B=\mathbb Z[\phi]$, $\phi^2=\phi+1$, and
$\mathcal O=\mathbb Z[j]=B\oplus jB$, where $j=\zeta_5$.
Conjugation on $B$ sends $\phi$ to $-\phi^{-1}$.
For a divisor $D$ of $M$ and an integral element $S$, write
\[
 g_D(S)=\gcd(D,\operatorname{cont}S),
\]
using the nonnegative coordinate content, with content zero for the zero
element. Coordinates may be taken in any integral basis.

Define the factor-independent menu
\[
 \mathcal L_h=
 \{L_a+\epsilon L_b:
  0\le a<2h,\ a\text{ even},\quad
  0\le b<2h,\ b\text{ odd},\quad \epsilon=\pm1\}.
 \tag{1}
\]
It has $2h^2=50m^2$ labelled entries; duplicate integer or residue values
are retained. Each entry is a sum of four signed real units.

**Theorem.** For any sum $S$ of at most four signed real units
$\pm\phi^e$, there are at most two entries $T_i$ from (1) such that,
simultaneously for every divisor $D\mid M$,
\[
                 g_D(S)=\gcd(D,T_1,T_2).                    \tag{2}
\]
Either or both entries may be omitted; an empty list means $D$.
For any sum of at most four signed quartic units $\pm j^c\phi^e$,
the same assertion holds with at most four menu entries.

The choice of entries is made by signed exponent arithmetic modulo $2h$,
without factoring $M$ or $D$. Equation (2) preserves every prime-power
multiplicity. In particular, two distinct primes dividing $M$ can be
separated by some four-unit whole-ideal test if and only if some entry
of (1) separates them. The same equivalence holds inside either side
$A_-$ or $A_+$.

This is a completeness result for a specified weight. It does not assert
that the menu separates every prime pair, or that a universal weight exists.

## 1. Common labels and units of differences

The source proof gives the following exact facts.

* Every prime $p\mid M$ exceeds five, splits in $B$, and gives
  $B/pB\cong\mathbb F_p\times\mathbb F_p$.
* $\phi$ has order $2h$ in $B/pB$; the $4h$ signed labels
  $\epsilon\phi^e$, with $\epsilon=\pm1$ and $e$ modulo $2h$, are distinct.
  Equality of labels at any one such prime is consequently equality of
  their signs and exponent classes, independent of the prime.
* $\phi^{2h}=1$ modulo $MB$, including all multiplicities.
* The quadratic norm of a signed real unit is $(-1)^e$.

Two signed units of the same norm and different signed labels have a
difference which is a unit in $B/MB$. Indeed, in one split component they
have values $x,y$ and in the other values $s/x,s/y$, with the same
$s\in\{1,-1\}$. Equality in either component forces equality in both,
which the common signed-label kernel excludes at every $p\mid M$.
Thus the difference is nonzero in each residue component at every such
prime and is a unit modulo every prime power dividing $M$.

The same observation applies to a sum of two same-norm units: it is either
zero modulo $M$ because the labels are negatives, or a unit modulo $M$.

For at most three summands the source proof already gives $g_M(S)\in\{1,M\}$.
Its two-label cancellation rule and six normalized three-label solutions
decide which alternative holds by the same signed exponent arithmetic.
The empty sum is zero and uses the whole-divisor alternative.
The value one can be represented in (2) by the menu entry $L_0-L_1=1$;
the value $M$ uses the empty list. It remains to treat four summands.

## 2. Four equal norms give only universal cancellations

Suppose $S=u_1+u_2+u_3+u_4$ and all four norms are equal to $s$.
If $S=0$ modulo a prime $p\mid M$, let $x_i$ be the first split coordinates.
Then
\[
             \sum_i x_i=0,\qquad \sum_i x_i^{-1}=0.
\]
All $x_i$ are nonzero. Their first and third elementary symmetric
functions vanish, so the monic polynomial with roots $x_1,x_2,x_3,x_4$
is even. Its roots, with multiplicity, pair as $x,-x$.
The equal norms make the corresponding whole units negatives, not merely
opposites in one component. The common label kernel promotes each pairing
to an equality modulo $M$. Consequently $S=0$ modulo $M$.

Therefore a sum of this norm type has gcd either one or $M$.
The choice is determined without factoring: check the finite signed labels
for a partition into opposite pairs. If such a partition exists the gcd
is $M$; otherwise no prime divisor of $M$ can divide the content.

## 3. The two-plus, two-minus norm case is one menu entry

Write
\[
 S=u_1+u_2+v_1+v_2,
 \qquad N(u_1)=N(u_2)=1,\quad N(v_1)=N(v_2)=-1.
\]
Put $U=u_1u_2$, $V=v_1v_2$ and $Z=u_1+u_2$.
If $Z=0$ modulo $M$, then either $v_1+v_2=0$ modulo $M$ as well,
or that remaining pair is a unit modulo $M$. This gives the two trivial
gcds. Otherwise $Z$ is a unit modulo $M$ by Section 1.

At a prime where $S=0$, conjugation gives
\[
 0=\overline S=Z/U-(v_1+v_2)/V=Z(1/U+1/V).
\]
Hence $U=-V$ there. The common signed-label kernel forces
$U=-V$ modulo all of $M$. If this label identity fails, the gcd is one.
It is checked by signs and exponent classes alone.

Assume the identity holds. Write
\[
 u_i=\epsilon_i\phi^{a_i},\qquad
 v_i=\delta_i\phi^{b_i},
\]
with $a_i$ even, $b_i$ odd. Then
\[
 \epsilon_1\epsilon_2=-\delta_1\delta_2,
 \qquad a_1+a_2\equiv b_1+b_2\pmod{2h}.
\]
Changing $b_2$ by a multiple of $2h$ makes the exponent sums exactly equal
without changing residues modulo $M$. Put
\[
 c=(a_1+a_2)/2=(b_1+b_2)/2,
 \quad r=a_1-c,\quad t=b_1-c,
 \quad \eta=\epsilon_1\epsilon_2,\quad \kappa=\epsilon_1\delta_1.
\]
The indices $r,t$ have opposite parity. Multiplication by a signed unit
reduces $S$, modulo $M$, to
\[
 E=\phi^r+\eta\phi^{-r}
       +\kappa(\phi^t-\eta\phi^{-t}).                    \tag{3}
\]
If $\eta=(-1)^r$, equation (3) is $L_r+\kappa L_t$.
Otherwise multiply by the unit $\phi^h$. Since $h$ is odd and
$\phi^{2h}=1$ modulo $M$,
\[
 \phi^h\big(\phi^n-(-1)^n\phi^{-n}\big)
             =L_{n+h}\pmod{MB}.
 \tag{4}
\]
Thus (3) becomes $L_{r+h}+\kappa L_{t+h}$, again at opposite parities.
This explicitly includes the branch sometimes written
$\sqrt5(F_r+\kappa F_t)$.

Finally $L_{n+2h}=L_n$ modulo $M$, so reduce both indices to
$[0,2h)$, and exchange them if necessary, multiplying by a scalar sign.
The resulting expression belongs to (1). Every multiplier used is a unit
modulo $M$. Hence $g_D(S)=\gcd(D,T)$ for every $D\mid M$, with full
multiplicity.

## 4. The three-plus, one-minus case is two such tests

When three units have one norm and the fourth has the opposite norm,
divide the equation by the negative of the exceptional unit. The normalized
expression is
\[
                       E=x+y+z-1,
             \qquad N(x)=N(y)=N(z)=-1.                    \tag{5}
\]
The normalization preserves all content gcds against divisors of $M$.
If all three labels are equal, a vanishing equation at $p\mid M$ would give
$3x=1$. Taking norms would give $-9=1$ modulo $p$, so $p\mid10$,
which is excluded. This case has gcd one.

Otherwise choose distinct labels $x,y$, permuting the three summands if
necessary. Define four-unit expressions
\[
 T_x=yz-x+yz/x+1,
 \qquad T_y=xz-y+xz/y+1.                                \tag{6}
\]
Each has two norm-one summands and two norm-minus-one summands. All the
division symbols denote multiplication by existing signed units.
Because $\bar x=-x^{-1}$ and likewise for $y,z$, the following are exact
identities in $B$, not numerical observations:
\[
 T_x=-E-yz\bar E,
 \qquad T_y=-E-xz\bar E,
 \qquad T_x-T_y=z(x-y)\bar E.                            \tag{7}
\]
The factor $z(x-y)$ is a unit modulo $M$ by Section 1.
It follows for every $D\mid M$ that
\[
       E=0\pmod{DB}
       \quad\Longleftrightarrow\quad
       T_x=T_y=0\pmod{DB}.                              \tag{8}
\]
The forward direction uses conjugation stability of $DB$; the reverse
direction first obtains $\bar E=0$ and then $E=0$ from (7).
Consequently
\[
 g_D(E)=\gcd\big(D,\operatorname{cont}T_x,
                         \operatorname{cont}T_y\big).   \tag{9}
\]
Apply Section 3 separately to (6). Each contributes either one menu
entry or a trivial flag; this proves (2). A trivial one flag uses
$L_0-L_1=1$, and a trivial whole flag is omitted. No more than two
entries are necessary.

## 5. Fifth-root phases and pair separation

In the basis $B\oplus jB$, the five powers of $j$ have coefficient pairs
\[
 (1,0),\quad(0,1),\quad(-1,\phi^{-1}),\quad
 (-\phi^{-1},-\phi^{-1}),\quad(\phi^{-1},-1).
\]
Each coordinate of one signed quartic unit is therefore either zero or
one signed real unit. A sum of at most four quartic units gives two real
coordinate sums, each of weight at most four. Whole divisibility is their
simultaneous divisibility, and contents satisfy
\[
 g_D(S_0+jS_1)=\gcd\big(g_D(S_0),g_D(S_1)\big).
\]
Applying (2) to both coordinates proves the at-most-four-entry assertion.

If a four-unit sum vanishes modulo a prime $p$ and not modulo another
$q$, every menu entry in its gcd representation vanishes modulo $p$
and at least one fails modulo $q$. That entry itself is a four-unit
separator. Conversely every entry of (1) is an admitted four-unit sum.
Thus identical zero flags for the complete finite menu are equivalent
to identical flags for all four-unit whole-ideal tests, even with
arbitrary exponents and fifth-root phases.

The menu can also be used with its full integer gcd outputs. Every
four-unit gcd lies in the family of intersections of at most four menu
outputs. This is an inclusion, not a claim that every such intersection
is itself realizable by one four-unit expression.

## 6. An exact reflected menu

The same separation information is obtained by the smaller prescribed menu
\[
 \mathcal R_h=
 \{L_a+\epsilon L_b:
   0\le a\le h-1,\ a\text{ even},\quad
   1\le b\le h-2,\ b\text{ odd},\quad\epsilon=\pm1\}.
 \tag{10}
\]
It has exactly $(h^2-1)/2$ labelled entries. This is a residue symmetry
reduction of (1), not a change to the domain of an already frozen audit.

Indeed, since $\phi^{2h}=1$ modulo $M$ and $2h$ is even,
\[
            L_{2h-n}=L_{-n}=(-1)^nL_n\pmod M.
\]
For the even indices, reflection leaves $L_n$ unchanged and fixes only
zero modulo $2h$, because $h$ is odd. The even representatives
$0,2,\ldots,h-1$ therefore suffice. For the odd indices reflection
changes the scalar sign, which the menu already permits. Its only fixed
index is $h$, and $L_h=0$ modulo $M$.

The entries with $b=h$ have gcd one against every divisor of $M$:
if $p\mid M$ divided $L_a$ for even $a$, then
$\phi^{2a}=-1$ in $B/pB$, contradicting the odd order $h$ of
$\phi^2$. Thus every omitted entry is either congruent up to a scalar
sign to a retained entry, or has the fixed gcd one.

There are $(h+1)/2$ even representatives and $(h-1)/2$ nonfixed odd
representatives, with two signs, giving $(h^2-1)/2$ entries as stated.
The constant entry $L_0-L_1=1$ is retained, so the exact gcd-meet theorem
also holds with entries from (10), with the same bounds of two and four.

## Consequence for the previous finite audit

At $m=25$, $h=125$, menu (1) is exactly the $31\,250$ comparisons frozen
and executed in PR #2092. The new paper theorem proves completeness of
that menu for four-unit separation. It changes no frozen program, input,
search domain, output, or computation status. The theorem is a later
paper deduction; the recorded run remains candidate-C on one architecture.

For a new index the menu must be frozen under a new prospective audit.
A failure to split a pair with its complete menu would now be a complete
four-unit obstruction for that pair, rather than a failure of a chosen
subfamily. It would not exclude weight five or higher.

**Falsifiers.** A four-unit whole-ideal separator for two primes dividing
the fixed $M$, while every entry of (1) has identical zero flags at those
primes, refutes completeness. A violation of (2) at any divisor of $M$
refutes the stronger full-multiplicity statement. Every order, carrier,
weight, and whole-ideal hypothesis above is part of the claim.

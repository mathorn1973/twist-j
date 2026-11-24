# Exact defect readings

NON-CANONICAL. New statements: candidate-D, L1.
No authority or status promotion. See SOURCE.md for registered inputs.

## 1. Domain and existing arithmetic

Use

\[
\mathcal O=\mathbb Z[j],\quad
j^4+j^3+j^2+j+1=0,\quad
J=1+j^2,\quad
\phi=-j^2-j^3,\quad J\phi=j,\quad \lambda=1-j.
\]

Both \(j\) and \(J\) are units, so

\[
d_n=\Delta(n)=J^n-1-j^{2n}
\]

is defined for every integer \(n\).
Positive-index Fibonacci and norm statements below have their own domain.

Registered inputs include

\[
\mathcal O/(2)=\mathbb F_{16},\qquad
\mathcal O/(\lambda)=\mathbb F_5,\qquad
\mathcal O/(5)=\mathbb F_5[t]/(t^4),\quad t=\lambda\bmod5.
\]

The orders of \(J\) in these three rings are respectively \(15,4,20\).
The order of \(j\) modulo two is five, and \(\phi\bmod2\) generates
\(\mathbb F_4^\times\). These are existing arithmetic premises, not new
discoveries in this note.

The reduced quotient is
\(A=\mathcal O/(2\lambda)=\mathbb F_{16}\times\mathbb F_5\).
It is different from the thicker quotient
\(\mathcal O/(10)=\mathbb F_{16}\times\mathbb F_5[t]/(t^4)\).
The latter has \(10^4\) elements.

## 2. The two reduced character tests

For a unit index \(n\bmod30\), write
\(\chi=\chi_5(n)\), and let \(\chi_3(n)\) be \(+1\) on \(1\bmod3\)
and \(-1\) on \(-1\bmod3\).
Choose the unique \(k\in\{0,1,2,3\}\) with \(n\equiv2^k\bmod5\).
If \(g=J\bmod2\), then characteristic two gives

\[
1+(g-1)^n=g^{2^k}.
\]

Consequently \(d_n=0\bmod2\) iff \(n\equiv2^k\bmod15\).
The condition modulo five was already imposed, and the condition modulo
three is \(n\equiv(-1)^k\). Since \((-1)^k=\chi_5(n)\),

\[
d_n=0\bmod2
\quad\Longleftrightarrow\quad
\chi_3(n)\chi_5(n)=1.                                      \tag{2.1}
\]

At the ramified residue place,

\[
d_n=2^n-2\bmod\lambda.
\]

For odd \(n\), this is zero iff \(n\equiv1\bmod4\), equivalently
\(\chi_4(n)=1\). These are vanishing flags. The full numerical residual
at two has more information than its zero/nonzero flag.

The group \(A^\times\) is cyclic of order sixty. Its sixteen power
automorphisms are indexed by \((\mathbb Z/60)^\times\). Ring automorphisms
act by a Frobenius power on \(\mathbb F_{16}\) and the identity on
\(\mathbb F_5\), so their exponents are

\[
1,\ 17,\ 49,\ 53\bmod60.
\]

They form the common kernel of the independent characters
\((\chi_3\chi_5,\chi_4)\), and therefore

\[
\operatorname{Aut}(A^\times)/\operatorname{Aut}(A)\simeq C_2^2.
\]

Within this declared class of power maps, testing the one relation
\(J=1+j^2\) selects exactly these ring automorphisms. This assertion is
about the reduced ring \(A\). It is not a classification of ring
automorphisms of thicker, nonreduced quotients.

## 3. One defect residue reads all sixty classes

### Proposition 3.1

For all integers \(n,m\),

\[
d_n\equiv d_m\pmod{10\mathcal O}
\quad\Longleftrightarrow\quad n\equiv m\pmod{60}.             \tag{3.1}
\]

In particular, no external phase coordinate is needed.

### Proof

Put \(a=n\bmod5\), \(u=2^n\bmod5\), and \(x=d_n\bmod2\).
The identity \(J^n=j^n\phi^{-n}\) gives

\[
x=j^a\bigl(\phi^{-n}-h_a\bigr),\qquad
h_a=j^a+j^{-a}\in\mathbb F_4.                              \tag{3.2}
\]

The membership in \(\mathbb F_4\) follows because fourth-power Frobenius
interchanges \(j^a\) and \(j^{-a}\). If \(x\ne0\), its factor in
\(\mathbb F_4^\times\) has order dividing three, so

\[
x^6=j^a.                                                  \tag{3.3}
\]

Thus the nonzero binary residual itself reads \(a\).
If \(x=0\), then \(a\ne0\): at \(a=0\), \(h_a=0\) in characteristic two,
and the right side of (3.2) is the nonzero element \(\phi^{-n}\).

Now expand in the ramified ring. We have

\[
J=2-2t+t^2,\qquad j^{2n}=(1-t)^{2n},\qquad
d_n=c_0+c_1t+c_2t^2+c_3t^3.
\]

All coefficients below lie in \(\mathbb F_5\):

\[
\begin{aligned}
c_0&=u-2,\\
c_1&=(2-u)a,\\
c_2&=(u/2-2)a^2+a,\\
c_3&=\frac{(2a)(2a-1)(2a-2)}6
       -\frac{u\,a(a-1)(a+1)}6 .
\end{aligned}                                             \tag{3.4}
\]

The divisions by two and six are divisions by units in \(\mathbb F_5\).
For negative \(n\), the same finite expansion follows from the binomial
identity in a nilpotent variable; only terms of degree at most three occur.

The constant coefficient recovers \(u=c_0+2\), and hence \(n\bmod4\).
If \(x=0\), we still need \(a\), which is now known to be nonzero.
For \(u\ne2\), use \(a=c_1/(2-u)\).
For \(u=2\), (3.4) reduces to

\[
c_2=a(1-a),\qquad c_3=a(a-1)^2.
\]

If \(c_2=0\), the nonzero condition on \(a\) gives \(a=1\).
Otherwise

\[
a=1-\frac{c_3}{c_2}.                                      \tag{3.5}
\]

Thus all cases recover \(a\).
The element

\[
x+1+j^{2a}=J^n\bmod2
\]

then recovers \(n\bmod15\), since \(g=J\bmod2\) has order fifteen.
Together with \(n\bmod4\), it recovers \(n\bmod60\).
This recovery is a fixed finite lookup in a stated cyclic group, not an
assumed discrete-log algorithm for varying large fields.

Conversely, the component orders of \(J\bmod2\) and \(J\bmod5\) are
fifteen and twenty. The phase \(j^{2n}\) has period five. Hence the
sequence modulo ten has period sixty. This proves both directions.

The same proof shows that sixty is the least period. Alternatively, any
period \(T\) satisfies
\(J^n(J^T-1)=j^{2n}(j^{2T}-1)\).
The equations at \(n=0,1\), together with \(J-j^2=1\), force \(J^T=1\)
modulo ten; its order is sixty.

### Interpretation and scope

The cubic nilpotent coefficient supplies information absent from the
residue field \(\mathbb F_5\). This is a specific arithmetic use of the
existing ramified layer. It does not identify the sixty-element arithmetic
orbit with a native checkpoint orbit or a physical clock.

## 4. Every finer quotient retains the complete power reading

### Proposition 4.1

For every ideal \(I\subseteq10\mathcal O\), including the zero ideal,

\[
d_n=d_m\bmod I\quad\Longleftrightarrow\quad
J^n=J^m\bmod I.                                           \tag{4.1}
\]

If the left equality holds, reduce modulo ten and apply Proposition 3.1.
Then \(n=m\bmod60\), so \(j^{2n}=j^{2m}\) exactly in \(\mathcal O\).
Subtracting these equal phase terms proves the right equality.

Conversely the right equality, reduced modulo ten, gives \(n=m\bmod60\)
because \(J\bmod10\) has order sixty. Again the phase terms agree exactly,
which proves the left equality.

Thus on its actual image the defect is a lossless coordinate for the
power orbit of \(J\), at every refinement of the modulus ten. No
generality is asserted for unrelated quotients.

### Binary precision with the five-place depth fixed

For \(s\ge1\),

\[
\operatorname{ord}_{2^s}(\phi)=3\cdot2^{s-1},\qquad
\operatorname{ord}_{2^s}(J)=15\cdot2^{s-1}.                \tag{4.2}
\]

Here is an exact proof. At two, \(\phi\) has order three and

\[
\phi^3=1+2\phi,\qquad \phi^6-1=4\phi^3.
\]

The first difference has valuation one, and the second has valuation two.
Once a unit is \(1\bmod4\), squaring increases the two-adic valuation
of its difference from one by exactly one, by
\((v^2-1)=(v-1)(v+1)\).
An odd power does not change that valuation.
This proves the first formula, including \(s=1,2\).
Since \(J=j\phi^{-1}\), the order-five and the \(3\cdot2^{s-1}\)
factors have coprime orders; their product has the displayed second order.

Combine this with \(\operatorname{ord}_5(J)=20\) and Proposition 4.1:

\[
d_n=d_m\bmod(5\cdot2^s)
\quad\Longleftrightarrow\quad
n=m\bmod L_s,\qquad
L_s=15\cdot2^{\max(2,s-1)}.                                \tag{4.3}
\]

For \(s\ge3\), each further binary precision step doubles \(L_s\).
Starting with a representative \(r_s=n\bmod L_s\), the only two
representatives at the next depth are \(r_s\) and \(r_s+L_s\).
Decode \(a=n\bmod5\) from the reduction modulo ten and form, using the
next binary precision,

\[
V=j^{-a}d_n+j^a+j^{-a}=\phi^{-n}\pmod{2^{s+1}}.
\]

If \(\phi^{r_s}V=1\bmod2^{s+1}\), choose \(r_s\); otherwise choose
\(r_s+L_s\). Exactly one choice works, by (4.2).
This is an arithmetic digit lift with two alternatives at each step.
It is not the native chronological update.

Given \(t\ge2\), the precision \(5\cdot2^{t+1}\) therefore reads the lowest
\(t\) binary digits of \(n\), as well as its residue modulo fifteen.
Increasing precision can recover arbitrarily long binary prefixes from
the low end. A fixed precision cannot do so. With a separately given
bound \(0\le n<L_s\), it reads the whole \(n\). It does not determine
primality without further arithmetic.

## 5. Exact arithmetic recurrences

Put \(z_n=j^{2n}\). The initial state is
\((d_0,z_0)=(-1,1)\).
Substituting \(J^n=d_n+1+z_n\) gives

\[
\begin{aligned}
z_{2n}&=z_n^2,\\
d_{2n}&=d_n^2+2(1+z_n)d_n+2z_n,\\
z_{2n+1}&=j^2z_n^2,\\
d_{2n+1}&=Jd_{2n}+(J-1)+z_n^2.
\end{aligned}                                             \tag{5.1}
\]

These recurrences evaluate the defect along the binary digits of an
index. Separately, its chronological arithmetic recurrence is

\[
(d_{n+1},z_{n+1})=(Jd_n+(J-1)+z_n,\ j^2z_n).               \tag{5.2}
\]

Both are identities in \(\mathcal O\) and in every quotient.
Neither identifies their state with the canonical six-coordinate
checkpoint. In particular \(n\mapsto2n+b\) is not silently substituted
for a native tick.

## 6. Fibonacci/Lucas content and norm

Assume \(n\) is positive and odd, with \(5\nmid n\).
Let \(\chi=\chi_5(n)\) and \(r=(n-\chi)/2\).
The real cyclotomic sums are

\[
j^n+j^{-n}=\chi\phi^{-\chi}.
\]

Therefore

\[
d_n=J^n(1-\chi\phi^{2r}).                                 \tag{6.1}
\]

Let \(\psi=-\phi^{-1}\), so
\(\sqrt5 F_r=\phi^r-\psi^r\) and \(L_r=\phi^r+\psi^r\).
For \(n=1\bmod4\), \(\chi=(-1)^r\); for \(n=3\bmod4\),
\(\chi=-(-1)^r\). Equation (6.1) becomes

\[
d_n=-\chi J^n\phi^r
\begin{cases}
\sqrt5 F_r,&n=1\bmod4,\\
L_r,&n=3\bmod4.
\end{cases}                                               \tag{6.2}
\]

Define the rational content of an element of \(\mathcal O\) as the
nonnegative gcd of its four coordinates in the integral basis
\(1,j,j^2,j^3\), with content zero for zero.
Multiplication by an algebraic unit is a unimodular integral change.
Moreover

\[
\sqrt5=2\phi-1=-1-2j^2-2j^3
\]

is primitive. Hence

\[
\operatorname{cont}(d_n)=
\begin{cases}
F_r,&n=1\bmod4,\\
L_r,&n=3\bmod4.
\end{cases}                                               \tag{6.3}
\]

Taking the degree-four field norm gives

\[
M_n=N_{\mathbb Q(j)/\mathbb Q}(d_n)=
\begin{cases}
25F_r^4,&n=1\bmod4,\\
L_r^4,&n=3\bmod4.
\end{cases}                                               \tag{6.4}
\]

The factor \(\sqrt5\) is not a unit; its norm is precisely the extra
factor twenty-five. The preceding factor \(-\chi J^n\phi^r\) is a unit
of degree-four norm one.

### Proposition 6.1: the unrestricted norm reads the complete index

On this positive odd domain, \(M_n\) determines \(n\) uniquely.
The value zero occurs only at \(n=1\). For \(n>1\), \(r\ge2\).
The identity

\[
L_r^2-5F_r^2=4(-1)^r
\]

implies \(5\nmid L_r\). Thus \(5\mid M_n\) identifies the Fibonacci
branch, and otherwise the Lucas branch applies.
Taking the appropriate exact fourth root of \(M_n/25\) or \(M_n\)
recovers \(F_r\) or \(L_r\).
Both sequences are strictly increasing for \(r\ge2\), so \(r\) is
unique. Finally

\[
n=2r+(-1)^r\quad\hbox{on the Fibonacci branch},\qquad
n=2r-(-1)^r\quad\hbox{on the Lucas branch}.
\]

This is an inverse on the admitted image, not a characterization of all
integers that can occur as norms.
The bit length of a nonzero \(M_n\) is
\(2n\log_2\phi+O(1)\), from Binet's formula.
The full norm therefore carries an unbounded amount of information, but
uses \(\Theta(n)\) bits for an index initially expressible in
\(\Theta(\log n)\) bits.

### Exact divisibility boundary

Because \(n\) is coprime to five, (6.2) also gives

\[
d_n\in n\mathcal O
\Longleftrightarrow
\begin{cases}
n\mid F_r,&n=1\bmod4,\\
n\mid L_r,&n=3\bmod4,
\end{cases}
\Longleftrightarrow n^4\mid M_n.                           \tag{6.5}
\]

The last norm equivalence uses this special factorization. It is not a
general implication from norm divisibility to divisibility of an
algebraic integer.
Primes satisfy (6.5); some composites do as well.
For \(n=49\), \(r=24\), \(F_{24}=46368\) and
\(\gcd(49,F_{24})=7\).
OBSTRUCTIONS.md gives a composite that passes even the universal
Frobenius identity, not merely this one-element test.

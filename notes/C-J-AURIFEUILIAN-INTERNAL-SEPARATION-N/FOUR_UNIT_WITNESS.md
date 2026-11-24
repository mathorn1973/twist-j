# One four-unit test splits the tower at exactly one side and index

**NON-CANONICAL. No authority. L1 arithmetic.** The tower law below
is a paper deduction, candidate-D. The finite search at $m=25$ and its
minimality checks carry candidate-C for their audited domain.

For $m=5^k$, $k\ge1$, put $f=F_m$ and
$A_\sigma(m)=5f^2+5\sigma f+1$ for $\sigma=\pm1$. Then
\[
 \gcd\big(A_\sigma(m),L_{4m+3}+L_2\big)=
 \begin{cases}
 251,&m=25,\quad \sigma=+1,\\
 1,&\text{otherwise}.
 \end{cases}                                                            \tag{1}
\]
The integer $L_2=3$ represents the two signed units
$\phi^2+\phi^{-2}$, and the odd-index trace $L_{4m+3}$ represents
$\phi^{4m+3}-\phi^{-(4m+3)}$. Thus (1) concerns a test of weight four.

## The norm that bounds the entire gcd [candidate-D]

Use $j=\zeta_5$, $\mathcal O=\mathbb Z[j]$ and
$\phi=1+j+j^{-1}$. Write $u=\phi^3$, $v=\phi^{-3}$.
We have $uv=1$ and $u-v=L_3=4$. The Laurent polynomial
\[
                 P(Z)=3+uZ^4-vZ^{-4}
\]
has $P(\phi^m)=L_{4m+3}+3$. At $c=\delta j^a$, with $\delta=\pm1$
and $1\le a\le4$, its value is
\[
                 P(c)=P_a=3+u j^{-a}-v j^a .
\]
In particular the sign of $c$ disappears. The four $P_a$ give the
four conjugate factors of $N_{K/\mathbb Q}(P_1)$, $K=\mathbb Q(j)$.
Indeed $j\mapsto j^b$ fixes $u,v$ for $b=1,4$ and exchanges
$u,v$ with $-v,-u$ for $b=2,3$. Hence it sends $P_1$ to $P_b$ in
the first case and $P_{-b}$ in the second, with indices modulo five.

Pair $P_a$ with $P_{-a}$. On writing $t=j^a+j^{-a}$, direct
multiplication and $u^2+v^2=(u-v)^2+2=18$ give
\[
                 P_aP_{-a}=29+12t-t^2=28+13t.
\]
For $a=1,2$ the two values $t_1,t_2$ are the roots of $t^2+t-1=0$.
It follows that
\[
       N_{K/\mathbb Q}(P_1)=(28+13t_1)(28+13t_2)
                         =28^2-28\cdot13-13^2=251.                      \tag{2}
\]

Let $g$ denote the gcd in (1). The distinguished map
$\theta:\mathcal O\to\mathbb Z/A_\sigma(m)\mathbb Z$ satisfies
$\theta(\phi^m)=-\sigma\theta(j)$.
Consequently $\theta(P(\phi^m))=\theta(P(-\sigma j))=\theta(P_1)$,
including for the negative Laurent exponent. Since $P(\phi^m)$ is a
rational integer divisible by $g$, reducing $\theta$ modulo $g$
gives a surjection $\mathcal O/(P_1)\to\mathbb Z/g\mathbb Z$.
The source has order $251$ by (2), so $g\mid251$ for every $m,\sigma$.
This is the full-divisor argument of the
[split-coordinate](SPLIT_COORDINATES.md) and
[affine](AFFINE_DICHOTOMY.md) proofs specialized to this test.
The integer $251$ is prime by trial division by $2,3,5,7,11,13$.

## Verifying the exceptional input by hand [candidate-D]

All entries in the following table are residues modulo $251$. From a row
$(L_n,L_{n+1})=(a,b)$ use
\[
 L_{2n}=a^2-2(-1)^n,\qquad
 L_{2n+1}=ab-(-1)^n,\qquad L_{2n+2}=b^2+2(-1)^n.
\]
These follow by multiplying the expressions $L_n=\phi^n+(-\phi^{-1})^n$.

| $n$ | $L_n$ | $L_{n+1}$ |
|---:|---:|---:|
| 6 | 18 | 29 |
| 12 | 71 | 19 |
| 25 | 93 | 112 |
| 51 | 126 | $-8$ |

Hence $L_{103}\equiv126(-8)+1\equiv-3$. Also
$5F_n=2L_{n+1}-L_n$ follows from $2\phi-1=\sqrt5$ and its conjugate.
At $n=25$ this gives $5f\equiv2\cdot112-93\equiv-120$, so
$f\equiv-24$. Thus
\[
 A_+(25)\equiv5\cdot24^2-5\cdot24+1=11\cdot251\equiv0.
\]
Both input integers are divisible by $251$, and (2) excludes any other
factor or higher power in their gcd. This gcd is proper since
$F_{25}\ge F_8=21$ implies $A_+(25)>251$.
At the same index $A_+-A_-=10f\not\equiv0\pmod{251}$, which excludes
the other sign.

Finally any prime divisor of $A_\sigma(m)$ has whole-ideal order
$5m$ for $\phi^2$, as proved in [Split coordinates](SPLIT_COORDINATES.md).
Our inclusion $251\mid A_+(25)$ gives
$\operatorname{ord}_{251\mathcal O}(\phi^2)=125$. Thus $251$ divides no side
with $m\ne25$. This proves (1) without using a primality or order
calculation for the cofactor of $251$.

## Origin and scope

**Finite result [candidate-C].** For the single input $A_+(25)$, the
[preregistered search](PREREG.md) examined the $31\,250$ specified
ordered signed trace comparisons. Its first proper gcd occurred at
$(a,b,\epsilon)=(2,103,+1)$. Its auxiliary checks reported no
separating equality of weight at most three among the signed real units
at $251$ and $112128001$. The separate paper phase-projection result
extends that lower bound to quartic units. The preregistration describes
the distinction. [Verifier output](EXPECTED.txt).
[Breaker output](BREAK_EXPECTED.txt).

**Post-audit deduction [candidate-D].** The choice $103=4\cdot25+3$
extends the observed witness to a particular affine prescription.
Equation (1) classifies that prescription throughout the tower.
The search order, histogram, and minimality checks pertain to the
original finite audit. No new search enters the tower proof.

**Falsifiers.** A gcd other than $251$ on the stated positive side
at $m=25$, or a nonunit gcd at any other stated side or index, would
refute (1). A different fixed trace prescription is a separate claim.

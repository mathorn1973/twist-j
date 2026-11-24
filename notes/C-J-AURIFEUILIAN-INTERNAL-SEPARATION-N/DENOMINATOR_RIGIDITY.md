# A bound on the full divisor read by rational affine exponents

**NON-CANONICAL. No authority. All deductions are candidate-D, L1.**
Paper proof for [claim #2090](https://github.com/mathorn1973/twist-j/issues/2090).
Use the explicit evaluations and prime-divisor bound proved in
[Split coordinates](SPLIT_COORDINATES.md).

## Statement

Write $K=\mathbb Q(j)$, $\mathcal O=\mathbb Z[j]$, $j=\zeta_5$,
$\phi=1+j+j^{-1}>1$ in the chosen real embedding of its quadratic
subfield, and $m=5^k$ with $k\ge1$. Fix a sign $\sigma=\pm1$ and put
$A=5F_m^2+5\sigma F_m+1$. Let $D\ge1$ have five-part
$D_5=5^{v_5(D)}$ dividing $m$. Take a sum of $w\ge1$ signed units
\[
   S=\sum_{i=1}^w \epsilon_i j^{c_i}\phi^{(a_i m+b_i)/D},
\]
where $\epsilon_i=\pm1$, $a_i,b_i,c_i\in\mathbb Z$, and every displayed
exponent of $\phi$ is an integer. Count repeated summands separately.
The integers $a_i$ can have either sign or any magnitude, and all input
parameters can depend on $m$. Use the given representation of the exponents
to define
\[
 H=\frac{\max_i b_i-\min_i b_i}{D},\qquad
 C_H=\frac w2\big(\phi^{H/2}+\phi^{-H/2}\big),\qquad
 g=\gcd(A,\operatorname{cont}S).
\]
Here $H$ is the span of the **offsets** $b_i/D$ from $a_i m/D$.
The exponents themselves can be much farther apart.

**Theorem.** Either $g=A$, or $g\le C_H^{4D}$. The latter bound is
on the entire integer divisor. More precisely the proof constructs four
algebraic integers $U_\tau$ in one field $L$. If all four are zero,
$g=A$. For each nonzero $U_\tau$,
\[
               g\mid |N_{L/\mathbb Q}(U_\tau)|\le C_H^{4D}.              \tag{1}
\]
With $E=2\lceil H/2\rceil$, a sufficient integer condition for
$g\in\{1,A\}$ is
\[
     [w^2(L_E+2)]^{2D}<4^{2D}(10m+1).                                  \tag{2}
\]

## The extension of degree $D$

Write $D=D_5 t$ and let $u$ be the least nonnegative residue of $m$
modulo $D$. Since $m$ is a power of five and $D_5\mid m$,
$\gcd(u,D)=D_5$. In particular $u=0$ is possible and then $t=1$.
Set $n_0=(m-u)/D$ and $x=\phi^{n_0}$. Choose a root $y$ of
\[
                         Y^D+\sigma j\phi^{-u}=0.                        \tag{3}
\]
We prove $[K(y):K]=D$. Both $y$ and $y^{-1}$ are algebraic integers,
since their $D$-th powers are units of $\mathcal O$. Write
$n=[K(y):K]$ and $\eta=N_{K(y)/K}(y)$. Then $\eta$ is a unit and
\[
                 \eta^D=(-\sigma j)^n\phi^{-un}.
\]
Let the bar denote complex conjugation on $K$. The unit $\eta\bar\eta$
in the real quadratic subfield is positive at both real embeddings,
and hence equals $\phi^{2v}$ for some $v\in\mathbb Z$. For completeness,
a positive quadratic unit strictly between $1$ and $\phi$ would have
integer trace strictly between $2$ and $3$ for norm $+1$, or strictly
between $0$ and $1$ for norm $-1$. Dividing any positive quadratic
unit by an appropriate power of $\phi$ puts it in $[1,\phi)$, proving
that all are powers of $\phi$. Total positivity forces an even power.
Multiplication by the complex conjugate of the displayed equality
now gives $vD=-un$. Therefore $t\mid n$.

The element $y^t\phi^{u/D_5}$ has $D_5$-th power $-\sigma j$.
After a possible change of sign it has $D_5$-th power $j$, since
$D_5$ is odd. It then has exact order $5D_5$ and generates over
$K=\mathbb Q(\zeta_5)$ an extension of degree $D_5$ by the cyclotomic
degree formula. Hence $D_5\mid n$. Since $t$ and $D_5$ are coprime,
$D\mid n$. Equation (3) gives the reverse bound $n\le D$.
This proves irreducibility also for even $D$ and for $u=0$.

Put $L=K(y)$ and $R=\mathcal O[y]$. By (3) and irreducibility, $R$
is the quotient of $\mathcal O[Y]$ by (3) and is free of rank $4D$
over $\mathbb Z$. Its elements include $y^{-1}$ because $y^D$ is a
unit in $\mathcal O$.

## Four lifted sums and the whole gcd

Write $C=\mathbb Z/A\mathbb Z$, and take $\rho=3+5\sigma F_m$ and
$\lambda=-\sigma\rho^m$ in $C$. The first coordinate
$\theta:\mathcal O\to C$ in the companion proof sends $j$ to $\lambda$
and $\phi$ to $\rho$. It extends to a surjection
\[
        \pi:R\longrightarrow C,\qquad y\longmapsto\rho^{n_0}.
\]
Indeed $(\rho^{n_0})^D=\rho^{m-u}=-\sigma\lambda\rho^{-u}$
as required by (3), and integer constants map onto $C$.

For each $i$ put $d_i=(a_i u+b_i)/D\in\mathbb Z$. Then
$S=\sum_i\epsilon_i j^{c_i}x^{a_i}\phi^{d_i}$ in $\mathcal O$.
For $\tau\in\operatorname{Gal}(K/\mathbb Q)$ take $y_\tau=y$ when
$\tau(\phi)=\phi$, and take $y_\tau=(-1)^{n_0}y^{-1}$ when
$\tau(\phi)=-\phi^{-1}$. Define
\[
         U_\tau=\sum_i\epsilon_i\tau(j^{c_i})y_\tau^{a_i}
                              \tau(\phi)^{d_i}\ \in R.
\]
Every factor raised to a negative power is a unit. By construction,
$\pi(U_\tau)=\theta(\tau S)$, including the sign at the conjugate
quadratic embedding. The four maps $\theta\circ\tau$ together give
the isomorphism $\mathcal O/A\mathcal O\cong C^4$.
If all $U_\tau$ vanish in $L$, we obtain $S\in A\mathcal O$ and $g=A$.

Otherwise fix one nonzero $U_\tau$. Since $S\in g\mathcal O$, the
composite $R\xrightarrow{\pi}\mathbb Z/A\mathbb Z\to\mathbb Z/g\mathbb Z$
annihilates $U_\tau$. Constants still map onto the target, giving a
surjection of finite additive groups
\[
                    R/U_\tau R\ \longrightarrow\ \mathbb Z/g\mathbb Z.
\]
The group on the left has order $|N_{L/\mathbb Q}(U_\tau)|$.
Indeed multiplication by $U_\tau$ on a $\mathbb Z$-basis of the
order $R$ is injective with image $U_\tau R$ and determinant equal
to the field norm. Thus the entire $g$, including all its prime
powers, divides this one nonzero norm. This argument applies even if
a prime dividing $g$ divides $D$.

## Norm estimate and scope

For any complex embedding $\iota:L\to\mathbb C$, equation (3) gives
$|\iota(y)|=|\iota(\phi)|^{-u/D}$. Put $\delta=1$ if $\tau$ fixes
$\phi$ and $\delta=-1$ otherwise. The magnitude of the $i$-th term of
$\iota(U_\tau)$ is exactly $|\iota(\phi)|^{\delta b_i/D}$, since
$d_i-a_i u/D=b_i/D$. Thus the numerator slopes $a_i$ do not appear
in the bound.

Of the $4D$ embeddings of $L$, $2D$ have $|\iota(\phi)|=\phi$ and
$2D$ have $|\iota(\phi)|=\phi^{-1}$. Center the offsets at their
midpoint $c=(\max_i b_i+\min_i b_i)/(2D)$ and let
$B_\pm=\sum_i\phi^{\pm(b_i/D-c)}$.
The triangle inequality bounds the absolute norm by $(B_+B_-)^{2D}$.
The midpoint factors cancel between the two sets of embeddings.
The arithmetic-geometric mean inequality and $|b_i/D-c|\le H/2$ give
\[
   \sqrt{B_+B_-}\le\tfrac12(B_++B_-)
                \le\tfrac w2(\phi^{H/2}+\phi^{-H/2})=C_H.
\]
This proves (1). Every prime divisor of $A$ is at least $10m+1$ by
the companion proof. Thus $C_H^{4D}<10m+1$ forces every $g$ other
than $A$ to equal one. Since $E$ is even,
$(\phi^{E/2}+\phi^{-E/2})^2=L_E+2$.
Using $E\ge H$ gives the sufficient integer condition (2).

These results apply to each test separately. Any number of tests
satisfying the strict bound has the same divisibility flags at every
prime in this particular $A_\sigma$, and each test returns either the
entire factor or one even when the factor has repeated prime divisors.
Signed unit weight $w$ counts terms of a single test. The number of
tested expressions does not enter (1). For example the exponents
$\lfloor a_i m/D\rfloor$ have offsets $b_i/D$ in $(-1,0]$, independently
of the magnitudes or signs of the $a_i$. A fixed bound on $D,w,H$
therefore implies eventual failure of all such internal splits.
If $C_H>1$, an internal split requires
$4D\log C_H\ge\log(10m+1)$, without any assertion of sufficiency.
For $C_H=1$, (1) itself rules out an internal split.

The existence of a bounded-weight reader with unrestricted exponents
and the existence of infinitely many composite values on an individual
side $A_\sigma$ remain open here. Failure of the strict size condition
leaves the existence of a proper gcd undecided.

**Falsifiers.** A proper gcd $g>1$ exceeding $C_H^{4D}$ under the
stated hypotheses would refute the main bound. A single proper gcd
$g>1$ under (2) would refute the integer criterion. Failure of
$g\mid N_{L/\mathbb Q}(U_\tau)$ for any nonzero lifted sum would
refute the stronger divisibility assertion even if $g$ met the size bound.

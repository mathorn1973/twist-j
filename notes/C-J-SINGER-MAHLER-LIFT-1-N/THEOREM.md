# Exact decision of the Singer-Mahler lift tiers A0-A3

```text
STATUS:       NON-CANONICAL candidate-T
AUTHORITY:    NONE
SCOPE:        CHARACTERISTIC-POLYNOMIAL ONLY
CANDIDATE:    C-J-SINGER-MAHLER-LIFT-1-N
FROZEN PIN:   49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a
METHOD:       Exact proof; no numerical roots; no coefficient enumeration
```

This note decides the frozen statements `J_MIN(A_r)` for the monic integer
quartics

\[
 f(x)=x^4+a x^3+b x^2+c x+1
\]

that have no root on the unit circle and exactly two roots outside and two
roots inside it. It makes no matrix-conjugacy, dynamical, or physical claim.

Put

\[
 \tau=\varphi^2=\frac{3+\sqrt5}{2},
 \qquad \tau+\tau^{-1}=3.
\]

The frozen decision statement is

\[
 J_{\min}(A_r):\quad M(f)\geq \tau,
 \qquad M(f)=\tau\iff f=f_J,
\]

where

\[
 f_J(x)=x^4-3x^3+4x^2-2x+1=\Phi_5(x-1).
\]

## Result

\[
\boxed{A_0:\mathrm{F},\qquad A_1:\mathrm{F},\qquad
       A_2:\text{candidate-T},\qquad A_3:\text{candidate-T}.}
\]

The failures of `A0` and `A1` have exact witnesses. The result for `A2` is
global: it does not use the frozen coefficient bounds. The result for `A3`
is a corollary and also has a direct square certificate.

## 1. Exact falsifier for A0 and A1

Take

\[
 h(x)=x^4-x^3+1.
\]

Modulo two,

\[
 h(x)\equiv x^4+x^3+1,
\]

so `h` lies in `A1` and hence in `A0`. Its coefficients also lie in the
frozen search box.

### 1.1 No unit-circle root

Suppose that \(|z|=1\) and \(h(z)=0\). Then

\[
 z^3(z-1)=-1,
\]

so \(|z-1|=1\). Together with \(|z|=1\), this gives

\[
 z+z^{-1}=1,
 \qquad z^2-z+1=0,
 \qquad z^3=-1.
\]

Substitution in \(z^3(z-1)=-1\) then forces \(z=2\), a contradiction.
Thus `h` has no root on the unit circle.

### 1.2 Exact 2/2 root count

The polynomial has no real root. For \(x\leq0\), all three terms in
\(x^4-x^3+1\) are nonnegative and the constant term is positive. For
\(x\geq0\),

\[
 h'(x)=x^2(4x-3),
\]

and the only nonzero critical point is \(x=3/4\), where

\[
 h(3/4)=\frac{229}{256}>0.
\]

The four roots therefore form two nonreal conjugate pairs. Their total
modulus product is the absolute value of the constant term, namely one.
Since no root has modulus one, neither all four roots can be inside nor all
four outside. Conjugate pairs have equal moduli, so exactly two roots are
outside and two are inside.

### 1.3 Exact Mahler upper bound

Jensen's formula, the geometric-to-quadratic mean inequality, and Parseval
give the standard Landau bound

\[
 M(h)
 \leq \left(\frac1{2\pi}\int_0^{2\pi}|h(e^{it})|^2\,dt\right)^{1/2}
 =\sqrt{1^2+(-1)^2+1^2}
 =\sqrt3.
\]

Since \(\sqrt3<2<\tau\), this is an exact witness with

\[
 M(h)<\tau.
\]

Therefore the lower-bound clause of both `J_MIN(A0)` and `J_MIN(A1)` is
false.

Their uniqueness clause also fails independently. The polynomial

\[
 f_J(-x)=x^4+3x^3+4x^2+2x+1
\]

is distinct from \(f_J\), lies in `A1`, has the same root moduli as
\(f_J\), and hence has Mahler measure \(\tau\). In the other `A0` parity
branch, the reciprocal polynomial

\[
 x^4 f_J(1/x)=x^4-2x^3+4x^2-3x+1
\]

is another exact tie.

## 2. Preliminary facts for A2

In `A2`,

\[
 a=-3,\qquad b\equiv c\equiv0\pmod2.
\]

Consequently

\[
 f(x)\bmod2=x^4+x^3+1.
\]

This polynomial has no root in \(\mathbf F_2\), and evaluating it at a root
of the only irreducible quadratic \(x^2+x+1\) gives the nonzero value
\(x\). It is therefore irreducible over \(\mathbf F_2\). In particular,
every `A2` polynomial is irreducible over \(\mathbf Q\) and, in
characteristic zero, separable.

Also set

\[
 E=f(1)=b+c-1,
 \qquad A=f(-1)=b-c+5.
\]

Both are odd and hence nonzero.

## 3. Exhaustion of the sign cases

Let \(N_+\) be the number of real roots greater than one, and let \(N_-\)
be the number of real roots less than minus one. Complex roots occur in
conjugate pairs. Directly from the factorizations at \(1\) and \(-1\),

\[
 \operatorname{sgn} f(1)=(-1)^{N_+},
 \qquad
 \operatorname{sgn} f(-1)=(-1)^{N_-}.
\]

There are exactly two outside roots. The number of nonreal outside roots is
even, so \(N_++N_-\) is even. Hence \(N_+\) and \(N_-\) have the same
parity, and \(f(1)\) and \(f(-1)\) have the same sign.

Since neither is zero, exactly two cases remain:

1. \(f(1)>0\) and \(f(-1)>0\);
2. \(f(1)<0\) and \(f(-1)<0\).

Opposite signs are impossible.

## 4. Exterior resolvent

Let \(r_1,\ldots,r_4\) be the roots of \(f\). The polynomial of pairwise
root products is

\[
\begin{aligned}
 G(y)
  &:=\prod_{i<j}(y-r_i r_j)\\
  &=y^6-b y^5+(ac-1)y^4-(a^2+c^2-2b)y^3\\
  &\phantom{={}} +(ac-1)y^2-b y+1.
\end{aligned}
\]

This follows by direct expansion in the elementary symmetric functions

\[
 e_1=-a,\qquad e_2=b,\qquad e_3=-c,\qquad e_4=1.
\]

The sextic is reciprocal and satisfies

\[
 G(y)=y^3 H(y+y^{-1}),
\]

where

\[
 H(X)=X^3-bX^2+(ac-4)X+(4b-a^2-c^2).
\]

The three roots of \(H\) are \(q+q^{-1}\), one for each complementary
partition of the four roots into two unordered pairs.

## 5. The positive-sign case

Assume \(f(1)>0\) and \(f(-1)>0\).

### 5.1 The outside product is positive

If the outside roots are nonreal, they form a conjugate pair and their
product is positive. If they are real, the two positive signs force them
either both to exceed one or both to be less than minus one. The latter is
impossible: their sum would be less than \(-2\), while the real sum of the
two inside roots has absolute value less than two. Their total sum could
not equal

\[
 r_1+r_2+r_3+r_4=-a=3.
\]

Thus the product of the outside roots is positive in every case. It equals
the Mahler measure \(M=M(f)\). The corresponding root of \(H\) is

\[
 X_0=M+M^{-1}>2.
\]

### 5.2 Exact comparison with tau

Label the outside roots \(\alpha_1,\alpha_2\) and the inside roots
\(\beta_1,\beta_2\). Each of the other two roots of \(H\) comes from a
cross product \(q=\alpha_i\beta_j\). Since

\[
 |\alpha_1\alpha_2|=M,
 \qquad |\beta_1\beta_2|=M^{-1},
\]

with every \(|\alpha_i|>1\) and every \(|\beta_j|<1\), one has the strict
annulus bound

\[
 M^{-1}<|q|<M.
\]

Put \(X=q+q^{-1}\). If \(X\) is real, then either \(|q|=1\), in which
case \(X\in[-2,2]\), or \(q\) itself is real. If \(q<0\), then
\(X\leq-2\). If \(q>0\) and \(M\leq\tau\), the strict annulus bound gives

\[
 X<M+M^{-1}\leq\tau+\tau^{-1}=3.
\]

If the two cross values \(X_1,X_2\) are nonreal, they are complex
conjugates because \(H\) has real coefficients. Therefore, whenever
\(M\leq\tau\),

\[
 C:=(3-X_1)(3-X_2)>0.
\]

The exact factorization at three is consequently

\[
 H(3)=(3-X_0)C=(3-M-M^{-1})C.
\]

The function \(t+t^{-1}\) is strictly increasing for \(t>1\). Hence,
under the stated condition \(M\leq\tau\),

\[
 M<\tau\Longrightarrow H(3)>0,
 \qquad
 M=\tau\Longrightarrow H(3)=0.
\]

Equivalently,

\[
 M\leq\tau\Longrightarrow H(3)\geq0,
\]

with equality exactly when \(M=\tau\). This equality statement is scoped
to \(M\leq\tau\); no sign claim for larger Mahler measure is required.

### 5.3 Parity forces fJ

At \(a=-3\),

\[
 D:=H(3)=6-5b-9c-c^2.
\]

Suppose \(M\leq\tau\). The preceding comparison gives \(D\geq0\).
Moreover, \(f(1)>0\) gives

\[
 b>1-c.
\]

It follows that

\[
 5(1-c)<5b\leq6-9c-c^2,
\]

or equivalently

\[
 (c+2)^2<5.
\]

Because \(c\) is even,

\[
 c\in\{-4,-2,0\}.
\]

Each case is exact:

* If \(c=-4\), then \(f(1)>0\) and even \(b\) give \(b\geq6\), but
  \(D=26-5b\leq-4\), a contradiction.
* If \(c=0\), then \(f(1)>0\) and even \(b\) give \(b\geq2\), but
  \(D=6-5b\leq-4\), a contradiction.
* If \(c=-2\), then \(f(1)>0\) gives \(b\geq4\), while
  \(D=20-5b\geq0\) gives \(b\leq4\).

Thus

\[
 c=-2,\qquad b=4,
\]

and \(f=f_J\) uniquely.

## 6. The negative-sign case

Assume \(f(1)<0\) and \(f(-1)<0\). Since \(f(0)=1\), and since a monic
quartic tends to positive infinity at both ends, the intermediate value
theorem gives at least one root in each interval

\[
 (-\infty,-1),\qquad(-1,0),\qquad(0,1),\qquad(1,\infty).
\]

These four distinct roots exhaust the degree. Write them as

\[
 -Y,\qquad -v,\qquad u,\qquad X,
\]

where \(X,Y>1\) and \(0<u,v<1\). Then

\[
 M=XY,
 \qquad uv=M^{-1},
 \qquad 3=X-Y+u-v.
\]

Since \(Y>1\),

\[
 X=M/Y<M,
 \qquad X-Y<M-1.
\]

Since \(u<1\) and \(uv=M^{-1}\),

\[
 v>M^{-1},
 \qquad u-v<1-M^{-1}.
\]

Therefore

\[
 3<M-M^{-1}.
\]

As \(M>0\), this is equivalent to

\[
 M^2-3M-1>0,
\]

and hence

\[
 M>\frac{3+\sqrt{13}}2
   >\frac{3+\sqrt5}2
   =\tau.
\]

Thus the negative-sign case has a strict global gap above the proposed
minimum.

## 7. Completion of A2 and A3

The sign exhaustion in Section 3 covers every admissible `A2` polynomial.
Section 6 excludes \(M\leq\tau\) in the negative-sign case. Sections 5.1
through 5.3 show that the only polynomial with \(M\leq\tau\) in the
positive-sign case is \(f_J\).

Finally,

\[
 f_J(x)=\Phi_5(x-1),
\]

so its roots are \(1+\zeta_5^k\), \(k=1,2,3,4\). Their moduli are

\[
 \varphi,\quad\varphi,\quad\varphi^{-1},\quad\varphi^{-1}.
\]

Thus \(f_J\) is admissible and

\[
 M(f_J)=\varphi^2=\tau.
\]

This proves `J_MIN(A2)` at candidate-T level, globally and without the
frozen coefficient bounds. Since `A3` is a subclass of `A2`, `J_MIN(A3)`
follows immediately.

There is also a direct `A3` fingerprint. Its extra condition \(f(1)=1\)
gives \(b+c=2\), and therefore

\[
 H(3)=6-5b-9c-c^2=-(c+2)^2.
\]

Under \(M\leq\tau\), the positive-sign comparison requires
\(H(3)\geq0\), so \(c=-2\), \(b=4\), and again \(f=f_J\).

## 8. Scope and limitations

1. This is a noncanonical exact proof certificate, not a public claim or a
   promotion package.
2. It decides only the frozen characteristic-polynomial classes `A0-A3`.
3. It makes no assertion about integral matrix conjugacy, lift uniqueness
   beyond characteristic polynomials, canonical bases, dynamics, entropy,
   or physics.
4. No numerical root approximation, coefficient scan, frozen coefficient
   bound, builder, or breaker output is used.
5. Independent proof review is still required before any promotion.

# Regular-simplex pair incidence and quadratic reading

Status target: **T**.
Public probe: `P-QDD-SIMPLEX-PAIR-INCIDENCE-2`.
Scope: **L4 regular-simplex support and scalar reading only**.

This is the fresh successor proof to abandoned pin
`P-QDD-SIMPLEX-PAIR-INCIDENCE-1`. The predecessor earned no result. The
mathematics below is self-contained.

The p=5 incidence cardinalities and QDD quadratic values are already public.
The new theorem is the uniform regular-simplex identity, the minimal integral
scale and the injective integer lift that explain why those two p=5
representations coincide.

## 1. Simplex and projector

Fix `N>=2` and

\[
V_N=\{x\in\mathbb Q^N:\mathbf1^Tx=0\},\qquad q(x)=x^Tx.
\]

Put

\[
u_k=e_k-\frac1N\mathbf1.
\]

Then

\[
q(u_k)=\frac{N-1}{N},\qquad
P_k=\frac{N}{N-1}u_ku_k^T,\qquad Q_k=I-P_k.
\tag{1}
\]

For every `y in V_N`, `u_k^Ty=y_k`, hence

\[
P_ky=\frac{N}{N-1}y_k u_k.
\tag{2}
\]

Choose a bijection

\[
\beta:\{0,\ldots,N-2\}\to\{0,\ldots,N-1\}\setminus\{k\}
\]

and integer source `z=(z_0,...,z_(N-2))`. Define

\[
s=\sum_i z_i,\qquad S_2=\sum_i z_i^2,\qquad
x=\sum_i z_i u_{\beta(i)}.
\tag{3}
\]

Its coordinates are

\[
x_k=-\frac{s}{N},\qquad x_{\beta(i)}=z_i-\frac{s}{N},
\tag{4}
\]

so

\[
q(x)=S_2-\frac{s^2}{N}.
\tag{5}
\]

## 2. The scale U=N(N-1) is forced

Let

\[
a_k=Nu_k=Ne_k-\mathbf1,\qquad U=N(N-1).
\tag{6}
\]

The vector `a_k` has coordinates `N-1,-1,...,-1`, so it is primitive and

\[
q(a_k)=(N-1)^2+(N-1)=U.
\tag{7}
\]

Every integer vector on `Q u_k` is an integer multiple of `a_k`: if rational
`r a_k` is integral, any coordinate away from k equals `-r`, hence `r in Z`.
Thus `+/-a_k` are the primitive integral generators of the LOW ray.

By (2) and (4),

\[
P_kx=-\frac{s}{N-1}u_k=-\frac{s}{U}a_k.
\tag{8}
\]

Suppose a positive integer M makes `M P_k x` integral for every integer source.
Take `z=(1,0,...,0)`, so `s=1`. Then

\[
MP_kx=-\frac{M}{U}a_k.
\]

Primitivity of `a_k` forces `U|M`. Conversely `M=U` works. Therefore U is the
least universal integral scale for the LOW projection, and hence for the pair
`(x,P_kx)` once we show Ux integral.

Set

\[
X=Ux.
\]

From (4),

\[
X_k=-(N-1)s,
\qquad
X_{\beta(i)}=N(N-1)z_i-(N-1)s.
\tag{9}
\]

Thus `X in A_(N-1)`. Equation (8) gives

\[
P_kX=-s a_k\in A_{N-1},
\qquad Q_kX=X-P_kX\in A_{N-1}.
\tag{10}
\]

The lift is injective because

\[
\boxed{X_{\beta(i)}-X_k=Uz_i}.
\tag{11}
\]

The complete ordered branch pair also reconstructs X because
`P_kX+Q_kX=X`.

## 3. Pair census

The ordered Cartesian square of `|a|` labeled amplitude units has cardinality
`a^2`. Define

\[
A=s^2.
\tag{12}
\]

For HIGH use N separately labeled copies of every source-difference square:

\[
B=N\sum_{i<j}(z_i-z_j)^2.
\tag{13}
\]

These are literal finite cardinalities. Signs may be retained as payload and do
not alter them.

For `N-1` source coordinates,

\[
\sum_{i<j}(z_i-z_j)^2=(N-1)S_2-s^2.
\tag{14}
\]

Hence

\[
B=N((N-1)S_2-s^2).
\tag{15}
\]

With `D=A+B`,

\[
D=(N-1)(NS_2-s^2).
\tag{16}
\]

## 4. Pair census equals quadratic reading

Using (8) and (7),

\[
q(P_kx)=\frac{s^2}{U}=\frac{A}{U}.
\tag{17}
\]

Since P and Q are orthogonal,

\[
\begin{aligned}
q(Q_kx)
 &=q(x)-q(P_kx)\\
 &=S_2-\frac{s^2}{N}-\frac{s^2}{N(N-1)}\\
 &=\frac{N((N-1)S_2-s^2)}{N(N-1)}\\
 &=\frac{B}{U}.
\end{aligned}
\tag{18}
\]

Equations (5) and (16) likewise give

\[
q(x)=\frac{D}{U}.
\tag{19}
\]

Therefore

\[
\boxed{
Uq(P_kx)=A,\qquad
Uq(Q_kx)=B,\qquad
Uq(x)=D.
}
\tag{20}
\]

The scale U was fixed independently in Section 2 by integral minimality. It is
not chosen after seeing the pair counts.

On the integer lift `X=Ux`, homogeneity yields

\[
\boxed{
q(P_kX)=UA,\qquad q(Q_kX)=UB,\qquad q(X)=UD.
}
\tag{21}
\]

Thus the chosen second-order Cartesian-pair census and the quadratic P/Q scalar
read are exactly the same reading written in count coordinates and norm
coordinates.

## 5. Ratios and exact boundaries

For nonzero z, Cauchy gives

\[
s^2\le(N-1)S_2,
\]

so `NS_2-s^2>=S_2>0` and therefore `D>0`. Hence

\[
\boxed{
\frac{q(P_kx)}{q(x)}=\frac{A}{D},
\qquad
\frac{q(Q_kx)}{q(x)}=\frac{B}{D}.
}
\tag{22}
\]

Boundary cases:

- z=0 gives A=B=D=0 and no normalized ratio;
- s=0 gives A=0 and LOW vanishes;
- B=0 iff every `z_i-z_j=0`, equivalently all source coordinates are equal,
  and then HIGH vanishes.

These are algebraic statements, not event semantics.

## 6. N=5 and the public QDD reading

At N=5,

\[
U=5\cdot4=20=q(5u_k).
\tag{23}
\]

Equation (14) becomes

\[
\sum_{i<j}(z_i-z_j)^2=4S_2-s^2.
\]

Therefore

\[
A=s^2,
\qquad B=5(4S_2-s^2),
\qquad D=4(5S_2-s^2),
\tag{24}
\]

and

\[
q(P_kx)=A/20,
\qquad q(Q_kx)=B/20,
\qquad q(x)=D/20.
\tag{25}
\]

Choose the public source transport `k=2,beta=(0,1,3,4)`. Then x is exactly the
public transported four-source simplex relation with missing vertex 2. The
public incidence theorem already owns A, B and D, and the public stabilizer
theorem already owns P and Q. The new conclusion is not their rediscovery. It
is that their common factor 20 is the primitive LOW-ray norm and the least
universal integral lift of the same regular-simplex relation.

Equations (17) through (25) hold for every integer source, so this scalar
identity is independent of the predecessor's finite 544-slot calendar. The old
record and occurrence boundaries are unchanged.

## 7. Scientific scope

**T target at L4:** quadratic registration admits an exact integer relational
interpretation as a second-order Cartesian-pair probe, with its scale fixed by
regular-simplex integrality.

**No claim:** that this probe is unique, physically selected, or itself a
realized detector. No physical effect, apparatus, event, occurrence law,
sampling law, post-state law, reset or L6 measure follows from this theorem.

The result therefore supplies a structural reason for the chosen quadratic
reading while remaining fully compatible with the public theorem that other
positive additive mathematical readings exist.

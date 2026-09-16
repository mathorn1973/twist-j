# Regular-simplex pair incidence and quadratic reading

Status target: **T**.
Public probe: `P-QDD-SIMPLEX-PAIR-INCIDENCE-1`.
Scope: **L4 regular-simplex support and scalar reading only**.

The p=5 incidence cardinalities and QDD quadratic values already exist publicly.
This proof does not reclaim them. It proves the uniform regular-simplex theorem
that identifies their common structure, fixes the denominator by a minimal
integral lift, and shows that the prepared integral relation retains the source.

## 1. Regular-simplex carrier

Fix an integer `N>=2`. Let

\[
V_N=\left\{x\in\mathbb Q^N:\mathbf1^Tx=0\right\},
\qquad q(x)=x^Tx,
\]

and

\[
u_k=e_k-\frac1N\mathbf1,
\qquad
q(u_k)=\frac{N-1}{N}.
\tag{1}
\]

The orthogonal projector onto the ray `Q u_k` is

\[
P_k=\frac{u_ku_k^T}{q(u_k)}
   =\frac{N}{N-1}u_ku_k^T,
\qquad Q_k=I-P_k.
\tag{2}
\]

For every `y in V_N`,

\[
u_k^Ty=y_k,
\]

because the common `1/N` term pairs with `sum y_r=0`. Hence

\[
P_ky=\frac{N}{N-1}y_k u_k.
\tag{3}
\]

Choose one setting `k` and a bijection

\[
\beta:\{0,\ldots,N-2\}
   \longrightarrow \{0,\ldots,N-1\}\setminus\{k\}.
\]

For an integer source `z=(z_0,...,z_(N-2))`, write

\[
s=\sum_i z_i,
\qquad S_2=\sum_i z_i^2,
\qquad
x=\sum_i z_i u_{\beta(i)}.
\tag{4}
\]

Its coordinates are

\[
x_k=-\frac{s}{N},
\qquad
x_{\beta(i)}=z_i-\frac{s}{N}.
\tag{5}
\]

Expanding gives

\[
q(x)=S_2-\frac{s^2}{N}.
\tag{6}
\]

No dynamics is asserted here. Equation (4) is a relation in one rational
regular-simplex carrier.

## 2. The integral scale is forced

Define

\[
a_k:=Nu_k=Ne_k-\mathbf1,
\qquad U:=N(N-1).
\tag{7}
\]

The integer vector `a_k` has coordinate `N-1` at k and `-1` elsewhere, so it
is primitive and

\[
q(a_k)=(N-1)^2+(N-1)=N(N-1)=U.
\tag{8}
\]

Moreover every integer vector on the ray `Q u_k` is an integer multiple of
`a_k`: if `r a_k` is integral for rational r, any coordinate away from k is
`-r`, so `r in Z`. Thus, up to sign, `a_k` is the unique primitive integral
generator of the LOW ray and U is its squared norm.

By (3) and (5),

\[
P_kx=-\frac{s}{N-1}u_k=-\frac{s}{U}a_k.
\tag{9}
\]

This also proves minimality of the common lift. Suppose a positive integer M
makes `M P_k x` integral for every integer source. Choose
`z=(1,0,...,0)`, so `s=1`. Then

\[
MP_kx=-\frac{M}{U}a_k.
\]

Since `a_k` is primitive, integrality forces `U | M`. Conversely `M=U`
works. Therefore

\[
\boxed{U=N(N-1)}
\tag{10}
\]

is the least positive universal integer that makes `M P_k x` integral for all
integer sources. It also makes x integral, because from (5)

\[
X:=Ux
\]

has coordinates

\[
X_k=-(N-1)s,
\qquad
X_{\beta(i)}=N(N-1)z_i-(N-1)s.
\tag{11}
\]

Equation (9) gives

\[
P_kX=-s a_k\in A_{N-1},
\qquad
Q_kX=X-P_kX\in A_{N-1}.
\tag{12}
\]

Thus the same minimal U clears the prepared relation and both branch vectors.

The lift is injective. Subtract the missing coordinate from a populated one:

\[
X_{\beta(i)}-X_k=U z_i,
\qquad
\boxed{z_i=\frac{X_{\beta(i)}-X_k}{U}}.
\tag{13}
\]

Also `P_kX+Q_kX=X`. The complete ordered branch pair therefore retains the
whole prepared relation. This is not a claim that branch norms alone retain it.

## 3. Cartesian-pair census

For an integer amplitude a define its signed unit list only up to cardinality:
there are `|a|` units carrying the common sign `sign(a)`. The ordered
Cartesian square has cardinality

\[
|\{0,\ldots,|a|-1\}^2|=a^2.
\tag{14}
\]

For source z define

\[
\mathcal I_L(z)
 =\{(r,t):0\le r,t<|s|\},
\tag{15}
\]

so

\[
A:=|\mathcal I_L|=s^2.
\tag{16}
\]

For HIGH retain N separately labeled copies of every pair-difference fibre:

\[
\mathcal I_H(z)=
\left\{(c,i,j,r,t):
\begin{array}{l}
0\le c<N,\quad 0\le i<j<N-1,\\
0\le r,t<|z_i-z_j|
\end{array}
\right\}.
\tag{17}
\]

Therefore

\[
B:=|\mathcal I_H|
 =N\sum_{i<j}(z_i-z_j)^2.
\tag{18}
\]

The standard difference identity for `N-1` source coordinates is

\[
\sum_{i<j}(z_i-z_j)^2=(N-1)S_2-s^2.
\tag{19}
\]

It follows that

\[
B=N\big((N-1)S_2-s^2\big),
\tag{20}
\]

and, with `D=A+B`,

\[
D=(N-1)(NS_2-s^2).
\tag{21}
\]

The sets in (15) and (17) are mathematical relation-pair sets. Their members
are not asserted to be physical detector events.

## 4. Quadratic reading equals the pair census

From (9) and (8),

\[
q(P_kx)=\frac{s^2}{U}=\frac{A}{U}.
\tag{22}
\]

Orthogonality of P and Q gives

\[
q(Q_kx)=q(x)-q(P_kx).
\]

Using (6), (20) and `U=N(N-1)`,

\[
\begin{aligned}
q(Q_kx)
 &=S_2-\frac{s^2}{N}-\frac{s^2}{N(N-1)}\\
 &=S_2-\frac{s^2}{N-1}\\
 &=\frac{N((N-1)S_2-s^2)}{N(N-1)}\\
 &=\frac{B}{U}.
\end{aligned}
\tag{23}
\]

Finally (6) and (21) give

\[
q(x)=\frac{D}{U}.
\tag{24}
\]

Hence

\[
\boxed{
Uq(P_kx)=A=|\mathcal I_L|,
\quad
Uq(Q_kx)=B=|\mathcal I_H|,
\quad
Uq(x)=D.
}
\tag{25}
\]

This is the pair-incidence / quadratic-reading equivalence. The scale U is not
chosen to make (25) work. Section 2 already characterized U independently as
the least universal integral scale of the prepared relation and its LOW
projection.

On the integer lift `X=Ux`, homogeneity gives the equivalent identities

\[
\boxed{
q(P_kX)=UA,
\quad q(Q_kX)=UB,
\quad q(X)=UD.
}
\tag{26}
\]

Thus the quadratic scalar read can be described either as squared norm on the
rational simplex relation or as a normalized exact count of ordered amplitude
pairs. The two descriptions are mathematically identical on this declared
family.

## 5. Normalized branches and boundaries

If `z!=0`, Cauchy on `N-1` coordinates gives

\[
s^2\le (N-1)S_2.
\]

Therefore

\[
NS_2-s^2\ge S_2>0,
\]

so `D>0`. Dividing (25) yields

\[
\boxed{
\frac{q(P_kx)}{q(x)}=\frac{A}{D},
\qquad
\frac{q(Q_kx)}{q(x)}=\frac{B}{D}.
}
\tag{27}
\]

The boundaries are exact:

- `z=0`: `A=B=D=0`, both branches vanish and no normalized ratio is defined;
- `s=0`: `A=0`, so LOW vanishes;
- `B=0` iff every difference `z_i-z_j` vanishes, equivalently all source
  coordinates are equal, so HIGH vanishes.

None of these cases requires a probability convention.

## 6. The TWIST-J specialization N=5

Set `N=5`. Then

\[
U=N(N-1)=20=q(5u_k).
\tag{28}
\]

For four source coordinates, (19) is

\[
\sum_{i<j}(z_i-z_j)^2=4S_2-s^2.
\tag{29}
\]

Therefore

\[
A=s^2,
\qquad
B=5(4S_2-s^2),
\qquad
D=4(5S_2-s^2),
\tag{30}
\]

and

\[
q(P_kx)=\frac{A}{20},
\qquad
q(Q_kx)=\frac{B}{20},
\qquad
q(x)=\frac{D}{20}.
\tag{31}
\]

For the public QDD source transport choose `k=2` and

\[
\beta=(0,1,3,4).
\]

Then (4) is exactly the existing transported source

\[
x=\sum_{i=0}^3 z_i u_{\beta(i)}
\]

with missing simplex vertex 2. The public incidence theorem already names the
same cardinalities A and B, and the public stabilizer theorem already names the
same P/Q decomposition. Equations (28) through (31) do not promote those prior
facts. They explain their common factor 20 as the primitive simplex norm and as
the minimal denominator-clearing scale of the projected integer relation.

The theorem is stronger than the old 544-slot implementation in one narrow
mathematical sense: (22) through (31) hold for every integer source, with no
finite slot bound or calendar. It does not inherit the old record protocol or
turn its cardinalities into physical events.

## 7. What has and has not been derived

**Derived at L4:**

- a regular-simplex relation built linearly from integer source coefficients;
- the least universal integral lift of that relation together with its LOW
  projection;
- exact source recovery from the integral relation;
- exact LOW/HIGH Cartesian-pair cardinalities;
- exact equality of those pair counts with the chosen quadratic P/Q read;
- the p=5 factor `20=5*4` from the primitive simplex direction, not from a fit.

**Not derived:**

- that second-order pair incidence is the unique possible reading;
- that a physical apparatus implements these mathematical pair sets;
- that one pair is selected as an exclusive event;
- a trial distribution, occurrence law, sampling law or L6 measure;
- a physical post-state, reset law or native capture from `Omega,U`.

The result therefore supplies a structural reason for choosing the quadratic
decoder branch without reviving the disproved requirement that all admissible
mathematical readings must be quadratic.

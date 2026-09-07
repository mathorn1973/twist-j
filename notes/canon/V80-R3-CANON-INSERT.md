# Public Canon v80 r3 exact Canon insertion

**NON-CANONICAL / FOLD INPUT.** Insert the body below immediately before
`## 3. The kernel and the census` in the old-v80 Canon byte source from content
commit `79f09fb50530ec2f39dc4be8e972038a04ef746c`.

The delimiter lines `BEGIN` and `END` are not part of Canon.

<!-- BEGIN V80-R3 CANON INSERT -->

### A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS [T]

Let

```text
A4 = {v in Z^5 : sum_i v_i = 0},
V  = A4 tensor_Z Q,
q(v)=sum_i v_i^2.
```

A ray is a one-dimensional rational subspace of V and a complete frame is any
four mutually orthogonal rational rays spanning V. For a nonzero rational
number `a=3^k u`, with numerator and denominator of u prime to 3, define

```text
h_3(a)=0   if k is even,
       -1  if k is odd and u=1 mod 3,
       +1  if k is odd and u=2 mod 3,
H([v])=h_3(q(v)).
```

Multiplying a ray representative by a rational scalar multiplies its norm by a
square, so H is projectively well defined. The binary diagonal-change identity

```text
h_3(a)+h_3(b)
  = h_3(a+b)+h_3(ab/(a+b))     mod 4
```

for nonzero `a,b,a+b` makes the sum of H over a rational orthogonal basis an
invariant modulo four. On the explicit A4 orthogonal basis with norms
`4,4,4,20` this invariant is zero. For any rational orthogonal basis with
coordinate matrix C in an integral A4 basis,

```text
prod_i q(v_i)=5(det C)^2.
```

After removing powers of three, the unit part of the product is therefore 2
modulo 3. Hence the four H values cannot all equal +1 or all equal -1. Since
each lies in {-1,0,+1} and their sum is zero modulo four, the only remaining
possibility is the exact integer identity

```text
sum_i H([v_i])=0.
```

Consequently, for every rational `|t|<=1/4`,

```text
w_t([v])=1/4+t H([v])
```

is a nonnegative normalized weight on every complete rational orthogonal
frame; for `|t|<1/4` it is uniformly strictly positive. The thirty inner
Cl(4) rays have primitive norms 2,4 or 20, hence H=0 and weight 1/4 for every
t.

This family is nevertheless not quadratic for nonzero t. In the rational plane
`U_012`, let

```text
d1=( 2,-1,-1,0,0)   r1=(0, 1,-1,0,0)
d2=(-1, 2,-1,0,0)   r2=(1, 0,-1,0,0)
d3=(-1,-1, 2,0,0)   r3=(1,-1, 0,0,0).
```

The two triples have the same projector cover,

```text
sum_m P_(d_m)=sum_m P_(r_m)=(3/2)P_U,
```

while the d rays have norm 6 and the r rays norm 2. Thus

```text
sum_m w_t(d_m)-sum_m w_t(r_m)=3t.
```

Any single quadratic representation `w([v])=tr(WP_v)` would assign equal sums
to equal projector covers, so every nonzero-t member is nonquadratic.
Therefore positivity plus noncontextual additivity on all complete rational A4
records do not force the owner-adopted quadratic reading.

This is an L4 theorem about mathematical weights. It does not assert that the
nonquadratic family is physically realized, does not reject the chosen
quadratic decoder, and supplies no effect, apparatus, event, occurrence law,
sampling law or L6 measure. Global decoder uniqueness remains unnecessary.

### QDD-SIMPLEX-PAIR-INCIDENCE [T]

For every integer `N>=2`, let

```text
V_N={x in Q^N : sum_r x_r=0},
u_k=e_k-(1/N)1,
P_k=(N/(N-1))u_k u_k^T,
Q_k=I-P_k.
```

Choose a setting k and any bijection beta from `N-1` integer source
coordinates `z_i` to all simplex vertices except k. Put

```text
s=sum_i z_i,
S2=sum_i z_i^2,
x=sum_i z_i u_(beta(i)),
U=N(N-1),
A=s^2,
B=N sum_(i<j)(z_i-z_j)^2,
D=A+B.
```

The primitive integral generator of the LOW ray is

```text
a_k=N e_k-1,
q(a_k)=N(N-1)=U.
```

For every y in V_N, `u_k^T y=y_k`. Since the missing k coordinate of x is
`-s/N`,

```text
P_k x=-(s/U)a_k.
```

Taking a source with s=1 shows that every positive integer M that makes
`M P_kx` integral for all integer sources must satisfy `U | M`. Conversely
`U=N(N-1)` clears both x and its LOW projection. Thus U is the least universal
integral scale for the prepared relation and its LOW branch.

With `X=Ux`,

```text
X_k=-(N-1)s,
X_(beta(i))=N(N-1)z_i-(N-1)s,
P_kX=-s a_k,
Q_kX=X-P_kX.
```

All three vectors are integral and sum to zero. The lift loses no source
information:

```text
z_i=(X_(beta(i))-X_k)/U.
```

The ordered branch pair also reconstructs X by addition.

Now form a second-order relation census. The ordered Cartesian square of
`|s|` signed amplitude units has cardinality

```text
A=s^2.
```

For HIGH take N separately labelled copies of the ordered Cartesian square of
every difference fibre `|z_i-z_j|`. Its cardinality is

```text
B=N sum_(i<j)(z_i-z_j)^2.
```

Using

```text
sum_(i<j)(z_i-z_j)^2=(N-1)S2-s^2
```

and orthogonality of P_k and Q_k gives exactly

```text
q(P_kx)=A/U,
q(Q_kx)=B/U,
q(x)=D/U.
```

Equivalently on the integer lift,

```text
q(P_kX)=UA,
q(Q_kX)=UB,
q(X)=UD.
```

Thus the owner-adopted quadratic P/Q scalar reading is exactly the same chosen
second-order relation read as a normalized integer Cartesian-pair census. The
scale U is not fitted to these counts; it was already forced by the primitive
simplex ray and universal integrality.

For every nonzero source D>0 and

```text
q(P_kx)/q(x)=A/D,
q(Q_kx)/q(x)=B/D.
```

Zero has no normalized ratio; `s=0` kills LOW; HIGH is zero exactly when all
source coordinates are equal.

At the TWIST-J specialization `N=p=5`,

```text
U=20=q(5u_k),
A=s^2,
B=5(4S2-s^2),
D=4(5S2-s^2).
```

For the public QDD transport `k=2`, `beta=(0,1,3,4)`, these A,B,D quantities
are exactly those already owned by QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD,
and P/Q is the existing algebraic simplex split. The new theorem identifies
their common structure and explains the factor 20 by the minimal integral
simplex scale.

This is an L4 structural reason for the chosen quadratic reading, not a
uniqueness theorem and not a physical detector model. The Cartesian pairs are
mathematical relations, not realized clicks. No physical effect, apparatus,
exclusive event, occurrence or sampling law, post-state selection, reset, L5
stream or L6 measure follows.

<!-- END V80-R3 CANON INSERT -->
